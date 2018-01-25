#!/usr/local/bin/python3
# encoding:utf-8
from selenium import webdriver

# chromeDriver = "/Users/muyuanqiang/Downloads/chromedriver"
# os.environ["webdriver.chrome.driver"] = chromeDriver
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
# browser.find_element_by_id("kw").send_keys("selenium")
# browser.find_element_by_id("su").click()
# browser.find_element_by_css_selector("")
print(browser.page_source)
browser.quit()
