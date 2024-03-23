# from tkinter import *
# from tkinter import ttk
# from PIL import Image , ImageTk 

# class Face_recognise:
#     def __init__(self,root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Face Recognization System")
        
#         #FIRST IMG
#         # img = Image.open(r"D:\Python\bgimg2.jpg")
#         img = Image.open(r"D:\Python\face4.jpg")
#         img = img.resize((500 , 130))
#         self.photoimg = ImageTk.PhotoImage(img)

#         f_lbl = Label(self.root ,  image=self.photoimg)
#         f_lbl.place(x=0 , y=0 ,width=500 , height=130)

#         #SECOND IMG
#         img1 = Image.open(r"D:\Python\face4.jpg")
#         img1 = img1.resize((500 , 130))
#         self.photoimg1 = ImageTk.PhotoImage(img1)

#         f_lbl = Label(self.root ,  image=self.photoimg)
#         f_lbl.place(x=500 , y=0 ,width=500 , height=130)

#         #THIRD IMG
#         img2 = Image.open(r"D:\Python\face4.jpg")
#         img2 = img2.resize((500 , 130))
#         self.photoimg2 = ImageTk.PhotoImage(img2)

#         f_lbl = Label(self.root ,  image=self.photoimg)
#         f_lbl.place(x=1000 , y=0 ,width=550 , height=130)

#         #bg img
#         img3 = Image.open(r"D:\Python\face4.jpg")
#         img3 = img3.resize((500 , 130))
#         self.photoimg3 = ImageTk.PhotoImage(img3)

#         bg_img = Label(self.root ,  image=self.photoimg)
#         bg_img.place(x=0 , y=130 ,width=1530 , height=710)


#         title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
#         title_lbl.place(x=0,y=0,width=1530,height=45)

#         #student button
#         img4 =Image.open(r"D:\Python\face4.jpg")
#         img4 = img4.resize((220 , 220))
#         self.photoimg4 = ImageTk.PhotoImage(img4)

#         b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
#         b1.place(x=200,y=100,width=220,height=220)

#         b1_1=Button(bg_img,text="Student details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b1_1.place(x=200,y=300,width=220,height=40)


#         #detect face button
#         img5 = Image.open(r"D:\Python\face4.jpg")
#         img5 = img5.resize((220 , 220))
#         self.photoimg5 = ImageTk.PhotoImage(img5)

#         b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
#         b1.place(x=500,y=100,width=220,height=220)

#         b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b1_1.place(x=500,y=300,width=220,height=40)


#         #attendence face button
#         img6 = Image.open(r"D:\Python\face4.jpg")
#         img6 = img6.resize((220 , 220))
#         self.photoimg6 = ImageTk.PhotoImage(img6)

#         b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
#         b1.place(x=800,y=100,width=220,height=220)

#         b1_1=Button(bg_img,text="attendence",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b1_1.place(x=800,y=300,width=220,height=40)


#         #help deskbutton
#         img7 = Image.open(r"D:\Python\face4.jpg")
#         img7 = img7.resize((220 , 220))
#         self.photoimg7 = ImageTk.PhotoImage(img7)

#         b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
#         b1.place(x=1100,y=100,width=220,height=220)

#         b1_1=Button(bg_img,text="help desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b1_1.place(x=1100,y=300,width=220,height=40)


#         #train face button
#         img8 =Image.open(r"D:\Python\face4.jpg")
#         img8 = img8.resize((220 , 220))
#         self.photoimg8 = ImageTk.PhotoImage(img8)

#         b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
#         b1.place(x=200,y=380,width=220,height=220)

#         b1_1=Button(bg_img,text="Train data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b1_1.place(x=200,y=580,width=220,height=40)


#         #photos button
#         img9 =Image.open(r"D:\Python\face4.jpg")
#         img9 = img9.resize((220 , 220))
#         self.photoimg9 = ImageTk.PhotoImage(img9)

#         b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
#         b1.place(x=500,y=380,width=220,height=220)

#         b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b1_1.place(x=500,y=580,width=220,height=40)


#         # developer button
#         img10 = Image.open(r"D:\Python\face4.jpg")
#         img10 = img10.resize((220 , 220))
#         self.photoimg10 = ImageTk.PhotoImage(img10)

#         b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
#         b1.place(x=800,y=380,width=220,height=220)

#         b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b1_1.place(x=800,y=580,width=220,height=40)


#         # exit button
#         img11 =Image.open(r"D:\Python\face4.jpg")
#         img11 = img11.resize((220 , 220))
#         self.photoimg11 = ImageTk.PhotoImage(img11)

#         b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
#         b1.place(x=1100,y=380,width=220,height=220)

#         b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
#         b1_1.place(x=1100,y=580,width=220,height=40)


# if __name__=="__main__":
#     root=Tk()
#     obj = Face_recognise(root)
#     root.mainloop()



from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import student
from train import Train

class Face_recognise:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognization System")

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

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
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=screen_width, height=int(screen_height / 15))

        # Student button
        img4 =Image.open(r"D:\Python\Images\face4.jpg")
        img4 = img4.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=int(screen_width / 10), y=int(screen_height / 10), width=int(screen_width / 7),
                 height=int(screen_height / 4))

        b1_1 = Button(bg_img, text="Student details", cursor="hand2",command=self.student_details, font=("times new roman", 15, "bold"),
                      bg="darkblue", fg="white")
        b1_1.place(x=int(screen_width / 10), y=int(screen_height / 10) + int(screen_height / 4) + 10,
                   width=int(screen_width / 7), height=int(screen_height / 20))

        # Detect face button
        img5 = Image.open(r"D:\Python\Images\face4.jpg")
        img5 = img5.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b2.place(x=int(screen_width / 2.7), y=int(screen_height / 10), width=int(screen_width / 7),
                  height=int(screen_height / 4))

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 15, "bold"),
                       bg="darkblue", fg="white")
        b2_1.place(x=int(screen_width / 2.7), y=int(screen_height / 10) + int(screen_height / 4) + 10,
                    width=int(screen_width / 7), height=int(screen_height / 20))

        # Attendance face button
        img6 = Image.open(r"D:\Python\Images\face4.jpg")
        img6 = img6.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b3.place(x=int(screen_width / 1.6), y=int(screen_height / 10), width=int(screen_width / 7),
                  height=int(screen_height / 4))

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 15, "bold"),
                       bg="darkblue", fg="white")
        b3_1.place(x=int(screen_width / 1.6), y=int(screen_height / 10) + int(screen_height / 4) + 10,
                    width=int(screen_width / 7), height=int(screen_height / 20))

        # Help desk button
        # img7 = Image.open(r"D:\Python\face4.jpg")
        # img7 = img7.resize((int(screen_width / 7), int(screen_height / 4)))
        # self.photoimg7 = ImageTk.PhotoImage(img7)

        # b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        # b4.place(x=int(screen_width / 1.16), y=int(screen_height / 10), width=int(screen_width / 7),
        #           height=int(screen_height / 4))

        # b4_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"),
        #                bg="darkblue", fg="white")
        # b4_1.place(x=int(screen_width / 1.16), y=int(screen_height / 10) + int(screen_height / 4) + 10,
        #             width=int(screen_width / 7), height=int(screen_height / 20))

        # Train face button
        img8 = Image.open(r"D:\Python\Images\face4.jpg")
        img8 = img8.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.train_data)
        b5.place(x=int(screen_width / 10), y=int(screen_height / 2.1), width=int(screen_width / 7),
                  height=int(screen_height / 4))

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"),
                       bg="darkblue", fg="white")
        b5_1.place(x=int(screen_width / 10), y=int(screen_height / 2.1) + int(screen_height / 4) + 10,
                    width=int(screen_width / 7), height=int(screen_height / 20))

        # Photos button
        img9 = Image.open(r"D:\Python\Images\face4.jpg")
        img9 = img9.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b6.place(x=int(screen_width / 2.7), y=int(screen_height / 2.1), width=int(screen_width / 7),
                  height=int(screen_height / 4))

        b6_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"),
                       bg="darkblue", fg="white")
        b6_1.place(x=int(screen_width / 2.7), y=int(screen_height / 2.1) + int(screen_height / 4) + 10,
                    width=int(screen_width / 7), height=int(screen_height / 20))

        # Developer button
        img10 = Image.open(r"D:\Python\Images\face4.jpg")
        img10 = img10.resize((int(screen_width / 7), int(screen_height / 4)))
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b7.place(x=int(screen_width / 1.6), y=int(screen_height / 2.1), width=int(screen_width / 7),
                  height=int(screen_height / 4))

        b7_1 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"),
                       bg="darkblue", fg="white")
        b7_1.place(x=int(screen_width / 1.6), y=int(screen_height / 2.1) + int(screen_height / 4) + 10,
                    width=int(screen_width / 7), height=int(screen_height / 20))

        # Exit button
        # img11 = Image.open(r"D:\Python\face4.jpg")
        # img11 = img11.resize((int(screen_width / 7), int(screen_height / 4)))
        # self.photoimg11 = ImageTk.PhotoImage(img11)

        # b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        # b8.place(x=int(screen_width / 1.16), y=int(screen_height / 2.1), width=int(screen_width / 7),
        #           height=int(screen_height / 4))

        # b8_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 15, "bold"),
        #                bg="darkblue", fg="white")
        # b8_1.place(x=int(screen_width / 1.16), y=int(screen_height / 2.1) + int(screen_height / 4) + 10,
        #             width=int(screen_width / 7), height=int(screen_height / 20))





    def open_img(self):
        os.startfile("data")

    # function
        
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)    


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognise(root)
    root.mainloop()







