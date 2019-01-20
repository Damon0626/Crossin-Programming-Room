# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-12-23 下午9:25
# @Email : wwymsn@163.com
# @Software: PyCharm

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import requests
import csv
import os
import datetime
import pandas as pd
import numpy as np


class MainWindow(QDialog):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle("电子辞典")
		self.resize(360, 640)
		self.setMinimumSize(QSize(360, 640))
		self.setStyleSheet("background-color: rgb(255, 255, 255)")

		# 每日一句
		'''提头'''
		self.daily_sentence_title = QLabel(self)
		self.daily_sentence_title.setGeometry(QRect(0, 0, 360, 40))
		font = QFont()
		font.setPixelSize(20)
		# font.setBold(True)
		self.daily_sentence_title.setFont(font)
		self.daily_sentence_title.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(41, 196, 242)")

		self.daily_sentence_title.setText("  每日一句")

		'''图片'''
		self.daily_sentence_pic = QLabel(self)
		self.daily_sentence_pic.setGeometry(QRect(30, 45, 300, 170))
		self.daily_sentence_pic.setPixmap(Functions.getImageData(self))
		self.daily_sentence_pic.setAlignment(Qt.AlignCenter)

		'''句子'''
		self.daily_sentence_sentence_eng = QTextBrowser(self)
		self.daily_sentence_sentence_eng.setGeometry(QRect(30, 240, 300, 80))
		self.daily_sentence_sentence_eng.setStyleSheet("color: rgb(0, 74, 128)")
		font = QFont()
		font.setBold(True)
		font.setPixelSize(15)
		self.daily_sentence_sentence_eng.setFont(font)
		self.daily_sentence_sentence_eng.setText(Functions.getEngSentence(self))
		self.daily_sentence_sentence_eng.setFrameShape(QtWidgets.QFrame.NoFrame)

		'''翻译'''
		self.daily_sentence_sentence_chs = QTextBrowser(self)
		self.daily_sentence_sentence_chs.setGeometry(QRect(30, 330, 300, 80))
		font = QFont()
		font.setBold(True)
		font.setPixelSize(15)
		self.daily_sentence_sentence_chs.setFont(font)
		self.daily_sentence_sentence_chs.setText(Functions.getChsSentence(self))
		self.daily_sentence_sentence_chs.setFrameShape(QtWidgets.QFrame.NoFrame)

		'''注释'''
		self.daily_sentence_ps = QTextBrowser(self)
		self.daily_sentence_ps.setGeometry(QRect(30, 410, 300, 120))
		self.daily_sentence_ps.setText(Functions.getPS(self)+'\n\n'+Functions.getDateLine(self))
		self.daily_sentence_ps.setFrameShape(QtWidgets.QFrame.NoFrame)


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

		# 按钮的连接
		self.btTranslatePage.clicked.connect(self.showTranslatePage)
		self.btReviewPage.clicked.connect(self.showReviewPage)
		self.btBookPage.clicked.connect(self.showBookPage)

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
		self.btAddToBook.setEnabled(False)
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

		# 获取数据
		self.data = self.createTables()
		self.reviewWordLoc = self.getRandomMinLoc()

		# 复习单词显示框
		self.wordsToReview = QTextBrowser(self.reviewpage)
		self.wordsToReview.setGeometry(QRect(60, 90, 250, 75))
		self.wordsToReview.setObjectName("wordsToReview")
		self.wordsToReview.setText(self.data['words'][self.reviewWordLoc])  # 次数最少的随机一个单词
		font = QFont()
		font.setPointSize(25)
		self.wordsToReview.setFont(font)
		self.wordsToReview.setAlignment(Qt.AlignCenter)

		# 复习单词提示框
		self.textviewTranslate = QTextBrowser(self.reviewpage)
		self.textviewTranslate.setGeometry(QRect(60, 190, 250, 190))
		self.textviewTranslate.setMaximumSize(QSize(250, 190))
		self.textviewTranslate.setObjectName("textviewTranslate")

		# 提示按钮
		self.btTips = QPushButton(self.reviewpage)
		self.btTips.setGeometry(QRect(150, 420, 81, 27))
		font = QFont()
		font.setFamily("AR PL UKai CN")
		self.btTips.setFont(font)
		self.btTips.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.btTips.setObjectName("btTips")
		self.btTips.setText("提示")
		self.btTips.clicked.connect(self.tipsInformation)

		# 下一个按钮
		self.btNextWord = QPushButton(self.reviewpage)
		self.btNextWord.setGeometry(QRect(250, 420, 81, 27))
		font = QFont()
		font.setFamily("AR PL UKai CN")
		self.btNextWord.setFont(font)
		self.btNextWord.setStyleSheet("background-color: rgb(255, 170, 127);")
		self.btNextWord.setObjectName("btNextWord")
		self.btNextWord.setText("下一词")
		self.reviewpage.setVisible(True)
		self.btNextWord.clicked.connect(self.nextWordPlus1)

	def showBookPage(self):
		self.bookpage = QFrame(self)
		self.bookpage.resize(360, 500)
		self.wordstable = QtWidgets.QTableWidget(self.bookpage)
		self.wordstable.setGeometry(QRect(5, 10, 350, 490))
		self.wordstable.setObjectName("WordsTable")
		self.wordstable.setGridStyle(Qt.DotLine)  # 虚线

		self.wordsinbook = self.createTables()  # 获取生词本中的数据

		self.wordstable.setColumnCount(3)
		self.wordstable.setRowCount(self.wordsinbook.shape[0])
		self.wordstable.horizontalHeader().setCascadingSectionResizes(True)
		self.wordstable.setColumnWidth(0, 80)
		self.wordstable.setColumnWidth(1, 90)
		self.wordstable.setColumnWidth(2, 145)
		self.wordstable.verticalHeader().setCascadingSectionResizes(False)
		self.wordstable.verticalHeader().setDefaultSectionSize(30)

		# 设置表头
		self.wordstable.setHorizontalHeaderLabels([self.wordsinbook.columns[i] for i in [0, 2, 3]])

		# 填充数据
		for xloc in range(self.wordsinbook.shape[0]):
			for yloc in [0, 2, 3]:
				self.items = QTableWidgetItem(str(self.wordsinbook.iloc[xloc, yloc]))  # 必须str
				self.items.setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter)  # 水平和垂直居中

				# 生词本中和显示的表格坐标不同,处理－1
				if yloc == 0:
					self.wordstable.setItem(xloc, yloc, self.items)
				else:
					self.wordstable.setItem(xloc, yloc-1, self.items)

		self.wordstable.setStyleSheet("selection-background-color:pink")
		self.wordstable.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.wordstable.raise_()
		self.bookpage.setVisible(True)

	def createTables(self):  # 填充生词本的数据
		try:
			data = pd.read_csv('dic.csv')
			return data
		except:
			QMessageBox.information(self, '提示', '没有单词本，请添加单词！', QMessageBox.Yes)

	def btTranslateFunc(self):  # 翻译按钮
		info = self.inputwords.text()
		text = Functions.jinshanTranslateAPI(self, info)
		self.textviewTranslate.setText(text)
		self.btAddToBook.setEnabled(True)


	def btAddToBookFunc(self):
		info = self.inputwords.text()
		flag = Functions.addToBook(self, info)
		# print(info)
		if not flag:
			QMessageBox.information(self, '提示', '已添加成功！', QMessageBox.Yes)
		elif flag == 1:
			QMessageBox.information(self, '提示', '已存在！', QMessageBox.Yes)
		elif flag == 2:
			QMessageBox.information(self, '提示', '信息为空！', QMessageBox.Yes)
		self.btAddToBook.setEnabled(False)

	def tipsInformation(self):
		self.textviewTranslate.setText(self.data['means'][self.reviewWordLoc])

	def nextWordPlus1(self):
		self.data.iloc[self.reviewWordLoc, 3] += 1  # 点击下一次认为复习了一次
		pd.DataFrame.to_csv(self.data, 'dic.csv', index=None)  # 保证重新写入的与原来一致
		self.showReviewPage()  # 清屏处理

	def getRandomMinLoc(self):
		allLocs = np.where(self.data['have_review_times'] == np.min(self.data['have_review_times']))[0]  # 所有最小
		choseLoc = np.random.choice(allLocs)  # 随机选取1个
		# print(choseLoc)
		return choseLoc


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
			if flag:  # 单词存在，返回１
				return 1
			else:
				if info == '':  # 信息为空，提示'为空'
					return 2
				else:  # 否则写入文件
					Functions.writeCSV(self, './dic.csv', info)
					# print('yes already')
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
		time = datetime.datetime.now().strftime('%Y-%m-%d')
		with open(path, "a+", newline='') as file:
			csv_file = csv.writer(file)
			data = [info, Functions.jinshanTranslateAPI(self, info).split('\n')[1::], time, 0]
			csv_file.writerow(data)

	def reqContent(self):
		req = requests.get('http://open.iciba.com/dsapi')
		req_content = req.json()
		return req_content

	def getImageData(self):
		req_contents = Functions.reqContent(self)
		# print(pic_address)
		pic_data = requests.get(req_contents['picture'])
		photo = QPixmap()
		photo.loadFromData(pic_data.content)
		# print(pic_data.content)
		return photo

	def getEngSentence(self):
		req_contents = Functions.reqContent(self)
		return req_contents['content']

	def getChsSentence(self):
		req_contents = Functions.reqContent(self)
		return req_contents['note']

	def getPS(self):
		req_contents = Functions.reqContent(self)
		return req_contents['translation']

	def getDateLine(self):
		req_contents = Functions.reqContent(self)
		return req_contents['dateline']


if __name__ == "__main__":
	app = QApplication(sys.argv)
	# dialog = logindialog()
	# if dialog.exec_()==QDialog.Accepted:
	the_window = MainWindow()
	the_window.show()
	sys.exit(app.exec_())