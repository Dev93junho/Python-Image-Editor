# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
# from engine import dataloader

class Ui_AirNote(object):
    def setupUi(self, AirNote):
        AirNote.setObjectName("AirNote")
        AirNote.resize(1362, 825)
        AirNote.setStyleSheet("background-color : #393636")
        self.centralwidget = QtWidgets.QWidget(AirNote)
        self.centralwidget.setObjectName("centralwidget")
        self.img_view_lg = QtWidgets.QWidget(self.centralwidget)
        self.img_view_lg.setGeometry(QtCore.QRect(350, 50, 641, 481))
        self.img_view_lg.setStyleSheet("background-color : rgb(3, 3, 3)")
        self.img_view_lg.setObjectName("img_view_lg")
        self.gridLayout = QtWidgets.QGridLayout(self.img_view_lg)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 454, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 660, 1300, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.graph_view = QtWidgets.QWidget(self.layoutWidget)
        self.graph_view.setMouseTracking(True)
        self.graph_view.setStyleSheet("background-color : rgba(255, 255, 255, 128)\n"
"")
        self.graph_view.setObjectName("graph_view")
        self.gridLayout_3.addWidget(self.graph_view, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(1298, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_4.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_4.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_4.addWidget(self.checkBox_4, 0, 3, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_4.addWidget(self.checkBox_5, 0, 4, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_4.addWidget(self.checkBox_6, 0, 5, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 560, 1301, 91))
        self.layoutWidget1.setMouseTracking(True)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.img_view_sm = QtWidgets.QWidget(self.layoutWidget1)
        self.img_view_sm.setMouseTracking(True)
        self.img_view_sm.setStyleSheet("background-color : #000000")
        self.img_view_sm.setObjectName("img_view_sm")
        self.gridLayout_2.addWidget(self.img_view_sm, 0, 0, 1, 1)
        self.img_view_sm_2 = QtWidgets.QWidget(self.layoutWidget1)
        self.img_view_sm_2.setMouseTracking(True)
        self.img_view_sm_2.setStyleSheet("background-color : #000000\n"
"")
        self.img_view_sm_2.setObjectName("img_view_sm_2")
        self.gridLayout_2.addWidget(self.img_view_sm_2, 0, 1, 1, 1)
        self.img_view_sm_3 = QtWidgets.QWidget(self.layoutWidget1)
        self.img_view_sm_3.setMouseTracking(True)
        self.img_view_sm_3.setStyleSheet("background-color : #000000\n"
"")
        self.img_view_sm_3.setObjectName("img_view_sm_3")
        self.gridLayout_2.addWidget(self.img_view_sm_3, 0, 2, 1, 1)
        self.img_view_sm_4 = QtWidgets.QWidget(self.layoutWidget1)
        self.img_view_sm_4.setMouseTracking(True)
        self.img_view_sm_4.setStyleSheet("background-color : #000000\n"
"")
        self.img_view_sm_4.setObjectName("img_view_sm_4")
        self.gridLayout_2.addWidget(self.img_view_sm_4, 0, 3, 1, 1)
        self.img_view_sm_5 = QtWidgets.QWidget(self.layoutWidget1)
        self.img_view_sm_5.setMouseTracking(True)
        self.img_view_sm_5.setStyleSheet("background-color : #000000\n"
"")
        self.img_view_sm_5.setObjectName("img_view_sm_5")
        self.gridLayout_2.addWidget(self.img_view_sm_5, 0, 4, 1, 1)
        self.img_view_sm_6 = QtWidgets.QWidget(self.layoutWidget1)
        self.img_view_sm_6.setMouseTracking(True)
        self.img_view_sm_6.setStyleSheet("background-color : #000000\n"
"")
        self.img_view_sm_6.setObjectName("img_view_sm_6")
        self.gridLayout_2.addWidget(self.img_view_sm_6, 0, 5, 1, 1)
        self.img_view_sm_7 = QtWidgets.QWidget(self.layoutWidget1)
        self.img_view_sm_7.setMouseTracking(True)
        self.img_view_sm_7.setStyleSheet("background-color : #000000\n"
"")
        self.img_view_sm_7.setObjectName("img_view_sm_7")
        self.gridLayout_2.addWidget(self.img_view_sm_7, 0, 6, 1, 1)
        self.img_view_sm_8 = QtWidgets.QWidget(self.layoutWidget1)
        self.img_view_sm_8.setMouseTracking(True)
        self.img_view_sm_8.setStyleSheet("background-color : #000000")
        self.img_view_sm_8.setObjectName("img_view_sm_8")
        self.gridLayout_2.addWidget(self.img_view_sm_8, 0, 7, 1, 1)
        self.img_view_sm_9 = QtWidgets.QWidget(self.layoutWidget1)
        self.img_view_sm_9.setMouseTracking(True)
        self.img_view_sm_9.setStyleSheet("background-color : #000000\n"
"")
        self.img_view_sm_9.setObjectName("img_view_sm_9")
        self.gridLayout_2.addWidget(self.img_view_sm_9, 0, 8, 1, 1)
        self.img_view_sm_10 = QtWidgets.QWidget(self.layoutWidget1)
        self.img_view_sm_10.setMouseTracking(True)
        self.img_view_sm_10.setStyleSheet("background-color : #000000\n"
"")
        self.img_view_sm_10.setObjectName("img_view_sm_10")
        self.gridLayout_2.addWidget(self.img_view_sm_10, 0, 9, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1290, 30, 41, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.filedialog)
        
        
        AirNote.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AirNote)
        self.statusbar.setObjectName("statusbar")
        AirNote.setStatusBar(self.statusbar)

        self.retranslateUi(AirNote)
        QtCore.QMetaObject.connectSlotsByName(AirNote)

    def retranslateUi(self, AirNote):
        _translate = QtCore.QCoreApplication.translate
        AirNote.setWindowTitle(_translate("AirNote", "MainWindow"))
        self.checkBox.setText(_translate("AirNote", "min_x"))
        self.checkBox_2.setText(_translate("AirNote", "min_y"))
        self.checkBox_3.setText(_translate("AirNote", "min_z"))
        self.checkBox_4.setText(_translate("AirNote", "fist_x"))
        self.checkBox_5.setText(_translate("AirNote", "fist_y"))
        self.checkBox_6.setText(_translate("AirNote", "fist_z"))
        self.pushButton.setText(_translate("AirNote", "o"))

    def filedialog(self):
        fname = QFileDialog.getOpenFileName(self)
        print(fname)
        # self.label.setPixmap(QPixmap(fname[0]))
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AirNote = QtWidgets.QMainWindow()
    ui = Ui_AirNote()
    ui.setupUi(AirNote)
    AirNote.show()
    sys.exit(app.exec_())
