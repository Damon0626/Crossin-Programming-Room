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
import getpass  # 获取host
import datetime
import pandas as pd
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt


class MainWindow(QDialog):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setWindowTitle("电子辞典")
		self.resize(360, 640)
		self.setMinimumSize(QSize(360, 640))
		self.setStyleSheet("background-color: rgb(255, 255, 255)")

		# 每日一句
		self.dailySentence()

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
		self.btMyInfoPage.clicked.connect(self.showMypage)

	def dailySentence(self):
		# 每日一句
		'''提头'''
		self.dailySentencePage = QFrame(self)
		self.dailySentencePage.setGeometry(QRect(0, 0, 360, 550))
		self.daily_sentence_title = QLabel(self.dailySentencePage)
		self.daily_sentence_title.setGeometry(QRect(0, 0, 360, 40))
		font = QFont()
		font.setPixelSize(20)
		# font.setBold(True)
		self.daily_sentence_title.setFont(font)
		self.daily_sentence_title.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(41, 196, 242)")
		self.daily_sentence_title.setText("  每日一句")

		'''图片'''
		self.daily_sentence_pic = QLabel(self.dailySentencePage)
		self.daily_sentence_pic.setGeometry(QRect(30, 45, 300, 170))
		self.daily_sentence_pic.setPixmap(Functions.getImageData(self))
		self.daily_sentence_pic.setAlignment(Qt.AlignCenter)

		'''句子'''
		self.daily_sentence_sentence_eng = QTextBrowser(self.dailySentencePage)
		self.daily_sentence_sentence_eng.setGeometry(QRect(30, 240, 300, 80))
		self.daily_sentence_sentence_eng.setStyleSheet("color: rgb(0, 74, 128)")
		font = QFont()
		font.setBold(True)
		font.setPixelSize(15)
		self.daily_sentence_sentence_eng.setFont(font)
		self.daily_sentence_sentence_eng.setText(Functions.getEngSentence(self))
		self.daily_sentence_sentence_eng.setFrameShape(QtWidgets.QFrame.NoFrame)

		'''翻译'''
		self.daily_sentence_sentence_chs = QTextBrowser(self.dailySentencePage)
		self.daily_sentence_sentence_chs.setGeometry(QRect(30, 330, 300, 80))
		font = QFont()
		font.setBold(True)
		font.setPixelSize(15)
		self.daily_sentence_sentence_chs.setFont(font)
		self.daily_sentence_sentence_chs.setText(Functions.getChsSentence(self))
		self.daily_sentence_sentence_chs.setFrameShape(QtWidgets.QFrame.NoFrame)

		'''注释'''
		self.daily_sentence_ps = QTextBrowser(self.dailySentencePage)
		self.daily_sentence_ps.setGeometry(QRect(30, 410, 300, 120))
		self.daily_sentence_ps.setText(Functions.getPS(self) + '\n\n' + Functions.getDateLine(self))
		self.daily_sentence_ps.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.dailySentencePage.setVisible(True)

	def showTranslatePage(self):
		self.translatepage = QFrame(self)
		self.translatepage.resize(360, 550)

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
		self.reviewpage.resize(360, 550)

		# 获取数据
		self.data = self.createTables()
		self.reviewWordLoc = self.getRandomMinLoc()

		# 复习单词显示框
		self.wordsToReview = QTextBrowser(self.reviewpage)
		self.wordsToReview.setGeometry(QRect(60, 90, 250, 75))
		self.wordsToReview.setObjectName("wordsToReview")

		if self.reviewWordLoc == None:  # 0的话，屏蔽第一个位置
			self.wordsToReview.setText("")
		else:
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
		self.btNextWord.clicked.connect(self.nextWordPlus1)



		self.reviewpage.setVisible(True)


	def showBookPage(self):
		self.bookpage = QFrame(self)
		self.bookpage.resize(360, 550)
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

	def showMypage(self):
		self.mypage = QFrame(self)
		self.mypage.resize(360, 550)

		# 上部份背景
		self.top_bkground = QLabel(self.mypage)
		self.top_bkground.setGeometry(QRect(0, 0, 360, 120))
		self.top_bkground.setStyleSheet("background-color: rgb(77, 77, 77);")
		self.top_bkground.setText("")
		self.top_bkground.setObjectName("top_bkground")

		# 单词总数label
		font = QFont()
		font.setPixelSize(12)
		font.setFamily('Ubuntu')
		font.setStyleName('Normal')
		self.label_counts = QLabel(self.mypage)
		self.label_counts.setFont(font)
		self.label_counts.setGeometry(QRect(145, 40, 70, 17))
		self.label_counts.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(77, 77, 77);")
		self.label_counts.setAlignment(Qt.AlignCenter)
		self.label_counts.setObjectName("label_counts")
		self.label_counts.setText("单词总数")

		# 单词总数显示
		font = QFont()
		font.setBold(True)
		font.setPixelSize(24)
		font.setFamily('Ubuntu')
		self.words_counts = QTextBrowser(self.mypage)
		self.words_counts.setGeometry(QRect(120, 60, 120, 50))
		self.words_counts.setStyleSheet("color: rgb(255, 255, 255);\n""background-color: rgb(77, 77, 77);")
		self.words_counts.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.words_counts.setObjectName("words_counts")
		self.words_counts.setFont(font)
		self.words_counts.setText(str(self.createTables().shape[0]))
		# self.words_counts.setText(str(2222))
		self.words_counts.setAlignment(Qt.AlignCenter)

		# 我的数据label
		self.label_mydata = QLabel(self.mypage)
		self.label_mydata.setGeometry(QRect(10, 125, 71, 17))
		font = QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_mydata.setFont(font)
		self.label_mydata.setStyleSheet("color: rgb(128, 128, 128);")
		self.label_mydata.setObjectName("label_mydata")
		self.label_mydata.setText("我的数据")

		# 我的数据图表
		self.data_display = PlotCanvas(self.mypage) # 350*190, 100分辨率
		self.data_display.move(5, 140)
		self.data_display.init_plot()

		# 产品信息label
		self.label_prod_info = QLabel(self.mypage)
		self.label_prod_info.setGeometry(QRect(10, 355, 71, 17))
		font = QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_prod_info.setFont(font)
		self.label_prod_info.setStyleSheet("color: rgb(128, 128, 128);")
		self.label_prod_info.setObjectName("label_prod_info")
		self.label_prod_info.setText("产品信息")

		# 产品信息内容
		self.produc_info = QTextBrowser(self.mypage)
		self.produc_info.setGeometry(QRect(5, 375, 350, 55))
		self.produc_info.setStyleSheet("color: rgb(128, 128, 128);")
		self.produc_info.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.produc_info.setObjectName("produc_info")
		self.produc_info.setText("产品： E-dict\t\t作者： Damon0626\n版本： 19.1.20")

		# 附加信息label
		self.label_overhead_info = QLabel(self.mypage)
		self.label_overhead_info.setGeometry(QRect(10, 430, 71, 17))
		font = QFont()
		font.setPointSize(10)
		font.setBold(True)
		font.setWeight(75)
		self.label_overhead_info.setFont(font)
		self.label_overhead_info.setStyleSheet("color: rgb(128, 128, 128);")
		self.label_overhead_info.setObjectName("label_overhead_info")
		self.label_overhead_info.setText("附加信息")

		# 附加信息内容
		self.hostname, self.path = Functions.getHostAndPath(self)
		self.overhead_info = QTextBrowser(self.mypage)
		self.overhead_info.setGeometry(QRect(5, 450, 350, 70))
		self.overhead_info.setStyleSheet("color: rgb(128, 128, 128);")
		self.overhead_info.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.overhead_info.setObjectName("overhead_info")
		self.overhead_info.setText("主机名称："+self.hostname+'\n'+"生词本路径："+self.path+'/dic.csv')

		# 返回每日一句按钮的背景
		self.label_daily_sentence_bg = QLabel(self.mypage)
		self.label_daily_sentence_bg.setGeometry(QRect(0, 520, 360, 30))
		self.label_daily_sentence_bg.setStyleSheet("background-color: rgb(41, 196, 242);")
		self.label_daily_sentence_bg.setText("")
		self.label_daily_sentence_bg.setObjectName("label_daily_sentence_bg")

		# 返回每日一句按钮
		self.btBackDailySentence = QPushButton(self.mypage)
		self.btBackDailySentence.setGeometry(QRect(0, 520, 360, 30))
		font = QFont()
		font.setBold(True)
		font.setWeight(75)
		self.btBackDailySentence.setFont(font)
		self.btBackDailySentence.setStyleSheet("color: rgb(255, 255, 255);")
		self.btBackDailySentence.setFlat(True)
		self.btBackDailySentence.setObjectName("btBackDailySentence")
		self.btBackDailySentence.setText("每日一句")
		self.btBackDailySentence.clicked.connect(self.dailySentence)

		self.mypage.setVisible(True)

	def createTables(self):  # 填充生词本的数据
		try:
			data = pd.read_csv('dic.csv')
			return data
		except:
			QMessageBox.information(self, '提示', '没有单词本，已初始化单词本！', QMessageBox.Yes)
			Functions.addToBook(self, None)
			return pd.read_csv('dic.csv')

	def btTranslateFunc(self):  # 翻译按钮
		info = self.inputwords.text()
		text = Functions.jinshanTranslateAPI(self, info)
		self.btAddToBook.setEnabled(True)

		if not text:
			text = "Error:\n place check for your network or input something..."
			self.btAddToBook.setEnabled(False)
		self.textviewTranslate.setText(text)


	def btAddToBookFunc(self):
		info = self.inputwords.text()
		flag = Functions.addToBook(self, info)
		# print(info)
		if not flag:
			QMessageBox.information(self, '提示', '已添加成功！', QMessageBox.Yes)
		elif flag == 1:
			QMessageBox.information(self, '提示', '已存在！', QMessageBox.Yes)
		elif flag == 2:
			self.btAddToBook.setEnabled(False)
			QMessageBox.information(self, '提示', '信息为空或信息有误！', QMessageBox.Yes)



	def tipsInformation(self):
		if self.data.empty:
			self.textviewTranslate.setText("")
		else:
			self.textviewTranslate.setText(self.data['means'][self.reviewWordLoc])

	def nextWordPlus1(self):
		if self.data.empty:
			QMessageBox.information(self, '提示', '没有单词', QMessageBox.Yes)
		else:
			self.data.iloc[self.reviewWordLoc, 3] += 1  # 点击下一次认为复习了一次
			pd.DataFrame.to_csv(self.data, 'dic.csv', index=None)  # 保证重新写入的与原来一致
			self.showReviewPage()  # 清屏处理

	def getRandomMinLoc(self):
		if self.data.empty:
			return None
		else:
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
			return 0

	def addToBook(self, info):
		if os.path.exists('dic.csv'):
			flag = Functions.readCSV(self, './dic.csv', info)
			if flag:  # 单词存在，返回１
				return 1
			else:
				if info == '' or (not Functions.jinshanTranslateAPI(self, info)):  # 信息为空，提示'为空或错误'
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

	def getHostAndPath(self):
		path = os.getcwd()
		hostname = getpass.getuser()
		return hostname, path


class PlotCanvas(FigureCanvas):

	def __init__(self, parent=None):
		plt.style.use('ggplot')
		fig = plt.figure(figsize=(3.5, 1.9), dpi=100)
		self.axes = fig.add_subplot(111)

		FigureCanvas.__init__(self, fig)
		self.setParent(parent)
		FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)
		self.init_plot()

	def init_plot(self):
		# 初始值
		x = ["Mon", "Tues", "Whe", "Thur", "Fri", "Sat", "Sun"]
		y = [0, 0, 0, 0, 0, 0, 0]

		# 建立插入时间的集合
		insertTimeList = MainWindow.createTables(self)['insert_time']
		insertTimeSet = {}
		for time in insertTimeList:
			insertTimeSet[time] = list(insertTimeList).count(time)

		# 获取当前日期和星期
		weekToday = datetime.datetime.now().weekday()  # 0-6表示周一到周日
		dayToday = datetime.datetime.now().strftime("%Y-%m-%d")

		# 创建要显示的日期集合
		dateToDispaly = []
		for i in range(weekToday):
			dateToDispaly.append((datetime.datetime.now()-datetime.timedelta(days=weekToday-i)).strftime("%Y-%m-%d"))
		dateToDispaly.append(dayToday)

		# 如果插入时间中有当前日期，则显示其数量，否则为0
		for date in dateToDispaly:
			if date in insertTimeSet:
				y[dateToDispaly.index(date)] = insertTimeSet[date]
			else:
				continue

		plt.bar(x, y)
		for a, b in zip(x, y):
			plt.text(a, b, '%.0f' % b, ha='center', va='bottom', fontsize=7)
		plt.xticks(size=8)
		plt.yticks([])
		plt.ylim((0, max(y)*1.1+0.1))

		# 由于全是0纵坐标显示小数,不合理,遂将坐标轴去掉,换成数值显示


		plt.title("Words added this week", color='black', fontsize=10)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	# dialog = logindialog()
	# if dialog.exec_()==QDialog.Accepted:
	the_window = MainWindow()
	the_window.show()
	sys.exit(app.exec_())