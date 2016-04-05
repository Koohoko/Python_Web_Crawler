from HK import Html_Downloader, Url_Manager, Html_Parser, Outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = Url_Manager.UrlManager()
        self.downloader = Html_Downloader.HtmlDownloader()
        self.parser = Html_Parser.HtmlParser()
        self.outputer = Outputer.Outputer()

    def crawl(self, root_url):
        pass


if __name__=="__main__":
    root_url = 'http://www.hko.gov.hk/cis/dailyExtract_e.htm?y=2010&m=1'
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)