# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-3-5 下午10:25
# @Email : wwymsn@163.com
# @Software: PyCharm

'''
迭代的方式更好理解下, 通过观察前几组数据得到的规律，猛一开始也没想到递归的方法．多看＼多练
'''


def cows_nums(years):
	if years <= 4:
		return years
	else:
		return cows_nums(years - 1) + cows_nums(years - 3)


if __name__ == "__main__":
	print([cows_nums(year+1) for year in range(20)])
