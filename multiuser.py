from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import cv2
from admin import Admin
from teacherpanel import teacher_panel
from DBMS import dbms_attendance


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("340x470+610+150")
        self.root.title("Login")
        self.root.resizable(False,False)

        frame = Frame(self.root, bg="white")
        frame.place(x=0, y=0, width=340, height=470)

        img1 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\anyrgb.com.png")
        img1 = img1.resize((100, 100))
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="white")
        lblimg1.place(x=120, y=5, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="black", bg="white")
        get_str.place(x=95, y=120)

        username_lbl = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="black", bg="white")
        username_lbl.place(x=70, y=175)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=200, width=270)
        self.txtuser.bind('<Return>', lambda event: self.txtpass.focus_set())  # Bind Enter key to move to password entry

        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="black", bg="white")
        password_lbl.place(x=70, y=240)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"),show="*")
        self.txtpass.place(x=40, y=265, width=270)

        img2 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\user-login-305.png")
        img2 = img2.resize((25, 25))
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="white")
        lblimg2.place(x=40, y=175, width=25, height=25)

        img3 = Image.open(r"C:\Users\Ronish\Desktop\test project\test image\549-5493419_login-icon-png.png")
        img3 = img3.resize((25, 25))
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="white")
        lblimg3.place(x=40, y=240, width=25, height=25)

        loginbtn = Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bd=3,relief=RIDGE, fg="black", bg="skyblue", activeforeground="black",activebackground="blue")
        loginbtn.place(x=110, y=320, width=120, height=35)

    # login function
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        elif self.txtuser.get() == "admin" and self.txtpass.get() == "adminpass":
            self.new_window=Toplevel(self.root)
            self.app=Admin(self.new_window)
        elif self.txtuser.get() == "user1" and self.txtpass.get() == "userpass1":
            self.new_window=Toplevel(self.root)
            self.app=teacher_panel(self.new_window)
        elif self.txtuser.get() == "user2" and self.txtpass.get() == "userpass2":
            self.new_window=Toplevel(self.root)
            self.app=dbms_attendance(self.new_window)
        elif self.txtuser.get() == "user3" and self.txtpass.get() == "userpass3":
            messagebox.showinfo("Success", "Welcome, User3!")
            # Add functionality for user3
        elif self.txtuser.get() == "user4" and self.txtpass.get() == "userpass4":
            messagebox.showinfo("Success", "Welcome, User4!")
            # Add functionality for user4
        elif self.txtuser.get() == "user5" and self.txtpass.get() == "userpass5":
            messagebox.showinfo("Success", "Welcome, User5!")
            # Add functionality for user5
        elif self.txtuser.get() == "user6" and self.txtpass.get() == "userpass6":
            messagebox.showinfo("Success", "Welcome, User6!")
            # Add functionality for user6
        else:
            messagebox.showerror("Error", "Invalid username or password")


if __name__ == "__main__":
    root = Tk()
    app = Login_Window(root)
    root.mainloop()
