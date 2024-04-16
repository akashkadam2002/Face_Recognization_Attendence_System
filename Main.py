from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import os
from student import student
from train import Train
from Face_Recognition import Face_Recognition
from Attendance import Attendance
import pyttsx3

class Face_recognise:
        
    def __init__(self, root):
        self.engine = pyttsx3.init()
        self.root = root
        self.root.title("Face Recognization System")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.after(1000, self.display_welcome_message)

        # FIRST IMG
        img = Image.open(r"D:\Python\Images\face4.jpg")
        img = img.resize((int(screen_width / 3), int(screen_height / 10)))
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=int(screen_width / 3), height=int(screen_height / 10))

        # SECOND IMG
        img1 = Image.open(r"D:\Python\Images\face4.jpg")
        img1 = img1.resize((int(screen_width / 3), int(screen_height / 10)))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=int(screen_width / 3), y=0, width=int(screen_width / 3), height=int(screen_height / 10))

        # THIRD IMG
        img2 = Image.open(r"D:\Python\Images\face4.jpg")
        img2 = img2.resize((int(screen_width / 3), int(screen_height / 10)))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=2 * int(screen_width / 3), y=0, width=int(screen_width / 3), height=int(screen_height / 10))

        # BG IMG
        img3 = Image.open(r"D:\Python\Images\face4.jpg")
        img3 = img3.resize((screen_width, screen_height - int(screen_height / 10)))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=int(screen_height / 10), width=screen_width, height=screen_height - int(screen_height / 10))

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="orange")
        title_lbl.place(x=0, y=0, width=screen_width, height=int(screen_height / 15))




        # Student button
        img4 =Image.open(r"D:\Python\Images\face4.jpg")
        img4 = img4.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=int(screen_width / 7), y=int(screen_height / 10), width=int(screen_width / 7),
                 height=int(screen_height / 4))

        b1_1 = Button(bg_img, text="STUDENT DETAILS", cursor="hand2",command=self.student_details, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=int(screen_width / 7), y=int(screen_height / 10) + int(screen_height / 4) + 10,
                   width=int(screen_width / 7), height=int(screen_height / 20))

        # Detect face button
        img5 = Image.open(r"D:\Python\Images\face4.jpg")
        img5 = img5.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, command=self.face_data ,cursor="hand2")
        b2.place(x=int(screen_width / 2.4), y=int(screen_height / 10), width=int(screen_width / 7),
                  height=int(screen_height / 4))

        b2_1 = Button(bg_img, text="FACE DETECTOR", cursor="hand2", command=self.face_data ,font=("times new roman", 15, "bold"),
                       bg="darkblue", fg="white")
        b2_1.place(x=int(screen_width / 2.4), y=int(screen_height / 10) + int(screen_height / 4) + 10,
                    width=int(screen_width / 7), height=int(screen_height / 20))

        # Attendance face button
        img6 = Image.open(r"D:\Python\Images\face4.jpg")
        img6 = img6.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, command=self.attend , cursor="hand2")
        b3.place(x=int(screen_width / 1.4), y=int(screen_height / 10), width=int(screen_width / 7),
                  height=int(screen_height / 4))

        b3_1 = Button(bg_img, text="ATTENDENCE", cursor="hand2",command=self.attend , font=("times new roman", 15, "bold"),
                       bg="darkblue", fg="white")
        b3_1.place(x=int(screen_width / 1.4), y=int(screen_height / 10) + int(screen_height / 4) + 10,
                    width=int(screen_width / 7), height=int(screen_height / 20))

        # Train face button
        img8 = Image.open(r"D:\Python\Images\face4.jpg")
        img8 = img8.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b5.place(x=int(screen_width / 7), y=int(screen_height / 2.1), width=int(screen_width / 7),
                  height=int(screen_height / 4))

        b5_1 = Button(bg_img, text="TRAIN DATA", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"),
                       bg="darkblue", fg="white")
        b5_1.place(x=int(screen_width / 7), y=int(screen_height / 2.1) + int(screen_height / 4) + 10,
                    width=int(screen_width / 7), height=int(screen_height / 20))

        # Photos button
        img9 = Image.open(r"D:\Python\Images\face4.jpg")
        img9 = img9.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b6.place(x=int(screen_width / 2.4), y=int(screen_height / 2.1), width=int(screen_width / 7),
                  height=int(screen_height / 4))

        b6_1 = Button(bg_img, text="PHOTOS", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"),
                       bg="darkblue", fg="white")
        b6_1.place(x=int(screen_width / 2.4), y=int(screen_height / 2.1) + int(screen_height / 4) + 10,
                    width=int(screen_width / 7), height=int(screen_height / 20))

        # Exit button
        img10 = Image.open(r"D:\Python\Images\face4.jpg")
        img10 = img10.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2" ,command=self.exit)
        b7.place(x=int(screen_width / 1.4), y=int(screen_height / 2.1), width=int(screen_width / 7),
                  height=int(screen_height / 4))

        b7_1 = Button(bg_img, text="EXIT", cursor="hand2",command=self.exit , font=("times new roman", 15, "bold"),
                       bg="darkblue", fg="white")
        b7_1.place(x=int(screen_width / 1.4), y=int(screen_height / 2.1) + int(screen_height / 4) + 10,
                    width=int(screen_width / 7), height=int(screen_height / 20))
        
    def display_welcome_message(self):
            self.engine.say("Welcome to the face recognition attendance system application")
            self.engine.runAndWait()
        

    def open_img(self):
        os.startfile("data")


    def exit(self):
        self.engine.say("Are you sure you want to exit")
        self.engine.runAndWait()

        self.exit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want exit", parent=self.root)  
        if self.exit > 0:
            self.root.destroy()
            self.engine.say("Thank You!")
            self.engine.runAndWait()

        else:
            return      

    # function
      
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window) 

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window) 

    def attend(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)            


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognise(root)
    root.mainloop()
    
