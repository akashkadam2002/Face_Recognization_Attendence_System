
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
import cv2
import re
import os
import csv
from tkinter import filedialog

myData=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recgnition System")

        # -----------Variables---------------------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # first Image
        img1= Image.open(r"Images\face.jpg")
        img1 = img1.resize((800, 200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=800,height=200)


        # second Image
        img2=Image.open(r"Images\face.jpg")
        img2 = img2.resize((800, 200))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=800,y=0,width=800,height=200)

        # bg Image
        img4= Image.open(r"Images\face.jpg")
        img4 = img4.resize((1650,660))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1650,height=660)

        title_lbl=Label(bg_img,text="ATTENDENCE  MANAGEMENT  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1650,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=30,y=50,width=1450,height=515)

        # left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attedence Details",font=("times new roman",20,"bold"))
        left_frame.place(x=10,y=5,width=700,height=500)

        # img_left=Image.open(r"Images\face.jpg")
        # img_left = img_left.resize((615,150))
        # self.photoimg_left=ImageTk.PhotoImage(img_left)

        # f_lbl=Label(left_frame,image=self.photoimg_left)
        # f_lbl.place(x=5,y=0,width=680,height=150)

        left_inside_frame=Frame(left_frame,relief=RIDGE,bd=2)
        left_inside_frame.place(x=0,y=35,width=690,height=370)

        # label and entry
        #attendance id
        attendanceid_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
        attendanceid_label.grid(row=0,column=0,padx=10,pady=5)

        attendanceid_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=22,font=("times new roman",12,"bold"))
        attendanceid_entry.grid(row=0,column=1,padx=5)

        #Roll
        roll_label=Label(left_inside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8)

        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=22,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)

        # Name
        nameLabel=Label(left_inside_frame, text="Name:", bg="white", font="comicsansns 11 bold")
        nameLabel.grid(row=1, column=0)

        atten_name=ttk. Entry (left_inside_frame,textvariable=self.var_atten_name, width=22, font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1, pady=8)

        # Department
        depLabel=Label(left_inside_frame, text="Department: ", bg="white", font="comicsansns 11 bold")
        depLabel.grid(row=1, column=2)

        atten_dep=ttk. Entry (left_inside_frame,textvariable=self.var_atten_dep, width=22, font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)

        # time
        timeLabel=Label(left_inside_frame, text="Time:", bg="white", font="comicsansns 11 bold")
        timeLabel.grid(row=2, column=0)

        atten_time=ttk. Entry (left_inside_frame,textvariable=self.var_atten_time, width=22, font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        # dateLabel=Label (left_inside_frame, text="Date:",bg="white", font="comicsansns 11 bold")
        # dateLabel.grid(row=2, column=2)

        # atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date, width=22, font="comicsansns 11 bold")
        # atten_date.grid(row=2, column=3, pady=8)
        dob_label = Label(left_inside_frame, text="Date:",bg="white", font="comicsansns 11 bold")
        # dob_label.grid(row=2, column=2, padx=10, pady=5)
        dob_label.grid(row=2, column=2)

        dob_entry = DateEntry(left_inside_frame,textvariable=self.var_atten_date, width=22, font="comicsansns 11 bold")
        dob_entry.grid(row=2, column=3, pady=8)


        # attendance
        attendanceLabel=Label(left_inside_frame, text="Attendance Status", bg="white", font="comicsansns 11 bold")
        attendanceLabel.grid(row=3, column=0)

        self.atten_status=ttk.Combobox (left_inside_frame,textvariable=self.var_atten_attendance, width=20, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # buttons frame
        btn_frame=Frame (left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=300, width=720,height=35)

        save_btn=Button (btn_frame, text="Import csv",command=self.importCsv, width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn=Button(btn_frame, text="Export csv",command=self.exportCsv, width=16, font=("times new roman", 13, "bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button (btn_frame, text="Update", width=16, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn=Button(btn_frame, text="Reset",command=self.reset_Data, width=16, font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0, column=3)

        # Right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attedence Details",font=("times new roman",20,"bold"))
        Right_frame.place(x=730,y=5,width=585,height=410)
        
        table_frame=Frame (Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5,y=5, width=570,height=380)

        #--------scroll bar table----
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id",text="Attendance ID")
        self.AttendaceReportTable.heading("roll", text="Roll") 
        self.AttendaceReportTable.heading("name", text="Name") 
        self.AttendaceReportTable.heading("department", text="Department") 
        self.AttendaceReportTable.heading("time", text="Time")
        self.AttendaceReportTable.heading("date", text="Date") 
        self.AttendaceReportTable.heading("attendance", text="Attendance")

        self.AttendaceReportTable["show"]="headings"
        
        self.AttendaceReportTable.column("id", width=100, anchor="center")
        self.AttendaceReportTable.column("roll", width=100, anchor="center")
        self.AttendaceReportTable.column("name", width=100, anchor="center")
        self.AttendaceReportTable.column("department", width=200, anchor="center")
        self.AttendaceReportTable.column ("time", width=100, anchor="center")
        self.AttendaceReportTable.column("date", width=100, anchor="center")
        self.AttendaceReportTable.column("attendance", width=100, anchor="center")

        self.AttendaceReportTable.pack(fill=BOTH,expand=1)

        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # ================ fetch data ================
    def fetch_data(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)

    # Import CSV
    def importCsv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file",".csv"),("All file",".*")),parent=self.root)   
        with open(fln) as myFile:
            csvread=csv.reader(myFile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetch_data(myData)


    # Export CSV
    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data", "No Data found to export", parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file",".csv"),("All file",".*")),parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        row=content['values']
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])

    def reset_Data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()