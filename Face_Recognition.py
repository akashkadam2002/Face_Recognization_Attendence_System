
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="FACE_RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1380,height=45)

        #First Image
        img_top= Image.open(r"Images\face.jpg")
        img_top = img_top.resize((580,650))
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        bg_img=Label(self.root,image=self.photoimg_top)
        bg_img.place(x=0,y=50,width=580,height=650)

        #Second Image
        img_bottom= Image.open(r"Images\face2.jpg")
        img_bottom = img_bottom.resize((800,650))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        bg_img=Label(self.root,image=self.photoimg_bottom)
        bg_img.place(x=580,y=50,width=800,height=650)

        #Button
        b1_1 = Button(bg_img, text="Face Recognition", cursor="hand2", command=self.face_recog , font=("times new roman", 18, "bold"),bg="green", fg="white")
        b1_1.place(x=340, y=580,width=200, height=40)
      

    #=======================Attendence===========================
    def mark_attendence(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]   
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")



    #=======================Face Recognition======================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            coord=[]

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)  # Corrected typo here
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Akash@18",database="face_recognization")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n) 

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r) 

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d) 

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i) 


                # my_cursor.execute("select Name from student where Student_id=" + str(id))
                # name_row = my_cursor.fetchone()
                # n = "+".join(name_row) if name_row else ""

                # my_cursor.execute("select Roll from student where Student_id=" + str(id))
                # roll_row = my_cursor.fetchone()
                # r = "+".join(roll_row) if roll_row else ""

                # my_cursor.execute("select Dep from student where Student_id=" + str(id))
                # dep_row = my_cursor.fetchone()
                # d = "+".join(dep_row) if dep_row else ""

                # my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                # id_row = my_cursor.fetchone()
                # i = "+".join(id_row) if id_row else ""


                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-70),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255),3)
                    cv2.putText(img,f"Roll No.:{r}",(x,y-45),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255),3)
                    self.mark_attendence(i,r,n,d)
                else:
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)
                    cv2.putText(img,f"Unknown Face:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255),3)

                coord=[x,y,w,h]

            return  coord

        def recognize (img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img


        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1) == 13:
                break
            
        cv2.destroyAllWindows()    
        video_cap.release()
        # self.root.quit()


        
if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()

