
import requests

url = 'https://xmrth.fun/user/checkin'

headers = {
    'content-type': 'application/json',
    'Cookie': '
uid=3703; email=458137665%40qq.com; key=751bf70c40cea9b0a652a3e9ad74b3bc90d45098932ad; ip=66a2e8bc0197ab70317b72231069d943; expire_in=1691222874; crisp-client%2Fsession%2F5690d3a5-53e4-435e-a52b-12af296b5cd9=session_b8ec7983-d28c-46eb-8652-370704bf2c17; crisp-client%2Fsession%2F5690d3a5-53e4-435e-a52b-12af296b5cd9%2F9c805a3b-7bac-39ff-9728-7520af5fe7e4=session_b8ec7983-d28c-46eb-8652-370704bf2c17'
}
# 与 get 请求一样，r 为响应对象
r = requests.post(url, headers=headers)
# 查看响应结果
print(r.json())
