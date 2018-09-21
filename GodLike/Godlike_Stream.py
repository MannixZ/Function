import requests
import json
import time
from Function_Godlike import *

# url = 'http://god.gameyw.netease.com/v1/app/feed/hot'

headers_str = '''
GL-ClientType: 50
GL-CurTime: 1537253960696
GL-DeviceId: 2d86d3dddd1c4bc28bfeb875afa66eaf
GL-Version: 1.4.1
GL-Nonce: 326785210626795566
GL-Uid: 4fab3d323e604a13ae910dd589f97759
GL-Token: be879cdf849d417b8c9f6121070e4b56
GL-Source: URS
GL-CheckSum: 7c3cf5a04d5445ceab75b432f41da2467a07c591
Content-Type: application/json; charset=utf-8
Content-Length: 42
Host: god-test.gameyw.netease.com
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
    # url = 'http://god.gameyw.netease.com/v1/app/feed/comment'   #正式服
    # url = "http://god-test.gameyw.netease.com/v1/app/feed/comment?ts=1536927189&uf=02f28b62-7cd9-45d0-8e74-43f5c0409f11&ab=727763be9bec8c81fc54d6f619f3c20c89&ef=e98b879c348966453f1c75b5b7bb782917"   #测试服
    url = "http://god-test.gameyw.netease.com/v1/app/feed/comment"
    for i in  range(100):
        headers['GL-CurTime'] = get_curTime()  # 添加 GL-CurTime 字段进入字典
        data = {"content":i,
                "feedId":"5ba09d2ae795d1368a5fb8ba",
                "feedUid":"7afb177ff48541f790bdc1523a46ca15"}
        res = requests.post(url, headers=headers,data=json.dumps(data) ,verify=False)
        print("try to common : %s" %i)

if __name__ == "__main__":
    try_to_comment()



