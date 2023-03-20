# coding=gbk
#@Time: 2021/11/2 21:47
#@File : 不同公司类型的岗位数量.py

import pandas as pd
import pymysql
from pyecharts import options as opts
from pyecharts.charts import  Scatter

connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT 公司类型 ,count(岗位名称) as 数量  FROM bigdata  GROUP BY 公司类型 order by 数量 desc;'
df=pd.read_sql(sql,connect)
x=df['公司类型']
y=df['数量']
scatter = (Scatter()
           .add_xaxis(x.tolist())
           .add_yaxis('', y.tolist())
           .set_global_opts( visualmap_opts=opts.VisualMapOpts(
            type_="size",range_size=[5,50]),
            xaxis_opts=opts.AxisOpts(name='类型',axislabel_opts={"rotate":40}),
            yaxis_opts=opts.AxisOpts(name="数量")

            )
            .set_series_opts(label_opts=opts.LabelOpts(position='top'))
)
scatter.render('C:\BIGDATA\python1912\毕业设计\图表\不同公司类型的岗位数量.html')