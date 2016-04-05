from HK import Html_Downloader, Url_Manager, Html_Parser, Outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = Url_Manager.UrlManager()
        self.downloader = Html_Downloader.HtmlDownloader()
        self.parser = Html_Parser.HtmlParser()
        self.outputer = Outputer.Outputer()

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            obj_url = self.urls.get_new_url()
            try:
                print("success:{} url:{}".format(count, obj_url))
                html_content = self.downloader.dowload(obj_url)
                data = self.parser.parse(html_content)
                self.urls.add_new_urls()
                self.outputer.collect_data(data)
            except:
                print("failed:{} url:{}".format(count, obj_url))
            count = count + 1
        self.outputer.output_html()
        self.outputer.output_csv()


if __name__=="__main__":
    root_url = 'http://www.hko.gov.hk/cis/dailyExtract_e.htm?y=2010&m=1'
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)