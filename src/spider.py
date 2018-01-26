#!/usr/local/bin/python3
# encoding:utf-8
import queue
import threading

import time
import urllib

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


# if __name__ == '__main__':
#     get_pengfu_joke()
# get_qiubai_joke()

baseUrl = 'http://www.pythontab.com/html/pythonjichu/'
urlQueue = queue.Queue()
for i in range(2, 10):
    url = baseUrl + str(i) + '.html'
    urlQueue.put(url)
    # print(url)


def fetchUrl(url_queue):
    while True:
        try:
            # 不阻塞的读取队列数据
            request_url = url_queue.get_nowait()
            i = url_queue.qsize()
        except Exception as e:
            break
        print('Current Thread Name %s, Url: %s ' % (threading.currentThread().name, request_url))
        try:
            response = urllib.request.urlopen(request_url)
            response_code = response.getcode()
        except Exception as e:
            continue
        if response_code == 200:
            # 抓取内容的数据处理可以放到这里
            # 为了突出效果， 设置延时
            time.sleep(1)


if __name__ == '__main__':
    startTime = time.time()
    threads = []
    # 可以调节线程数， 进而控制抓取速度
    threadNum = 4
    for i in range(0, threadNum):
        t = threading.Thread(target=fetchUrl, args=(urlQueue,))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        # 多线程多join的情况下，依次执行各线程的join方法, 这样可以确保主线程最后退出， 且各个线程间没有阻塞
        t.join()
    endTime = time.time()
    print('Done, Time cost: %s ' % (endTime - startTime))
