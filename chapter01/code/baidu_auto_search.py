"""
    文件名：baidu_auto_search.py
    用途：百度一下，你就知道，自动化搜索脚本
"""
import time
from selenium import webdriver

# 创建的是一个全新的浏览器
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")

# 元素定位
keyword_input = browser.find_element_by_id("kw")
search_button = browser.find_element_by_id("su")

# 元素操作
keyword_input.send_keys("selenium")
search_button.click()

time.sleep(3)

# 场景还原
browser.get("https://www.baidu.com")
# browser.quit()