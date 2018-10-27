# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-10-27 上午10:24
# @Email : wwymsn@163.com
# @Software: PyCharm

import math
import numpy as np


# method1:我也不知道下面的c语言代码是什么数学原理，根据别人的整理，转换成python3代码贴出来,轻松求得2800位
'''
这段C代码是这样的：
#include "stdio.h"
long a=10000, b, c=2800, d, e, f[2801], g;
void main() {
for( ;b-c; ) f[b++] =a/5;
for( ; d=0, g=c*2; c-=14,printf("%.4d",e+d/a),e=d%a)
for(b=c; d+=f[b]*a,f[b] =d%--g,d/=g--,--b; d*=b) ;
}
'''

c = 2800
f = np.zeros(2801)
b = 0
for i in range(c):  # 除最后一位，其余全部是2
	f[i] = 2
e = 0
while c > 0:
	d = 0
	b = c
	while b > 0:
		d *= b
		d += (f[b] * 10)
		f[b] = d % (b * 2-1)
		d = int(d/(b * 2 - 1))  # 如果不取整，源代码结果不对
		b -= 1
	c -= 1
	print("%d" % ((e+int(d)/10) % 10), end="")
	e = d % 10


# method2: 割圆术
''' 
假设正6边形的变长为１，以后的正多边形为6*２^n条边, an为正多边形的边长
Sn+1为其中一个小三角形的面积，n,n+1,n+2均为下标
Sn+1 = 1/4 * an
Sn+2 = 1/4 * an+1
'''
i = 0
n = 15
an = 1
while i < n:
	an1Pow = 2 - math.sqrt(4-math.pow(an, 2))
	an1 = math.sqrt(an1Pow)
	an = an1
	i += 1
print("由正%d边形求出的PI为%.50f" % (6*math.pow(2, n), (3*math.pow(2, n)*an)))


# method1: Leibniz formula
def xrange(x):
	n = 1
	while n <= x:
		yield n
		n += 2


quarterPi = 0
flag = 1

for i in xrange(100000000):
	quarterPi += (1/i)*flag
	flag = -flag

print(4*quarterPi)
