from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import cv2
import numpy as np
import mysql.connector
from time import strftime
from datetime import datetime

class AI_attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("340x470+610+150")
        self.root.title("AI attendance")

        img1 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\Screenshot 2024-02-11 124953.png")
        img1 = img1.resize((200, 200))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="white")
        lblimg1.place(x=0, y=0, width=340, height=200)

        # Load the first button icon
        img1 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\button.png")
       
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Create the first button without the rectangle border
        b1 = Button(root, image=self.photoimg1,command=self.face_recog,cursor="hand2", bd=0, highlightthickness=0)
        b1.place(x=4, y=200)

        # Load the second button icon
        img2 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\button1 (1).png")
        
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Create the second button without the rectangle border
        b2 = Button(root, image=self.photoimg2, cursor="hand2", bd=0, highlightthickness=0)
        b2.place(x=4, y=320)


    #export to csv file
    def mark_attendence(self,i,n,d):
        with open("AI.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M/%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},present")    

     
    #Face recognition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighours)
            
            
            coord=[]
            
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confident=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host="localhost",username="root",password="iambest1",database="facerecog")
                my_cursor=conn.cursor()
               
                my_cursor.execute("Select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d="+".join(d)
            
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i="+".join(i)
            

                
                if confident>75:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    self.mark_attendence(i,n,d)
                    
                
                
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)    

                coord=[x,y,w,h]
                
            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1)==13:
                break
        video_cap.release() 
    cv2.destroyAllWindows()    

    






if __name__ == "__main__":
    root = Tk()
    obj = AI_attendance(root)
    root.mainloop()
