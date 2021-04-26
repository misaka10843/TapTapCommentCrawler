# coding:utf-8
# 2021-2-23
#TapTap游戏评论存json爬虫
import requests
import json
import csv
import time
import random


headers = {
    'Host': 'api.taptapdada.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.10.0'

}

# 声明一个列表存储字典
data_list = []


def start_spider():
    page = 0
    while < 100: #这里的100可以输入你想爬取的页数
        time.sleep(round(random.uniform(0.5, 1.5), 1))
        url = 'https://api.taptapdada.com/review/v1/by-app?limit=10&app_id=185982' \ #185982可改成你需要爬的id
              '&X-UA=V%3D1%26PN%3DTapTap%26VN_CODE%3D551%26LOC%3DCN%26LANG%3Dzh_CN%26CH%3Dtencent%26' \
              'UID%3Dda4b99bf-5e2b-4204-a92f-235474b32c4c&from={}'.format(page)
        page += 10
        resp = requests.get(url, headers=headers).json()
        datas = resp.get('data').get('list')
        if datas:
            for data in datas:
                # 评论人
                name = data.get('author').get('name')
                # 游戏时长
                played_tips = data.get('played_tips')
                # 评论内容
                contents = data.get('contents').get('text')

                # 声明一个字典储存数据
                data_dict = {}
                data_dict['name'] = name
                data_dict['played_tips'] = played_tips
                data_dict['contents'] = contents.replace('<br />', '')
                data_list.append(data_dict)

                print(data_dict)
        else:
            break


def main():

    start_spider()
    # 将数据写入json文件
    with open('game.json', 'a+', encoding='utf-8') as f:#game.json可改存放路径
        json.dump(data_list, f, ensure_ascii=False, indent=4)
    print('json文件写入完成')
if __name__ == '__main__':

    main()
