#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import urllib.request
from bs4 import BeautifulSoup

def get_html():
    # url = 'http://mp.weixin.qq.com/mp/homepage?__biz=MzIzOTk0NjM3MQ==&hid=1&sn=541fe5d6af6107a0f5cb663723b3ee1e&scene=18&uin=NjM3NTU1MDg0&key=7f41773530cef10190539d225e0405936ceeeb10bfacc7ba8a9f4629abd0d169c0de8742e53c1e4deada152e05f1717908f977d27733a5a20b35ad5190524c131a1cdc8d10f24a34f9daa522f64df86b&devicetype=Windows+10&version=62060619&lang=zh_CN&ascene=7&pass_ticket=sXWqqXHq7nYq1aOieQZMBuZWtpIdRTPMRtmNhS6E3dEY0P7pw%2Bc87X%2BzU6dvvGen&winzoom=1'
    num = '6'
    url = 'http://mp.weixin.qq.com/mp/homepage?__biz=MzIzOTk0NjM3MQ==&hid=1&sn=541fe5d6af6107a0f5cb663723b3ee1e&scene=18&uin=NjM3NTU1MDg0&key=52fe516b925e4ce864bf922674ff9cc9090d0abfe3b1ac10b862b98b356f298befc0dc5bf5c916d914cd23b8a73e30474ec74d8b5c58fbcc6434d0afaf1ce5c6215d90cdc10de061ad7690592a0e501d&devicetype=Windows+10&version=62060619&lang=zh_CN&ascene=7&pass_ticket=sXWqqXHq7nYq1aOieQZMBuZWtpIdRTPMRtmNhS6E3dEY0P7pw%2Bc87X%2BzU6dvvGen&winzoom=1&cid=0&begin='+ num +'&count=5&action=appmsg_list&f=json&r=0.08375340956263244&appmsg_token=989_im89tHqGLcWOITBZpWsEWTgej-ccfdpb6zBSOA~~'
    # url = 'http://mp.weixin.qq.com/s?__biz=MzIzOTk0NjM3MQ==&mid=2247485512&idx=1&sn=209ba2804736648bd54e5c38d11f3f47&scene=19#wechat_redirect'
    req = requests.get(url=url)
    req_text = req.text
    json_req = json.loads(req_text)
    content_list = json_req['data']['homepage_render']['plugin_data']
    for cts in content_list:
        title = cts['plugin1']['appmsg_list'][0]['title']
        link = cts['plugin1']['appmsg_list'][0]['link']
        print(title)
        print(cts)
        exit()
    print(content_list)


if __name__ == '__main__':
    get_html()