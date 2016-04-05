class UrlManager(object):

    def generate_new_urls(self):
        urllist = set()
        #url = 'http://www.hko.gov.hk/cis/dailyExtract/dailyExtract_2010.xml'
        for year in range(2010,2017):
            new_url = 'url = http://www.hko.gov.hk/cis/dailyExtract/dailyExtract_{}.xml'.format(year)
            urllist.add(new_url)
        return urllist