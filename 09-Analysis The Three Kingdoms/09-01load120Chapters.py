# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-10 下午2:51
# @Email : wwymsn@163.com
# @Software: PyCharm


import requests
from bs4 import BeautifulSoup as bs


book = []
for i in range(120):
	print("处理第{}回...".format(i+1))
	if i+1 < 10:
		url = "http://www.purepen.com/sgyy/00{}.htm".format(i+1)
	elif i+1 < 100:
		url = "http://www.purepen.com/sgyy/0{}.htm".format(i+1)
	else:
		url = "http://www.purepen.com/sgyy/{}.htm".format(i+1)

	req = requests.get(url)
	result = req.content.decode('gb18030')  # 注意字符编码
	bsObj = bs(result, 'lxml')
	chapter = bsObj.table.font.contents[0]
	book.append(chapter)

# 分成120回，便于后续分析每回人物
with open("sanguo.txt", 'w') as f:
	for chap in book:
		s = chap.strip()
		f.write("".join(s.split()))
		f.write('\n')
