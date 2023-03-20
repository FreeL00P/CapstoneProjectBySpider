# coding=gbk
#@Time: 2021/10/31 20:04
#@File : ��ͬ���е�ƽ��н�ʶԱ�.py



import pandas as pd
import pymysql as pl
from pyecharts.charts import Line, Bar
from pyecharts import options as opts
connect = pl.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT ����,avg(SUBSTRING_INDEX(н��, "-", 1)) as ���ƽ��н��,avg(SUBSTRING_INDEX(н��, "-", -1)) as ���ƽ��н�� FROM bigdata group by ����;'
df=pd.read_sql(sql,connect)
x=df['����']
y1=df['���ƽ��н��']
y2=df['���ƽ��н��']
y1=[round(i,0) for i in y1]
y2=[round(i,0) for i in y2]
line = (Line()
       .add_xaxis(x.tolist())
       .add_yaxis("���ƽ��н��",y2,z_level=1,color='')
       .extend_axis(yaxis=opts.AxisOpts(name='��λ(Ԫ)',max_=25000))
       .set_global_opts(
            title_opts=opts.TitleOpts(title="��ͬ����ƽ��н�ʶԱ�",pos_left='center'),
            legend_opts=opts.LegendOpts(pos_left="center",pos_bottom="0"),
            yaxis_opts=opts.AxisOpts(name="��λ(Ԫ)"),
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45})
            )

)

bar = (Bar()
       .add_xaxis(x.tolist())
       .add_yaxis("���ƽ��н��",y1,yaxis_index=1)
       .reversal_axis()
       .set_global_opts(
            title_opts=opts.TitleOpts(title="��ͬ����ƽ��н�ʶԱ�",pos_left='center'),
            legend_opts=opts.LegendOpts(pos_left="center",pos_bottom="5%"),
            yaxis_opts=opts.AxisOpts(name="��λ(Ԫ)"))
        .set_series_opts(label_opts=opts.LabelOpts(position='top'))
)

line.overlap(bar)
line.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\��ͬ���е�ƽ��н�ʶԱ�.html')