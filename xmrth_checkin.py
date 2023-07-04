
import requests

url = 'https://xmrth.fun/user/checkin'

headers = {
    'content-type': 'application/json',
    'Cookie': 'uid=3703; email=458137665%40qq.com; key=135be4e5686b37772b346eb7fc6355073afef37348107; ip=dc4e6b99511bd34f3a29ef94e819d262; expire_in=1689236180; crisp-client%2Fsession%2F5690d3a5-53e4-435e-a52b-12af296b5cd9=session_eabbd0c9-d33f-44e5-abc6-0795e6c5a073; crisp-client%2Fsession%2F5690d3a5-53e4-435e-a52b-12af296b5cd9%2F9c805a3b-7bac-39ff-9728-7520af5fe7e4=session_eabbd0c9-d33f-44e5-abc6-0795e6c5a073'
}
# 与 get 请求一样，r 为响应对象
r = requests.post(url, headers=headers)
# 查看响应结果
print(r.json())
