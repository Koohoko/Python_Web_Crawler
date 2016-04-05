import urllib2

class HtmlDownloader(object):
    def download(self, url, year):
        request = urllib2.Request(url)
        referer = 'http://www.hko.gov.hk/cis/dailyExtract_e.htm?y={}&m=1'.format(year)
        request.add_header('Connection', 'keep-alive')
        request.add_header('Cache-Control', 'max-age=0')
        request.add_header('Accept', 'text/plain, */*; q=0.01')
        request.add_header('X-Requested-With', 'XMLHttpRequest')
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36')
        request.add_header('Referer', referer)
        request.add_header('Accept-Encoding', 'gzip, deflate, sdch')
        request.add_header('Accept-Language', 'en,en-US;q=0.8,zh-CN;q=0.6,zh;q=0.4')
        request.add_header('Cookie', 'HKO_Language=auto; HKO_DefaultHomePage=nclf')
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()

