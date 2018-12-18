# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget
import sys


class MainWindow(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(360, 640)
		Form.setMaximumSize(QtCore.QSize(360, 640))
		Form.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.btTranslatePage = QtWidgets.QPushButton(Form)
		self.btTranslatePage.setGeometry(QtCore.QRect(15, 600, 81, 27))
		self.btTranslatePage.setObjectName("btTranslatePage")
		self.btBookPage = QtWidgets.QPushButton(Form)
		self.btBookPage.setGeometry(QtCore.QRect(95, 600, 81, 27))
		self.btBookPage.setObjectName("btBookPage")
		self.btReviewPage = QtWidgets.QPushButton(Form)
		self.btReviewPage.setGeometry(QtCore.QRect(175, 600, 81, 27))
		self.btReviewPage.setObjectName("btReviewPage")
		self.btMyInfoPage = QtWidgets.QPushButton(Form)
		self.btMyInfoPage.setGeometry(QtCore.QRect(255, 600, 81, 27))
		self.btMyInfoPage.setObjectName("btMyInfoPage")
		self.inputWords = QtWidgets.QTextEdit(Form)
		self.inputWords.setGeometry(QtCore.QRect(55, 140, 250, 75))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.inputWords.sizePolicy().hasHeightForWidth())
		self.inputWords.setSizePolicy(sizePolicy)
		self.inputWords.setMaximumSize(QtCore.QSize(250, 75))
		font = QtGui.QFont()
		font.setPointSize(28)
		font.setItalic(True)
		self.inputWords.setFont(font)
		self.inputWords.setFocusPolicy(QtCore.Qt.StrongFocus)
		self.inputWords.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.inputWords.setAutoFillBackground(False)
		self.inputWords.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.inputWords.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.inputWords.setMidLineWidth(0)
		self.inputWords.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
		self.inputWords.setObjectName("inputWords")
		self.btTranslate = QtWidgets.QPushButton(Form)
		self.btTranslate.setGeometry(QtCore.QRect(150, 490, 81, 27))
		font = QtGui.QFont()
		font.setFamily("AR PL UKai CN")
		self.btTranslate.setFont(font)
		self.btTranslate.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.btTranslate.setObjectName("btTranslate")
		self.textviewTranslate = QtWidgets.QTextBrowser(Form)
		self.textviewTranslate.setGeometry(QtCore.QRect(55, 230, 250, 190))
		self.textviewTranslate.setMaximumSize(QtCore.QSize(250, 190))
		self.textviewTranslate.setObjectName("textviewTranslate")
		self.btAddToBook = QtWidgets.QPushButton(Form)
		self.btAddToBook.setGeometry(QtCore.QRect(250, 490, 81, 27))
		font = QtGui.QFont()
		font.setFamily("AR PL UKai CN")
		self.btAddToBook.setFont(font)
		self.btAddToBook.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.btAddToBook.setObjectName("btAddToBook")

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "词典"))
		self.btTranslatePage.setText(_translate("Form", "翻译"))
		self.btBookPage.setText(_translate("Form", "生词本"))
		self.btReviewPage.setText(_translate("Form", "记单词"))
		self.btMyInfoPage.setText(_translate("Form", "我的"))
		self.btTranslate.setText(_translate("Form", "翻译"))
		self.btAddToBook.setText(_translate("Form", "添加生词"))


class ReviewBook(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(360, 640)
		Dialog.setMaximumSize(QtCore.QSize(360, 640))
		Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")



		self.scrollArea = QtWidgets.QScrollArea(Dialog)
		self.scrollArea.setGeometry(QtCore.QRect(55, 40, 250, 490))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")

		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setMinimumSize(250, 2000)
		# self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 250, 480))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

		# self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
		# self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 250, 481))
		# self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.addWidget(self.scrollArea)


		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		for i in range(50):
			self.mapbutton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
			self.mapbutton.setText(str(i*10))
			self.mapbutton.move(10, i*40)

		Dialog.setLayout(self.verticalLayout)

		self.translateB = QtWidgets.QPushButton(Dialog)
		self.translateB.setGeometry(QtCore.QRect(240, 550, 81, 27))
		font = QtGui.QFont()
		font.setFamily("AR PL UKai CN")
		self.translateB.setFont(font)
		self.translateB.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.translateB.setObjectName("translateB")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
		self.translateB.setText(_translate("Dialog", "删除"))


class pageOfReviewBook(QWidget, ReviewBook):
	def __init__(self):
		super(pageOfReviewBook,self).__init__()
		self.setupUi(self)

# 主界面
class displayPages(QtWidgets.QMainWindow, MainWindow):
	def __init__(self):
		super(displayPages, self).__init__()
		self.setupUi(self)

	def clickEvents(self):
		self.hide()
		self.por = pageOfReviewBook()
		self.por.show()


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWindow = displayPages()
	mainWindow.show()
	mainWindow.btBookPage.clicked.connect(mainWindow.clickEvents)
	sys.exit(app.exec_())