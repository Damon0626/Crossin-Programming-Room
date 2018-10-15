# -*- coding: utf-8 -*-
'''
author: Damon0626
Email: wwymsn@163.com
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys


class Ui_Form(QWidget):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.setEnabled(True)
		Form.resize(300, 450)
		Form.setWindowOpacity(1.0)
		Form.setStyleSheet("background-color: rgb(255, 255, 255);")
		self.title = QtWidgets.QLabel(Form)
		self.title.setGeometry(QtCore.QRect(75, 20, 150, 20))
		font = QtGui.QFont()
		font.setFamily("AR PL UMing CN")
		font.setPointSize(14)
		self.title.setFont(font)
		self.title.setObjectName("title")
		self.gross_pay = QtWidgets.QLabel(Form)
		self.gross_pay.setGeometry(QtCore.QRect(50, 70, 54, 30))
		font = QtGui.QFont()
		font.setFamily("AR PL UMing CN")
		font.setPointSize(10)
		self.gross_pay.setFont(font)
		self.gross_pay.setObjectName("gross_pay")
		self.gross_pay_input = QtWidgets.QPlainTextEdit(Form)
		self.gross_pay_input.setGeometry(QtCore.QRect(110, 70, 104, 30))
		self.gross_pay_input.setObjectName("gross_pay_input")
		self.yuan0 = QtWidgets.QLabel(Form)
		self.yuan0.setGeometry(QtCore.QRect(220, 70, 21, 30))
		self.yuan0.setObjectName("yuan0")
		self.five_and_one = QtWidgets.QLabel(Form)
		self.five_and_one.setGeometry(QtCore.QRect(50, 110, 54, 30))
		font = QtGui.QFont()
		font.setFamily("AR PL UMing CN")
		font.setPointSize(10)
		self.five_and_one.setFont(font)
		self.five_and_one.setObjectName("five_and_one")
		self.threshold = QtWidgets.QLabel(Form)
		self.threshold.setGeometry(QtCore.QRect(50, 150, 54, 30))
		font = QtGui.QFont()
		font.setFamily("AR PL UMing CN")
		font.setPointSize(10)
		self.threshold.setFont(font)
		self.threshold.setAlignment(QtCore.Qt.AlignCenter)
		self.threshold.setObjectName("threshold")
		self.taxable_income = QtWidgets.QLabel(Form)
		self.taxable_income.setGeometry(QtCore.QRect(20, 250, 81, 30))
		font = QtGui.QFont()
		font.setFamily("AR PL UMing CN")
		font.setPointSize(10)
		self.taxable_income.setFont(font)
		self.taxable_income.setObjectName("taxable_income")
		self.tax_rate = QtWidgets.QLabel(Form)
		self.tax_rate.setGeometry(QtCore.QRect(70, 290, 31, 30))
		font = QtGui.QFont()
		font.setFamily("AR PL UMing CN")
		font.setPointSize(10)
		self.tax_rate.setFont(font)
		self.tax_rate.setObjectName("tax_rate")
		self.tax_pay = QtWidgets.QLabel(Form)
		self.tax_pay.setGeometry(QtCore.QRect(50, 330, 51, 30))
		font = QtGui.QFont()
		font.setFamily("AR PL UMing CN")
		font.setPointSize(10)
		self.tax_pay.setFont(font)
		self.tax_pay.setObjectName("tax_pay")
		self.post_tax_wage = QtWidgets.QLabel(Form)
		self.post_tax_wage.setGeometry(QtCore.QRect(50, 370, 51, 30))
		font = QtGui.QFont()
		font.setFamily("AR PL UMing CN")
		font.setPointSize(10)
		self.post_tax_wage.setFont(font)
		self.post_tax_wage.setObjectName("post_tax_wage")
		self.link = QtWidgets.QLabel(Form)
		self.link.setGeometry(QtCore.QRect(105, 410, 90, 20))
		font = QtGui.QFont()
		font.setFamily("AR PL UMing CN")
		font.setPointSize(8)
		self.link.setFont(font)
		self.link.setAutoFillBackground(False)
		self.link.setObjectName("link")
		self.author = QtWidgets.QLabel(Form)
		self.author.setGeometry(QtCore.QRect(200, 430, 111, 15))
		font = QtGui.QFont()
		font.setFamily("URW Chancery L")
		font.setPointSize(10)
		font.setItalic(True)
		self.author.setFont(font)
		self.author.setObjectName("author")
		self.five_and_one_input = QtWidgets.QPlainTextEdit(Form)
		self.five_and_one_input.setGeometry(QtCore.QRect(110, 110, 104, 30))
		self.five_and_one_input.setObjectName("five_and_one_input")
		self.taxable_income_brow = QtWidgets.QTextBrowser(Form)
		self.taxable_income_brow.setGeometry(QtCore.QRect(110, 250, 104, 30))
		self.taxable_income_brow.setObjectName("taxable_income_brow")
		self.tax_rate_brow = QtWidgets.QTextBrowser(Form)
		self.tax_rate_brow.setGeometry(QtCore.QRect(110, 290, 104, 30))
		self.tax_rate_brow.setObjectName("tax_rate_brow")
		self.tax_pay_edit = QtWidgets.QPlainTextEdit(Form)
		self.tax_pay_edit.setGeometry(QtCore.QRect(110, 330, 104, 30))
		self.tax_pay_edit.setObjectName("tax_pay_edit")
		self.post_tax_wage_edit = QtWidgets.QPlainTextEdit(Form)
		self.post_tax_wage_edit.setGeometry(QtCore.QRect(110, 370, 104, 30))
		self.post_tax_wage_edit.setObjectName("post_tax_wage_edit")
		self.threshold_list = QtWidgets.QComboBox(Form)
		self.threshold_list.setGeometry(QtCore.QRect(110, 150, 104, 30))
		self.threshold_list.setEditable(False)
		self.threshold_list.setCurrentText("")
		self.threshold_list.setMaxVisibleItems(2)
		self.threshold_list.setMaxCount(2)
		self.threshold_list.setObjectName("threshold_list")
		self.threshold_list.addItems(['3500', '5000'])
		self.count = QtWidgets.QPushButton(Form)
		self.count.setGeometry(QtCore.QRect(60, 200, 60, 25))
		self.count.setStyleSheet("background-color:  rgb(91, 155, 213);")
		self.count.setObjectName("count")
		self.reset = QtWidgets.QPushButton(Form)
		self.reset.setGeometry(QtCore.QRect(180, 200, 60, 25))
		self.reset.setStyleSheet("background-color: rgb(255, 0, 4);")
		self.reset.setObjectName("reset")
		# self.recal1 = QtWidgets.QPushButton(Form)
		# self.recal1.setGeometry(QtCore.QRect(240, 333, 40, 25))
		# self.recal1.setStyleSheet("background-color: rgb(91, 155, 213);")
		# self.recal1.setObjectName("recal1")
		# self.recal2 = QtWidgets.QPushButton(Form)
		# self.recal2.setGeometry(QtCore.QRect(240, 373, 40, 25))
		# self.recal2.setStyleSheet("background-color: rgb(91, 155, 213);")
		# self.recal2.setObjectName("recal2")
		self.yuan1 = QtWidgets.QLabel(Form)
		self.yuan1.setGeometry(QtCore.QRect(220, 110, 21, 30))
		self.yuan1.setObjectName("yuan1")
		self.yuan2 = QtWidgets.QLabel(Form)
		self.yuan2.setGeometry(QtCore.QRect(220, 150, 21, 30))
		self.yuan2.setObjectName("yuan2")
		self.yuan3 = QtWidgets.QLabel(Form)
		self.yuan3.setGeometry(QtCore.QRect(220, 250, 21, 30))
		self.yuan3.setObjectName("yuan3")
		self.rate = QtWidgets.QLabel(Form)
		self.rate.setGeometry(QtCore.QRect(220, 290, 21, 30))
		self.rate.setObjectName("rate")
		self.yuan4 = QtWidgets.QLabel(Form)
		self.yuan4.setGeometry(QtCore.QRect(220, 330, 15, 30))
		self.yuan4.setObjectName("yuan4")
		self.yuan5 = QtWidgets.QLabel(Form)
		self.yuan5.setGeometry(QtCore.QRect(220, 370, 15, 30))
		self.yuan5.setObjectName("yuan5")

		self.retranslateUi(Form)
		self.threshold_list.setCurrentIndex(-1)
		QtCore.QMetaObject.connectSlotsByName(Form)
		self.messageBox = QtWidgets.QMessageBox(Form)
		self.count.clicked.connect(self.calculate)
		self.reset.clicked.connect(self.resetAll)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "个人所得税计算器"))
		self.title.setText(_translate("Form", "个人所得税计算器"))
		self.gross_pay.setText(_translate("Form", "税前工资"))
		self.yuan0.setText(_translate("Form", "元"))
		self.five_and_one.setText(_translate("Form", "五险一金"))
		self.threshold.setText(_translate("Form", "起征点"))
		self.taxable_income.setText(_translate("Form", "应纳税所得额"))
		self.tax_rate.setText(_translate("Form", "税率"))
		self.tax_pay.setText(_translate("Form", "应纳税额"))
		self.post_tax_wage.setText(_translate("Form", "税后工资"))
		self.link.setText("<A href = 'https://mp.weixin.qq.com/s/AO_ZFpqqQ3mGHjNL2Qoa3Q'>查看详细计算过程</a>")
		self.link.setOpenExternalLinks(True)
		self.author.setText(_translate("Form", "author: Damon0626"))
		self.count.setText(_translate("Form", "计算"))
		self.reset.setText(_translate("Form", "重置"))
		# self.recal1.setText(_translate("Form", "反算"))
		# self.recal2.setText(_translate("Form", "反算"))
		self.yuan1.setText(_translate("Form", "元"))
		self.yuan2.setText(_translate("Form", "元"))
		self.yuan3.setText(_translate("Form", "元"))
		self.rate.setText(_translate("Form", "%"))
		self.yuan4.setText(_translate("Form", "元"))
		self.yuan5.setText(_translate("Form", "元"))

	def calculate(self):

		input_wages = self.gross_pay_input.toPlainText()
		five_risks_and_gold = self.five_and_one_input.toPlainText()
		threshold = self.threshold_list.currentText()

		# 如果不是数字报错
		flag = self.judgementFornumeric(input_wages, five_risks_and_gold, threshold)

		if flag == 1:
			pass
		else:
			if 0 < float(input_wages) < 99999999 and 0 < float(five_risks_and_gold) < 99999999:
				taxalbe_income = float(input_wages) - float(five_risks_and_gold) - float(threshold)

				if threshold == "5000":
					if float(taxalbe_income) <= 3000:
						self.tax_rate_brow.setText("3")
						tax_rate = 0.03
						quick_cal_num = 0
					elif float(taxalbe_income) <= 12000:
						self.tax_rate_brow.setText("10")
						tax_rate = 0.10
						quick_cal_num = 210
					elif float(taxalbe_income) <= 25000:
						self.tax_rate_brow.setText("20")
						tax_rate = 0.20
						quick_cal_num = 1410
					elif float(taxalbe_income) <= 35000:
						self.tax_rate_brow.setText("25")
						tax_rate = 0.25
						quick_cal_num = 2660
					elif float(taxalbe_income) <= 55000:
						self.tax_rate_brow.setText("30")
						tax_rate = 0.30
						quick_cal_num = 4410
					elif float(taxalbe_income) <= 80000:
						self.tax_rate_brow.setText("35")
						tax_rate = 0.35
						quick_cal_num = 7160
					else:
						self.tax_rate_brow.setText("45")
						tax_rate = 0.45
						quick_cal_num = 15160

				if threshold == "3500":
					if float(taxalbe_income) <= 1500:
						self.tax_rate_brow.setText("3")
						tax_rate = 0.03
						quick_cal_num = 0
					elif float(taxalbe_income) <= 4500:
						self.tax_rate_brow.setText("10")
						tax_rate = 0.10
						quick_cal_num = 105
					elif float(taxalbe_income) <= 9000:
						self.tax_rate_brow.setText("20")
						tax_rate = 0.20
						quick_cal_num = 555
					elif float(taxalbe_income) <= 35000:
						self.tax_rate_brow.setText("25")
						tax_rate = 0.25
						quick_cal_num = 1005
					elif float(taxalbe_income) <= 55000:
						self.tax_rate_brow.setText("30")
						tax_rate = 0.30
						quick_cal_num = 2755
					elif float(taxalbe_income) <= 80000:
						self.tax_rate_brow.setText("35")
						tax_rate = 0.35
						quick_cal_num = 5505
					else:
						self.tax_rate_brow.setText("45")
						tax_rate = 0.45
						quick_cal_num = 13505

				tax_pay = float(taxalbe_income) * tax_rate - quick_cal_num
				post_tax_wage = float(input_wages) - float(five_risks_and_gold) - tax_pay

				if taxalbe_income > 0 and tax_pay > 0 and post_tax_wage > 0:
					self.taxable_income_brow.setText(str(taxalbe_income))
					self.tax_pay_edit.setPlainText(str(tax_pay))
					self.post_tax_wage_edit.setPlainText(str(post_tax_wage))
				else:
					self.showFault("超范围，算不来，算不来！")
			else:
				self.showFault("超范围，算不来，算不来！")

	def judgementFornumeric(self, *args):
		try:
			for i in args:
				float(i)
		except:
			self.showFault("识别有限，还是全部输入数字吧！")
			return 1

	def resetAll(self):
		self.gross_pay_input.setPlainText("")
		self.five_and_one_input.setPlainText("")
		self.tax_pay_edit.setPlainText("")
		self.tax_rate_brow.setText("")
		self.taxable_income_brow.setPlainText("")
		self.post_tax_wage_edit.setPlainText("")

	def showFault(self, info):
		self.messageBox.information(self, "info", info)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	widget = QtWidgets.QWidget()
	ui = Ui_Form()
	ui.setupUi(widget)
	widget.show()
	sys.exit(app.exec_())