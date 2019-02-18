# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-11 下午9:09
# @Email : wwymsn@163.com
# @Software: PyCharm


import jieba
import csv
import codecs
import jieba.posseg as pseg
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from scipy.misc import imread
import pandas as pd
from pyecharts import Bar
from pyecharts import Scatter
from pyecharts import Line
import sys


class anylysisThreeKindoms():
	def __init__(self):
		self.percentage = 0
		self.nouns = {}
		self.Top10 = None
		self.nameList = ['曹操', '玄德', '孔明', '关公', '丞相', '孔明曰', '玄德曰', '云长',
						'张飞', '主公', '吕布', '刘备', '孙权', '赵云', '司马懿',
						'周瑜', '魏延', '袁绍', '马超', '姜维', '黄忠', '诸葛亮',
						'庞德', '张辽', '刘表', '董卓', '孙策', '鲁肃', '邓艾', '大将军',
						'张苞', '袁术', '刘玄德', '玄德大', '子龙', '司马', '孔明笑', '公瑾',
						'操大喜', '翼德', '刘皇叔', '赵子龙', '郭嘉', '仲达', '关云长',
						'操大怒', '玄德问', '阿斗', '刘豫州', '玄德闻', '玄德乃', '曹丞相'
						]
		self.heroAppearTimes = {}
		self.eachChapter = {}
		self.relationNode = ['曹操', '张飞', '吕布', '刘备', '孙权', '赵云', '司马懿', '周瑜', '魏延',
							'袁绍', '马超', '姜维', '黄忠', '诸葛亮', '庞德', '张辽', '刘表', '董卓', '孙策',
							'鲁肃', '邓艾', '大将军', '张苞', '袁术', '赵子龙',
							'郭嘉', '关云长', '阿斗']
		self.relationNodeToChange = [['刘备', '玄德', '玄德曰', '主公', '刘皇叔', '刘玄德','玄德大', '玄德问', '刘豫州', '玄德闻', '玄德乃'],
									['诸葛亮', '孔明曰', '孔明笑', '孔明'],
									['曹操', '丞相', '操大怒', '曹丞相', '操大喜'],
									['关云长', '云长', '关公'],
									['赵云', '子龙', '赵子龙'],
									['司马懿', '司马', '仲达'],
									['公瑾', '周瑜'],
									['张飞', '翼德']]
		self.relationNodeChangeTo = ['刘备', '诸葛亮', '曹操', '关云长', '赵云', '司马懿', '周瑜', '张飞']
		self.node = {}
		self.edge = {}

	def makeWordCloud(self, book, picture):
		text = open(book).read()
		picWithColor = imread(picture)

		wc = WordCloud(background_color='white', max_words=2000,
						mask=picWithColor, stopwords=STOPWORDS,
						max_font_size=40,
						random_state=42, font_path='simsun.ttf')

		wc.generate(text)  # 正常词云
		image_colors = ImageColorGenerator(picWithColor)  # 原图色彩

		plt.figure()
		plt.imshow(wc.recolor(color_func=image_colors))
		plt.axis('off')
		plt.show()

	def appearEachEpisode(self, readBook, writeFile):  # 每回中人物出现次数
		with open(readBook, 'r') as f:
			all_chaps = [chap for chap in f.readlines()]
		dictionary = []
		# 读取文件并分词
		for i in range(120):
			print("处理第{}回".format(i + 1))
			words = list(jieba.cut(all_chaps[i]))
			for word in words:
				if word in self.nameList:
					if word in self.eachChapter:
						self.eachChapter[word] += 1
					else:
						self.eachChapter[word] = 1
			dictionary.append(self.eachChapter)
			self.eachChapter = {}
		data = pd.DataFrame(dictionary)
		data.to_excel(writeFile, index=True, header=True)

	def findMostWords(self, dict, readBook, writeFile):
		jieba.load_userdict(dict)  # 加载字典
		with codecs.open(readBook, 'r', 'utf8') as f:
			i = 0
			for line in f.readlines():
				self.processBar(i, 120)
				i += 1
				poss = pseg.cut(line)  # 返回各个词及其词性
				for w in poss:
					if w.flag != 'nr' or len(w.word) < 2:
						continue
					if self.nouns.get(w.word) is None:
						self.nouns[w.word] = 0
					self.nouns[w.word] += 1  # 如果出现依次，则次数加1
		self.nouns = sorted(self.nouns.items(), key=lambda x: x[:][1], reverse=True)

		with open(writeFile, 'w') as f:
			writer = csv.writer(f, delimiter=',')
			header = ['人物', '出现次数']
			writer.writerow(header)
			for name in self.nouns:
				writer.writerow(name)
			f.close()

	def occurrencesTop10(self, file, html):  # 截取了出现20次以上
		self.Top10 = pd.read_excel(file)
		bar = Bar(html)
		bar.add("出场次数", list(self.Top10['人物'])[:10], list(self.Top10["出场次数"])[:10],
				xaxis_rotate=60, is_label_show=True)
		bar.show_config()
		bar.render(html)

	def nodeAndRelationship(self, readBook):
		for name in self.relationNode:
			self.node[name] = 0
		with open(readBook, 'r') as f:
			i = 0
			for line in f.readlines():  # 循环每行
				self.processBar(i, 2408)
				i += 1
				words = list(jieba.cut(line))

				# 名称处理
				for word in words:
					for changeword in self.relationNodeToChange:
						# 如果在要修改的名单里，直接修改
						if word in changeword:
							word = self.relationNodeChangeTo[self.relationNodeToChange.index(changeword)]
							break

					if word in self.relationNode:  # 出现了人物，node加1, 关系初始化
						self.node[word] += 1
						self.edge[word] = {}
						for name in words:  # 出现其他人物

							# 同样处理人物名称
							for changeword in self.relationNodeToChange:
								if name in changeword:
									name = self.relationNodeChangeTo[self.relationNodeToChange.index(changeword)]
									break

							if name in self.relationNode:
								if word == name:  # 自己同自己不算关系加强
									continue
								if self.edge[word].get(name) is None:
									self.edge[word][name] = 1
								else:
									self.edge[word][name] += 1

		with open("node.csv", 'w', encoding='utf8') as f:
			f.write('ID Label Weight\r\n')
			for name, times in self.node.items():
				f.write(name + " " + name + " " + str(times) + '\r\n')

		with open("edge.csv", 'w', encoding='utf8') as f:
			f.write('Source Target Weight\r\n')
			for name, edge in self.edge.items():
				for v, w in edge.items():
					f.write(name + " " + v + " " + str(w) + '\r\n')

	def everyHeroAppearTimes(self, readBook, writeFile):
		with open(readBook, 'r') as f:
			all_chaps = [chap for chap in f.readlines()]
		self.heroAppearTimes = {}

		# 读取文件并分词
		for i in range(120):
			print("处理第{}回".format(i + 1))
			words = list(jieba.cut(all_chaps[i]))
			for word in words:
				if word in self.nameList:
					if word in self.heroAppearTimes:
						self.heroAppearTimes[word] += 1
					else:
						self.heroAppearTimes[word] = 1
		self.heroAppearTimes = sorted(self.heroAppearTimes.items(), key=lambda x: x[:][1], reverse=True)
		with open(writeFile, 'w', encoding='utf8') as f:
			writer = csv.writer(f, delimiter=',')  # 之所以用csv.writer,是因为会根据人名统一排列，没出现人数为NaN
			for hui in self.heroAppearTimes:
				writer.writerow(hui)

	def drawPicture(self, file):
		df = pd.read_excel(file)
		df = pd.DataFrame(df)
		df.fillna(0, inplace=True)
		df['曹操'] = df['曹操'] + df['丞相'] + df['操大怒'] + df['曹丞相'] + df['操大喜']
		df['诸葛亮'] = df['诸葛亮'] + df['孔明曰'] + df['孔明笑'] + df['孔明']
		df['刘备'] = df['刘备'] + df['玄德'] + df['玄德曰'] + df['主公'] + df['刘皇叔'] + \
					df['刘玄德'] + df['玄德大'] + df['玄德问'] + df['刘豫州'] + df['玄德闻'] + df['玄德乃']
		df['关云长'] = df['关云长'] + df['云长'] + df['关公']
		df['赵云'] = df['赵子龙'] + df['子龙'] + df['赵云']
		df['司马懿'] = df['司马懿'] + df['仲达'] + df['司马']
		df['周瑜'] = df['公瑾'] + df['周瑜']
		df['张飞'] = df['张飞'] + df['翼德']

		del ([df['丞相'], df['操大怒'], df['曹丞相'], df['操大喜'], df['孔明曰'],
			df['孔明笑'], df['孔明'], df['玄德'], df['玄德曰'], df['主公'],
			df['刘皇叔'], df['刘玄德'], df['玄德大'], df['玄德问'], df['刘豫州'],
			df['玄德闻'], df['玄德乃'], df['云长'], df['关公'], df['赵子龙'],
			df['子龙'], df['仲达'], df['司马'], df['公瑾'], df['翼德']])

		data = pd.DataFrame(df)

		kings = ['曹操', '刘备', '孙权', '司马懿']
		shuGuo = ['刘备', '关云长', '张飞', '诸葛亮']

		x = [i for i in range(120)]
		s = Scatter('四位当权者活跃回')

		for king in kings:
			s.add('{}'.format(king), x, data[king], xaxis_rotate=60, symbol_size=4)
		s.show_config()
		s.render('四位当权者活跃回.html')
		nameS = Line('蜀国')

		for name in shuGuo:
			nameS.add('{}'.format(name), x, data[name], xaxis_rotate=60, symbol_size=0, area_opacity=0.6)
		nameS.show_config()
		nameS.render('蜀国.html')

	def processBar(self, num, total):
		rate_num = num/total*100
		sys.stdout.write('\r已完成%.2f%%' % (rate_num))
		if num == total:
			sys.stdout.flush()


if __name__ == "__main__":
	anylysisThreeKindoms = anylysisThreeKindoms()
	anylysisThreeKindoms.findMostWords('dict.txt', 'sanguo.txt', 'wordRootList.csv')  # 找到大约7238个nr词汇
	'''
	接下来是手工整理：
	将出现次数少于20次的词汇删除掉，保留高频词汇，同时剔除一些非人名，如"魏兵"，最终整理了以下词汇表
	namelist = ['曹操', '玄德', '孔明', '关公', '丞相', '孔明曰', '玄德曰', '云长', '张飞', '主公',
				'吕布', '刘备', '孙权', '赵云', '司马懿', '周瑜', '魏延', '袁绍', '马超', '姜维', '黄忠', '诸葛亮',
				'庞德', '张辽', '刘表', '董卓', '孙策', '鲁肃', '邓艾', '大将军', '张苞', '袁术', '刘玄德', '玄德大',
				'子龙', '司马', '孔明笑', '公瑾', '操大喜', '翼德', '刘皇叔', '赵子龙', '郭嘉', '仲达', '关云长',
				'操大怒', '玄德问', '阿斗', '刘豫州', '玄德闻', '玄德乃', '曹丞相']
	'''
	anylysisThreeKindoms.everyHeroAppearTimes('sanguo.txt', 'handledTopNames.csv')

	# 根据上面清单去掉同一个人的不同称呼，得到handledTopNames.xlsx
	anylysisThreeKindoms.occurrencesTop10('handledTopNames.xlsx', 'top10.html')
	anylysisThreeKindoms.makeWordCloud('sanguo.txt', 'zhu.png')
	anylysisThreeKindoms.appearEachEpisode('sanguo.txt', 'appearEachEpisode.xlsx')
	anylysisThreeKindoms.drawPicture('appearEachEpisode.xlsx')
	anylysisThreeKindoms.nodeAndRelationship('sanguo-utf8.txt')