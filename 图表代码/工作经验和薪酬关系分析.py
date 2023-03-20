# coding=gbk
#@Time: 2021/11/1 17:19
#@File : ���������н���ϵ����.py

import pandas as pd
import pymysql
from pyecharts.charts import Line
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql="SELECT ����,SUBSTRING_INDEX(н��, '-', 1) as ���н��,SUBSTRING_INDEX(н��, '-', -1) as ���н�� FROM bigdata group by ���� ORDER BY FIELD(����,'����','�޾���','1������','1-3��','3-5��','5-10��','10������') ;"
df=pd.read_sql(sql,connect)
x=df['����']
y1=df['���н��']
y2=df['���н��']
line=(Line()
      .add_xaxis(x.tolist())
      .add_yaxis('���н��',y1.tolist())
      .add_yaxis('���н��',y2.tolist())
      .set_global_opts(title_opts=opts.TitleOpts(title='���������н��֮��Ĺ�ϵ'),
                       yaxis_opts=opts.AxisOpts(name="н�ʣ���λ��Ԫ��"),
                       xaxis_opts=opts.AxisOpts(name='����'))
      )
line.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\���������н��֮��Ĺ�ϵ.html')