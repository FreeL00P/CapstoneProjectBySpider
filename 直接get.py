# coding=utf8
# @Time: 2021/10/27 19:19
import io
import sys
from urllib import parse

import numpy as np
import pandas as pd
import requests

# df = pd.read_csv(r'C:\BIGDATA\python1912\test\shopid.csv', header=0)
# df = df.values.tolist()
# df = list(np.ravel(df))
# print()

url = 'https://10.0.0.'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
}
for i in range(1, 300):
    newUrl = url + str(i);
    print(newUrl)
    try:
        resp = requests.get(newUrl, headers=headers)
        print(resp.text)
    except Exception as e:
        continue
