# coding=gbk
#@Time: 2021/10/31 20:45
#@File : 经验要求.py
import pandas as pd
import pymysql
from pyecharts.charts import Radar
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT 经验,count(经验) 岗位数 FROM bigdata group by 经验 ORDER BY 岗位数 DESC;'
df=pd.read_sql(sql,connect)
x=df['经验']
y=df['岗位数']
y=[y.tolist()]
c_schema= [opts.RadarIndicatorItem(name=i,max_=2600,min_=1) for i in list(x)]
radar = (Radar()
        .add('岗位数',y)
        .add_schema(c_schema)

         )
radar.render('C:\BIGDATA\python1912\毕业设计\图表\经验要求.html')