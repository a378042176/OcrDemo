#!/usr/bin/env python
# coding:utf8
import random, threading, time
from Queue import Queue
import IPGetHelper
import TouPiao
from Logger import Logger

log=Logger().getlog()
class Producer(threading.Thread):
    def __init__(self, t_name, queue):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue

    def run(self):
        urls = ["http://www.xicidaili.com/nn/","http://www.xicidaili.com/nt/",
                "http://www.xicidaili.com/wn/", "http://www.xicidaili.com/wt/"]
        urlindex = 0
        index=1
        while 1:
            if self.data.qsize()==0:
                url="{0}{1}".format(urls[urlindex],index)
                self.addIp(url)
                index=index+1
                if index>=10:
                    index=1
                    urlindex=urlindex+1
                    if urlindex>=4:
                        urlindex=0
            # time.sleep(1000)

    def addIp(self,url):
         try:
             ips = IPGetHelper.get_ip(url)
             for ip in ips:
                 self.data.put(ip)
             log.info(u"IP池添加了{0}个{1}".format(len(ips), url))

         except Exception,ex:
             print u"获取IP时出现异常:"+ex.message


# Consumer thread
class Consumer(threading.Thread):
    def __init__(self, t_name, queue, queueSuccess):
        threading.Thread.__init__(self, name=t_name)
        self.data = queue
        self.queueSuccess = queueSuccess
        log.info(u'线程{0}启动'.format(self.getName()))

    def run(self):
        urls = ["http://www.xicidaili.com/nn/", "http://www.xicidaili.com/nt/",
                "http://www.xicidaili.com/wn/", "http://www.xicidaili.com/wt/"]
        while 1:
            if not self.data.empty():
                ip = self.data.get()
                print u'IP池当前还剩余{0}个IP'.format(self.data.qsize())
                TouPiao.TouPiao().toupiao(ip, self.queueSuccess)


# Main thread
def main():
    # 定义线程池
    threads = []

    queue = Queue()
    queueSucess = Queue()
    threads.append(Producer('Pro.', queue))

    # 创建线程对象
    for x in xrange(0, 30):
        threads.append(Consumer('{0}{1}'.format('Con_even', x), queue, queueSucess))
    # 启动线程
    for t in threads:
        t.setDaemon(True)
        t.start()
    # 等待子线程结束
    for t in threads:
        t.join()
    # producer.join()


if __name__ == '__main__':
    main()
