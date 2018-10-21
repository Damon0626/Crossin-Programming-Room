# -*-coding:utf-8-*-
from PIL import Image
import re
import numpy as np


init_info = []
get_info = []


def read_image(path):
	img = Image.open(path)
	pixels = np.array(img)
	return pixels
	# im_pixels_with_info


def get_pixels_with_info(pixels):
	for i in range(pixels.shape[0]):
		for j in range(pixels.shape[1]):
			get_info.append(bin(pixels[i][j][-1])[-1])
	return len(pixels), get_info


def info_handing(get_info):
	info_handing = "".join(get_info)
	return info_handing


# 汉字编码
def character_encode(info_mark):
	return ''.join([bin(ord(item)).replace('0b', '').zfill(16) for item in info_mark])


# 汉字解码
def character_decode(info):
	result = re.findall(r'.{16}', info)
	return ''.join([chr(i) for i in [int(item, 2) for item in result]])


def write_pic(info_binary, path):
	pixes = read_image(path)
	j = 0
	for i in range(0, len(pixes), 100):
		bin(pixes[i][-1])[2:][-1] = info_binary[j]
		j += 1
		if j == len(info_binary):
			break
	return pixes


# 用户输入
def user_input():
	print("请输入要制作的数字水印：")
	content = str(input())
	return content


if __name__ == '__main__':
	# info_mark = user_input()
	# info_binary = character_encode(info_mark)
	# a = write_pic(info_binary, '.info.png')
	p = read_image('./info1.jpg')
	l, info = get_pixels_with_info(p)
	info_h = info_handing(info)
	c = character_decode(info_h)
	print(info_h)
