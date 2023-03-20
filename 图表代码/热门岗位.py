# coding=gbk
#@Time: 2021/10/31 19:44
#@File : ���Ÿ�λ.py
import pandas as pd
import pymysql
from pyecharts.charts import WordCloud
from pyecharts import options as opts
# ���ӵ����ݿ�
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT ��λ���,count(��λ����) as ����  FROM bigdata group by ��λ���;'
df=pd.read_sql(sql,connect)
x=df['��λ���']
y=df['����']
data=[list(i) for i in zip(x,y)]
wordcloud=(WordCloud()
           .add("���Ÿ�λ",data)
           .set_global_opts(title_opts=opts.TitleOpts(title='���Ÿ�λ',pos_left='center'))
           )
wordcloud.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\���Ÿ�λ.html')