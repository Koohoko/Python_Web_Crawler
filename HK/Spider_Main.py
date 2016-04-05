from HK import Html_Downloader, Url_Manager, Html_Parser, Outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = Url_Manager.UrlManager()
        self.downloader = Html_Downloader.HtmlDownloader()
        self.parser = Html_Parser.HtmlParser()
        self.outputer = Outputer.Outputer()

    def crawl(self):
        count = 1
        url_list = self.urls.generate_new_urls()
        for obj_url in url_list:
            try:
                print("success:{} url:{}".format(count, obj_url))
                html_content = self.downloader.download(obj_url)
                data = self.parser.parse(html_content)
                self.outputer.collect_data(data)
            except:
                print("failed:{} url:{}".format(count, obj_url))
            count = count + 1
        self.outputer.output_html()
        self.outputer.output_csv()


if __name__=="__main__":
    obj_spider = SpiderMain()
    obj_spider.crawl()