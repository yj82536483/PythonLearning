# -*- coding: utf-8 -*-
import urllib.request
import os
import re


def jokeCrawler(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    HTML = str(response.read())
    with open(os.getcwd() + os.sep + "1.html","w",encoding='utf-8') as f:
        f.write(HTML)


    pat = r'<div class="author clearfix">(.*?)</span>'
    re1 = re.compile(pat)

    for i in re1.findall(HTML):
        #print(i)
        pat_au = r'<h2>(.*?)</h2>'



url = "https://www.qiushibaike.com/8hr/page/1/"
jokeCrawler(url)