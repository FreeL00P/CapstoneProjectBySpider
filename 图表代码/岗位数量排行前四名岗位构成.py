# coding=gbk
#@Time: 2021/11/1 14:59
#@File : 岗位数量排行前四名岗位构成.py


import pandas as pd
import pymysql
from pyecharts.charts import Pie as pi
from pyecharts import options as opts
connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306, db='jundb', charset='utf8')
cursor = connect.cursor()
beijing='SELECT 岗位类别,count(岗位类别) 岗位数量 FROM bigdata WHERE 地区="北京" GROUP BY 岗位类别 HAVING 岗位数量>10 ORDER BY count(`岗位类别`) desc;'
shanghai="SELECT 岗位类别,count(岗位类别) 岗位数量 FROM bigdata WHERE 地区='上海' GROUP BY 岗位类别 HAVING 岗位数量>10 ORDER BY count(`岗位类别`) desc;"
guangzhou="SELECT 岗位类别,count(岗位类别) 岗位数量 FROM bigdata WHERE 地区='广州' GROUP BY 岗位类别 HAVING 岗位数量>10 ORDER BY count(`岗位类别`) desc;"
shenzhen="SELECT 岗位类别,count(岗位类别) 岗位数量 FROM bigdata WHERE 地区='深圳' GROUP BY 岗位类别 HAVING 岗位数量>10 ORDER BY count(`岗位类别`) desc;"
bj=pd.read_sql(beijing,connect)
x_b=bj['岗位类别']
y_b=bj['岗位数量']
bj=pd.read_sql(shanghai,connect)
x_s=bj['岗位类别']
y_s=bj['岗位数量']
bj=pd.read_sql(guangzhou,connect)
x_g=bj['岗位类别']
y_g=bj['岗位数量']
bj=pd.read_sql(shenzhen,connect)
x_sz=bj['岗位类别']
y_sz=bj['岗位数量']
data_bj=[list(i) for i in zip(x_b,y_b)]
data_sh=[list(i) for i in zip(x_s,y_s)]
data_gz=[list(i) for i in zip(x_g,y_g)]
data_sz=[list(i) for i in zip(x_sz,y_sz)]
# 按学历绘制饼图
pie = (pi(init_opts=opts.InitOpts(height='1200px',width='2000px'))
        .add("北京",data_bj,radius=['35%','75%'],rosetype="radius")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="北京的岗位构成",pos_bottom='50%',pos_right='center'),
            legend_opts=opts.LegendOpts(is_show=False),
            )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%",font_size=25))
)
pie.render('C:\BIGDATA\python1912\毕业设计\图表\北京的岗位构成.html')

pie = (pi(init_opts=opts.InitOpts(height='1200px',width='2000px'))
        .add("上海",data_sh,radius=['35%','75%'],rosetype="radius")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="上海的岗位构成",pos_bottom='50%',pos_right='center'),
            legend_opts=opts.LegendOpts(is_show=False),
            )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%",font_size=25))
)
pie.render('C:\BIGDATA\python1912\毕业设计\图表\上海的岗位构成.html')

pie = (pi(init_opts=opts.InitOpts(height='1200px',width='2000px'))
        .add("广州",data_gz,radius=['35%','75%'],rosetype="radius")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="广州的岗位构成",pos_bottom='50%',pos_right='center'),
            legend_opts=opts.LegendOpts(is_show=False),
            )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%",font_size=25))
)
pie.render('C:\BIGDATA\python1912\毕业设计\图表\广州的岗位构成.html')

pie = (pi(init_opts=opts.InitOpts(height='1200px',width='2000px'))
        .add("深圳",data_sz,radius=['35%','75%'],rosetype="radius")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="深圳的岗位构成",pos_bottom='50%',pos_right='center'),
            legend_opts=opts.LegendOpts(is_show=False),
            )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%",font_size=25))
)
pie.render('C:\BIGDATA\python1912\毕业设计\图表\深圳的岗位构成.html')