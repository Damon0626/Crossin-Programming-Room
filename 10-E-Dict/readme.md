如果喜欢，欢迎```star```和```fork```。
#### 利用PyQt5制作电子词典
年前（*2018年12月22日*）Crossin编程教室发布了一个制作电子词典的小作业，自己懒懒散散的做了一个，大体上的功能都实现了。码的过程，个人觉得对入门python还是有一定的帮助，就整理了下，一为复习总结，二来随意吧☺。
#### 主要功能
1.**每日一句，中英文对照**```(调用金山词霸API)```;  
2.**单词翻译，显示中文释义和音标**```(调用金山词霸API)```;  
3.**添加生词；**  
4.**单词复习；**  
5.**单词总数显示；**  
6.**本周添加单词数柱状图显示；**  
7.**当前运行用户和生词本路径显示**。  
____
**上图：**  

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190122102430752.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM2MTcyMjk=,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20190122102021388.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM2MTcyMjk=,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20190122102016492.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM2MTcyMjk=,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/2019012210201258.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM2MTcyMjk=,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20190122102008876.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM2MTcyMjk=,size_16,color_FFFFFF,t_70)
#### 涉及到的知识点
###### 1.PyQt5
1.```QDialog```使用；  
2.```QPushButton```按钮使用、信号槽；  
3.```QStatusBar```状态栏使用；  
4.```QFrame```页面使用；  
5.```QLabel```标签使用、设置像素图显示图片；  
6.```QTextBrower```文本显示框使用；  
7.```QLineEdit```输入框使用；  
8.```QTableWidget```表格使用、设置表头、内容等操作；  
9.上述各元件属性的设置，包括**字体、背景、字号、位置、格式......**  
###### 2.Pandas & CSV & Numpy
利用常用的几个数据处理的库，简直不能再好用，处理csv文件也特别好用，这里没有特殊处理，用户可以直接打开，有需求可以使用```pickle```阻止用户直接预览  


使用CSV来创建生词本```dic.csv```,单次写入等操作用Pandas配合Numpy处理  

1.```read_csv```；  
2.```dataframe```；  
3.```writerow```;  
###### 3.Request
首页调用了[**金山词霸的API**](http://open.iciba.com/dsapi),显示其**每日一句**内容，原本打算直接使用Qt的web组件来显示内容，但是显示的太随心所欲了，驾驭不了...  

1.```request.get```获取所有内容；  
2.```request.get().json()```将内容专为```json```格式，具体的```key```对应的内容，可以去搜索，根据自己需求获取对应的内容，这里不列出；    
###### 4.Datetime
要显示每周学习的情况，添加生词的时候直接插入了时间  

1.```datetime.now().strftime()```按照格式设置当前时间；  
2.```datetime.delta()```计算日期差；  
###### 5.matplotlib.pyplot
主要用来显示本周添加生词数  

1.```plt.bar()```柱状图；  
2.```plt.text()```添加文字说明；  
3.```plt.style.use()```更换显示格式，本文使用```ggplot```;  
4.```plt.figure()```图像；  
5.```FigureCanvas```画布；  
###### 6.os & getpass
在**我的**页面，附加信息获取当前运行用户的```host```和当前运行本程序的```path```  

1.```os.getcwd()```获取当前运行路径；  
2.```getpass.getuser()```获取当前主机名；  
___
#### 写在后面
简单的实现了主要的功能，当然还可以更复杂，如：  

1.添加用户登录、验证等功能；  
2.将单词本换成服务器端的数据库存储，可以实现更换设备登录后自动恢复生词本；  
3.获取用户GPS地址，显示周围的小伙伴；  
4.对学习情况进行排名；  
5.复习单词策略更科学；  
.......
