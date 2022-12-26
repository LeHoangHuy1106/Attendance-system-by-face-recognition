from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from matplotlib.backends.backend_qt5 import MainWindow
import sys,os
import cv2
from Controller import method,homeDAO
from View import StudentManagement, ClassManagement

from database import connectDB
#Khởi tạo các biến.
global ui
ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def classDAO():
    global ui
    ui = ClassManagement.Ui_MainWindow()  # truy cap  toi layout main
    ui.setupUi(MainWindow)
    ui.btnThemLop.clicked.connect(even_btnThemLop)
    ui.btnXoa.clicked.connect(even_btnXoa)
    ui.btnXemDanhSach.clicked.connect(even_btnXemDanhSach)
    ui.btnThemSinhVien.clicked.connect(even_btnThemSinhVien)

    table_DanhSachLopHoc()


    MainWindow.show()




def even_btnXemDanhSach():
    table_DanhSachSinhVienLopHoc()
def even_btnXoa():
    global ui
    ui.edtTenLop.setText("")
    ui.edtCaHoc.setText("")
    ui.edtHocKi.setText("")
    ui.edtSoPhong.setText("")
    ui.edtKhoaHoc.setText("")


def even_btnThemLop():
    global ui
    tenLop = (ui.edtTenLop.toPlainText()).strip()
    caHoc = ui.edtCaHoc.toPlainText().strip()
    hocKi = ui.edtHocKi.toPlainText().strip()
    soPhong = ui.edtSoPhong.toPlainText().strip()
    khoaHoc = ui.edtKhoaHoc.toPlainText().strip()
    thu = ui.edtThu.toPlainText().strip()
    soBuoi = ui.edtSoBuoi.toPlainText().strip()

    checkInputAddClass(tenLop, caHoc, hocKi, soPhong, khoaHoc,thu,soBuoi)


def checkInputAddClass(tenLop, caHoc, hocKi, soPhong, khoaHoc,thu,soBuoi):

    if(len(tenLop)==0):
        method.message('Bạn chưa nhập tên lớp')
    elif(len(caHoc)==0):
        method.message('Bạn chưa nhập ca học')
    elif(len(hocKi)==0):
        method.message('Bạn chưa nhập học kì')
    elif(len(soPhong)==0):
        method.message('Bạn chưa nhập số phòng')
    elif(len(khoaHoc)==0):
        method.message('Bạn chưa nhập khóa học')
    elif (len(thu) == 0):
        method.message('Bạn chưa nhập thứ học trong tuần ')
    elif(len(soBuoi)==0):
        method.message('Bạn chưa nhập số buổi học')

    else:
        tenlop = "'" + tenLop + "'"
        cahoc = "'" + caHoc.upper() + "'"
        hocki = "'" + hocKi.upper() + "'"
        sophong = "'" + soPhong.upper() + "'"
        khoahoc = "'" + khoaHoc + "'"
        thu2 =  "'Thu" + thu + "'"
        maLop =  thu.upper()+ '_' + caHoc.upper()+'_' +hocKi.upper() +'_'+ soPhong.upper() + '_' + khoaHoc
        query = "SELECT COUNT(*) FROM Class where maLop =" +"'" +maLop +"'"
        if (int(connectDB.getData(query)[0][0]) > 0):
            method.message('Lớp này đã tồn tại')
        else:
            query = "INSERT INTO Class  Values(" + "'" +maLop +"'"+ "," + tenlop + "," + khoahoc + "," + hocki + "," + thu2 +","+ cahoc +"," +sophong +","+ soBuoi+ ")"
            print(query)
            connectDB.setData(query)
            table_DanhSachLopHoc()
            method.message('Thêm  lớp học thành công')
            even_btnXoa()

def even_btnThemSinhVien():
    global ui
    edtMaLop = (ui.edtMaLop_SV.toPlainText()).strip()
    edtMSSV = ui.edtMSSV.toPlainText().strip()
    if (len(edtMaLop) == 0):
        method.message('Bạn chưa nhập  mã lớp')
    elif (len(edtMSSV) == 0):
        method.message('Bạn chưa nhập MSSV')
    else:
        malop = "'" + edtMaLop.upper() + "'"
        mssv = "'" + edtMSSV.upper() + "'"

        query = "SELECT COUNT(*) FROM Class where maLop ="+ malop
        if (int(connectDB.getData(query)[0][0]) == 0):
            method.message('Lớp này không tồn tại')
        else:
            query = "select count(*) from attendance where MSSV =" + mssv + "AND maLop =" + malop
            if (int(connectDB.getData(query)[0][0]) > 0):
                method.message('Sinh viên đã có trong lớp này')
            else:

                query = "INSERT INTO attendance Values("  + mssv  + "," + malop + "," + '1' + "," + '0' + "," + "'Null')"
                connectDB.setData(query)
                table_DanhSachSinhVienLopHoc();
                method.message('Thêm  lớp học thành công')
                ui.edtMSSV.setText("")
















def table_DanhSachLopHoc():
    global ui

    dslh = connectDB.getData("select * from Class")
    print(dslh)
    ui.tableLop.setRowCount(len(dslh))
    for i in range(0, len(dslh)):

        ui.tableLop.setItem(i, 0,  QtWidgets.QTableWidgetItem(str(dslh[i][0])))
        ui.tableLop.setItem(i, 1,  QtWidgets.QTableWidgetItem(str(dslh[i][1])))
        ui.tableLop.setItem(i, 2, QtWidgets.QTableWidgetItem(str(dslh[i][6])))
        ui.tableLop.setItem(i, 3, QtWidgets.QTableWidgetItem(str(dslh[i][3])))
        ui.tableLop.setItem(i, 4, QtWidgets.QTableWidgetItem(str(dslh[i][2])))
        ui.tableLop.setItem(i, 5, QtWidgets.QTableWidgetItem(str(dslh[i][5])))
        ui.tableLop.setItem(i, 6, QtWidgets.QTableWidgetItem(str(dslh[i][4])))
        ui.tableLop.setItem(i, 7, QtWidgets.QTableWidgetItem(str(dslh[i][7])))

def table_DanhSachSinhVienLopHoc():
    global ui
    maLopSV = (ui.edtMaLop_SV.toPlainText()).strip()
    if (len(maLopSV) == 0):
        method.message('Bạn chưa nhập mã lớp')
    else:
        query = "select Class.maLop,Class.tenLop,Student.MSSV, Student.hoVaTen, Student.gioiTinh   from attendance, student, class where class.maLop =  attendance.maLop and student.MSSV =  attendance.MSSV  and Class.maLop='"+maLopSV+ "' group by (student.MSSV)"
        dslhsv  = connectDB.getData(query)
        ui.tableSinhVienLopHoc.setRowCount(0)
        ui.tableSinhVienLopHoc.setRowCount(len(dslhsv))
        print(dslhsv)
        for i in range(0, len(dslhsv)):
            ui.tableSinhVienLopHoc.setItem(i,0, QtWidgets.QTableWidgetItem(str(dslhsv[i][0])))
            ui.tableSinhVienLopHoc.setItem(i,1, QtWidgets.QTableWidgetItem(str(dslhsv[i][1])))
            ui.tableSinhVienLopHoc.setItem(i,2, QtWidgets.QTableWidgetItem(str(dslhsv[i][2])))
            ui.tableSinhVienLopHoc.setItem(i,3, QtWidgets.QTableWidgetItem(str(dslhsv[i][3])))
            ui.tableSinhVienLopHoc.setItem(i,4, QtWidgets.QTableWidgetItem(str(dslhsv[i][4])))




