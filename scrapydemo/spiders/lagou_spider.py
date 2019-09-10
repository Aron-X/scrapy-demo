import scrapy

from scrapydemo.items import LagouItem


class LagouSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = [
        "https://www.lagou.com/zhaopin/Java/1/",
        "https://www.lagou.com/zhaopin/Python/1/",
    ]

    cookie_list = "JSESSIONID=ABAAABAAAGGABCBCB01C6AA46970C708E1E25DB1BE9CDDD; user_trace_token=20190905134616-6b80aa49-c5e6-47b0-8fb1-5c158fdc5713; _ga=GA1.2.128277111.1567662377; LGUID=20190905134616-7a9591d6-cfa0-11e9-a50a-5254005c3644; _gid=GA1.2.1366641045.1567662377; WEBTJ-ID=09052019%2C134621-16cfff59b018ac-073e19ddeedf62-38607701-1764000-16cfff59b02a05; index_location_city=%E5%85%A8%E5%9B%BD; X_MIDDLE_TOKEN=703566feaa1c6778d8e9726f7343e747; TG-TRACK-CODE=index_navigation; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1567662377,1567663232; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d04a5bbf0307-042e86d3ac9868-38607701-1764000-16d04a5bbf13b3%22%2C%22%24device_id%22%3A%2216d04a5bbf0307-042e86d3ac9868-38607701-1764000-16d04a5bbf13b3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; LGSID=20190906130855-6d37acf2-d064-11e9-8f98-525400f775ce; gate_login_token=476c61395b85ff64fce89f035ae3c5efb4154d2d7c21107d596660972e268a35; _putrc=EC38704DF2035F02123F89F2B170EADC; login=true; unick=%E8%AE%B8%E6%B5%92; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; privacyPolicyPopup=false; SEARCH_ID=9f16facfc0aa4c70a2878facd800065f; X_HTTP_TOKEN=c0319a1fc1ea43c93618477651ba605632ec30022e; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1567748164; LGRID=20190906133604-37bc89e4-d068-11e9-a50b-5254005c3644"
    custom_settings = {
        "COOKIES_ENABLED": False,
        "DOWNLOAD_DELAY": 1,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': cookie_list,
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.meta = {
            'dont_redirect': True,
            'handle_httpstatus_list': [301, 302]
        }

        """
        def parse(self, response):
            folder = "html/"
            filename = response.url.split("/")[-2] + '_job.html'
            if not os.path.exists(folder):
                os.makedirs(folder)
            with open(folder + filename, 'wb') as f:
                f.write(response.body)
        """

        """
        def parse(self, response):
            for item in response.xpath('//ul/li'):
                title = item.xpath('a/text()').extract()
                link = item.xpath('a/@href').extract()
                desc = item.xpath('text()').extract()
                print(title, link, desc)
        """

    def parse(self, response):
        for sel in response.css('ul.item_con_list > li'):
            text = sel.css('.list_item_top').xpath('./div[1]//text()').re(r'[^ \s\[\]]+')
            item = LagouItem()
            item['job'] = text[0]
            item['location'] = text[1]
            item['publish_time'] = text[2]
            item['salary'] = text[3]
            item['requirement'] = text[4] + text[5] + text[6]
            yield item
        next_page = response.css('div.pager_container').xpath('./a[last()]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url + "?filterOption=3&sid=7a2adf6ca33d46fe9222545807beb985", callback=self.parse)


if __name__ == '__main__':
    from scrapy import cmdline

    cmdline.execute("scrapy crawl lagou".split())
