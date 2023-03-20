# coding=gbk
#@Time: 2021/10/31 19:44
#@File : 热门岗位.py
import pandas as pd
import pymysql
from pyecharts.charts import WordCloud
from pyecharts import options as opts
# 连接到数据库
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT 岗位类别,count(岗位名称) as 数量  FROM bigdata group by 岗位类别;'
df=pd.read_sql(sql,connect)
x=df['岗位类别']
y=df['数量']
data=[list(i) for i in zip(x,y)]
wordcloud=(WordCloud()
           .add("热门岗位",data)
           .set_global_opts(title_opts=opts.TitleOpts(title='热门岗位',pos_left='center'))
           )
wordcloud.render('C:\BIGDATA\python1912\毕业设计\图表\热门岗位.html')