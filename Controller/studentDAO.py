from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from matplotlib.backends.backend_qt5 import MainWindow
import sys,os
import cv2
from Controller import method,homeDAO
from View import StudentManagement
import numpy as np
from PIL import Image

from database import connectDB
#Khởi tạo các biến.
global ui
ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()


def studentDAO():
    global ui
    ui = StudentManagement.Ui_MainWindow()  # truy cap  toi layout main
    ui.setupUi(MainWindow)
    ui.btnThemSinhVien.clicked.connect(event_btnThemSinhVien)
    ui.btnLayHinhAnh.clicked.connect(event_btnLayHinhAnh)
    ui.btnDatLaiSinhVien.clicked.connect(event_btnDatLaiSinhVien)
    ui.btnTrainingata.clicked.connect(event_btnTrainingata)
    table_DanhSachSinhVien()
    # ui.btnThoat.clicked.connect(event_btnThoat)


    MainWindow.show()

def event_btnThemSinhVien():
    global ui
    tenSV = (ui.edtTenSinHVien.toPlainText()).strip()
    MSSV = ui.edtMSSV.toPlainText().strip()
    khoaHoc = ui.edtKhoaHoc.toPlainText().strip()
    dataFace =ui.edtDuLieuGuongMat.toPlainText().strip()

    gioiTinh = ''
    if (ui.rbNam.isChecked()):
        gioiTinh = 'Nam'
    if (ui.rbNu.isChecked()):
        gioiTinh = 'Nữ'
    checkInputAddStudent(tenSV,MSSV,khoaHoc,dataFace,gioiTinh)

def checkInputAddStudent(tenSV,MSSV,khoaHoc,dataFace,gioiTinh):
    if (len(tenSV)==0):
        method.message('Nhập tên sinh viên')
    elif (len(MSSV)==0):
        method.message('Nhập mã số sinh viên')

    elif (len(khoaHoc)==0):
        method.message('Nhập khóa học của sinh viên')

    elif  (len(gioiTinh)==0):
        method.message('Nhập giới tính của sinh viên')
    elif (dataFace!='Thành công'):
        method.message('THêm dữ liệu gương mặt')
    else:
        mssv= "'"+ MSSV +"'"
        tensv = "'"+ tenSV.upper() +"'"
        gioitinh ="'"+ gioiTinh.upper() +"'"
        namsinh = '2022'
        query = "SELECT COUNT(*) FROM Student where MSSV = "+ mssv
        if(int(connectDB.getData(query)[0][0])>0):
            method.message('Mã số sinh viên đã tồn tại')
        else:
            query = "INSERT INTO Student  Values("+ mssv + "," +tensv + "," +khoaHoc + "," + namsinh +"," + gioitinh +")"
            connectDB.setData(query)
            method.message('Thêm sinh viên thành công')
            table_DanhSachSinhVien()
            event_btnDatLaiSinhVien()

def event_btnDatLaiSinhVien():
    global ui
    ui.edtMSSV.setText("")
    ui.edtTenSinHVien.setText("")
    ui.edtKhoaHoc.setText("")
    ui.rbNam.setChecked(False)
    ui.rbNu.setChecked(False)
    ui.edtDuLieuGuongMat.setText("")
def event_btnLayHinhAnh():
    global ui

    MSSV = ui.edtMSSV.toPlainText().strip()
    mssv = "'" + MSSV + "'"
    if (len(MSSV)==0):
        method.message('Nhập mã số sinh viên')
    else:
        query = "SELECT COUNT(*) FROM Student where MSSV = " + mssv
        if (int(connectDB.getData(query)[0][0]) > 0):
            method.message('Mã số sinh viên đã tồn tại')
        else:
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # captureDevice = camera

            sampleNum = 0
            while (True):
                ret, frame = cap.read()

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    if not os.path.exists('dataSet'):
                        os.makedirs('dataSet')

                    sampleNum += 1

                    cv2.imwrite('Controller/dataSet/User.' + str(MSSV) + '.' + str(sampleNum) + ' .jpg', gray[y: y + h, x: x + w])

                cv2.imshow('frame', frame)
                cv2.waitKey(1)

                if sampleNum > 200:
                    ui.edtDuLieuGuongMat.setText("Thành công")
                    break

            cap.release()
            cv2.destroyAllWindows()


def getImageWithId(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L');
        faceNp = np.array(faceImg, 'uint8')

        print(faceNp)
        print(os.path.split(imagePath)[1].split('.'))
        # split to get ID of the image
        ID = int(os.path.split(imagePath)[1].split('.')[1])

        faces.append(faceNp)
        IDs.append(ID)

        cv2.imshow('tranning', faceNp)
        cv2.waitKey(10)

    return IDs, faces

def event_btnTrainingata():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = 'Controller/dataSet'
    Ids, faces = getImageWithId(path)

    # trainning
    recognizer.train(faces, np.array(Ids))

    if not os.path.exists('Controller/recognizer'):
        os.makedirs('Controller/recognizer')

    recognizer.save('Controller/recognizer/trainningData.yml')
    cv2.destroyAllWindows()


def table_DanhSachSinhVien():
    global ui

    dssv = connectDB.getData("select * from Student")
    ui.table_DSSV.setRowCount(0)
    ui.table_DSSV.setRowCount(len(dssv))

    # ui.table_DSSV.setColumnCount(len(dssv))
    for i in range(0, len(dssv)):
        ui.table_DSSV.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i+1)))
        ui.table_DSSV.setItem(i, 1,  QtWidgets.QTableWidgetItem(str(dssv[i][0])))
        ui.table_DSSV.setItem(i, 2,  QtWidgets.QTableWidgetItem(str(dssv[i][1])))
        ui.table_DSSV.setItem(i, 3, QtWidgets.QTableWidgetItem(str(dssv[i][4])))
        ui.table_DSSV.setItem(i, 4, QtWidgets.QTableWidgetItem(str(dssv[i][2])))


