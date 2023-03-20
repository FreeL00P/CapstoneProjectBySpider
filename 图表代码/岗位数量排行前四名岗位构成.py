# coding=gbk
#@Time: 2021/11/1 14:59
#@File : ��λ��������ǰ������λ����.py


import pandas as pd
import pymysql
from pyecharts.charts import Pie as pi
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
beijing='SELECT ��λ���,count(��λ���) ��λ���� FROM bigdata WHERE ����="����" GROUP BY ��λ��� HAVING ��λ����>10 ORDER BY count(`��λ���`) desc;'
shanghai="SELECT ��λ���,count(��λ���) ��λ���� FROM bigdata WHERE ����='�Ϻ�' GROUP BY ��λ��� HAVING ��λ����>10 ORDER BY count(`��λ���`) desc;"
guangzhou="SELECT ��λ���,count(��λ���) ��λ���� FROM bigdata WHERE ����='����' GROUP BY ��λ��� HAVING ��λ����>10 ORDER BY count(`��λ���`) desc;"
shenzhen="SELECT ��λ���,count(��λ���) ��λ���� FROM bigdata WHERE ����='����' GROUP BY ��λ��� HAVING ��λ����>10 ORDER BY count(`��λ���`) desc;"
bj=pd.read_sql(beijing,connect)
x_b=bj['��λ���']
y_b=bj['��λ����']
bj=pd.read_sql(shanghai,connect)
x_s=bj['��λ���']
y_s=bj['��λ����']
bj=pd.read_sql(guangzhou,connect)
x_g=bj['��λ���']
y_g=bj['��λ����']
bj=pd.read_sql(shenzhen,connect)
x_sz=bj['��λ���']
y_sz=bj['��λ����']
data_bj=[list(i) for i in zip(x_b,y_b)]
data_sh=[list(i) for i in zip(x_s,y_s)]
data_gz=[list(i) for i in zip(x_g,y_g)]
data_sz=[list(i) for i in zip(x_sz,y_sz)]
# ��ѧ�����Ʊ�ͼ
pie = (pi(init_opts=opts.InitOpts(height='1200px',width='2000px'))
        .add("����",data_bj,radius=['35%','75%'],rosetype="radius")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="�����ĸ�λ����",pos_bottom='50%',pos_right='center'),
            legend_opts=opts.LegendOpts(is_show=False),
            )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%",font_size=25))
)
pie.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\�����ĸ�λ����.html')

pie = (pi(init_opts=opts.InitOpts(height='1200px',width='2000px'))
        .add("�Ϻ�",data_sh,radius=['35%','75%'],rosetype="radius")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="�Ϻ��ĸ�λ����",pos_bottom='50%',pos_right='center'),
            legend_opts=opts.LegendOpts(is_show=False),
            )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%",font_size=25))
)
pie.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\�Ϻ��ĸ�λ����.html')

pie = (pi(init_opts=opts.InitOpts(height='1200px',width='2000px'))
        .add("����",data_gz,radius=['35%','75%'],rosetype="radius")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="���ݵĸ�λ����",pos_bottom='50%',pos_right='center'),
            legend_opts=opts.LegendOpts(is_show=False),
            )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%",font_size=25))
)
pie.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\���ݵĸ�λ����.html')

pie = (pi(init_opts=opts.InitOpts(height='1200px',width='2000px'))
        .add("����",data_sz,radius=['35%','75%'],rosetype="radius")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="���ڵĸ�λ����",pos_bottom='50%',pos_right='center'),
            legend_opts=opts.LegendOpts(is_show=False),
            )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%",font_size=25))
)
pie.render('C:\BIGDATA\python1912\��ҵ���\ͼ��\���ڵĸ�λ����.html')