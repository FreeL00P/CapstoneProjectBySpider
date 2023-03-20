# coding=gbk
#@Time: 2021/11/1 18:35
#@File : ѧ����н��Ĺ�ϵ.py
import pandas as pd
import pymysql
from pyecharts.charts import Bar
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql="SELECT `ѧ��`,SUBSTRING_INDEX(н��, '-', 1) as ���н��,SUBSTRING_INDEX(н��, '-', -1) as ���н�� FROM bigdata group by ѧ�� ORDER BY FIELD(ѧ��,'��ר/�м�','����','��ר','����','��ʿ','˶ʿ','ѧ������');"
df=pd.read_sql(sql,connect)
x=df['ѧ��']
y1=df['���н��']
y2=df['���н��']
# y1=[round(i,0) for i in y1]
# y2=[round(i,0) for i in y2]
bar=(Bar()
      .add_xaxis(x.tolist())
      .add_yaxis('���н��', y2.tolist() )
      .add_yaxis('���н��',y1.tolist())
      .set_global_opts(title_opts=opts.TitleOpts(title='ѧ����н��֮��Ĺ�ϵ'),
                       xaxis_opts=opts.AxisOpts(name='ѧ��'),
                       yaxis_opts=opts.AxisOpts(name='н�ʣ�Ԫ��')
                      )
      )
bar.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\ѧ����н��֮��Ĺ�ϵ.html')