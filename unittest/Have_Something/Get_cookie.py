import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

#chrome配置文件位置
profile_directory = r'--user-data-dir=C:\Users\wb.zengmingjie\AppData\Local\Google\Chrome\User Data\Default'

s = requests.session()   #建立session会话
url = "https://home.cnblogs.com/u/yoyoketang"

def get_cookie(url):
    try:
        # 加载配置
        profile = webdriver.ChromeOptions()
        profile.add_argument(profile_directory)
        # 启动浏览器配置
        driver = webdriver.Chrome(chrome_options=profile)

        driver.get(url)
        time.sleep(3)
        cookies = driver.get_cookies()
        print(cookies)
        driver.quit()
        return cookies
    except Exception as msg:
        print(u"启动浏览器的时候遇到一个错误了哦：%s" %str(msg))

def add_cookies(cookies):
    '''
    往seesion添加cookies
    '''
    try:
        #添加cookies到cookieJar
        c = requests.cookies.RequestsCookieJar()
        for i in cookies:
            c.set(i["name"], i["value"])

        s.cookies.update(c) #更新session里cookies
    except Exception as msg:
        print(u'添加cookies的时候遇到了错误哦： %s' %str(msg))

def get_ye_num(url):
    '''
    获取粉丝数量
    '''
    try:
        # 发请求
        r1 = s.get(url + "/relation/followers")
        soup = BeautifulSoup(r1.content, "html.parser")
        # 抓取我的粉丝数
        fensinub = soup.find_all(class_="current_nav")
        print(fensinub[0].string)
        num = re.findall(u"Ta的粉丝\((.+?)\)", fensinub[0].string)
        print(u"Ta的粉丝数量：%s" % str(num[0]))

        # 计算有多少页，每页45条
        ye = int(int(num[0]) / 45) + 1
        print(u"总共分页数：%s" % str(ye))
        return ye
    except Exception as msg:
        print(u"获取粉丝页数报错了，默认返回数量1 ：%s" % str(msg))
        return 1

def save_name(nub):
    '''
    抓取粉丝名称
    '''
    try:
        # 抓取第一页的数据
        if nub<1:
            url_page = url + "/relation/followers"
        else:
            url_page = url + "/relation/followers?page=%s"% str(nub)
        print(u"正在抓取的页面: %s" %url_page)
        r2 = s.get(url_page, verify=False)
        soup = BeautifulSoup(r2.content, 'html.parser')
        fensi = soup.find_all(class_="avatar_name")
        for i in fensi:
            name = i.string.replace("\n", "").replace(" ", "")
            print(name)
            with open("name.txt", "a", encoding="utf-8") as f :#追加写入
                f.write(name+"\n")

    except Exception as msg:
        print(u"抓取粉丝名称过程中报错了 :%s"%str(msg))

if __name__ == "__main__":
    cookies = get_cookie(url)
    add_cookies(cookies)
    n = get_ye_num(url)
    for i in list(range(1, n+1)):
        save_name(i)
