import urllib2

class HtmlDownloader(object):
    def download(self, url):
        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None
        return response.read()

