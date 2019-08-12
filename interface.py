# pyuic5 foo.ui > foo.py
# Form implementation generated from reading ui file 'interface.ui'
# Created by: PyQt5 UI code generator 5.12.2
# 2019-06-06

# This is main interface for the Identifier

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 212)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 10, 381, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_data = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_data.setObjectName("button_data")
        self.gridLayout_2.addWidget(self.button_data, 1, 1, 1, 1)
        self.button_database = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.button_database.setObjectName("button_database")
        self.gridLayout_2.addWidget(self.button_database, 0, 1, 1, 1)
        self.label_data = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_data.setText("")
        self.label_data.setObjectName("label_data")
        self.gridLayout_2.addWidget(self.label_data, 1, 0, 1, 1)
        self.label_database = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_database.setText("")
        self.label_database.setObjectName("label_database")
        self.gridLayout_2.addWidget(self.label_database, 0, 0, 1, 1)
        self.button_run = QtWidgets.QPushButton(self.centralwidget)
        self.button_run.setGeometry(QtCore.QRect(40, 100, 381, 91))
        self.button_run.setObjectName("button_run")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("IdentifierSP", "IdentifierSP"))
        self.button_data.setText(_translate("MainWindow", "Select data"))
        self.button_database.setText(_translate("MainWindow", "Select database"))
        self.button_run.setText(_translate("MainWindow", "Run identification"))


