#coding:utf-8
#@Time: 2021/10/26 12:28
#@File : spider.py
import json,os,time,requests,re,pymysql
from pip import main
import pandas as pd
from lxml import etree
from pymysql import Error
from selenium.webdriver.chrome.options import Options
from selenium import  webdriver

#模拟登陆
def login():
    driver.get(base_url)
    driver.find_element_by_class_name('zppp-panel-qrcode-bar__triangle').click()
    driver.find_element_by_xpath('//div[@class="zppp-panel-normal__inner"]/ul/li[2]').click()
    driver.find_elements_by_xpath('//div[@class="zppp-input__container"]/input')[0].send_keys('18573044937')
    driver.find_elements_by_xpath('//div[@class="zppp-input__container"]/input')[1].send_keys('qq1084472249')
    #同意服务条款
    driver.find_element_by_xpath('//*[@id="accept"]').click()
    driver.find_element_by_class_name('zppp-submit').click()#点击登陆
    input('登陆完成后按回车继续任务')
#不同城市的链接
def city(url):
    resp = requests.get(url, headers=headers)
    html = resp.text
    json_data = re.search(r'<script>__INITIAL_STATE__=(.*?)</script>', html).groups()[0]
    data = json.loads(json_data)
    cityMapList = data['cityList']['cityMapList']
    for letter, citys in cityMapList.items():
        for city in citys:
            city_name = city['name']
            city_url = 'https:' + city['url']
            citys =input_city_name
            if city_name in citys:
                print(f'正在获取{input_city_name}的信息')
                city_job(city_url)
                time.sleep(3)
            else:
                pass

#搜索城市的大数据工作岗位
def city_job(city_url):
    driver.get(city_url)
    # 搜索框send大数据
    driver.find_element_by_class_name('zp-search__input').send_keys("大数据")
    # 点击搜索
    driver.find_element_by_xpath('//div[@class="zp-search__common"]//a').click()
    driver.switch_to.window(driver.window_handles[-1])  #切换到最后一个窗口 (新打开的窗口)

    # 判断当前查询结果是否不存在
    content = driver.find_elements_by_class_name('positionlist')
    if not content:
        print(f'{input_city_name}未查找到大数据岗位')
    else:
        #传入源代码到parse()获取数据
        parse(driver.page_source)
#获取当前城市的数据
def parse(city_url):
    html=etree.HTML(city_url)
    job_list=html.xpath('/html/body/div[1]/div[4]/div[2]/div[2]/div[2]/div')
    item={}
    for job in job_list:
        #岗位名称
        work_name=job.xpath('./a/div[1]/div[1]/span[1]/@title')
        #招聘公司
        company=job.xpath('./a/div[1]/div[2]/span/text()')
        #薪资
        money=job.xpath('./a/div[2]/div[1]/p/text()')
        #经验
        exper=job.xpath('./a/div[2]/div[1]/ul/li[2]/text()')
        #学历
        edu=job.xpath('./a/div[2]/div[1]/ul/li[3]/text()')
        #公司类型
        com_type=job.xpath('./a/div[2]/div[2]/span[1]/text()')
        #技能要求
        ability=job.xpath('./a/div[3]/div[1]/div/text()')
        #公司规模
        scale=job.xpath('./a/div[2]/div[2]/span[2]/text()')
        #key 和 value 一一对应
        for work_name_,company_,money_,exper_,edu_,com_type_,scale_ \
            in zip(work_name,company,money,exper,edu,com_type,scale):
            item["岗位名称"]=work_name_
            item["招聘公司"]=company_
            item["薪资"]=money_.replace('\n          ','')
            item["地区"]=input_city_name
            item["经验"]=exper_
            item["学历"]=edu_
            # ability是list类型 用 join 转换为 String 用-做分隔符 方便后面拆出多列
            item["公司类型"]=com_type_
            Strability="-".join(ability)
            item["技能要求"]=Strability
            item["公司规模"]=scale_
            print(item)
            save_file(item)
            save_to_mysql(item)
    #调用page()判断有没有下一页
    page()
#保存到本地
def save_file (item):
    #如果文件不存在则添加表头
    if not os.path.exists('D:\\bigdata.csv'):
        #如果使用所有标量值，则必须传递索引(ability) index=0
        pd.DataFrame(item,index=[0]).to_csv('D:\\bigdata.csv',mode='a',encoding='utf_8_sig',index=False) # index=False  去除序号
    else:
        pd.DataFrame(item,index=[0]).to_csv('D:\\bigdata.csv',mode='a',encoding='utf_8_sig',index=False,header=False)
#保存到MySql
def save_to_mysql(item):
    #print("[INFO]开始保存到MySQL")
    keys = ','.join(item.keys())  # 键
    values = ','.join(['%s'] * len(item))  # 值
    sql1 = 'INSERT INTO newbigdata({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format( keys=keys,
                                                                                        values=values)  # 通过 ON DUPLICATE KEY UPDATE找出相同的键，然后更新
    updata = ','.join([" {key} = %s ".format(key=key) for key in item])
    sql1 += updata
    try:
        #针对字典 会返回字典value组成的tuple
        if cursor.execute(sql1, tuple(item.values()) * 2):
            print('[INFO]保存到MySQL成功')
            connect.commit()  # 插入
    except Error as e:
        print(e)
        print('Failed')
        connect.rollback()  # 回滚
#判断是否有下一页
def page():
    nexts = driver.find_elements_by_xpath('//*[@class="btn soupager__btn"]')
    #如果在源码中找不到该元素
    if not nexts:
        print(input_city_name+"爬取完成")
        pass
    else:
        #找到下一页位置 点击下一页
        next = driver.find_element_by_xpath('//*[@id="positionList-hook"]/div[2]/div[31]/div[2]/div/button[2]')  # 点击下一页
        driver.execute_script("arguments[0].click();", next)
        time.sleep(2)

        #点击后网页源码不改变   刷新页面
        driver.refresh()
        parse(driver.page_source)
#程序入口
if __name__ == '__main__':
    # 添加请求头
    options = Options()
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
    driver = webdriver.Chrome(options=options)
    #用做登陆的url
    base_url = "https://passport.zhaopin.com/login"
    #连接数据库
    connect=pymysql.connect(host='127.0.0.1',user='root',password='123456',port=3306,db='jobDB',charset='utf8')
    cursor=connect.cursor()
    sql='CREATE TABLE IF NOT EXISTS newbigdata ( 岗位名称 VARCHAR(255)  , 招聘公司 VARCHAR(255)  , 薪资 VARCHAR(50)  , 地区 VARCHAR(25) ,经验 VARCHAR(25) ,学历 VARCHAR(25),公司类型 VARCHAR(50) ,技能要求 VARCHAR(255),公司规模 VARCHAR(50) );'
    cursor.execute(sql)
    #登陆
    login()
    city_name_list = ['株洲','北京','上海','广州','深圳','天津','武汉','西安','成都','大连','长春','沈阳','南京','济南','青岛','杭州','苏州','无锡','宁波','重庆','郑州','长沙','福州','厦门',',哈尔滨']
    for i in range(len(city_name_list)):
        input_city_name=city_name_list[i]
        city('https://www.zhaopin.com/citymap')