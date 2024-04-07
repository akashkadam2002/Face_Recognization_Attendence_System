from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from tkcalendar import DateEntry
import cv2
import re

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x750+0+0")
        self.root.title("Face Recgnition System")

        # variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        # first Image
        img1= Image.open(r"D:\Python\Images\face4.jpg")
        img1 = img1.resize((450, 130))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=450,height=130)


        # second Image
        img2= Image.open(r"D:\Python\Images\face4.jpg")
        img2 = img2.resize((500, 130))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=450,y=0,width=500,height=130)


        # third Image
        img3=Image.open(r"D:\Python\Images\face4.jpg")
        img3 = img3.resize((450, 130))
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=950,y=0,width=450,height=130)


        # bg Image
        img4= Image.open(r"D:\Python\Images\face4.jpg")
        img4 = img4.resize((1380,660))
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1380,height=660)

        title_lbl=Label(bg_img,text="STUDENT  MANAGEMENT  SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1380,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=30,y=50,width=1300,height=515)

        # left frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",20,"bold"))
        left_frame.place(x=10,y=5,width=630,height=500)

        # img_left=Image.open(r"C:\Users\PC\OneDrive\Desktop\Python-Face Recognition System\College Images\studLeft.jpg")
        # img_left = img_left.resize((615,150))
        # self.photoimg_left=ImageTk.PhotoImage(img_left)

        # f_lbl=Label(left_frame,image=self.photoimg_left)
        # f_lbl.place(x=5,y=0,width=615,height=150)

        # current course
        currentCourse_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",14,"bold"))
        currentCourse_frame.place(x=5,y=0,width=615,height=150)

        # Department
        dept_lbl=Label(currentCourse_frame,text="Department",font=("times new roman",12,"bold"))
        dept_lbl.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","IT","Computer Science","Electronics & Telecommunication","Civil","Mechanical", "Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=20,sticky=W)

        # course
        course_lbl=Label(currentCourse_frame,text="Course",font=("times new roman",12,"bold"))
        course_lbl.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FY","SY","TY","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        Year_lbl=Label(currentCourse_frame,text="Year",font=("times new roman",12,"bold"))
        Year_lbl.grid(row=1,column=0,padx=10)

        Year_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        Year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26","2026-27")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        Semester_lbl=Label(currentCourse_frame,text="Semester",font=("times new roman",12,"bold"))
        Semester_lbl.grid(row=1,column=2,padx=10)

        Semester_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        Semester_combo["values"]=("Select Semester","Semester-1","Semester-2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Student_class Information
        Student_class_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Student Class Information",font=("times new roman",14,"bold"))
        Student_class_frame.place(x=5,y=160,width=615,height=300)

        #student id
        studentid_label=Label(Student_class_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=5)

        studentid_entry=ttk.Entry(Student_class_frame,textvariable=self.var_std_id,width=18,font=("times new roman",12,"bold"))
        studentid_entry.grid(row=0,column=1,padx=5)

        #student name
        studentname_label=Label(Student_class_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5)

        studentname_entry=ttk.Entry(Student_class_frame,textvariable=self.var_std_name,width=18,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5)

        validation = self.root.register(validate_student_name_input)
        studentname_entry.config(validate="key", validatecommand=(validation, "%P"))


        #class division
        class_div_label=Label(Student_class_frame,text="Class Division: ",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5)

        div_combo=ttk.Combobox(Student_class_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=16)
        div_combo["values"]=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #rollno
        roll_no_label=Label(Student_class_frame,text="Roll no: ",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5)

        roll_no_entry=ttk.Entry(Student_class_frame,textvariable=self.var_roll,width=18,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5)

        #gender
        gender_label=Label(Student_class_frame,text="Gender: ",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5)

        gender_combo=ttk.Combobox(Student_class_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=16)
        gender_combo["values"]=("Select Gender","Male","Female","other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date of birth
        # dob_label=Label(Student_class_frame,text="DOB: ",font=("times new roman",12,"bold"),bg="white")
        # dob_label.grid(row=2,column=2,padx=10,pady=5)

        # dob_entry=ttk.Entry(Student_class_frame,textvariable=self.var_dob,width=18,font=("times new roman",12,"bold"))
        # dob_entry.grid(row=2,column=3,padx=10,pady=5)

        #email
        email_label=Label(Student_class_frame,text="Email: ",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5)

        email_entry=ttk.Entry(Student_class_frame,textvariable=self.var_email,width=18,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5)


        # validation = root.register(validate_email)
        # email_entry.config(validate="key", validatecommand=(validation, "%P"))

        #phoneno
        phone_label=Label(Student_class_frame,text="Phone no: ",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5)

        phone_entry=ttk.Entry(Student_class_frame,textvariable=self.var_phone,width=18,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5)


        validation = self.root.register(validate_phone_input)
        phone_entry.config(validate="key", validatecommand=(validation, "%P"))


        #address
        address_label=Label(Student_class_frame,text="Address: ",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5)

        address_entry=ttk.Entry(Student_class_frame,textvariable=self.var_address,width=18,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5)
  

       # Date of birth
        dob_label = Label(Student_class_frame, text="DOB: ", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5)

       # Replace ttk.Entry with DateEntry
        dob_entry = DateEntry(Student_class_frame, textvariable=self.var_dob, width=18, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5)


        #teacher name
        teacher_label=Label(Student_class_frame,text="Subject Name: ",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5)

        teacher_entry=ttk.Entry(Student_class_frame,textvariable=self.var_teacher,width=18,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5)

        #radio buttonssef
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Student_class_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        # self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(Student_class_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(Student_class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=610,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(Student_class_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=230,width=610,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        # Right frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",20,"bold"))
        Right_frame.place(x=650,y=5,width=630,height=500)

        img_right= Image.open(r"D:\Python\Images\face4.jpg")
        img_right = img_right.resize((615,130))
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=615,height=130)

        # searach frame
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",20,"bold"))
        search_frame.place(x=5,y=120,width=615,height=80)

        search_label=Label(search_frame,text="Search By ",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        Search_combo["values"]=("Select","Roll No","Phone No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        Search_entry=ttk.Entry(search_frame,width=12,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5)

        ShowAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        ShowAll_btn.grid(row=0,column=4)


        # table frame-
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=210, width=615, height=250)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns=("dept", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "phone", "address", "subject", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dept", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="RollNo")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("subject", text="Teacher")
        self.student_table.heading("photo", text="photosample")
        self.student_table["show"] = "headings"

        self.student_table.column("dept", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("subject", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # -------------------------function declaration---------------------------
    # Save function
    def add_data(self):
        if ( self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_teacher.get()=="" or self.var_address.get()=="" or  self.var_radio1.get() == ""):

            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Akash@18",database="face_recognization")
                my_cursor=conn.cursor()
                my_cursor.execute("Insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_id.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get()
                        ))
                conn.commit()
                # self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details Has Been Added",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    # Fetch function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Akash@18",database="face_recognization")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # get cursor function
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # update data function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_teacher.get()=="" or self.var_address.get()=="" or  self.var_radio1.get() =="":

            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Akash@18",database="face_recognization")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Name=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                            self.var_dep.get(),
                                            self.var_course.get(),
                                            self.var_year.get(),
                                            self.var_semester.get(),
                                            self.var_std_name.get(),
                                            self.var_div.get(),
                                            self.var_roll.get(),
                                            self.var_gender.get(),
                                            self.var_dob.get(),
                                            self.var_email.get(),
                                            self.var_phone.get(),
                                            self.var_address.get(),
                                            self.var_teacher.get(),
                                            self.var_std_id.get(),
                                            self.var_radio1.get()
                                        ))
                else:
                    if not Update:
                        return
                    messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    

    # Delete Function
    def delete_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_teacher.get()=="" or self.var_address.get()=="" or  self.var_radio1.get() =="":

            messagebox.showerror("Error","student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Akash@18",database="face_recognization")
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
                messagebox.showinfo("Delete","Successfully deleted student details")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)


    # Reset function
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


    ################### Generate data set ##################

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_roll.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_teacher.get()=="" or self.var_address.get()=="" or  self.var_radio1.get() =="":

            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Akash@18",database="face_recognization")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                            self.var_dep.get(),
                                            self.var_course.get(),
                                            self.var_year.get(),
                                            self.var_semester.get(),
                                            self.var_std_name.get(),
                                            self.var_div.get(),
                                            self.var_roll.get(),
                                            self.var_gender.get(),
                                            self.var_dob.get(),
                                            self.var_email.get(),
                                            self.var_phone.get(),
                                            self.var_address.get(),
                                            self.var_teacher.get(),
                                            self.var_radio1.get(),
                                            self.var_std_id.get()==id+1
                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ======Load predefined data on face frontals from opencv======

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling factor = 1.3
                    # Minimum Neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating data sets completed!!!!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 


# Student Name Validator

def validate_student_name_input(new_value):
        if re.match(r'^[a-zA-Z\s]*$', new_value):
            return True
        elif new_value == "":
            return True  # Allow empty input
        else:
            return False


# Mobile No. validator

def validate_phone_input(new_value):
    if new_value.isdigit() and len(new_value) <= 10:
        return True
    elif new_value == "":
        return True  # Allow empty input
    else:
        return False  


# def validate_email(new_value):
#     # pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', new_value):
#         return True
#     elif new_value == "":
#         return True  # Allow empty input
#     else:
#         return False



if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()                    