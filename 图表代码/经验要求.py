# coding=gbk
#@Time: 2021/10/31 20:45
#@File : ����Ҫ��.py
import pandas as pd
import pymysql
from pyecharts.charts import Radar
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT ����,count(����) ��λ�� FROM bigdata group by ���� ORDER BY ��λ�� DESC;'
df=pd.read_sql(sql,connect)
x=df['����']
y=df['��λ��']
y=[y.tolist()]
c_schema= [opts.RadarIndicatorItem(name=i,max_=2600,min_=1) for i in list(x)]
radar = (Radar()
        .add('��λ��',y)
        .add_schema(c_schema)

         )
radar.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\����Ҫ��.html')