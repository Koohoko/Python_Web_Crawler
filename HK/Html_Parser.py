import re


class HtmlParser(object):
    def parse(self, html_content):
        if html_content == None:
            return None
        nohead = re.sub(re.compile(r'{"stn":{\r\n"data":\[\r\n'), '', html_content)
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
        listw = re.split(re.compile(r'\),'), listo)
        return listw
