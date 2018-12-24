# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-23 下午9:25
# @Email : wwymsn@163.com
# @Software: PyCharm

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
import csv
import os
import datetime


class MainWindow(QDialog):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle("电子辞典")
		self.resize(360, 640)
		self.setMinimumSize(QSize(360, 640))
		self.setStyleSheet("background-color: rgb(255, 255, 255)")

		# 翻译页按钮
		self.btTranslatePage = QPushButton(self)
		self.btTranslatePage.setGeometry(QRect(15, 555, 81, 27))
		self.btTranslatePage.setObjectName("btTranslatePage")


		# 复习页按钮
		self.btReviewPage = QPushButton(self)
		self.btReviewPage.setGeometry(QRect(175, 555, 81, 27))
		self.btReviewPage.setObjectName("btReviewPage")

		# 个人信息页按钮
		self.btMyInfoPage = QPushButton(self)
		self.btMyInfoPage.setGeometry(QRect(255, 555, 81, 27))
		self.btMyInfoPage.setObjectName("btMyInfoPage")

		# 生词本页按钮
		self.btBookPage = QPushButton(self)
		self.btBookPage.setGeometry(QRect(95, 555, 81, 27))
		self.btBookPage.setObjectName("btBookPage")

		# 菜单栏
		self.menubar = QMenuBar(self)
		self.menubar.setGeometry(QRect(0, 0, 360, 25))
		self.menubar.setObjectName("menubar")
		# self.setMenuBar(self.menubar)

		# 状态栏
		self.statusbar = QStatusBar(self)
		self.statusbar.setObjectName("statusbar")
		font = QFont()
		font.setFamily("URW Chancery L")
		font.setPointSize(9)
		font.setItalic(True)
		self.statusbar.setFont(font)
		self.statusbar.setGeometry(0, 618, 360, 22)
		self.statusbar.showMessage("Created by Damon0626")

		self.btTranslatePage.setText("翻译")
		self.btReviewPage.setText("记单词")
		self.btMyInfoPage.setText("我的")
		self.btBookPage.setText("生词本")

		self.btTranslatePage.clicked.connect(self.showTranslatePage)
		self.btReviewPage.clicked.connect(self.showReviewPage)

	def showTranslatePage(self):
		self.translatepage = QFrame(self)
		self.translatepage.resize(360, 500)

		# 添加生词按钮
		self.btAddToBook = QPushButton(self.translatepage)
		self.btAddToBook.setGeometry(QRect(150, 420, 81, 27))
		font = QFont()
		font.setFamily("AR PL UKai CN")
		self.btAddToBook.setFont(font)
		self.btAddToBook.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.btAddToBook.setObjectName("btAddToBook")
		self.btAddToBook.clicked.connect(self.btAddToBookFunc)  # 添加生词按钮的信号

		# 翻译按钮
		self.btTranslate = QPushButton(self.translatepage)
		self.btTranslate.setGeometry(QRect(250, 420, 81, 27))
		font = QFont()
		font.setFamily("AR PL UKai CN")
		self.btTranslate.setFont(font)
		self.btTranslate.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.btTranslate.setObjectName("btTranslate")
		self.btTranslate.clicked.connect(self.btTranslateFunc)  # 翻译按钮的信号

		# 输入框QLineEdit
		self.inputwords = QLineEdit(self.translatepage)
		self.info = self.inputwords.text()
		self.inputwords.setGeometry(QRect(60, 100, 250, 75))
		font = QFont()
		font.setPointSize(18)
		self.inputwords.setFont(font)
		self.inputwords.setMaxLength(100)
		self.inputwords.setFrame(False)
		self.inputwords.setAlignment(Qt.AlignCenter)
		self.inputwords.setObjectName("inputwords")
		self.inputwords.setPlaceholderText("在此输入单词或句子")

		# 翻译输出框
		self.textviewTranslate = QTextBrowser(self.translatepage)
		self.textviewTranslate.setGeometry(QRect(60, 190, 250, 190))
		self.textviewTranslate.setMaximumSize(QSize(250, 190))
		self.textviewTranslate.setObjectName("textviewTranslate")

		self.btAddToBook.setText("添加生词")
		self.btTranslate.setText("翻译")
		self.translatepage.setVisible(True)

	def showReviewPage(self):
		self.reviewpage = QFrame(self)
		self.reviewpage.resize(360, 500)
		ReviewPage.reviewPageUi(self, self.reviewpage)
		self.reviewpage.setVisible(True)

	def btTranslateFunc(self): # 翻译按钮
		info = self.inputwords.text()
		text = Functions.jinshanTranslateAPI(self, info)
		self.textviewTranslate.setText(text)

	def btAddToBookFunc(self):
		info = self.inputwords.text()
		flag = Functions.addToBook(self, info)
		print(info)
		if not flag:
			QMessageBox.information(self, '提示', '已添加成功！', QMessageBox.Yes)
		else:
			QMessageBox.information(self, '提示', '已存在！', QMessageBox.Yes)

class ReviewPage(QDialog):
	def __init__(self, *args, **kwargs):
		super().__init__(self, *args, **kwargs)

	def reviewPageUi(self, Form):
		self.btTips = QPushButton(Form)
		self.btTips.setGeometry(QRect(150, 420, 81, 27))
		font = QFont()
		font.setFamily("AR PL UKai CN")
		self.btTips.setFont(font)
		self.btTips.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.btTips.setObjectName("btTips")

		# 复习单词显示框
		self.wordsToReview = QTextBrowser(Form)
		self.wordsToReview.setGeometry(QRect(60, 90, 250, 75))
		self.wordsToReview.setObjectName("wordsToReview")

		# 复习单词提示框
		self.textviewTranslate = QTextBrowser(Form)
		self.textviewTranslate.setGeometry(QRect(60, 190, 250, 190))
		self.textviewTranslate.setMaximumSize(QSize(250, 190))
		self.textviewTranslate.setObjectName("textviewTranslate")

		# 下一个按钮
		self.btNextWord = QPushButton(Form)
		self.btNextWord.setGeometry(QRect(250, 420, 81, 27))
		font = QFont()
		font.setFamily("AR PL UKai CN")
		self.btNextWord.setFont(font)
		self.btNextWord.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.btNextWord.setObjectName("btNextWord")

		self.btTips.setText("提示")
		self.btNextWord.setText("下一词")


class Functions(object):
	def jinshanTranslateAPI(self, info):
		info = info.lower()
		type = 'json'
		myurl = "http://dict-co.iciba.com/api/dictionary.php?w=" + info + "&type=" + type + "&key=28F8C6AEF4586DF52E9C74E958528DB1"

		try:
			req = requests.post(myurl)
			data = req.json()
			text = []
			text.append(str([data['symbols'][0]['ph_en']]))
			for i in data['symbols'][0]['parts']:
				text.append(str(i['part']) + ' ' + str(','.join(i['means'])))
			return '\n'.join(text)
		except:
			return "Error:\n place check for your network or input something..."

	def addToBook(self, info):
		if os.path.exists('dic.csv'):
			flag = Functions.readCSV(self, './dic.csv', info)
			# print('flag ==  ', flag)
			if flag:
				return 1
			else:
				print(info)
				Functions.writeCSV(self, './dic.csv', info)
				print('yes already')
		else:
			with open('./dic.csv', "w+", newline='') as file:
				csv_file = csv.writer(file)
				head = ['words', 'means', 'insert_time', 'have_review_times']
				csv_file.writerow(head)

	def readCSV(self, path, info):  # 判断是否在词典内
		with open(path, 'r') as f:
			reader = csv.reader(f)
			if info in [row[::][0] for row in reader]:
				return 1
			else:
				return 0

	def writeCSV(self, path, info):  # 插入词典
		time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		with open(path, "a+", newline='') as file:
			csv_file = csv.writer(file)
			data = [info, ['None'], [time], [0]]
			csv_file.writerow(data)



if __name__ == "__main__":
	app = QApplication(sys.argv)
	# dialog = logindialog()
	# if dialog.exec_()==QDialog.Accepted:
	the_window = MainWindow()
	the_window.show()
	sys.exit(app.exec_())