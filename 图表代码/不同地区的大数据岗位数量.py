# coding=gbk
#@Time: 2021/11/1 14:40
#@File : ��ͬ�����Ĵ����ݸ�λ����.py
import pandas as pd
import pymysql
from pyecharts.charts import Bar
from pyecharts import options as opts

connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT ����,count(`��λ����`) ��λ���� FROM bigdata GROUP BY ���� ORDER BY ��λ���� desc ;'
df=pd.read_sql(sql,connect)
x=df['����']
y=df['��λ����']
bar=(Bar()
           .add_xaxis(x.tolist())
           .add_yaxis('',y.tolist())
           .set_global_opts(title_opts=opts.TitleOpts(title='��ͬ�����Ĵ����ݸ�λ����',pos_left='center'),
                            xaxis_opts=opts.AxisOpts(name='����',axislabel_opts={"rotate":40}),
                            yaxis_opts=opts.AxisOpts(name="��λ����"))
           .set_series_opts(label_opts=opts.LabelOpts(position='top'))
           )
bar.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\��ͬ�����Ĵ����ݸ�λ����.html')


