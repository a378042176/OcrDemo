#encoding:utf8
import cookielib
import urllib
import urllib2
from StringIO import StringIO


class PostHelper(object):
    url=""

    def __init__(self):
        pass
    def post(self, code):
        # # 定义一个要提交的数据数组(字典)
        data = {}
        data['cid'] = '12'
        data['id'] = '174'
        data['CheckCode'] = code
        data['x'] = 44
        data['y'] = 33

        # # 定义post的地址
        url = 'http://tp.52hom.com/tp/tpjg.asp'
        post_data = urllib.urlencode(data)
        #
        # # 提交，发送数据
        # req = urllib2.urlopen(url, post_data)
        #
        # # 获取提交后返回的信息
        # content = req.read()
        # return content
        ckjar = cookielib.MozillaCookieJar("D:\cookies.txt")

        req = urllib2.Request(url, post_data)
        req.add_header(r'Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header(r'Accept-Encoding', 'gzip, deflate')
        req.add_header(r'Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
        req.add_header(r'User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0')

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))

        f = opener.open(req)
        htm = f.read()
        f.close()

        return htm
    def get(self):
        url = r"http://tp.52hom.com/tp/adminryx/verifycode1.asp"
        ckjar = cookielib.MozillaCookieJar("D:\cookies.txt")

        req = urllib2.Request(url)
        req.add_header(r'Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header(r'Accept-Encoding', 'gzip, deflate')
        req.add_header(r'Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
        req.add_header(r'User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0')

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ckjar))

        f = opener.open(req)
        return StringIO(f.read())

    def SaveCookies(self):
        import cookielib, urllib2
        url = r"http://tp.52hom.com/tp/adminryx/verifycode1.asp"
        req = urllib2.Request(url)
        req.add_header(r'Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
        req.add_header(r'Accept-Encoding','gzip, deflate')
        req.add_header(r'Accept-Language','zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
        req.add_header(r'User-Agent',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0')

        ckjar = cookielib.MozillaCookieJar("D:\cookies.txt")
        ckproc = urllib2.HTTPCookieProcessor(ckjar)

        opener = urllib2.build_opener(ckproc)

        f = opener.open(req)
        htm = f.read()
        f.close()

        ckjar.save(ignore_discard=True, ignore_expires=True)

