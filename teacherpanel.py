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
import csv

class teacher_panel:
    def __init__(self, root):
        self.root = root
        self.root.geometry("340x470+610+150")
        self.root.title("AI attendance")

        self.selected_subject = StringVar()  # Variable to hold the selected subject
        
        # Subject selection dropdown
        self.subject_label = Label(root, text="Select Subject:", font=("times new roman", 15, "bold"), bg="white")
        self.subject_label.place(x=95, y=180)

        self.subject_combo = ttk.Combobox(root, textvariable=self.selected_subject, font=("times new roman", 15, "bold"), state='readonly', width=17)
        self.subject_combo['values'] = ('AI', 'DBMS', 'OS', 'ES', 'Economics', 'OOAD')
        self.subject_combo.place(x=75, y=210)
        self.subject_combo.current(0)
          # Setting the default subject
        
        # Load the first button icon
        img1 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\button.png")
        img1 = img1.resize((200, 40))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Create the first button without the rectangle border
        b1 = Button(root, image=self.photoimg1, command=self.face_recog, cursor="hand2", bd=0, highlightthickness=0)
        b1.place(x=70, y=270)

        # Load the second button icon
        img2 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\button1 (1).png")
        img2 = img2.resize((200, 40))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Create the second button without the rectangle border
        b2 = Button(root, image=self.photoimg2, command=self.view_attendance, cursor="hand2", bd=0, highlightthickness=0)
        b2.place(x=70, y=330)

    # Create CSV file for the selected subject if it doesn't exist
    
    def mark_attendance(self,i,n,d,subject):
        folder_name = "AttendanceRecords"
        file_name = f"{folder_name}/{subject}.csv"
        
        if not os.path.exists(file_name):
            with open(file_name, "w", newline="\n") as f:
                writer = csv.writer(f)
                writer.writerow(["Student_ID", "Name", "Department", "Time" ,"Date", "Status"])

        with open(file_name,"r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{n},{d},{dtString},{d1},present")
 
    # Face recognition
    def face_recog(self):
        subject = self.selected_subject.get()  # Get the selected subject
        if subject == "":
            messagebox.showerror("Error", "Please select a subject first!")
            return

        def draw_boundary(img, classifier, scaleFactor, minNeighbours, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbours)

            coord=[]

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h),(0,0,255), 3)
                id, prediction = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - prediction / 300)))

                
                conn = mysql.connector.connect(host="localhost", username="root", password="iambest1", database="facerecog")
                my_cursor = conn.cursor()

                my_cursor.execute("Select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d="+".join(d)
            
                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i="+".join(i)
                
                if confidence > 79:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Name:{n}",(x,y-40),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    self.mark_attendance(i,n,d, subject)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),3)

                coord=[x,y,w,h]   

            return coord
        
        def recognize(img,clf,face_cascade):
            coord=draw_boundary(img,face_cascade,1.1,10,(255,25,255),"Face",clf)
            return img

        face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf =cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img =recognize(img,clf,face_cascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()

    def view_attendance(self):
        folder_name = "AttendanceRecords"
        if not os.path.exists(folder_name):
            messagebox.showerror("Error", "No attendance records found!")
            return

        subject = self.selected_subject.get()
        if subject == "":
            messagebox.showerror("Error", "Please select a subject first!")
            return

        file_name = f"{folder_name}/{subject}.csv"
        if not os.path.exists(file_name):
            messagebox.showerror("Error", "No attendance records found for selected subject!")
            return

        with open(file_name, "r") as f:
            attendance_data = f.read()
        
        # Display attendance data in a message box or some other GUI element
        messagebox.showinfo("Attendance Records", attendance_data)


if __name__ == "__main__":
    root = Tk()
    obj = teacher_panel(root)
    root.mainloop()
