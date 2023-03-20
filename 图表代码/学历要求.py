# coding=gbk
#@Time: 2021/10/31 19:01
#@File : ѧ��Ҫ��.py
#!/usr/bin/python3
import pandas as pd
import pymysql
from pyecharts.charts import  Funnel
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT COUNT(`��λ����`) as ��λ����,ѧ�� FROM bigdata GROUP BY `ѧ��` ;'
df=pd.read_sql(sql,connect)
x=df['ѧ��']
y=df['��λ����']
data=[list(i) for i in zip(x,y)]
# ��ѧ�����Ʊ�ͼ

funnel = (Funnel()
        .add("ռ��",data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="�����ݸ�λ��ѧ����Ҫ��ռ��",pos_left='center'),
            legend_opts=opts.LegendOpts(pos_left="center",pos_bottom="5%"),)
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%",))
)


funnel.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\ѧ��Ҫ��.html')