from PyQt5 import QtCore, QtGui, QtWidgets
from RR_info import Ui_RR_info
from SJF_non import Ui_SJF_non_info
from priority_non import Ui_priority_non_info


class Ui_first(object):

    def open_SJF_non(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SJF_non_info()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def open_RR(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RR_info()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def open_Priority_non(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_priority_non_info()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def setupUi(self, first):
        
        first.setObjectName("first")
        first.resize(520, 485)
        self.centralwidget = QtWidgets.QWidget(first)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 41))
        self.label.setObjectName("label")
        
        self.SJFnon_but = QtWidgets.QPushButton(self.centralwidget)
        self.SJFnon_but.setGeometry(QtCore.QRect(200, 150, 121, 31))
        self.SJFnon_but.setObjectName("SJFnon_but")

        self.SJFnon_but.clicked.connect(self.open_SJF_non)

        
        self.RR_but = QtWidgets.QPushButton(self.centralwidget)
        self.RR_but.setGeometry(QtCore.QRect(200, 220, 121, 31))
        self.RR_but.setObjectName("RR_but")

        self.RR_but.clicked.connect(self.open_RR)


        
        self.Prioritynon_but = QtWidgets.QPushButton(self.centralwidget)
        self.Prioritynon_but.setGeometry(QtCore.QRect(200, 300, 121, 31))
        self.Prioritynon_but.setObjectName("Prioritynon_but")

        self.Prioritynon_but.clicked.connect(self.open_Priority_non)
        
        first.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(first)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setObjectName("menubar")
        first.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(first)
        self.statusbar.setObjectName("statusbar")
        first.setStatusBar(self.statusbar)

        self.retranslateUi(first)
        QtCore.QMetaObject.connectSlotsByName(first)

    def retranslateUi(self, first):
        _translate = QtCore.QCoreApplication.translate
        first.setWindowTitle(_translate("first", "CPU Scheduler"))
        self.label.setText(_translate("first", ""))
        self.SJFnon_but.setText(_translate("first", "NonPre - SJF "))
        self.RR_but.setText(_translate("first", "Round Robin"))
        self.Prioritynon_but.setText(_translate("first", "NonPre - Priority "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    first = QtWidgets.QMainWindow()
    ui = Ui_first()
    ui.setupUi(first)
    first.show()
    sys.exit(app.exec_())
