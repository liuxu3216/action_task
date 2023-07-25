import requests
import json

mf = requests.session()
# 因为原始的session.cookies 没有save()方法，所以需要用到cookielib中的方法LWPCookieJar，
# 这个类实例化的cookie对象，就可以直接调用save方法。
# mf.cookies = cookielib.LWPCookieJar(filename="mfcookies.txt")

header = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    "Referer": "",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    'Cookie': 'PHPSESSID=2ki91era8e542qel5agkjpnutl; crisp-client%2Fsession%2F5690d3a5-53e4-435e-a52b-12af296b5cd9%2F9c805a3b-7bac-39ff-9728-7520af5fe7e4=session_b8ec7983-d28c-46eb-8652-370704bf2c17; crisp-client%2Fsession%2F5690d3a5-53e4-435e-a52b-12af296b5cd9=session_aac7cbba-fd4b-4e28-82ac-1b95900b6029'
}
# 使用cookies登录
login_url = 'https://xmrth.fun/auth/login'
post_data = {
    'fp': 'f709e114f40b7eb75b3da940b44a05ab',
    'email': username,
    'passwd': passwd,
    'code': ''
}
# 使用session直接post请求
resp = mf.post(login_url, data=post_data, headers=header)
print(json.loads(resp.text))
# 登录成功之后，将cookie保存在本地文件中
login_cookies = resp.cookies
print(login_cookies)
# cookies = requests.utils.dict_from_cookiejar(resp.cookies())
# print(cookies)
url = 'https://xmrth.fun/user/checkin'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
# 与 get 请求一样，r 为响应对象
r = mf.post(url, headers=headers, cookies=resp.cookies)
# 查看响应结果
print(r.json())
