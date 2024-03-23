from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recgnition System")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1380,height=45)

        img_top= Image.open(r"Images\face.jpg")
        img_top = img_top.resize((1400,290))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        bg_img=Label(self.root,image=self.photoimg_top)
        bg_img.place(x=0,y=50,width=1400,height=290)

        #Button
        b1_1 = Button(self.root, text="TRAIN DATA", cursor="hand2",command=self.train_classfier, font=("times new roman", 30, "bold"),
                      bg="blue", fg="white")
        b1_1.place(x=0, y= 320,width=1400, height=90)



        img_bottom= Image.open(r"Images\face.jpg")
        img_bottom = img_bottom.resize((1400,290))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        bg_img=Label(self.root,image=self.photoimg_bottom)
        bg_img.place(x=0,y=410,width=1400,height=290)


    def train_classfier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")   #Grey scale image
            imageNp=np.array(img,"uint8")     #uint8 is one type of datatype
            id=int(os.path.split(image)[1].split(".")[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #============== Train the classifier & save ============== 

        clf=cv2.face.createLBPHFaceRecognizer()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!")






       




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()                    