from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1280x720+0+0")

        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        # First Image
        img = Image.open(r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\Untitled-1-01-e1593183927231.jpg")
        img = img.resize((700,100), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=700, height=100)

        # Second Image
        img1 = Image.open(
            r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\1_zbPMmg3jYnNrkqr5q7jVng.png")
        img1 = img1.resize((700, 100), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=600, y=0, width=700, height=100)

        title_lbl = Label(text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 20, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=100, width=1280, height=30)

        main_frame=Frame(bd=2,bg="light blue")
        main_frame.place(x=10,y=100,width=1260, height=530)

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=610, height=510)

        img_left = Image.open(r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\images (3).jpeg")
        img_left = img_left.resize((600, 100), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=600, height=100)

        left_inside_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 12, "bold"))
        left_inside_frame.place(x=0, y=100, width=610, height=400)

        #Label entry
        attendanceId_label=Label(left_inside_frame, text="AttendanceId", font=("times new roman", 12, "bold"))
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_label=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceId_label.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        nameLabal = Label(left_inside_frame, text="Name", font=("times new roman", 12, "bold"))
        nameLabal.grid(row=1, column=0)

        atten_name = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        atten_name.grid(row=1, column=1, pady=8)

        depLabal = Label(left_inside_frame, text="Department", font=("times new roman", 12, "bold"))
        depLabal.grid(row=1, column=2)

        atten_dep = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        atten_dep.grid(row=1, column=3, pady=8)

        timeLabal = Label(left_inside_frame, text="Time", font=("times new roman", 12, "bold"))
        timeLabal.grid(row=2, column=0)

        atten_time = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        atten_time.grid(row=2, column=1, pady=8)

        dateLabal = Label(left_inside_frame, text="Date", font=("times new roman", 12, "bold"))
        dateLabal.grid(row=2, column=2)

        atten_date = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 13, "bold"))
        atten_date.grid(row=2, column=3, pady=8)

        attendanceLabel=Label(left_inside_frame,text="Attendance Status",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=3,column=0,pady=8)
        self.atten_status = ttk.Combobox(left_inside_frame, width=20, font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=40)

        # import Button
        save_btn = Button(btn_frame, text="Import csv",command=self.importCsv,width=12, font=("times new roman", 13, "bold"),
                          bg="blue",
                          fg="white")
        save_btn.grid(row=0, column=0, padx=8, pady=5)

        # export Button
        update_btn = Button(btn_frame, text="Export csv",command=self.exportCsv, width=12,
                            font=("times new roman", 13, "bold"),
                            bg="blue", fg="white")
        update_btn.grid(row=0, column=1, padx=8, pady=5)

        # update Button
        update_btn= Button(btn_frame, text="Update",command=self.update_data, width=12,
                            font=("times new roman", 13, "bold"),
                            bg="blue", fg="white")
        update_btn.grid(row=0, column=2, padx=8, pady=5)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=12,
                           font=("times new roman", 13, "bold"), bg="blue",
                           fg="white")
        reset_btn.grid(row=0, column=3, padx=8, pady=5)




        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                 font=("times new roman", 12, "bold"))
        right_frame.place(x=630, y=10, width=610, height=510)

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=610,height=455)


        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll no")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=150)
        self.AttendanceReportTable.column("roll", width=150)
        self.AttendanceReportTable.column("name", width=150)
        self.AttendanceReportTable.column("department", width=150)
        self.AttendanceReportTable.column("time", width=150)
        self.AttendanceReportTable.column("date", width=150)
        self.AttendanceReportTable.column("attendance", width=150)


        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
#import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd,title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
#export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.askopenfilename(initialdir=os.getcwd,title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to" +os.path.basename(fln)+"successfully")
        except Exception as es:event=""
        messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def update_data(self,event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])




if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
