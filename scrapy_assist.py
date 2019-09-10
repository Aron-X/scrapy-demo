import requests
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor


def get_response(url_str):
    """
    获得scrapy.HtmlResponse对象, 在不新建scrapy项目工程的情况下，
    使用scrapy的一些函数做测试
    :param url_str: {str} 链接
    :return: {HtmlResponse} scrapy响应对象
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0"
    }
    response_element = requests.get(url_str, headers=headers)
    return HtmlResponse(url=url_str, body=response_element.content)


def extract_links(response_element, allow, allow_domains):
    """
    解析所有符合要求的链接, 每次都解析不出来text属性，所以直接封装,可以做一些特定扩展
    :param response_element: {scrapy.http.HtmlResponse} scrapy响应
    :param allow: {tuple} 链接限定元组
    :param allow_domains: {tuple} 域名限定元组
    :return: {iterator({str})}
    """
    link_extractor = LinkExtractor(allow=allow, allow_domains=allow_domains)
    links = link_extractor.extract_links(response_element)
    return (link.url for link in links)


if __name__ == '__main__':
    url = "https://www.lagou.com/"

    response = get_response(url)
    links = extract_links(response, ("jobs/\d+.html"), ("lagou.com",))

    for link in links:
        print(link)
