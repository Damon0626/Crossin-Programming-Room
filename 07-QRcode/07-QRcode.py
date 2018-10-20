# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-10-19 下午11:06
# @Email : wwymsn@163.com
# @Software: PyCharm

import qrcode
import zbarlight
from PIL import Image
import random
import argparse

def encode(infoToencode):
	image = qrcode.make(infoToencode)  # 写入信息
	nameRand = random.randint(0, 100)
	image.save('qrcode-%d.jpg' % nameRand)
	image.show()
	print("Image has saved:'./qrcode-%d.jpg'" % nameRand)


def decode(imageTodecode):
	image = Image.open(imageTodecode)
	a = zbarlight.scan_codes('qrcode', image)  # 解码格式和图片
	print(a[0].decode('utf-8'))  # a为列表，为显示汉字处理


if __name__ == "__main__":
	# 建立两个参数，operation和content内容
	# 根据operation，选择encode和decode执行不同的功能
	parser = argparse.ArgumentParser()
	parser.add_argument("operation", choices=['encode', 'decode'], help='The operation, encode or decode')
	parser.add_argument("content")
	agrs = parser.parse_args()
	if agrs.operation == 'encode':
		encode(agrs.content)
	else:
		try:
			decode(agrs.content)
		except IOError:
			print("请输入正确的二维码")
