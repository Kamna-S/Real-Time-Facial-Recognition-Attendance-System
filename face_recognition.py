from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
import tkinter.filedialog as filedialog
import shutil
import numpy as np
from datetime import datetime
import cv2
import os


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1280x720+0+0")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 25, "bold"), bg="white",
                          fg="blue")
        title_lbl.place(x=0, y=0, width=1300, height=55)

        # 1st image
        img_top = Image.open(
            r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\loyalty-program-facial-recognition-jpeg.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=650, height=700)
        # 2nd image
        img_side = Image.open(
            r"C:\Users\Harish Mandal\Desktop\pythonProject13\images\facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_side = img_side.resize((650, 700), Image.LANCZOS)
        self.photoimg_side = ImageTk.PhotoImage(img_side)

        f_lbl = Label(self.root, image=self.photoimg_side)
        f_lbl.place(x=650, y=55, width=650, height=700)

        b1 = Button(self.root, text="Face Recognition", cursor="hand2",command=self.face_recog,
                    font=("times new roman", 18, "bold"),
                    bg="light blue", fg="black", )
        b1.place(x=870, y=150, width=205, height=40)

        self.attendance_marked = False

    def mark_attendance(self,n,r,d,i):
        file_path = "C:/Users/Harish Mandal/Desktop/pythonProject13/Attendane.csv"
        with open(file_path, "a", newline="\n") as f:
            now = datetime.now()
            d1=now.strftime("%d/%m/%Y")
            dtString=now.strftime("%H:%M:%S")
            f.writelines(f"\n{n},{r},{d},{i},{dtString},{d1},Present")


    def face_recog(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='root', database='face_recognizer')
        cursor = conn.cursor()
        if conn.is_connected():
            print("Connected to the database")
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord=[]
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))


                cursor.execute("select Name from student where Student_id = 15")
                n = cursor.fetchone()[0]

                cursor.execute("select Roll from student where Student_id = 15")
                r= cursor.fetchone()[0]

                cursor.execute("select Dep from student where Student_id = 15")
                d = cursor.fetchone()[0]

                cursor.execute("select Student_id from student where Student_id=50")
                i = cursor.fetchone()[0]




                if confidence > 70:
                    cv2.putText(img, f"Student_id:{i}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (64, 15, 233), 2)
                    cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (64, 15, 223), 2)
                    cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (64, 15, 223), 3)
                    cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (64, 15, 223), 3)


                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8,
                                (255, 255, 0), 3)

                if not self.attendance_marked:
                    self.mark_attendance(n, r, d, i)
                    self.attendance_marked = True

                coord = [x, y, w, y]


                self.mark_attendance(i, r, d, n)

            return coord
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("C:/Users/Harish Mandal/Desktop/pythonProject13/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("C:/Users/Harish Mandal/Desktop/pythonProject13/classifier.xml")

        video_cap = cv2.VideoCapture(0)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)

            # Mark attendance

            cv2.imshow("Welcome to face Recognition", img)

            if cv2.waitKey(7):
                break
        video_cap.release()

        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()    