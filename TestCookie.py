#  -*- coding: utf-8 -*-
# !/usr/bin/python

import urllib2
import urllib
import cookielib
import re
from StringIO import StringIO

import Image

import ImgHelper
import STHelper

auth_url = 'http://tp.52hom.com/tp/tpyz.asp?cid=12&id=174'
home_url = 'http://tp.52hom.com/tp/adminryx/verifycode1.asp';

# 发送头信息
headers ={
    'Connection':'keep-alive',
    'Host':'tp.52hom.com',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent':
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
}
# 初始化一个CookieJar来处理Cookie
cookieJar=cookielib.CookieJar()
# 实例化一个全局opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
# 获取cookie
req=urllib2.Request(auth_url,None,headers)
result = opener.open(req)
# 访问主页 自动带着cookie信息
req=urllib2.Request(home_url,None,headers)
result = opener.open(req)
img = Image.open(StringIO(result.read()))

#二值化
img=ImgHelper.ImgHelper().getImg(img)

code=STHelper.STHelper().getCode(img)
#
# # 提交信息
# data = {}
# data['cid'] = '12'
# data['id'] = '174'
# data['CheckCode'] = code
# data['x'] = 44
# data['y'] = 33
# # urllib进行编码
# post_data=urllib.urlencode(data)
# postUrl= 'http://tp.52hom.com/tp/tpjg.asp'
# req=urllib2.Request(postUrl,post_data,headers)
# result=opener.open(req)
# print result.read()
