# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import re

url = 'http://www.hko.gov.hk/cis/dailyExtract/dailyExtract_2010.xml'
request = urllib2.Request(url)
request.add_header('Connection', 'keep-alive')
request.add_header('Cache-Control', 'max-age=0')
request.add_header('Accept', 'text/plain, */*; q=0.01')
request.add_header('X-Requested-With', 'XMLHttpRequest')
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')
request.add_header('Referer', 'http://www.hko.gov.hk/cis/dailyExtract_e.htm?y=2010&m=1')
request.add_header('Accept-Encoding', 'gzip, deflate, sdch')
request.add_header('Accept-Language', 'en,en-US;q=0.8,zh-CN;q=0.6,zh;q=0.4')
request.add_header('Cookie', 'HKO_Language=auto; HKO_DefaultHomePage=nclf')
request.header_items()
response = urllib2.urlopen(request)
xml_content = response.read()

