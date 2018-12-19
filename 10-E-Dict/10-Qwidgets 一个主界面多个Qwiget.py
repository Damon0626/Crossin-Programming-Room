# -*- coding: utf-8 -*-

# @Author: Damon0626
# @Time  : 18-12-19 下午8:24
# @Email : wwymsn@163.com
# @Software: PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import hashlib
import requests
import json


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(360, 640)
		MainWindow.setMaximumSize(QtCore.QSize(360, 640))
		MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.page(MainWindow)
		self.btTranslatePage = QtWidgets.QPushButton(self.centralwidget)
		self.btTranslatePage.setGeometry(QtCore.QRect(15, 555, 81, 27))
		self.btTranslatePage.setObjectName("btTranslatePage")
		self.btReviewPage = QtWidgets.QPushButton(self.centralwidget)
		self.btReviewPage.setGeometry(QtCore.QRect(175, 555, 81, 27))
		self.btReviewPage.setObjectName("btReviewPage")
		self.btMyInfoPage = QtWidgets.QPushButton(self.centralwidget)
		self.btMyInfoPage.setGeometry(QtCore.QRect(255, 555, 81, 27))
		self.btMyInfoPage.setObjectName("btMyInfoPage")
		self.btBookPage = QtWidgets.QPushButton(self.centralwidget)
		self.btBookPage.setGeometry(QtCore.QRect(95, 555, 81, 27))
		self.btBookPage.setObjectName("btBookPage")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 25))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		font = QtGui.QFont()
		font.setFamily("URW Chancery L")
		font.setPointSize(9)
		font.setItalic(True)
		self.statusbar.setFont(font)
		self.statusbar.showMessage("Created by Damon0626")
		MainWindow.setStatusBar(self.statusbar)
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	# 主页面
	def page(self, MainWindow):
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.widget = QtWidgets.QWidget(self.centralwidget)
		self.widget.setGeometry(QtCore.QRect(0, 0, 360, 500))
		self.widget.setObjectName("widget")
		self.context1()

	# 翻译页面
	def context1(self):
		self.btAddToBook = QtWidgets.QPushButton(self.widget)
		self.btAddToBook.setGeometry(QtCore.QRect(150, 420, 81, 27))
		font = QtGui.QFont()
		font.setFamily("AR PL UKai CN")
		self.btAddToBook.setFont(font)
		self.btAddToBook.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.btAddToBook.setObjectName("btAddToBook")
		self.btTranslate = QtWidgets.QPushButton(self.widget)
		self.btTranslate.setGeometry(QtCore.QRect(250, 420, 81, 27))
		font = QtGui.QFont()
		font.setFamily("AR PL UKai CN")
		self.btTranslate.setFont(font)
		self.btTranslate.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.btTranslate.setObjectName("btTranslate")

		self.inputWords = QtWidgets.QTextEdit(self.widget)
		self.inputWords.setGeometry(QtCore.QRect(60, 100, 250, 75))
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
		self.inputWords.setFrameShape(QtWidgets.QFrame.Box)
		self.inputWords.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.inputWords.setMidLineWidth(0)
		self.inputWords.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
		self.inputWords.setObjectName("inputWords")
		self.textviewTranslate = QtWidgets.QTextBrowser(self.widget)
		self.textviewTranslate.setGeometry(QtCore.QRect(60, 190, 250, 190))
		self.textviewTranslate.setMaximumSize(QtCore.QSize(250, 190))
		self.textviewTranslate.setObjectName("textviewTranslate")

	def context2(self):
		self.translateB = QtWidgets.QPushButton(self.widget)
		self.translateB.setGeometry(QtCore.QRect(170, 420, 81, 27))
		font = QtGui.QFont()
		font.setFamily("AR PL UKai CN")
		self.translateB.setFont(font)
		self.translateB.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.translateB.setObjectName("translateB")
		self.wordsToReview = QtWidgets.QTextBrowser(self.widget)
		self.wordsToReview.setGeometry(QtCore.QRect(40, 90, 250, 75))
		self.wordsToReview.setObjectName("wordsToReview")
		self.textviewTranslate = QtWidgets.QTextBrowser(self.widget)
		self.textviewTranslate.setGeometry(QtCore.QRect(40, 190, 250, 190))
		self.textviewTranslate.setMaximumSize(QtCore.QSize(250, 190))
		self.textviewTranslate.setObjectName("textviewTranslate")
		self.translateB_2 = QtWidgets.QPushButton(self.widget)
		self.translateB_2.setGeometry(QtCore.QRect(270, 420, 81, 27))
		font = QtGui.QFont()
		font.setFamily("AR PL UKai CN")
		self.translateB_2.setFont(font)
		self.translateB_2.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.translateB_2.setObjectName("translateB_2")
	# 主页面翻译按钮
	def tranlate(self):
		info = self.inputWords.toPlainText()
		translate_info = self.baidu_trans(info)
		translate_info = str(translate_info)
		self.textviewTranslate.setText(translate_info)

	# 初始化总页面
	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		# if context == 1:
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.btAddToBook.setText(_translate("MainWindow", "添加生词"))
		self.btTranslate.setText(_translate("MainWindow", "翻译"))
		self.btTranslatePage.setText(_translate("MainWindow", "翻译"))
		self.btReviewPage.setText(_translate("MainWindow", "记单词"))
		self.btMyInfoPage.setText(_translate("MainWindow", "我的"))
		self.btBookPage.setText(_translate("MainWindow", "生词本"))
		# elif context == 2:
		# 	MainWindow.setWindowTitle(_translate("Dialog", "Dialog"))
		# 	self.translateB.setText(_translate("Dialog", " 提示"))
		# 	self.translateB_2.setText(_translate("Dialog", "下一词"))


	# 百度翻译API
	def baidu_trans(self, info):
		appid = "20180603000171420"
		key = "ae116ExDtMKb0Bhoqb5Y"
		salt = "1435660288"
		all = appid + info + salt + key
		m = hashlib.md5()
		m.update(all.encode())
		sign = m.hexdigest()
		src = info.replace(' ', '+')  # 生成sign前不能替换
		url = "http://api.fanyi.baidu.com/api/trans/vip/translate?q=" + src + "&from=en&to=zh&appid=" + appid + "&salt=" + salt + "&sign=" + sign

		try:
			req = requests.post(url)
			data = req.json()
			return data['trans_result'][0]['dst']
		except:
			return "出错了"

	def change(self):
		self.pagenum = 2
		m = QtWidgets.QMainWindow()
		self.setupUi(m)
		m.show()


if __name__ == "__main__":
	import sys

	app = QApplication(sys.argv)
	m = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(m)
	ui.btTranslate.clicked.connect(ui.tranlate)
	m.show()
	sys.exit(app.exec_())


