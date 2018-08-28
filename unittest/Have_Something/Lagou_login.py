import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re
from bs4 import BeautifulSoup
import urllib3
import hashlib


class LoginLaGou():

    def __init__(self, s):
        self.s = s

    def getToken(self):
        '''
        从 前端获取 token以及code，作用是拿来登录
        </script>

    <!-- 页面样式 -->    <!-- 动态token，防御伪造请求，重复提交 -->
    <script>
    window.X_Anti_Forge_Token = 'ef41b50a-0fed-4661-ab5e-fd07a046a371';
    window.X_Anti_Forge_Code = '53645300';
</script>
        '''
        url = 'https://passport.lagou.com/login/login.html'
        h = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
        }
        self.s.headers.update(h)
        data = self.s.get(url, verify=False)
        soup = BeautifulSoup(data.content, 'html.parser', from_encoding='utf-8')
        tokenCode = {}

        try:
            t = soup.find_all('script')[1].get_text()
            print(t)
            tokenCode['X_Anti_Forge_Token'] = re.findall(r"Token = '(.+?)'", t)[0]
            tokenCode['X_Anti_Forge_Code'] = re.findall(r"Code = '(.+?)'", t)[0]
            return tokenCode
        except:
            print("获取token和code失败")
            tokenCode['X_Anti_Forge_Token'] = ''
            tokenCode['X_Anti_Forge_Code'] = ''
            return tokenCode

    def encryptPwd(self, passwd):
        '''
        对密码进行md5双重加密
        :param passwd:
        :return:
        '''
        passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()
        #veenike 属于一个写死的值
        passwd = 'veenike' + passwd + 'veenkie'
        passwd = hashlib.md5(passwd.encode('utf-8')).hexdigest()
        print("经过哈希值后pwd变成 :%s" %str(passwd))
        return passwd

    def login(self, user, psw):
        '''
        登录拉勾网
        :param user: 账号
        :param psw:  密码
        :return:  返回json
        '''
        gtoken = self.getToken()
        print(gtoken)
        print(gtoken['X_Anti_Forge_Token'])
        print(gtoken['X_Anti_Forge_Code'])
        url2 = 'https://passport.lagou.com/login/login.json'
        h2 = { 'Host': 'passport.lagou.com',
  'Connection': 'keep-alive',
  # 'Content-Length': '154',
  'Origin': 'https://passport.lagou.com',
  'X-Anit-Forge-Code': gtoken['X_Anti_Forge_Code'],
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.25 Safari/537.36',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'X-Requested-With': 'XMLHttpRequest',
  'X-Anit-Forge-Token': gtoken['X_Anti_Forge_Token'],
  'Referer': 'https://passport.lagou.com/login/login.html',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,en-US;q=0.8,en;q=0.6,zh;q=0.4' ,
   'Content - Length': '154',
  'Cookie': 'user_trace_token=20180330130806-55250368-33d8-11e8-b663-5254005c3644; LGUID=20180330130806-5525089a-33d8-11e8-b663-5254005c3644; index_location_city=%E5%B9%BF%E5%B7%9E; login=false; unick=""; _putrc=""; LG_LOGIN_USER_ID=""; JSESSIONID=ABAAABAAAGHAABHC225FC0CC181E36FEC40249E2ACBF090; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fpassport.lagou.com%2Flogin%2Flogin.html%3Fts%3D1535422455272%26serviceId%3Dlagou%26service%3Dhttps%25253A%25252F%25252Fwww.lagou.com%25252F%26action%3Dlogin%26signature%3DF5CB6F25EDD335B9CD19E63C36956180; X_HTTP_TOKEN=ba3c758dcd26c18899e5fb3d472baded; _ga=GA1.2.363089562.1522386486; _gid=GA1.2.1305037165.1535421720; _ga=GA1.3.363089562.1522386486; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535421721; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535436385; LGSID=20180828140619-7b2fb848-aa88-11e8-b24b-5254005c3644; LGRID=20180828140625-7e94796a-aa88-11e8-baa1-525400f775ce; TG-TRACK-CODE=undefined'}

        #更新s的头部
        s.headers.update(h2)
        passwd = self.encryptPwd(psw)

        body = {
            "isValidate": "true",
            "username": user,
            "password": passwd,
            "request_form_verifyCode":"",
            "submit":"",
            "challenge": "51ea6ec1d59a1ddf192517ba8a565f0a"
        }
        r2 = self.s.post(url2, data=body, verify=False)
        try:
            print(r2.text)
            return r2.json
        except:
            print("登录异常啦 %s" %r2.text)
            return r2.json

if __name__ == "__main__":
    s = requests.session()
    lg = LoginLaGou(s)
    lg.login("13611467691", "aa3835968")