# -*- coding: utf-8 -*-
from Avparse import Avparse
import urllib2
import gzip,cStringIO

class Pageparse:
    """docstring for Pageparse"""
    def parse(self,page_id):
        url = r'http://www.bilibili.tv/video/'+page_id+'.html'
        print url
        content = urllib2.urlopen(url,timeout=10).read()
        if content[:6] == '\x1f\x8b\x08\x00\x00\x00':
            content = gzip.GzipFile(fileobj=cStringIO.StringIO(content)).read()
        print content

#x = Pageparse()
#x.parse('douga-mad-1')

x = Avparse()
if x.parse('394073'):
    print x.getDianji()
