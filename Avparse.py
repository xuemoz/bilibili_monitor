# -*- coding: utf-8 -*- 
import urllib2
import gzip,cStringIO

class Avparse:
    """解析av号"""
    def parse(self,av_num):
        url = r'http://interface.bilibili.tv/count?aid='+av_num
        try:
            html = urllib2.urlopen(url,timeout=10)
        except urllib2.URLError as e:
            print e.reason
            return False
        code = html.getcode()
        if code < 200 or code >=300:
            print 'error code:'+code
            return False
        content = html.read()
        info_list = content.split(';') 
        self.__dianji = info_list[0].split('.')[1][5:-1]
        self.__stow = info_list[1].split('.')[1][5:-1][1:-1]
        self.__coin = info_list[2].split('.')[1][5:-1]
        self.__cscores = info_list[3].split('.')[1][5:-1]

        url = r'http://www.bilibili.tv/video/av'+av_num
        try:
            html = urllib2.urlopen(url,timeout=10)
        except urllib2.URLError as e:
            print e.reason
            return False
        code = html.getcode()
        if code < 200 or code >= 300:
            print 'error code:'+code
            return False
        content = html.read()
        if content[:6] == '\x1f\x8b\x08\x00\x00\x00':
            content = gzip.GzipFile(fileobj=cStringIO.StringIO(content)).read()
        return True
    #点击数量
    def getDianji(self):
        return int(self.__dianji)
    #收藏数量
    def getStow(self):
        return int(self.__stow)
    #硬币数
    def getCoin(self):
        return int(self.__coin)
    #积分
    def getCscores(self):
        return int(self.__cscores)
