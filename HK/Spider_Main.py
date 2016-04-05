from HK import Html_Downloader, Html_Parser, Outputer


class SpiderMain(object):
    def __init__(self):

        self.downloader = Html_Downloader.HtmlDownloader()
        self.parser = Html_Parser.HtmlParser()
        self.outputer = Outputer.Outputer()

    def crawl(self):
        count = 1
        for year in range(2010, 2017):
            new_url = 'http://www.hko.gov.hk/cis/dailyExtract/dailyExtract_{}.xml'.format(year)
            #try:
            html_content = self.downloader.download(new_url, year)
            data = self.parser.parse(html_content)
            self.outputer.output_csv(data, year)
            print("success:{} url:{}".format(count, new_url))
            #except:
            #    print("failed:{} url:{}".format(count, new_url))
            count = count + 1

if __name__=="__main__":
    obj_spider = SpiderMain()
    obj_spider.crawl()