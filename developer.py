# coding:utf-8
# 2021-2-23
#TapTap厂商评论存json爬虫
import requests
import csv
import time
import pandas
from bs4 import BeautifulSoup
import re
import json


def get_page(url, headers):
    data = []
    url = url
    headers = headers
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.text, "lxml")
    for li in soup.find_all(name='li', class_="taptap-review-item collapse in"):
        user_name = li['data-user']
        review_id = str(li['id'])[7:]
        user_id = li.span['data-user-id']
        score_list = li.find_all(name='i')[0]  # "width:70px"
        score = str(score_list)[26:-6]
        revi_ew = []
        review_list = li.find_all(name='p')  # 抓取评论 <p>列表
        for i in range(len(review_list)):
            re = str(review_list[i])[3:-4]
            revi_ew.append(re)
        review = " ".join(revi_ew)
        r = li.find_all(name='span')
        time = r[3].string
        device = r[4].string
        data.append({'user': user_name, 'id': user_id, 'review_id': review_id, 'score':score, 'review':review, 'time':time, 'device':device })
    return data
def save_data(data):
       with open('developer.json', 'a') as fp:  #将所得的数据存储为json文件,developer.json可以改存放路径
        for i in range(1,2):
         json.dump(data, fp = fp, ensure_ascii = False, indent = 4, sort_keys = True)


def main():
    for i in range(1, 2):#2可以改成你想爬的页数，实际页数=修改的数字 - 1
        print("第", i, "页")
        url = "https://www.taptap.com/developer/2004/review?page="#2004改成你需要爬的id
        url = url + str(i)
        headers = {
            "Accept": 'application / json, text / javascript, * / *; q = 0.01',
            "Accept - Encoding": 'gzip, deflate, br',
            "Accept - Language": 'zh - CN, zh;q = 0.9',
            "Connection": 'keep - alive,',
            "User - Agent": 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 63.0.3239.132 Safari / 537.36'
        }
        time.sleep(4)
        data = get_page(url, headers)
        save_data(data)


if __name__ == "__main__":
    main()
