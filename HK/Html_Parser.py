from bs4 import BeautifulSoup


def content_filter(soup):
    data = soup.find_all()


class HtmlParser(object):
    def parse(self, html_content):
        if html_content == None:
            return None
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='ISO-8859-1')
        data = content_filter(soup)
        return data
        