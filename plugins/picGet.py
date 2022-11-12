import os

import requests

from plugins.RandomStr.RandomStr import random_str

url = 'https://iw233.cn/api.php?sort=yin' # 接口地址
headers ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
def pic():
    r = requests.get(url, headers=headers)
    # 下载图片
    ranpath=''
    while True:
        ranpath = random_str()
        exist = os.path.isfile("pictures\\" + ranpath + ".jpg")
        direxist =os.path.isdir("pictures")
        if direxist:
            if exist:
                continue
            else:
                break
        else:
            os.mkdir("pictures")
            continue

    with open("pictures\\" + ranpath + ".jpg", mode="wb") as f:
        f.write(r.content)  # 图片内容写入文件
    return "pictures\\" + ranpath + ".jpg"
if __name__ == '__main__':
    s=input("输入1开始执行")
    i=0
    if s=="1":
        while i<=10:
            pic()
            i+=1