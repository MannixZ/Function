import time

# headers_str = """
# GL-ClientType: 50
# GL-CurTime: 1534405919530
# GL-DeviceId: 6a7eb9d1117f4ab69330a064d2bb94eb
# GL-Version: 1.3.0
# GL-Nonce: 1672009375857366570
# GL-Uid: d9e9b75060964bce90b783a28aedcede
# GL-Token: 49204a0eff204a6d8add846db227a136
# GL-Source: URS
# GL-CheckSum: 334a762eae9911d0bb742483a3474c3b8ca73f36
# Content-Type: application/json; charset=utf-8
# Content-Length: 2
# Host: god.gameyw.netease.com
# Connection: Keep-Alive
# Accept-Encoding: gzip
# User-Agent: okhttp/3.11.0
#
# """

def get_curTime():
    return str(int(time.time()*1000))


def str2dict(headers_str):
    res = {}
    str_list = headers_str.split("\n")   #以 换行符为分割
    # print(str_list)
    for item in str_list:  #检查每一行元素
        try:
            tmp = item.split(": ")    #以 ： 号为分隔
            if tmp[0] == "Content-Length":
                continue
            res[tmp[0]] = tmp[1]
            # print(res)
        except Exception as e:
            pass
    return res

# if __name__ == "__main__":
#     print(str2dict(headers_str))