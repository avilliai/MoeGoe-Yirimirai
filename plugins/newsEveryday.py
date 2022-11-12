

import os
import datetime

import requests



url = 'https://api.vvhan.com/api/60s' # 接口地址
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
def news():
    r = requests.get(url, headers=headers)
    # 下载图片
    today = str(datetime.date.today())
    print(today)
    todayNews="MoYuPictures\\" + today + "news.jpg"
    exist = os.path.isfile(todayNews)
    direxist = os.path.isdir("MoYuPictures")
    if direxist:
        if exist:
             return todayNews
        elif exist==False:
            with open(todayNews, mode="wb") as f:
                f.write(r.content)  # 图片内容写入文件
            return todayNews
    else:
        os.mkdir("MoYuPictures")
        news()

if __name__ == '__main__':
    news()