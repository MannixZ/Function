import requests
import json
import time
from Function_Godlike import *

# url = 'http://god.gameyw.netease.com/v1/app/feed/hot'

headers_str = '''
GL-ClientType: 50
GL-CurTime: 1536234578684
GL-DeviceId: 66bda73041d94fceb691f50b9487b93c
GL-Version: 1.4.0
GL-Nonce: -7365621797954092460
GL-Uid: d9e9b75060964bce90b783a28aedcede
GL-Token: f46854b713da4342acde3e31f475f121
GL-Source: URS
GL-CheckSum: 38a84ab00ff9fb9d2ef110d6ad41f0852e2a6131
Content-Type: application/json; charset=utf-8
Content-Length: 39
Host: god.gameyw.netease.com
Connection: Keep-Alive
Accept-Encoding: gzip
User-Agent: okhttp/3.11.0
'''

# r = requests.post(url,headers=headers,verify=False)
# jsonr = json.loads(r)

headers = str2dict(headers_str)
def get_Hot(count):
    for i in range(count):
        headers['GL-CurTime'] = get_curTime()   #添加 GL-CurTime 字段进入字典
        res = requests.post(url, headers=headers, verify=False)
        jsonr = json.loads(res.text)
        assert  jsonr['code'] == 200
        print("try update %s : code = %s" %(i , jsonr["code"]))

def try_to_comment():
    url = 'http://god.gameyw.netease.com/v1/app/feed/comment'
    for i in  range(11111):
        headers['GL-CurTime'] = get_curTime()  # 添加 GL-CurTime 字段进入字典
        data = {"content":i,
                "feedId":"5b9114dc66636f743b54d914",
                "feedUid":"a7aee4dc4df94e0eb2e5af75b6aeae1c"}
        res = requests.post(url, headers=headers,data=json.dumps(data) ,verify=False)
        print("try to common : %s" %i)

if __name__ == "__main__":
    try_to_comment()



