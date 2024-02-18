from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class DatasetGen:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1528x790+0+0")
        self.root.title("Face Recognition Attendance System")

        #Variables
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar ()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        
    


        #bg_image
        img=Image.open(r"C:\Users\Ronish\Desktop\test project\test image\background.jpg")
        img=img.resize((1538,795))
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1538,height=795)

        title_lbl=Label(f_lbl,text="Dataset Generation",font=("times new roman",35,"bold"),background="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=0,y=45,width=1530,height=795)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",14,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=680)

        #current course
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",14,"bold"))
        current_course_frame.place(x=20,y=60,width=710,height=150)

        #department  
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",14,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="read only",width=20)
        dep_combo["values"]=("Select Department","BCT","BEI","BCX","BCE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #YEAR
        year_label=Label(current_course_frame,text="Year",font=("times new roman",14,"bold"),bg="white")
        year_label.grid(row=0,column=2,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=20)
        year_combo["values"]=("Select Year","2077","2078","2079","2080")
        year_combo.current(0)
        year_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Semester 
        sem_label=Label(current_course_frame,text="Semester",font=("times new roman",14,"bold"),bg="white")
        sem_label.grid(row=1,column=0,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="read only",width=20)
        sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Student Information 
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",14,"bold"))
        class_student_frame.place(x=10,y=200,width=710,height=430)

        #studentID
        studentId_label=Label(class_student_frame,text="StudentId:",font=("times new roman",14,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",14,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentName_label=Label(class_student_frame,text="Name:",font=("times new roman",14,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",14,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Class division:",font=("times new roman",14,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=20)
        div_combo["values"]=("A1","A2")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,sticky=W)

        #Roll No
        #rollno_label=Label(class_student_frame,text="Roll No:",font=("times new roman",14,"bold"),bg="white")
        #rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        #rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",14,"bold"))
        #rollno_entry.grid(row=1,column=3,padx=10,sticky=W)

        #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",14,"bold"),bg="white")
        dob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",14,"bold"))
        dob_entry.grid(row=2,column=1,padx=10,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",14,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=20)
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Phone No
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",14,"bold"),bg="white")
        phone_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        mail_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",14,"bold"))
        mail_entry.grid(row=3,column=1,padx=10,sticky=W)

        #Email
        mail_label=Label(class_student_frame,text="Email:",font=("times new roman",14,"bold"),bg="white")
        mail_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        mail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",14,"bold"))
        mail_entry.grid(row=2,column=3,padx=10,sticky=W)

        #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",14,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",14,"bold"))
        address_entry.grid(row=4,column=1,padx=10,sticky=W)

        #Teacher name
        #teacher_label=Label(class_student_frame,text="Teacher:",font=("times new roman",14,"bold"),bg="white")
        #teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        #teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",14,"bold"))
        #teacher_entry.grid(row=4,column=3,padx=10,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=8,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=8,column=1)

        #button frame
        button_frame=LabelFrame(class_student_frame,bd=2,bg="white",relief=RIDGE)
        button_frame.place(x=5,y=240,width=695,height=95)

        save_btn=Button(button_frame,text="Save",command=self.add_data,width=24,font=("times new roman",18,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(button_frame,text="Update",command=self.update_data,width=24,font=("times new roman",18,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(button_frame,text="Delete",command=self.delete_data,width=24,font=("times new roman",18,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=2,column=0)

        reset_btn=Button(button_frame,text="Reset",command=self.reset_data,width=24,font=("times new roman",18,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=2,column=1)

        button_frame1=LabelFrame(class_student_frame,bd=2,bg="white",relief=RIDGE)
        button_frame1.place(x=5,y=344,width=695,height=48)

        take_photo_btn=Button(button_frame1,command=self.generate_dataset,text="Take Photo Sample",width=24,font=("times new roman",18,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(button_frame1,text="Update Photo Sample",width=24,font=("times new roman",18,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",14,"bold"))
        Right_frame.place(x=760,y=10,width=720,height=680)

        

        #Table Frame
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Table",font=("times new roman",14,"bold"))
        table_frame.place(x=10,y=50,width=700,height=600)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("department","year","sem","id","name","div","gender","DOB","email","phone","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("department",text="Department")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("DOB",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("department",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    

    #Function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="iambest1",database="facerecog")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            

                                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)   


    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="iambest1",database="facerecog")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):   
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"] 

        self.var_dep.set(data[0]),
        self.var_year.set(data[1]),
        self.var_semester.set(data[2]),
        self.var_std_id.set(data[3]),
        self.var_std_name.set(data[4]),
        self.var_div.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_email.set(data[8]),
        self.var_phone.set(data[9]),
        self.var_address.set(data[10]),
        self.var_radio1.set(data[11])  

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="iambest1",database="facerecog")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()   

                                                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated successfully",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)  

    #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root) 
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="iambest1",database="facerecog")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted details",parent=self.root) 
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 

    #reset
    def reset_data(self):
        self.var_dep.set("Select Department") 
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("A1")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_radio1.set("")

    #Generate dataset and take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="iambest1",database="facerecog")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()==id+1   

                                                                                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #load predefined data on frontal face from openCV

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
                    faces=face_classifier.detectMultiScale(gray,1.3,5) 
                    #scaling factor=1.3
                    #minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(1)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None: 
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(700,700))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)  
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face) 

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset generation completed successfully.")  

            except Exception as es:
                 messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 


                        
                

                        

            



                     
    


                    

                    

                

                    

        

if __name__ == "__main__":
    root = Tk()
    obj = DatasetGen(root)
    root.mainloop()
