import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import  sqlite3
class Home(QDialog):
    def __init__(self):
        super(Home, self).__init__()
        loadUi("home.ui",self)
        self.push_info.clicked.connect(self.gotoinfo)
        self.push_diem_v1.clicked.connect(self.goto_diem_v1)

    def gotoinfo(self):
        info = in_fo()
        widget.addWidget(info)
        widget.setCurrentIndex(widget.currentIndex() + 1)
    def goto_diem_v1(self):
        diem_v1 = diemv1()
        widget.addWidget(diem_v1)
        widget.setCurrentIndex(widget.currentIndex() + 1)




class in_fo(QDialog):
    def __init__(self):
        super(in_fo, self).__init__()
        loadUi("in_fo.ui",self)

class diemv1(QDialog):
    def __init__(self):
        super(diemv1, self).__init__()
        loadUi("nhap_diem_vong_1.ui",self)
app=QApplication(sys.argv)
Homes = Home()
widget = QtWidgets.QStackedWidget()
widget.addWidget(Homes)
widget.setFixedHeight(650)
widget.setFixedWidth(700)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
