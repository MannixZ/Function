import urllib.request
import urllib.parse
import json


'''
爬取网页
'''
#爬取网页信息
html_url = 'http://www.baidu.com'
html_resp = urllib.request.urlopen(html_url)

#读取全部， 读取一行可用readline(), 多行返回列表可用readlines()
html = html_resp.read()   #读取url
html = html.decode('utf-8') #解码
print(html)

#获得其他信息：
html_resp.info() #获得头相关信息， HTTPMessage对象
html_resp.getcode()  #获得状态码
html_resp.geturl()  #获取爬取的url

# url中包含汉子是不符合URL标准的，需要进行编码
u = urllib.request.quote(html_url)
print(u)

# 对url进行解码
u = urllib.request.unquote(u)
print(u)

'''
爬取二进制文件（图片，音频等）
'''
# 下载图片
pic_url = 'http://static.zybuluo.com/coder-pig/agr9d5uow8r5ug8iafnl6dlz/1.jpg'
#urllib.request.urlretrieve(pic_url, "test.jpg")
pic_resp = urllib.request.urlopen(pic_url)
pic = pic_resp.read()
with open("test.jpg", 'wb') as f:
    f.write(pic)

# 直接调用urlretrieve下载， 下载音频
music_url = "http://7xl4pr.com2.z0.glb.qiniucdn.com/" \
            "%E4%B8%83%E7%94%B0%E7%9C%9F%E4%B8%93%E5%8C%BA%2F%E4%" \
            "B8%AD%E6%96%87%E8%AF%BE%2F%E6%83%B3%E8%" \
            "B1%A1%E7%82%B9%E5%8D%A1%2F%2B6.mp3"
urllib.request.urlretrieve(music_url, 'Music.mp3')

'''
模拟Get请求与Post请求
'''
# 模拟Get
get_url = "http://gank.io/api/data/" + urllib.request.quote("福利") + "/1/1"
print(get_url)
get_resp = urllib.request.urlopen(get_url)
print("你打开了一个什么类型啊")
# json.loads() JSON -> Python
get_result = json.loads(get_resp.read().decode("utf-8"))
print(get_result)
# 这里后面的参数用于格式化Json输出格式  json.dumps() Python -> Json
get_result_format = json.dumps(get_result, indent=2,
                               sort_keys=True,
                               ensure_ascii=False)
print(get_result_format)

#模拟Post
post_url = "http://xxx.xxx.login"
phone = "1313131313"
password = '123123123'
value = {
    "phone":phone,
    "password":password
}
data = urllib.parse.urlencode(value).encode(encoding="utf-8")
req = urllib.request.Request(post_url, data)
resp = urllib.request.urlopen(req)
result = json.loads(resp.read())  #将byte 结果转为 Json
print(json.dumps(result, sort_keys=True,
                 indent=2,
                 ensure_ascii=False))   #格式化输出Json

'''
修改请求头
'''
