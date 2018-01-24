#!/usr/local/bin/python3
# encoding:utf-8

from bs4 import BeautifulSoup
from pip._vendor import requests


def getHTML(url):
    # headers = {
    #     "User-Agent": "User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, "
    #                   "like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    # url_request = request.Request(url, headers=headers)
    # return request.urlopen(url_request).read().decode("utf-8")
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


def get_pengfu_results(url):
    soup = BeautifulSoup(getHTML(url), 'lxml')
    return soup.find_all('div', {'class': "content-img clearfix pt10 relative"})


def get_pengfu_joke():
    for index in range(11, 14):
        url = 'http://www.pengfu.com/xiaohua_%d.html' % index
        for item in get_pengfu_results(url):
            content = item.string
            try:
                string = content.lstrip()
                print(string + '\n\n')
            except:
                continue
    return


def get_qiubai_results(url):
    soup = BeautifulSoup(getHTML(url), 'lxml')
    contents = soup.find_all('div', {'class': 'content'})
    results = []
    for x in contents:
        result = x.find('span').getText('\n', '<br/>')
        results.append(result)
    return results


def get_qiubai_joke():
    for x in range(1, 2):
        url = 'https://www.qiushibaike.com/8hr/page/%d/' % x
        for x in get_qiubai_results(url):
            print(x + '\n\n')
    return


if __name__ == '__main__':
    get_pengfu_joke()
    get_qiubai_joke()
