# coding=gbk
#@Time: 2021/11/2 21:47
#@File : ��ͬ��˾���͵ĸ�λ����.py

import pandas as pd
import pymysql
from pyecharts import options as opts
from pyecharts.charts import  Scatter

connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT ��˾���� ,count(��λ����) as ����  FROM bigdata  GROUP BY ��˾���� order by ���� desc;'
df=pd.read_sql(sql,connect)
x=df['��˾����']
y=df['����']
scatter = (Scatter()
           .add_xaxis(x.tolist())
           .add_yaxis('', y.tolist())
           .set_global_opts( visualmap_opts=opts.VisualMapOpts(
            type_="size",range_size=[5,50]),
            xaxis_opts=opts.AxisOpts(name='����',axislabel_opts={"rotate":40}),
            yaxis_opts=opts.AxisOpts(name="����")

            )
            .set_series_opts(label_opts=opts.LabelOpts(position='top'))
)
scatter.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\��ͬ��˾���͵ĸ�λ����.html')