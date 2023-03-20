# coding=gbk
#@Time: 2021/10/31 20:00
#@File : 技能要求.py

import pandas as pd
import pymysql
from pyecharts.charts import WordCloud
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT  SUBSTRING_INDEX(技能要求, "-", -1)  技能要求,count(SUBSTRING_INDEX(技能要求, "-", -1)) as 数量  FROM bigdata group by SUBSTRING_INDEX(技能要求, "-", -1) ;'
df=pd.read_sql(sql,connect)
x=df['技能要求']
y=df['数量']
data=[list(i) for i in zip(x,y)]
wordcloud=(WordCloud()
           .add("技能要求",data,word_size_range=[10,100])
           .set_global_opts(title_opts=opts.TitleOpts(title='技能要求',pos_left='center'))
           )
wordcloud.render('C:\BIGDATA\python1912\毕业设计\图表\技能要求.html')
