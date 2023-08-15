from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class student:
    def __init__(self,root) :
        self.root=root
        self.root.geometry("1530x820+0+0")
        self.root.title("Student Section ")


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
       
       
       
        # First Image
        img=Image.open(r"//Users/safirahmad/Desktop/Advance face recognization system /images/i (2) copy.webp")
        img=img.resize((500,200))
        self.photoimag=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimag)
        f_lbl.place(x=0,y=0,width=500,height=200)


        # Second Image
        img2=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/i (1) copy.webp")
        img2=img2.resize((500,200))
        self.photoimag2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimag2)
        f_lbl.place(x=501,y=0,width=500,height=200)


        # Thirst Image
        img3=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/i (1) copy 4.webp")
        img3=img3.resize((500,200))
        self.photoimag3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.photoimag3)
        f_lbl.place(x=1001,y=0,width=500,height=200)



         # Background Image
        img4=Image.open(r"//Users/safirahmad/Desktop/Advance face recognization system /images/iamge 3.png")
        img4=img4.resize((1530,820))
        self.photoimag4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimag4)
        bg_img.place(x=0,y=200,width=1530,height=820)


        title_lbl=Label(bg_img,text="Student Section",font=("Exo",30,"bold"), fg="white")
        title_lbl.place(x=0,y=-1,width=1520,height=50)

        main_fram = Frame(bg_img, border=2)
        main_fram.place(x=8,y=56, width=1420,height=635)

        #left Frame 
        Left_Frame=LabelFrame(main_fram,bd=1,relief=RIDGE,text="Student Details",font=("Exo",15,"bold"), fg="White")
        Left_Frame.place(x=10,y=7,width=680,height=620)

        # Left Frame Image
        Left_frame_img=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/i (1) copy 4.webp")
        Left_frame_img=Left_frame_img.resize((500,200))
        self.photoimag_left=ImageTk.PhotoImage(Left_frame_img)

        f_lbl=Label(Left_Frame,image=self.photoimag_left)
        f_lbl.place(x=0,y=0,width=670,height=100)

        #Current Course  Frame 
        current_course_Frame=LabelFrame(main_fram,bd=1,relief=RIDGE,text="Current Course",font=("Exo",15,"bold"), fg="White")
        current_course_Frame.place(x=15,y=135,width=670,height=120)
        
        #Department 
        dep_label=Label(current_course_Frame,text="Department" , font=("Exo",13,"bold"), fg="White")
        dep_label.grid(row=0,column=0,padx=10,pady=5)

        dep_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_dep,font=("new time roman",12,"bold") , width=20,state="readonly")
        dep_combo["values"]=("Select Department", "Computer Science " , "English " ,"Chemistry" ,"Low","Socila Science ", "Geoghraphy")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5)
       
        #Course 
        courses_label=Label(current_course_Frame,text="Course" , font=("Exo",13,"bold"), fg="White")
        courses_label.grid(row=0,column=2,padx=10,pady=5 , sticky=W)

        course_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_course,font=("new time roman",12,"bold") , width=20,state="readonly")
        course_combo["values"]=("Select Course", "BSCS" , "MSc" ,"MS" ,"PHD")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5)


        #Year
        year_label=Label(current_course_Frame,text="Year" , font=("Exo",13,"bold"), fg="White")
        year_label.grid(row=1,column=0,padx=10,pady=5 , sticky=W)

        year_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_year,font=("new time roman",12,"bold") , width=20,state="readonly")
        year_combo["values"]=("Selecter Year ","2019-2023", "2023-2026" , "2026-2030" )
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5)

        #Semester 
        semester_label=Label(current_course_Frame,text="Semester" , font=("Exo",13,"bold"), fg="White")
        semester_label.grid(row=1,column=2,padx=10,pady=5 , sticky=W)

        semester_combo=ttk.Combobox(current_course_Frame,textvariable=self.var_semester,font=("new time roman",12,"bold") , width=20,state="readonly")
        semester_combo["values"]=("Select Semester","First Semester ", "Second Semester " , "Third Semester " ,"Fourth Semester " ,  "Fifth Semester " ,"Sixth Semester " ,"Seventh Semester " ,"Eigth Semester ")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5)
    
        #Class Student   Frame 
        class_student_Frame=LabelFrame(main_fram,bd=1,relief=RIDGE,text="Class Student ",font=("Exo",15,"bold"), fg="White")
        class_student_Frame.place(x=15,y=270,width=670,height=350)

        #Student ID 
        studentid_label=Label(class_student_Frame,text="Student ID" , font=("Exo",13,"bold"), fg="White")
        studentid_label.grid(row=0,column=0,padx=0,pady=5 , sticky=W)

        studentid_entry=Entry(class_student_Frame,textvariable=self.var_std_id,width=20,font=("Exo",13,"bold"), fg="White")
        studentid_entry.grid(row=0,column=1,padx=0,pady=5,sticky=W)


        #Student Name
        studentName_label=Label(class_student_Frame,text="Student Name" , font=("Exo",13,"bold"), fg="White")
        studentName_label.grid(row=0,column=2,padx=10,pady=5 , sticky=W)

        studentName_entry=Entry(class_student_Frame,textvariable=self.var_std_name,width=20,font=("Exo",13,"bold"), fg="White")
        studentName_entry.grid(row=0,column=3,padx=0,pady=5,sticky=W)


        #Class Divison 
        class_div_label=Label(class_student_Frame,text="Class Division" , font=("Exo",13,"bold"), fg="White")
        class_div_label.grid(row=1,column=0,padx=10,pady=5 , sticky=W)

        gender_combo=ttk.Combobox(class_student_Frame,textvariable=self.var_div,font=("new time roman",12,"bold") , width=18,state="readonly")
        gender_combo["values"]=("A","B","C")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=2,pady=5)


        #Student Roll Number
        roll_no_label=Label(class_student_Frame,text="Roll Number" , font=("Exo",13,"bold"), fg="White")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5 , sticky=W)

        roll_no_entry=Entry(class_student_Frame,textvariable=self.var_roll,width=20,font=("Exo",13,"bold"), fg="White")
        roll_no_entry.grid(row=1,column=3,padx=0,pady=5,sticky=W)

        #Gender 
        gender_label=Label(class_student_Frame,text="Gender" , font=("Exo",13,"bold"), fg="White")
        gender_label.grid(row=2,column=0,padx=10,pady=5 , sticky=W)

        gender_combo=ttk.Combobox(class_student_Frame,textvariable=self.var_gender,font=("new time roman",12,"bold") , width=18,state="readonly")
        gender_combo["values"]=("Male","Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5)


        #Data of birth 
        dob_label=Label(class_student_Frame,text="Date Of Birth" , font=("Exo",13,"bold"), fg="White")
        dob_label.grid(row=2,column=2,padx=10,pady=5 , sticky=W)

        dob_entry=Entry(class_student_Frame,textvariable=self.var_dob,width=20,font=("Exo",13,"bold"), fg="White")
        dob_entry.grid(row=2,column=3,padx=0,pady=5,sticky=W)


        #Email
        email_label=Label(class_student_Frame,text="Emails " , font=("Exo",13,"bold"), fg="White")
        email_label.grid(row=3,column=0,padx=10,pady=5 , sticky=W)

        email_entry=Entry(class_student_Frame,textvariable=self.var_email,width=20,font=("Exo",13,"bold"), fg="White")
        email_entry.grid(row=3,column=1,padx=0,pady=5,sticky=W)


        #Phone Number 
        phone_label=Label(class_student_Frame,text="Phone Number" , font=("Exo",13,"bold"), fg="White")
        phone_label.grid(row=3,column=2,padx=0,pady=5 , sticky=W)

        phone_entry=Entry(class_student_Frame,textvariable=self.var_phone,width=20,font=("Exo",13,"bold"), fg="White")
        phone_entry.grid(row=3,column=3,padx=0,pady=5,sticky=W)


        #Address 
        Address_label=Label(class_student_Frame,text="Address" , font=("Exo",13,"bold"), fg="White")
        Address_label.grid(row=4,column=0,padx=10,pady=5 , sticky=W)

        Address_entry=Entry(class_student_Frame,textvariable=self.var_address,width=20,font=("Exo",13,"bold"), fg="White")
        Address_entry.grid(row=4,column=1,padx=0,pady=5,sticky=W)


        # Teacher name 
        teacher_label=Label(class_student_Frame,text="Teacher Name" , font=("Exo",13,"bold"), fg="White")
        teacher_label.grid(row=4,column=2,padx=10,pady=5 , sticky=W)

        teacher_entry=Entry(class_student_Frame,textvariable=self.var_teacher,width=20,font=("Exo",13,"bold"), fg="White")
        teacher_entry.grid(row=4,column=3,padx=0,pady=5,sticky=W)


        #Radio Button 
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_Frame,variable=self.var_radio1,text="Take Photo Sample ",value="Yes")
        radiobtn1.grid(row=6,column=0 , padx=10, pady=8)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_student_Frame,variable=self.var_radio1,text="No Photo Sample ",value="NO")
        radiobtn2.grid(row=6,column=1 , padx=10, pady=8)

        # Button Frame 
        
        btn_frame=Frame(class_student_Frame,bd=1,relief=RIDGE)
        btn_frame.place(x=3.5,y=235,width=660,height=45)

        save_btn=Button(btn_frame,text="save",command=self.add_data , width=11,  font=("Exo",15,"bold"), fg="Black")
        save_btn.grid(row=0, column=0)

        update_btn=Button(btn_frame,text="Update" ,command=self.update_data, width=11,  font=("Exo",15,"bold"), fg="Black")
        update_btn.grid(row=0, column=1)

        delet_btn=Button(btn_frame,text="Delete" , command=self.delete_data ,width=11,  font=("Exo",15,"bold"), fg="Black")
        delet_btn.grid(row=0, column=2)

        reset_btn=Button(btn_frame,text="Reset" , command=self.reset_data ,width=11,  font=("Exo",15,"bold"), fg="Black")
        reset_btn.grid(row=0, column=3)

        

        # next Button Frame 
        new_btn_frame=Frame(class_student_Frame,bd=1,relief=RIDGE)
        new_btn_frame.place(x=3.5,y=270,width=660,height=40)

        take_photo_btn=Button(new_btn_frame,text="Take Photo" , command=self.generate_datasets,width=25,  font=("Exo",15,"bold"), fg="Black")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn=Button(new_btn_frame,text="Update Photo" , width=25,  font=("Exo",15,"bold"), fg="Black")
        update_photo_btn.grid(row=0, column=1)





        
        
        

    





        #Right Frame
        RIGHT_Frame=LabelFrame(main_fram,bd=1,relief=RIDGE,text="Student Details",font=("Exo",15,"bold"), fg="White")
        RIGHT_Frame.place(x=700,y=7,width=705,height=620)

        right_frame_img=Image.open(r"/Users/safirahmad/Desktop/Advance face recognization system /images/i (1) copy 4.webp")
        right_frame_img=right_frame_img.resize((500,200))
        self.photoimag_right=ImageTk.PhotoImage(right_frame_img)

        f_lbl=Label(RIGHT_Frame,image=self.photoimag_left)
        f_lbl.place(x=0,y=0,width=670,height=100)

        #Class Student   Frame 
        search_Frame=LabelFrame(RIGHT_Frame,bd=1,relief=RIDGE,text="Search System  ",font=("Exo",15,"bold"), fg="White")
        search_Frame.place(x=15,y=110,width=670,height=70)

        search_label=Label(search_Frame,text=" Search by " , font=("Exo",15,"bold"), fg="White")
        search_label.grid(row=0,column=0,padx=0,pady=5 , sticky=W)

        search_combo=ttk.Combobox(search_Frame,font=("new time roman",12,"bold") , width=17,state="readonly")
        search_combo["values"]=("Select","Roll NO", "Name" , "Phone Number ")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5)


        search_entry=Entry(search_Frame,width=17,font=("Exo",13,"bold"), fg="White")
        search_entry.grid(row=0,column=3,padx=0,pady=5,sticky=W)

        search_btn=Button(search_Frame,text="Search" , width=7,  font=("Exo",15,"bold"), fg="Black")
        search_btn.grid(row=0, column=4)
        showALL_btn=Button(search_Frame,text="Show All" , width=7,  font=("Exo",15,"bold"), fg="Black")
        showALL_btn.grid(row=0, column=5)


        # ===============Table Form===============
        table_frame=Frame(RIGHT_Frame,bd=1,relief=RIDGE)
        table_frame.place(x=10,y=205,width=680,height=380)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="course")
        self.student_table.heading("year",text="year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone Number")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        # ======================function Declaration add data to database======================

    def add_data(self):
        if self.var_dep.get()=="Select Department " or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error ", "All Field are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost" , username="root" , password="KHan@1122" , database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

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
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess ", "Student details has been added Sucessfully")
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}")
                
#========================fetch_data to right Frame of Table and add total database data==============================

    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost" , username="root" , password="KHan@1122" , database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student ")
            data=my_cursor.fetchall()

            if len(data) !=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
                
    #==================Get Cursor For Update Date ==========================

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
        # messagebox.showinfo("Success","Okay Done")

    #====================Get Data Update=============================-

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error ", "All Field are required")        

        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student details")    
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="KHan@1122",database="face_recognizer")
                    my_cursor=conn.cursor()
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
                                                                                                                                                                                    self.var_std_id.get()


                                                                                                                                                                                   ))
                else:
                    if  not update:
                        return
                messagebox.showinfo("Sucess","Student Details  Sucessfully Updated Completed")
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}")

#===========Delete Function==================
    # my_variable=int(self.var_std_name)
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Erro","Student Id must be requuired")
        else:
            try:
                delete=messagebox.askyesno("Studet Delete Page ","Do you want to delete this Student ")
                if delete >0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="KHan@1122",database="face_recognizer")
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
                messagebox.showinfo("Delete","Successfully Delete Student")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}") 

    #==================Reset Button ==================
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),    
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("A"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    #======================Generating Data Sets =======================


    def generate_datasets(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error ", "All Field are required")        

            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="KHan@1122",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select *from student")
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

#============================Load Predified data on face frontal From CV2===========================
                    
                    face_classification=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    #=====================Create Function ================================

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classification.detectMultiScale(gray,1.3,5)
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
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                            cv2.imshow("Crooped face",face)
                         
                        if cv2.waitKey(1)==3 or int(img_id)==100:
                            break 
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generrating Datasets are completed")








                # except Exception as es:
                
                #      messagebox.showerror("Error",f"Due To:{str(es)}") 
                except Exception as es:
                    messagebox.showerror("Error",f"Due To:{str(es)}")
                    
        












#======================This is main Object for class data ===================

if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()