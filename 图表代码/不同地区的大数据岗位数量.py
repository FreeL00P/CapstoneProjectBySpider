# coding=gbk
#@Time: 2021/11/1 14:40
#@File : 不同地区的大数据岗位数量.py
import pandas as pd
import pymysql
from pyecharts.charts import Bar
from pyecharts import options as opts

connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT 地区,count(`岗位名称`) 岗位数量 FROM bigdata GROUP BY 地区 ORDER BY 岗位数量 desc ;'
df=pd.read_sql(sql,connect)
x=df['地区']
y=df['岗位数量']
bar=(Bar()
           .add_xaxis(x.tolist())
           .add_yaxis('',y.tolist())
           .set_global_opts(title_opts=opts.TitleOpts(title='不同地区的大数据岗位数量',pos_left='center'),
                            xaxis_opts=opts.AxisOpts(name='城市',axislabel_opts={"rotate":40}),
                            yaxis_opts=opts.AxisOpts(name="岗位数量"))
           .set_series_opts(label_opts=opts.LabelOpts(position='top'))
           )
bar.render('C:\BIGDATA\python1912\毕业设计\图表\不同地区的大数据岗位数量.html')


