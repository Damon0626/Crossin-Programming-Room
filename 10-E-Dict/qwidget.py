# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qwidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QDialog, QApplication
import sys


class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(360, 640)
		Form.setMaximumSize(QtCore.QSize(360, 640))
		self.pushButton = QtWidgets.QPushButton(Form)
		self.pushButton.setGeometry(QtCore.QRect(120, 590, 101, 27))
		self.pushButton.setObjectName("pushButton")
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "Form"))
		self.pushButton.setText(_translate("Form", "词典"))


class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(360, 640)
		Dialog.setMaximumSize(QtCore.QSize(360, 640))
		Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.translateDisplay = QtWidgets.QTextBrowser(Dialog)
		self.translateDisplay.setGeometry(QtCore.QRect(55, 230, 250, 190))
		self.translateDisplay.setMaximumSize(QtCore.QSize(250, 190))
		self.translateDisplay.setObjectName("translateDisplay")
		self.wordDisplay = QtWidgets.QTextBrowser(Dialog)
		self.wordDisplay.setGeometry(QtCore.QRect(55, 161, 250, 50))
		self.wordDisplay.setMaximumSize(QtCore.QSize(250, 50))
		self.wordDisplay.setObjectName("wordDisplay")
		self.translateB = QtWidgets.QPushButton(Dialog)
		self.translateB.setGeometry(QtCore.QRect(150, 490, 81, 27))
		font = QtGui.QFont()
		font.setFamily("AR PL UKai CN")
		self.translateB.setFont(font)
		self.translateB.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.translateB.setObjectName("translateB")
		self.addToReviewBook = QtWidgets.QPushButton(Dialog)
		self.addToReviewBook.setGeometry(QtCore.QRect(250, 490, 81, 27))
		font = QtGui.QFont()
		font.setFamily("AR PL UKai CN")
		self.addToReviewBook.setFont(font)
		self.addToReviewBook.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.addToReviewBook.setObjectName("addToReviewBook")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.translateB.setText(_translate("Dialog", "翻译"))
		self.addToReviewBook.setText(_translate("Dialog", "添加生词"))



class Ui_Dialog(QWidget, Ui_Dialog):
    def __init__(self):
        super(Ui_Dialog,self).__init__()
        self.setupUi(self)

#主界面
class login(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(login, self).__init__()
        self.setupUi(self)
    #定义登录按钮的功能
    def loginEvent(self):
        self.hide()
        self.dia = Ui_Dialog()
        self.dia.show()

#运行窗口Login
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    first=login()
    first.show()
    first.pushButton.clicked.connect(first.loginEvent)
    sys.exit(app.exec_())
