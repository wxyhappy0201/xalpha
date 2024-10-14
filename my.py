'''
Author: wxyhappy0201 844720622@qq.com
Date: 2024-10-14 22:24:52
LastEditors: wxyhappy0201 844720622@qq.com
LastEditTime: 2024-10-14 22:55:06
FilePath: /git/xalpha/my.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import xalpha as xa
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
def get_xueqiu_specific_cookies():
    # 设置 Chrome 选项
    chrome_options = Options()
    chrome_options.add_argument("--headless") # 无头模式，不显示浏览器窗口
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # 初始化 WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # 访问雪球网
        driver.get("https://xueqiu.com")
        
        # 等待一段时间，让 JavaScript 有时间执行
        time.sleep(5)
        
        # 获取所有 cookies
        cookies = driver.get_cookies()
        
        # 只提取 'xq_a_token' 和 'u'
        specific_cookies = {}
        for cookie in cookies:
            if cookie['name'] in ['xq_a_token', 'u']:
                specific_cookies[cookie['name']] = cookie['value']
        
        return specific_cookies

    finally:
        # 确保关闭浏览器
        driver.quit()

if __name__ == "main":
    result = get_xueqiu_specific_cookies()
    # 写入 JSON 文件
    xuqiu_cookie_file = 'xalpha_xuqiu_cookie.data'
    with open(xuqiu_cookie_file, 'w') as f:
        json.dump(result, f)