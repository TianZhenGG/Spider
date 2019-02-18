import requests

from lxml import etree

class QiubaiSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/text/page/{}/"
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1,14)]

    def parse_url(self,url):
        response = requests.get(url,headers = self.headers)
        return response.content.decode()

    def get_content_list(self,html_str):
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id='content-left']/div")
        content_list = []
        for div in div_list:
            item={}
            item["content"] = div.xpath(".//div[@class='content']/span/text()")
            content_list.append(item)

        return content_list

    def save_content_list(self,content_list):
        for i in content_list:
            print(i)

    def run(self):
        url_list = self.get_url_list()

        for url in url_list:
            html_str = self.parse_url(url)
            content_list = self.get_content_list(html_str)
            self.save_content_list(content_list)


if __name__ == "__main__":

    qiubai = QiubaiSpider()
    qiubai.run()