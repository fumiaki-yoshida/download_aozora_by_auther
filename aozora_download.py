"""
writed by Fumiaki Yoshida
2018/12/18
"""

import pandas as pd
import os
import requests
import sys
import time
from datetime import datetime
import zipfile


df = pd.read_csv('list_person_all_extended.csv', encoding='cp932')
family_name = input('input auther 姓:')
first_name = input('input auther 名:')
df = df[df['姓'] == family_name]
df = df[df['名'] == first_name]
if len(df)==0:
    print('Name is not exist.')
    sys.exit()

url_list = df['テキストファイルURL']

now = datetime.now()
get_time = now.strftime('%Y%m%d%H%M')
dir_name = df['姓ローマ字'][:1].to_string() + get_time
os.mkdir(dir_name)
os.chdir(dir_name)

for url in url_list:
    time.sleep(1)
    zip_name = url.split("/")[-1]
    r = requests.get(url)
    if r.status_code == 200:
        # f = open(zip_name, 'wb')
        # f.write(r.content)
        # f.close()
        with zipfile.ZipFile(r, 'r') as zf:
            # txt_name = zip_name.replace('zip', 'txt')
            zf.extractall()
