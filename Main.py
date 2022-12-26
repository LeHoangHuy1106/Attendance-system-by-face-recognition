from database import connectDB
from Controller import homeDAO,studentDAO
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5 import MainWindow
import sys,os

global ui
ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

if __name__ == "__main__":
    homeDAO.homeDAO()


sys.exit(app.exec_())