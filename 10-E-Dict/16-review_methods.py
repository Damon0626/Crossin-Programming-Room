# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-3 下午11:10
# @Email : wwymsn@163.com
# @Software: PyCharm

import pandas as pd
import numpy as np
'''
复习的策略：（简单的设置为如下算法）
初始添加后，各个单词的复习次数都初始为0;

每点击＂下一次＂，认为单词复习过一次
根据复习次数排序，最少次数的第一个单词会被优先拿出来复习

如果点击"提示",则复习次数不增加，直接跳转到下一词
'''

path = 'dic.csv'

data = pd.read_csv(path)
least_time_of_review = np.argmax(data['have_review_times'])

w = data['words'][least_time_of_review]
print(w)