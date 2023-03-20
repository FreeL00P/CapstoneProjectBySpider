# coding=gbk
#@Time: 2021/10/31 19:01
#@File : 学历要求.py
#!/usr/bin/python3
import pandas as pd
import pymysql
from pyecharts.charts import  Funnel
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT COUNT(`岗位名称`) as 岗位数量,学历 FROM bigdata GROUP BY `学历` ;'
df=pd.read_sql(sql,connect)
x=df['学历']
y=df['岗位数量']
data=[list(i) for i in zip(x,y)]
# 按学历绘制饼图

funnel = (Funnel()
        .add("占比",data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="大数据岗位对学历的要求占比",pos_left='center'),
            legend_opts=opts.LegendOpts(pos_left="center",pos_bottom="5%"),)
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%",))
)


funnel.render('C:\BIGDATA\python1912\毕业设计\图表\学历要求.html')