# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClassManagement.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1232, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, -40, 951, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.label.setObjectName("label")
        self.edtTenLop = QtWidgets.QTextEdit(self.centralwidget)
        self.edtTenLop.setGeometry(QtCore.QRect(40, 130, 281, 51))
        self.edtTenLop.setObjectName("edtTenLop")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.edtCaHoc = QtWidgets.QTextEdit(self.centralwidget)
        self.edtCaHoc.setGeometry(QtCore.QRect(350, 130, 141, 51))
        self.edtCaHoc.setObjectName("edtCaHoc")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(350, 90, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.edtSoPhong = QtWidgets.QTextEdit(self.centralwidget)
        self.edtSoPhong.setGeometry(QtCore.QRect(350, 230, 141, 51))
        self.edtSoPhong.setObjectName("edtSoPhong")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 190, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.edtHocKi = QtWidgets.QTextEdit(self.centralwidget)
        self.edtHocKi.setGeometry(QtCore.QRect(190, 230, 141, 51))
        self.edtHocKi.setObjectName("edtHocKi")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 190, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.btnThemLop = QtWidgets.QPushButton(self.centralwidget)
        self.btnThemLop.setGeometry(QtCore.QRect(40, 770, 121, 41))
        self.btnThemLop.setObjectName("btnThemLop")
        self.btnXoa = QtWidgets.QPushButton(self.centralwidget)
        self.btnXoa.setGeometry(QtCore.QRect(320, 770, 121, 41))
        self.btnXoa.setObjectName("btnXoa")
        self.tableLop = QtWidgets.QTableWidget(self.centralwidget)
        self.tableLop.setGeometry(QtCore.QRect(-20, 310, 771, 441))
        self.tableLop.setObjectName("tableLop")
        self.tableLop.setColumnCount(8)
        self.tableLop.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLop.setHorizontalHeaderItem(7, item)
        self.edtMaLop_SV = QtWidgets.QTextEdit(self.centralwidget)
        self.edtMaLop_SV.setGeometry(QtCore.QRect(770, 120, 201, 51))
        self.edtMaLop_SV.setObjectName("edtMaLop_SV")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(770, 70, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tableSinhVienLopHoc = QtWidgets.QTableWidget(self.centralwidget)
        self.tableSinhVienLopHoc.setGeometry(QtCore.QRect(770, 250, 441, 501))
        self.tableSinhVienLopHoc.setObjectName("tableSinhVienLopHoc")
        self.tableSinhVienLopHoc.setColumnCount(4)
        self.tableSinhVienLopHoc.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVienLopHoc.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVienLopHoc.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVienLopHoc.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVienLopHoc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVienLopHoc.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVienLopHoc.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableSinhVienLopHoc.setHorizontalHeaderItem(3, item)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1000, 70, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.edtMSSV = QtWidgets.QTextEdit(self.centralwidget)
        self.edtMSSV.setGeometry(QtCore.QRect(1000, 120, 211, 51))
        self.edtMSSV.setObjectName("edtMSSV")
        self.btnCapNhatLop = QtWidgets.QPushButton(self.centralwidget)
        self.btnCapNhatLop.setGeometry(QtCore.QRect(180, 770, 121, 41))
        self.btnCapNhatLop.setObjectName("btnCapNhatLop")
        self.btnThemSinhVien = QtWidgets.QPushButton(self.centralwidget)
        self.btnThemSinhVien.setGeometry(QtCore.QRect(790, 200, 121, 41))
        self.btnThemSinhVien.setObjectName("btnThemSinhVien")
        self.btnXoaSinhVien = QtWidgets.QPushButton(self.centralwidget)
        self.btnXoaSinhVien.setGeometry(QtCore.QRect(930, 200, 111, 41))
        self.btnXoaSinhVien.setObjectName("btnXoaSinhVien")
        self.btnXoaTatCa = QtWidgets.QPushButton(self.centralwidget)
        self.btnXoaTatCa.setGeometry(QtCore.QRect(1070, 200, 101, 41))
        self.btnXoaTatCa.setObjectName("btnXoaTatCa")
        self.edtKhoaHoc = QtWidgets.QTextEdit(self.centralwidget)
        self.edtKhoaHoc.setGeometry(QtCore.QRect(520, 230, 131, 51))
        self.edtKhoaHoc.setObjectName("edtKhoaHoc")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(510, 190, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.btnXemDanhSach = QtWidgets.QPushButton(self.centralwidget)
        self.btnXemDanhSach.setGeometry(QtCore.QRect(810, 760, 351, 41))
        self.btnXemDanhSach.setObjectName("btnXemDanhSach")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(510, 90, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.edtThu = QtWidgets.QTextEdit(self.centralwidget)
        self.edtThu.setGeometry(QtCore.QRect(510, 130, 141, 51))
        self.edtThu.setObjectName("edtThu")
        self.edtSoBuoi = QtWidgets.QTextEdit(self.centralwidget)
        self.edtSoBuoi.setGeometry(QtCore.QRect(40, 230, 141, 51))
        self.edtSoBuoi.setObjectName("edtSoBuoi")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(40, 190, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1232, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "QU???N L?? L???P H???C"))
        self.label_3.setText(_translate("MainWindow", "T??n l???p"))
        self.label_4.setText(_translate("MainWindow", "Ca h???c"))
        self.label_5.setText(_translate("MainWindow", "S??? ph??ng"))
        self.label_6.setText(_translate("MainWindow", "H???c k??"))
        self.btnThemLop.setText(_translate("MainWindow", "TH??M"))
        self.btnXoa.setText(_translate("MainWindow", "X??A"))
        item = self.tableLop.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableLop.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableLop.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableLop.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "m?? l???p"))
        item = self.tableLop.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "t??n l???p"))
        item = self.tableLop.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "s??? ph??ng"))
        item = self.tableLop.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "h???c k??"))
        item = self.tableLop.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "kh??a"))
        item = self.tableLop.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "ca h???c"))
        item = self.tableLop.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "th???"))
        item = self.tableLop.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "s??? bu???i"))
        self.label_7.setText(_translate("MainWindow", "M?? L???p"))
        item = self.tableSinhVienLopHoc.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableSinhVienLopHoc.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableSinhVienLopHoc.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableSinhVienLopHoc.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "M?? L???p"))
        item = self.tableSinhVienLopHoc.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "t??n l???p"))
        item = self.tableSinhVienLopHoc.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "MSSV"))
        item = self.tableSinhVienLopHoc.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "gi???i T??nh"))
        self.label_8.setText(_translate("MainWindow", "MSSV"))
        self.btnCapNhatLop.setText(_translate("MainWindow", "C???P NH???T"))
        self.btnThemSinhVien.setText(_translate("MainWindow", "TH??M"))
        self.btnXoaSinhVien.setText(_translate("MainWindow", "X??A"))
        self.btnXoaTatCa.setText(_translate("MainWindow", "X??A T???T C???"))
        self.label_9.setText(_translate("MainWindow", "Kh??a H???c"))
        self.btnXemDanhSach.setText(_translate("MainWindow", "XEM DANH S??CH"))
        self.label_10.setText(_translate("MainWindow", "Th???"))
        self.label_11.setText(_translate("MainWindow", "S??? bu???i"))
