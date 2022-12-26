from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from matplotlib.backends.backend_qt5 import MainWindow
import sys,os
import cv2
from Controller import method,homeDAO
from PIL import Image
import numpy as np
import os

from Controller.method import output_Excel
from View import StudentManagement, Attendance

from database import connectDB
#Khởi tạo các biến.
global ui
ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def attendanceDAO():
    global ui
    ui = Attendance.Ui_MainWindow()  # truy cap  toi layout main
    ui.setupUi(MainWindow)
    ui.btnTruyVan.clicked.connect(even_btnTruyVan)
    ui.btnDiemDanh.clicked.connect(even_btnDiemDanh)
    ui.btnInFile.clicked.connect(even_btnInFile)

    MainWindow.show()
def even_btnTruyVan():
    global ui
    edtMaLop = (ui.edtMaLop.toPlainText()).strip()
    edtBuoi = (ui.edtBuoi.toPlainText()).strip()

    if (len(edtMaLop) == 0):
        method.message('Bạn chưa nhập  mã lớp')
    elif (len(edtBuoi) == 0):
        method.message('Bạn chưa nhập buổi học')

    else:
        malop = "'" + edtMaLop.upper() + "'"
        query = "SELECT COUNT(*) FROM Class where maLop =" + malop
        if (int(connectDB.getData(query)[0][0]) == 0):
            method.message('Lớp này không tồn tại')
        else:

            query = "select soBuoi from Class where maLop =" + malop
            if  (int(edtBuoi) > int(connectDB.getData(query)[0][0])):
                method.message("Buổi học không tồn lại, lớp "+ str(malop)+ " chỉ có "+ str(connectDB.getData(query)[0][0])+ " buổi")
            else:
                table_DiemDanh()

def even_btnDiemDanh():
    global ui
    edtMaLop = (ui.edtMaLop.toPlainText()).strip()
    edtBuoi = (ui.edtBuoi.toPlainText()).strip()


    if (len(edtMaLop) == 0):
        method.message('Bạn chưa nhập  mã lớp')
    elif (len(edtBuoi) == 0):
        method.message('Bạn chưa nhập buổi học')

    else:
        malop = "'" + edtMaLop.upper() + "'"
        query = "SELECT COUNT(*) FROM Class where maLop =" + malop
        if (int(connectDB.getData(query)[0][0]) == 0):
            method.message('Lớp này không tồn tại')
        else:

            query = "select soBuoi from Class where maLop =" + malop
            if  (int(edtBuoi) > int(connectDB.getData(query)[0][0])):
                method.message("Buổi học không tồn lại, lớp "+ str(malop)+ " chỉ có "+ str(connectDB.getData(query)[0][0])+ " buổi")
            else:
                NhanDienDiemDanh()

def even_btnInFile():
    global ui
    edtMaLop = (ui.edtMaLop.toPlainText()).strip()
    edtBuoi = (ui.edtBuoi.toPlainText()).strip()

    if (len(edtMaLop) == 0):
        method.message('Bạn chưa nhập  mã lớp')

    else:
        malop = "'" + edtMaLop.upper() + "'"
        query = "SELECT COUNT(*) FROM Class where maLop =" + malop
        if (int(connectDB.getData(query)[0][0]) == 0):
            method.message('Lớp này không tồn tại')
        else:
            query = "select attendance.stt,Class.maLop,Class.tenLop,Student.hoVaTen, Student.MSSV,attendance.trangThai,attendance.thoiGian from attendance, Class, Student where attendance.maLop= Class.maLop and attendance.MSSV= Student.MSSV and Class.maLop="+malop+" ORDER BY attendance.stt"
            data = connectDB.getData(query)
            data.insert(0,('buổi','mã lớp','tên lớp','họ tên','MSSV','trạng thái','thời gian'))
            edtMaLop = (ui.edtMaLop.toPlainText()).strip()
            output_excel_path = "./output/"+edtMaLop+".xlsx"
            output_Excel(data, output_excel_path)
            method.message("Export excel thành công")

def NhanDienDiemDanh():
    listSV = []
    # Thư viện nhận diện khuôn mặt
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('Controller/recognizer/trainningData.yml')
    cap = cv2.VideoCapture(0)
    fontface = cv2.FONT_HERSHEY_SIMPLEX
    while (True):
        # camera read
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            roi_gray = gray[y:y + h, x:x + w]

            id, confidence = recognizer.predict(roi_gray)

            if confidence < 90:
                query = "Select * from Student where MSSV='" + str(id) + "'"
                profile = connectDB.getData(query)

                if (profile != None):
                    if (len(profile) > 0):
                        if (profile[0][0] not in listSV):
                            listSV.append(profile[0][0])
                            addStudent(profile[0][0])
                        cv2.putText(frame, profile[0][0], (x + 10, y + h + 30), fontface, 1, (0, 255, 0), 2)


            else:
                cv2.putText(frame, "NO", (x + 10, y + h + 30), fontface, 1, (0, 0, 255), 2)

        cv2.imshow('image', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.release()
    cv2.destroyAllWindows()




def table_DiemDanh():
    global ui
    edtMaLop = (ui.edtMaLop.toPlainText()).strip()
    malop = "'" + edtMaLop.upper() + "'"
    edtBuoi = (ui.edtBuoi.toPlainText()).strip()

    query=  "select Student.MSSV,Student.hoVaTen, attendance.trangThai,attendance.thoiGian from attendance,Student where Student.MSSV = attendance.MSSV and maLop =" + malop + "and stt=" + edtBuoi
    dsdd = connectDB.getData(query)
    if(len(dsdd)==0):
        method.message('Lớp học chưa có dữ liệu điểm danh')
    else:
        ui.table_DiemDanh.setRowCount(0)
        ui.table_DiemDanh.setRowCount(len(dsdd))
        for i in range(0, len(dsdd)):

            ui.table_DiemDanh.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            ui.table_DiemDanh.setItem(i, 1, QtWidgets.QTableWidgetItem(str(dsdd[i][0])))
            ui.table_DiemDanh.setItem(i, 2, QtWidgets.QTableWidgetItem(str(dsdd[i][1])))
            ui.table_DiemDanh.setItem(i, 3, QtWidgets.QTableWidgetItem(str(dsdd[i][2])))
            ui.table_DiemDanh.setItem(i, 4, QtWidgets.QTableWidgetItem(str(dsdd[i][3])))


def addStudent(MSSV):
    edtMaLop = (ui.edtMaLop.toPlainText()).strip()
    malop = "'" + edtMaLop.upper() + "'"
    edtBuoi = (ui.edtBuoi.toPlainText()).strip()
    mssv ="'" + MSSV + "'"
    now = datetime.now()
    thoigian = now.strftime("%d/%m/%Y %H:%M:%S")
    query = "select count(*) from attendance where maLop ="+malop+" and stt="+edtBuoi+" and MSSV="+ mssv
    if (int(connectDB.getData(query)[0][0]) == 0):
        query = "INSERT INTO attendance Values(" + mssv + "," + malop + "," + edtBuoi + "," + '1' + "," + "'"+ thoigian+"')"
        connectDB.setData(query)
        table_DiemDanh()
    else:
        now = datetime.now()
        thoigian= now.strftime("%d/%m/%Y %H:%M:%S")
        query = "UPDATE attendance SET trangThai=" + '1' + ",thoiGian='" + thoigian + "' WHERE MSSV="+mssv +"and maLop="+malop +" and STT="+edtBuoi
        connectDB.setData(query)
        table_DiemDanh()








