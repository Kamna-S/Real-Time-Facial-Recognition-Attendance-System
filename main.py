from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Face_Recognition_System
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance

class Face_Recogination_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img_1 = Image.open(r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\2-Figure1-1.png")
        img_1= img_1.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img_1)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # Second Image
        img_2 = Image.open(r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\istockphoto-1168365129-1024x1024.jpg")
        img_2= img_2.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img_2)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # Third Image
        img_3 = Image.open(r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\istockphoto-1244665839-1024x1024.jpg")
        img_3 = img_3.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img_3)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # background image
        img3 = Image.open(
            r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\Background-PNG-Isolated-Pic.png")
        img3 = img3.resize((1366, 768), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Text
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDENCE SYSTEM", font=("times new roman", 25, "bold"),bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1300, height=45)

        # student button
        img4 = Image.open(r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\Screenshot 2023-09-07 204947.png")
        img4 = img4.resize((200, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=39, y=100, width=200, height=200)

        b1 = Button(bg_img, text="Students Details",command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"),
                    bg="darkblue", fg="white")
        b1.place(x=39, y=320, width=200, height=40)

        # Detection
        img5 = Image.open(
            r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\istockphoto-813581334-1024x1024.jpg")
        img5 = img5.resize((200, 200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(x=280, y=100, width=200, height=200)

        b2 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue",
                    fg="white")
        b2.place(x=280, y=320, width=200, height=40)

        # Attendance face button
        img6 = Image.open(
            r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\istockphoto-1270547297-1024x1024.jpg")
        img6 = img6.resize((200, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance)
        b3.place(x=530, y=100, width=200, height=200)

        b3 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance, font=("times new roman", 15, "bold"), bg="darkblue",
                    fg="white")
        b3.place(x=530, y=320, width=200, height=40)

        # Train data
        img7 = Image.open(r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\0_rZecOAy_WVr16810.jpg")
        img7 = img7.resize((200, 200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.train_data)
        b4.place(x=790, y=100, width=200, height=200)

        b4 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue",
                    fg="white")
        b4.place(x=790, y=320, width=200, height=40)

        # Photos
        img8 = Image.open(
            r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\Screenshot 2023-09-16 120701.png")
        img8 = img8.resize((200, 200), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b5.place(x=1041, y=100, width=200, height=200)

        b5 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b5.place(x=1041, y=320, width=200, height=40)


    def open_img(self):
        os.startfile("storage")

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def Close(self):
        root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recogination_System(root)
    root.mainloop()