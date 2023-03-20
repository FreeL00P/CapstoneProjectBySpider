# coding=gbk
#@Time: 2021/11/1 18:35
#@File : 学历与薪酬的关系.py
import pandas as pd
import pymysql
from pyecharts.charts import Bar
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql="SELECT `学历`,SUBSTRING_INDEX(薪资, '-', 1) as 最低薪资,SUBSTRING_INDEX(薪资, '-', -1) as 最高薪资 FROM bigdata group by 学历 ORDER BY FIELD(学历,'中专/中技','高中','大专','本科','博士','硕士','学历不限');"
df=pd.read_sql(sql,connect)
x=df['学历']
y1=df['最低薪资']
y2=df['最高薪资']
# y1=[round(i,0) for i in y1]
# y2=[round(i,0) for i in y2]
bar=(Bar()
      .add_xaxis(x.tolist())
      .add_yaxis('最高薪酬', y2.tolist() )
      .add_yaxis('最低薪酬',y1.tolist())
      .set_global_opts(title_opts=opts.TitleOpts(title='学历和薪酬之间的关系'),
                       xaxis_opts=opts.AxisOpts(name='学历'),
                       yaxis_opts=opts.AxisOpts(name='薪资（元）')
                      )
      )
bar.render('C:\BIGDATA\python1912\毕业设计\图表\学历和薪酬之间的关系.html')