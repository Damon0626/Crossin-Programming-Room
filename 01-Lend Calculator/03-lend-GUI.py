# -*-coding:utf-8-*-
'''
作者：Damon0626
邮箱：wwymsn@163.com

仿照支付宝界面尝试做个小界面;
存在的问题：
	基准利率为4.9%， 5年和10年及大于10年的基准利率不同，本程序没处理;
	未设置中文显示， ubuntu下中文太丑了， 英文稍好一点，未按转其他字体，全部用的‘Times’;
	未设置窗口最大最小化;
	窗口图标未设置，ubuntu下，tk.root.iconbitmap('/A/B/xxx.ico')报错， 未处理.

本人初学python半年，也都是工作之余，尝试了下，代码难免臃肿杂乱，还请多多指出不足之处，万分感谢。
'''

from tkinter import *
from tkinter import ttk
import numpy as np


class Calculator(object):
	def __init__(self):

		# 窗口和标题
		self.root = Tk()
		self.root.geometry('400x400')
		self.root.title('房贷计算器')

		# 输入和选框值
		self.funcchose = StringVar()  # 复选框变量
		self.years = 0  # 贷款时间
		self.str_rates = StringVar()  # 贷款利率
		self.amount = 0.0  # 贷款金额（万）
		self.month_rates = 0.0  # 月利率
		self.monthpay = 0.0  # 每月还款金额
		self.mondec = 0.0  # 每月递减
		self.interest = 0.0  # 总利息
		self.totalmoney = 0.0 # 总还款
		self.Combobox1 = ('基准利率', '7折利率', '8折利率', '8.3折利率', '8.5折利率', '8.8折利率',
		                  '9折利率', '9.5折利率', '1.05倍利率', '1.1倍利率', '1.2倍利率', '1.3倍利率')
		self.Combobox2 = (5, 10, 15, 20, 25, 30)
		self.baserates = 0.049  # 基准利率
		self.havepaid = 0.0  # 已还款

		# 各类金额显示
		self.L1 = Label(self.root, text=self.monthpay, font='Times 20 bold')
		self.L1.place(x=5, y=80)
		self.L2 = Label(self.root, text=self.mondec, font='Times 20 bold')
		self.L2.place(x=190, y=80)
		self.L3 = Label(self.root, text=self.interest, font='Times 20 bold')
		self.L3.place(x=5, y=150)
		self.L4 = Label(self.root, text=self.totalmoney, font='Times 20 bold')
		self.L4.place(x=190, y=150)

		# 各类金额名称
		Label(self.root, text='Reference Payment Each Month(CYN)', wraplength=180, justify='left').place(x=5, y=50)
		self.L5 = Label(self.root, text='Decrease in Each Month(CNY)')
		self.L5.place(x=190, y=50)  # 等额本息情况不显示
		Label(self.root, text='Pay Interest(CNY)').place(x=5, y=130)
		Label(self.root, text='Payoff Amount(CNY)').place(x=190, y=130)

		# 显示金额和输入之间的过度部分
		Label(self.root, text='Fixed-Payment Details', font='Times 10 bold').place(x=120, y=190)

		# 输入部分标签
		Label(self.root, text='Amount(10k)', font='Times 15').place(x=20, y=210)
		Label(self.root, text='Due Time(year)', font='Times 15').place(x=20, y=250)
		Label(self.root, text='Interest Rate(%)', font='Times 15').place(x=20, y=290)

		# 两个下拉列表
		self.yearschoes = ttk.Combobox(self.root, font='Times 15', textvariable=self.years)
		self.yearschoes['values'] = self.Combobox2
		self.yearschoes.place(x=180, y=250)
		self.yearschoes.current(0)

		self.rateschose = ttk.Combobox(self.root, font='Times 15', textvariable=self.str_rates)
		self.rateschose['values'] = self.Combobox1
		self.rateschose.place(x=180, y=290)
		self.rateschose.current(0)

		# 一个只能输入数字的输入框，整数部分最大9999,最多由两位小数
		self.E1 = Entry(self.root, justify=RIGHT,
					textvariable=self.amount,
					font='Times 15',
					validate='key',
					validatecommand=(self.root.register(self.OnlyDigit), '%P'))  # 每次输入内容变化时，都会调用该指令
		self.E1.place(x=180, y=210)

		# 两种不同计算方式
		Radiobutton(self.root, text="Fixed-Payment",
					variable=self.funcchose,
					value= 1,
					indicatoron=False,
					width=20,
					command = self.DEBXHK,
					height=2).place(x=50, y=10)

		Radiobutton(self.root, text="Fixed-Basis",
					variable=self.funcchose,
					value= 0,
					indicatoron=False,
					width=20,
					command = self.DEBJHK,
					height=2).place(x=180, y=10)

		# 注意信息
		Label(self.root, text='This is the latest Loan Rate released by PBOC on 2016', font='Times 8').place(x=5, y=320)
		self.root.mainloop()

	def Digit(self, content):  # 若可转小数， 则为数字可输入，否则其他字符，不可输入
		try:
			float(content)
			return True
		except:
			return False

	def OnlyDigit(self, content):
		if self.Digit(content) or (content == ""):  # 小数的情况下，content==""用于删除最后一个数字
			# print(len(content))
			data = content.split('.')
			if len(data) == 1:  # 处理整数情况
				if data[0] == '':  # 刚删空的瞬间
					return True
				elif int(data[0]) <= 9999:
					# print('PPPPPPPPP')
					return True
				else:
					return False
			elif len(data) == 2:  # 处理小数情况
				if (int(data[0]) <= 9999) and (data[1] == ''):  # 用于刚输入小数点的时候
					# print('OOOOOOOOOO')
					return True
				elif (int(data[0]) <= 9999) and (int(data[1]) <= 99):  # 仅允许输入两位小数
					# print('KKKKKKKK')
					return True
				else:
					return False
		else:
			# print('YYYYYYYYY')
			return False

	# 字符串转浮点类型
	def StrrateToMonthrate(self, item):
		index = self.Combobox1.index(item)  # 获取索引
		ratepool = (self.baserates, self.baserates*0.7, self.baserates*0.8, self.baserates*0.83,
		            self.baserates*0.85, self.baserates*0.88, self.baserates*0.9, self.baserates*0.95,
		            self.baserates*1.05, self.baserates*1.1, self.baserates*1.2, self.baserates*1.3)
		self.month_rates = ratepool[index]/12

	# 获取控件的值
	def GetItem(self, control):
		return control.get()

	def ReNew(self, *kwargs):  # 刷新显示
		# 计算金额
		self.L1.config(text=kwargs[0])
		self.L2.config(text=kwargs[1])
		self.L3.config(text=kwargs[2])
		self.L4.config(text=kwargs[3])
		self.L5.config(text=kwargs[4])  # 等额本息不显示

	def Reset(self):  # 上次计算的值影响下一步计算，复位所有参与计算的值
		self.mondec = 0
		self.havepaid = 0
		self.monthpay = 0
		self.mondec = 0
		self.interest = 0
		self.totalmoney = 0
		self.firstmonth = 0
		self.havepaid = 0

	def Amount(self):  # ‘w’转‘块’ 输出
		self.amount = self.GetItem(self.E1)
		if self.amount == '':
			self.amount = 0
			# print(0)
		else:
			self.amount = float(self.amount)*10000
		# print(self.amount)
		return self.amount

	# 等额本息还款
	def DEBXHK(self):
		self.years = int(self.GetItem(self.yearschoes))
		self.StrrateToMonthrate(self.GetItem(self.rateschose))
		self.amount = self.Amount()
		self.monthpay = self.month_rates * np.power((1 + self.month_rates), self.years*12)/\
						(np.power((1 + self.month_rates), self.years*12) - 1.0) *self.amount
		# print(self.monthpay, self.years, self.month_rates, self.amount)

		self.ReNew(round(self.monthpay, 2), '', round(self.monthpay*self.years*12-self.amount, 2),
					round(self.monthpay*self.years*12, 2), '')
		self.Reset()

	# 等额本金还款
	def DEBJHK(self):
		self.years = int(self.GetItem(self.yearschoes))
		self.StrrateToMonthrate(self.GetItem(self.rateschose))
		self.amount = self.Amount()
		for i in range(self.years*12):
			if i == 0:
				self.firstmonth = self.amount/(self.years*12) + (self.amount - self.havepaid) * self.month_rates
				self.havepaid = self.firstmonth
			else:
				self.nextmonth = self.amount/(self.years*12) +\
								(self.amount -self.amount/(self.years*12)*i) * self.month_rates

				self.havepaid += self.nextmonth

		self.mondec = self.amount/(self.years*12)*self.month_rates

		self.ReNew(round(self.firstmonth, 2), round(self.mondec, 2),
					round(self.havepaid-self.amount, 2), round(self.havepaid, 2), 'Decrease in Each Month(CNY)')
		self.Reset()


if __name__ == '__main__':
	cal = Calculator()
