# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : Testfile.py
# Time       ：2024/12/10 18:44
# Author     ：HiaHiaHia
# version    ：python 3.12
# Description：
"""
import requests

if __name__ == '__main__':
    url = 'https://github.com/NieXiaoFeng0805/CrawlerTest'
    response = requests.get(url)
    page_text = response.text
    # print(page_text)
    with open('./Data/HTML_Data/github.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取结束')
