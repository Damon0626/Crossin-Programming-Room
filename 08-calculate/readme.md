圆周率的计算
---
### 抛砖引玉三种方法
#### 1:传说中计算π的超牛的C程序，3行代码，计算π后面800位...
原c代码如下：  
#include "stdio.h"  
long a=10000, b, c=2800, d, e, f[2801], g;  
void main() {  
for( ;b-c; ) f[b++] =a/5;  
for( ; d=0, g=c*2; c-=14,printf("%.4d",e+d/a),e=d%a)  
for(b=c; d+=f[b]*a,f[b] =d%--g,d/=g--,--b; d*=b) ;  
}  
表示根本不理解**背后的数学推理**，后续再继续研读吧  
**已根据c代码，换成python代码**  
#### 2：我们老祖宗留下来的宝贵财富，割圆术
当计算到6*2^n边形, n=15以上的时候，貌似就不是很准确了...  
![image](https://github.com/Damon0626/Crossin-Programming-Room/blob/master/08-calculate/%E5%89%B2%E5%9C%86%E6%9C%AF.png)  
#### 3.莱布尼茨公式
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\pi&space;}{4}&space;=&space;1-\frac{1}{3}&plus;\frac{1}{5}-\frac{1}{7}&plus;\frac{1}{9}..." target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\pi&space;}{4}&space;=&space;1-\frac{1}{3}&plus;\frac{1}{5}-\frac{1}{7}&plus;\frac{1}{9}..." title="\frac{\pi }{4} = 1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\frac{1}{9}..." /></a>  
计算到了n=100000000时的情况，比较废资源，也比较慢，为了防止占用太多资源，使用了xrange函数
