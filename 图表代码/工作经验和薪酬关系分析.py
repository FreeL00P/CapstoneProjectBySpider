# coding=gbk
#@Time: 2021/11/1 17:19
#@File : 工作经验和薪酬关系分析.py

import pandas as pd
import pymysql
from pyecharts.charts import Line
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql="SELECT 经验,SUBSTRING_INDEX(薪资, '-', 1) as 最低薪资,SUBSTRING_INDEX(薪资, '-', -1) as 最高薪资 FROM bigdata group by 经验 ORDER BY FIELD(经验,'不限','无经验','1年以下','1-3年','3-5年','5-10年','10年以上') ;"
df=pd.read_sql(sql,connect)
x=df['经验']
y1=df['最低薪资']
y2=df['最高薪资']
line=(Line()
      .add_xaxis(x.tolist())
      .add_yaxis('最低薪酬',y1.tolist())
      .add_yaxis('最高薪酬',y2.tolist())
      .set_global_opts(title_opts=opts.TitleOpts(title='工作经验和薪酬之间的关系'),
                       yaxis_opts=opts.AxisOpts(name="薪资（单位：元）"),
                       xaxis_opts=opts.AxisOpts(name='经验'))
      )
line.render('C:\BIGDATA\python1912\毕业设计\图表\工作经验和薪酬之间的关系.html')