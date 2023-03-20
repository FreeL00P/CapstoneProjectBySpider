# coding=gbk
#@Time: 2021/10/31 20:04
#@File : 不同城市的平均薪资对比.py



import pandas as pd
import pymysql as pl
from pyecharts.charts import Line, Bar
from pyecharts import options as opts
connect = pl.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
sql='SELECT 地区,avg(SUBSTRING_INDEX(薪资, "-", 1)) as 最低平均薪资,avg(SUBSTRING_INDEX(薪资, "-", -1)) as 最高平均薪资 FROM bigdata group by 地区;'
df=pd.read_sql(sql,connect)
x=df['地区']
y1=df['最低平均薪资']
y2=df['最高平均薪资']
y1=[round(i,0) for i in y1]
y2=[round(i,0) for i in y2]
line = (Line()
       .add_xaxis(x.tolist())
       .add_yaxis("最高平均薪资",y2,z_level=1,color='')
       .extend_axis(yaxis=opts.AxisOpts(name='单位(元)',max_=25000))
       .set_global_opts(
            title_opts=opts.TitleOpts(title="不同城市平均薪资对比",pos_left='center'),
            legend_opts=opts.LegendOpts(pos_left="center",pos_bottom="0"),
            yaxis_opts=opts.AxisOpts(name="单位(元)"),
            xaxis_opts=opts.AxisOpts(axislabel_opts={"rotate": 45})
            )

)

bar = (Bar()
       .add_xaxis(x.tolist())
       .add_yaxis("最低平均薪资",y1,yaxis_index=1)
       .reversal_axis()
       .set_global_opts(
            title_opts=opts.TitleOpts(title="不同城市平均薪资对比",pos_left='center'),
            legend_opts=opts.LegendOpts(pos_left="center",pos_bottom="5%"),
            yaxis_opts=opts.AxisOpts(name="单位(元)"))
        .set_series_opts(label_opts=opts.LabelOpts(position='top'))
)

line.overlap(bar)
line.render('C:\BIGDATA\python1912\毕业设计\图表\不同城市的平均薪资对比.html')