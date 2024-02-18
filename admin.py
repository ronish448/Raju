from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from datasetgen import DatasetGen
from tkinter import messagebox
import os
import cv2
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime

class Admin:
    def __init__(self, root):
        self.root = root
        self.root.geometry("340x470+610+150")
        self.root.title("Admin")

        img4 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\Screenshot 2024-02-11 204339.png")
        img4 = img4.resize((200, 200))
        self.photoimage4 = ImageTk.PhotoImage(img4)
        lblimg4 = Label(image=self.photoimage4, bg="white")
        lblimg4.place(x=0, y=0, width=340, height=200)

        img5 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\button2.png")
        img6 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\button3.png")
        img7 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\button4.png")

        img5 = img5.resize((330, 60))
        img6 = img6.resize((330, 60))
        img7 = img7.resize((330, 60))

        self.photoimg5 = ImageTk.PhotoImage(img5)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        # Create the first button without the rectangle border
        b1 = Button(root, image=self.photoimg5,command=self.datasetgen_details, cursor="hand2", bd=0, highlightthickness=0)
        b1.place(x=4, y=200)

        # Create the second button without the rectangle border
        b2 = Button(root, image=self.photoimg6,command=self.train_classifier, cursor="hand2", bd=0, highlightthickness=0)
        b2.place(x=4, y=280)

        # Create the third button without the rectangle border
        b3 = Button(root, image=self.photoimg7,command=self.open_img, cursor="hand2", bd=0, highlightthickness=0)
        b3.place(x=4, y=360)

    #open data
    def open_img(self):
        os.startfile("data")   

    

    #Function button
    def datasetgen_details(self):
        self.new_window=Toplevel(self.root)
        self.app=DatasetGen(self.new_window)  

    #train function
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L')  #Gray scale conversion
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training ",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        
        #Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Completed")      


if __name__ == "__main__":
    root = Tk()
    obj = Admin(root)
    root.mainloop()
