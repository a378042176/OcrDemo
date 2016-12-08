#encoding:utf8
from StringIO import StringIO

import Image
import requests
from bs4 import BeautifulSoup

import ImgHelper
import STHelper
from Logger import Logger

log=Logger().getlog()


class TouPiao(object):
    def toupiao(self,ip,queueSuccess):
        auth_url = 'http://tp.52hom.com/tp/tpyz.asp?cid=12&id=174'
        home_url = 'http://tp.52hom.com/tp/adminryx/verifycode1.asp';
        headers = {
            "Referer": "http://tp.52hom.com/tp/tpyz.asp?cid=12&id=174",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
        }

        proxies = {
            "http": ip,
            "https": ip,
        }
        try:
            session = requests.Session()
            session.get(auth_url, headers=headers, proxies=proxies, timeout=60)
            r = session.get(home_url, headers=headers, proxies=proxies, timeout=60)
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
            r = session.post(postUrl, data=data, headers=headers, proxies=proxies, timeout=60)
            r.encoding = "GB2312"
            soup = BeautifulSoup(r.text, "html.parser")
            res=soup.script.string.encode("utf8")
            # print res.decode('utf-8').encode('gbk')
            if "同一品牌一天内只能投一次" in res:
                print "同一品牌一天内只能投一次".decode('utf-8').encode('gbk')
            if "投票成功" in res:
                queueSuccess.put(ip)
                log.info("投票成功,当前成功投票{0}次".format(queueSuccess.qsize()))
                self.writeFile(ip)

            if "您输入的确认码和系统产生的不一致，请重新输入" in res:
                print "验证码识别错误,重新使用此IP投票".decode('utf-8').encode('gbk')
                self.toupiao(ip,queueSuccess)
            # print r.text
        except :
            print 'IP:' + ip + '超时'.decode('utf-8').encode('gbk')

    def writeFile(self,text):
        f = open('d:\sucess.txt', 'a')
        f.write(text)
        f.write('\n')
        f.close()