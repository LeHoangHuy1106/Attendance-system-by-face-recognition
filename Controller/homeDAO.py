from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5 import MainWindow
import sys,os


from Controller import studentDAO, attendanceDAO
from Controller import classDAO
from View import home

#Khởi tạo các biến.
from database import connectDB

global ui
ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()


def homeDAO():
    ui = home.Ui_home_layout()  # truy cap  toi layout main
    ui.setupUi(MainWindow)
    ui.btnDiemDanh.clicked.connect(even_btnDiemDanh)
    ui.btnDuLieu.clicked.connect(even_btnDiemDanh)
    ui.btnLopHoc.clicked.connect(even_btnLopHoc)
    ui.btnSinhVien.clicked.connect(even_btnSinhVien)
    ui.btnThoat.clicked.connect(even_btnDiemDanh)
    MainWindow.show()

def even_btnDiemDanh():
    attendanceDAO.attendanceDAO()
def even_btnLopHoc():
    classDAO.classDAO()
def even_btnSinhVien():
    studentDAO.studentDAO()
if __name__ == "__main__":

    homeDAO()






