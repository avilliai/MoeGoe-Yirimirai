import requests

# 请求地址
url = "https://iw233.cn/api.php?sort=top"
# 发送get请求
r=requests.get(url)
# 获取返回的json数据

print(r.json())
