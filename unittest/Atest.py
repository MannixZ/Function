import requests
from PIL import Image
from io import BytesIO
from requests.auth import AuthBase
import json
import ssl
from requests.adapters import HTTPAdapter
from requests.packages import *
# r = requests.get("http://www.baidu.com")

#环境变量 HTTP_PROXY 和 HTTPS_PROXY 配置代理
# $ export HTTP_PROXY="http://10.10.1.10:3128"
# $ export HTTPS_PROXY="http://10.10.1.10:1080"

url = 'http://httpbin.org/get'
url1 = 'http://httpbin.org/status/404'
url2 = 'http://example.com/some/cookie/setting/url'
url3 = 'http://httpbin.org/cookies'
url4 = 'http://github.com'
url5 = 'http://ds.163.com'
url6 = 'http://httpbin.org/cookies/set/sessioncookie/123456789'
url7 = 'http://httpbin.org/headers'
url8 = 'http://httpbin.org/post'
url9 = 'http://httpbin.org'
url10 = 'http://pizzabin.org/admin'
url11 = 'http://httpbin.org/stream/20'
# headers = {"test":"testheader"}
# r = requests.get(url, headers=headers)
files = {'file': open('test.xls', 'rb')}
files1 = {'file': ('test.xls', open('test.xls', 'rb'),'application/vnd.ms-excel', {'Expires': '0'})}
files2 = {"file": ("test.xls", "some,data,to,send\nanother,row,to,send\n")}
# o = open('test.xls', 'rb')
# print(o)
payload = {
    "key1":"asdasd",
    "key2":"ahahha"
}
payload2 = (("key1","value1"),("key1","value2"))
cookiess = {
    'cookie' : 'value1',
    'cookie1' : 'value2',
    'cookie2' : 'value3',
    'cookie3' : 'value4'
}

jar = requests.cookies.RequestsCookieJar()
jar.set('ttest123123', 'yum', domain = 'httpbin.org', path = '/cookies')
jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')


multiple_files=[
    ('images',('test1.jpg', open('test1.jpg', 'rb'), 'image/jpg')),
    ('images',('test2.jpg', open('test2.jpg', 'rb'), 'image/jpg'))
]
# r = requests.post(url8, files=multiple_files)
# print(r.text)

# cookies = dict(cookiess)
# r = requests.get(url4, allow_redirects=False)

# s = requests.Session()
# s.auth = ('user', 'pass')
# s.headers.update({'xtest':'true'})
# r = s.get(url3, cookies={'test1':'test'})
# print(r.text)

# r = s.get(url4, verify=False)
# r = s.get(url3)

# print(r.text)
# r = requests.get(url4)
# t = r.raise_for_status()
# r1 = r.cookies['example_cookie_name']
# e = r.requests.exceptions.RequestException
# print(r,r.raise_for_status())
# print(r.headers.get('content-type'))
# print(r.status_code)
#事件挂钩
# def print_url(r, *args, **kwargs):
#     print(r.url)
# q = requests.get(url9, hooks=dict(response=print_url))
# print(q)

#自定义身份验证
# class PizzaAuth(AuthBase):
#     def __init__(self, username):
#         self.username = username
#
#     def __call__(self, r):
#         r.headers['X-Pizza'] = self.username
#         return r
#
# q = requests.get(url10, auth=PizzaAuth('kenneth'))
# print(q)

#流式请求
# r = requests.get(url11, stream=True)
#
# if r.encoding is None:
#     r.encoding = 'utf-8'
#
# for line in r.iter_lines(decoded_unicode=True):
#     if line:
#         print(json.loads(line))

#代理
# proxies = {
#     'http':'http://user:pass@10.10.1.10:3128',   #使用HTTP Basic Auth 使用http://user:password@host/ 语法
#     'https':'http://10.10.1.10:1080',
# }
#
# r = requests.get('http://example.org', proxies=proxies)

#HTTP动词
# r = requests.get('https://api.github.com/repos/requests/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad', verify=False)
#
# if(r.status_code == requests.codes.ok):
#     print(r.headers['content-type'])
#
# commit_data = r.json()
# print(commit_data.keys())
#
# print(commit_data[u'message'],commit_data[u'documentation_url'])
#
# verbs = requests.options(r.url)
# print(verbs.status_code)

#Issue 使用
# r = requests.get('https://api.github.com/requests/kennethreitz/requests/issues/482')
# print(r.status_code)
#
# issue = json.loads(r.text)
# print(issue)
#
# print(issue[u'documentation_url'])

#定制动词
# r = requests.request('mannix', url, data=data)
# print(r.status_code)

#响应头链接字段
# url = 'https://api.github.com/users/kennethreitz/repos?page=1&per_page=10'
# r = requests.head(url=url)
# r.headers['link']
# r.links['next']
# r.links['last']
# # r.headers['link']

#传输适配器
# s = requests.session()
# s.mount('http://www.github.com', MyAdapter())

#指定 SSL3 版本
# class Ssl3HttpAdapter(HTTPAdapter):
#     def init_poolmanager(self, connections, maxsize, block=False):
#         self.poolmanager = PoolManager(num_pools=connections,
#                                        maxsize=maxsize,
#                                        block=block,
#                                        ssl_version=ssl.PROTOCOL_SSLv3)


