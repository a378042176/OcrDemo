#  -*- coding: utf-8 -*-

import logging
from StringIO import StringIO

import Image
import requests
import ImgHelper
import STHelper
import IPGetHelper

ips=IPGetHelper.get_ip();

auth_url = 'http://tp.52hom.com/tp/tpyz.asp?cid=12&id=174'
home_url = 'http://tp.52hom.com/tp/adminryx/verifycode1.asp';
headers ={
    "Referer":"http://tp.52hom.com/tp/tpyz.asp?cid=12&id=174",
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent':
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
}
logging.basicConfig(level=logging.DEBUG)
for ip in ips:
    proxies = {
        "http": ip,
        "https": ip,
    }
    try:
        logging.info('开始使用IP'+ip)

        s = requests.Session()
        s.get(auth_url, headers=headers, proxies=proxies, timeout=30)
        r = s.get(home_url, headers=headers, proxies=proxies, timeout=30)
        img = Image.open(StringIO(r.content))
        # 二值化
        img = ImgHelper.ImgHelper().getImg(img)

        code = STHelper.STHelper().getCode(img).strip()
        print code
        data = {}
        data['cid'] = '12'
        data['id'] = '174'
        data['CheckCode'] = code
        data['x'] = 44
        data['y'] = 33

        postUrl = 'http://tp.52hom.com/tp/tpjg.asp'
        r = s.post(postUrl, data=data, headers=headers, proxies=proxies, timeout=30)
        r.encoding="GB2312"
        print r.text
    except :
        logging.error('IP:'+ip+'超时')

