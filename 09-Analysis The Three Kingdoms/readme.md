## 三国人物简单分析
#### 主要任务  
##### 1.找出《三国演义》中名字出现最多的10人；  
##### 2.分析主要几个人物120回中，每回出现的次数，结合具体内容，看发生了什么；  
##### 3.分析任务之间的关系，利用Gephi简单绘图；  
##### 4.绘制“逐”字词云。 
---
#### 准备工作
1.由于要分析120回中主要人物的出场次数，爬取《三国演义》120回，每回放在一个段落里；```len(f.readlines()) = 120.```  
2.安装主要的python库，如```jieba，wordcloud，pandas，codecs，matplotlib，pyecharts， bs4```等，还有Gephi；  

#### 开始工作
**1.首先是获取分成120回，每回一行的文件；**  
```url=http://www.purepen.com/sgyy/```根据规律爬出120回； 
  
**2.找到次数最多的nr(人名)词语；**    
函数```findMostWords```, 逐词查看，长度小于2的自动过滤，按照出现次数排序，写入到文件中，大约是长这个样子的...  
![iamge](https://github.com/Damon0626/Crossin-Programming-Room/blob/master/09-Analysis%20The%20Three%20Kingdoms/Image/wordroot.png)  
  
**3.根据找到的词语排序，大约有7238个词汇，然后手动选取超过出现20次以上的词语，大约200条，剔除一些非人名，如“曹兵”等，最终得到52个词;**  
```['曹操', '玄德', '孔明', '关公', '丞相', '孔明曰', '玄德曰', '云长', '张飞', '主公','吕布', '刘备', '孙权', '赵云', '司马懿', '周瑜', '魏延', '袁绍', '马超', '姜维', '黄忠', '诸葛亮', '庞德', '张辽', '刘表', '董卓', '孙策', '鲁肃', '邓艾', '大将军', '张苞', '袁术', '刘玄德', '玄德大', '子龙', '司马', '孔明笑', '公瑾', '操大喜', '翼德', '刘皇叔', '赵子龙', '郭嘉', '仲达', '关云长','操大怒', '玄德问', '阿斗', '刘豫州', '玄德闻', '玄德乃', '曹丞相']```  
  
**4.逐词匹配上述的52个词，得到52个词分别出现的次数**；  
![次数](https://github.com/Damon0626/Crossin-Programming-Room/blob/master/09-Analysis%20The%20Three%20Kingdoms/Image/handledTimes.png)  
  
**5.整理上述52个词汇，将```玄德曰，玄德怒，玄德乃，刘皇叔```等等词汇合并，绘制Top10;**  
![Top10](https://github.com/Damon0626/Crossin-Programming-Room/blob/master/09-Analysis%20The%20Three%20Kingdoms/Image/top10.png)  
  
**6.根据上述52个词汇，分别分析每一回，利用pandas.DataFrame很方便得到每回52个人分别出现的次数**；  
![每回人数](https://github.com/Damon0626/Crossin-Programming-Room/blob/master/09-Analysis%20The%20Three%20Kingdoms/Image/meihui.png)  
可以看出，表格中有大量的空白，后续使用，需要将空白填充0， ```DataFrame.fillna(0, inplace=True)```  
  
**7.绘制一些简单的图；**  
蜀国主要人物全书分布情况，三位结拜兄弟贯穿前80回左右，等他们退出历史舞台，诸葛亮继续辅佐，支撑着蜀国大业。  
![蜀国](https://github.com/Damon0626/Crossin-Programming-Room/blob/master/09-Analysis%20The%20Three%20Kingdoms/Image/%E8%9C%80%E5%9B%BD.png)  

诸葛亮在35-40, 80-100回出现了较多次数，自然是**“三顾茅庐”、“火烧七百里联营”、“巧布八阵图”、“七擒孟获”**等较为熟知的历史故事；
同时，80回后诸葛亮出现次数占据了全书中较大范围，也是“先帝托孤”后“鞠躬尽瘁”的具体表现。  
![刘诸葛](https://github.com/Damon0626/Crossin-Programming-Room/blob/master/09-Analysis%20The%20Three%20Kingdoms/Image/%E5%88%98%E8%AF%B8%E8%91%9B.png)  
  
四位当权者曹操、刘备、孙权、司马懿活动活度，前80回，曹刘孙较为活跃，体现出了三国纷争的局面，读这一部分，厮杀场面也是相当精彩；
待三位同时代的人物退出历史舞台后，逐渐司马懿开始活跃，“一同秦两汉，三分魏蜀吴，两晋前后延”，历史朝代更替，滚滚向前。  
![掌权](https://github.com/Damon0626/Crossin-Programming-Room/blob/master/09-Analysis%20The%20Three%20Kingdoms/Image/%E5%9B%9B%E4%BD%8D%E5%BD%93%E6%9D%83%E8%80%85.png)

分析数据的能力还优待提高，想不出较好的分析的内容，还需多写、多与人沟通交流，提升对数据的认识。  
**8.分析人物之间的关系。根据全文2700多个自然段，如果一个自然段内同时出现了A和B，将A和B之间的关系+1；**  
得到Node和Edge两份csv文件，输入到Gephi，得到以下关系图，故事还是围绕这曹刘的纷争开展，诸葛亮的经纬之才也体现的淋漓尽致。  
![relationship](https://github.com/Damon0626/Crossin-Programming-Room/blob/master/09-Analysis%20The%20Three%20Kingdoms/Image/guanxitu.png)  
**9.词云制作；**  
ps做了一张图，制作词云。  
![image](https://github.com/Damon0626/Crossin-Programming-Room/blob/master/09-Analysis%20The%20Three%20Kingdoms/Image/zhu.png)
![词云](https://github.com/Damon0626/Crossin-Programming-Room/blob/master/09-Analysis%20The%20Three%20Kingdoms/Image/wordcloud.png)  

---
真正自己去做的时候，才能一次次填补自己的坑。哈哈哈，加油！
