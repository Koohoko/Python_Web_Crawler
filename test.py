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
request.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')
request.add_header('Referer', 'http://www.hko.gov.hk/cis/dailyExtract_e.htm?y=2010&m=1')
request.add_header('Accept-Encoding', 'gzip, deflate, sdch')
request.add_header('Accept-Language', 'en,en-US;q=0.8,zh-CN;q=0.6,zh;q=0.4')
request.add_header('Cookie', 'HKO_Language=auto; HKO_DefaultHomePage=nclf')
request.header_items()
response = urllib2.urlopen(request)
xml_content = response.read()

# parser
nohead = re.sub(re.compile(r'{"stn":{\r\n"data":\[\r\n'), '', xml_content)
nohead2 = re.sub(re.compile(r'{"month":\d+,\r\n"dayData":\[\r\n'), '', nohead)
print(nohead2)
notail = re.sub(re.compile(r'\r\n]}\r\n]}}\r\n'), '', nohead2)
# "25.4"]\r\n]},\r\n["01",
notail2 = re.sub(re.compile(r'\r\n]}'), '', notail)
raw = re.sub(re.compile(r'\["Mean/Total",.+', ), '', notail2)
raw2 = re.sub(re.compile(r'\["Normal",.+', ), '', raw)
out = re.sub(re.compile(r'\s+'), '', raw2)
out2 = re.sub(re.compile(r'\['), '', out)
out3 = re.sub(re.compile(r']'), ')', out2)
listo = re.sub(re.compile(r'"'), '', out3)
list = re.split(re.compile(r'\),'), listo)

list[1]
type(list)
len(list)


with open('some.csv', 'wb') as f:
    writer = csv.writer(f)
    for i in range(0, len(list)):
        writer.writerow(re.split(re.compile(r','), list[i]))
