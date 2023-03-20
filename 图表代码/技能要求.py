# coding=gbk
#@Time: 2021/10/31 20:00
#@File : ����Ҫ��.py

import pandas as pd
import pymysql
from pyecharts.charts import WordCloud
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT  SUBSTRING_INDEX(����Ҫ��, "-", -1)  ����Ҫ��,count(SUBSTRING_INDEX(����Ҫ��, "-", -1)) as ����  FROM bigdata group by SUBSTRING_INDEX(����Ҫ��, "-", -1) ;'
df=pd.read_sql(sql,connect)
x=df['����Ҫ��']
y=df['����']
data=[list(i) for i in zip(x,y)]
wordcloud=(WordCloud()
           .add("����Ҫ��",data,word_size_range=[10,100])
           .set_global_opts(title_opts=opts.TitleOpts(title='����Ҫ��',pos_left='center'))
           )
wordcloud.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\����Ҫ��.html')
