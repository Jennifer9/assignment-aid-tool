# -*- coding: utf-8 -*-
import scrapy
from sys import *
import urllib.request
import os
import argparse
import requests
from urllib.parse  import *
from t1.items import MyItem

from scrapy.http import Request

desktop = os.path.expanduser("~/Desktop")
desktop += "/"
cs360_url = 'https://www.student.cs.uwaterloo.ca/~cs360/'
cs348_url = 'https://cs.uwaterloo.ca/~david/cs348/assignments.html'
# number = '1'

class Da(scrapy.Spider):
    name = "da"
    # start_urls = ['https://cs.uwaterloo.ca/~david/cs348/assignments.html']

    def __init__(self, *args, **kwargs):
        course = kwargs.pop('course', [])
        c = course.split(',')
        self.number = c[1]
        cs = c[0]
        if cs == '360':
            print("im here!")
            self.start_urls = [cs360_url]
            print(self.start_urls)
        if cs == '348':
            self.start_urls = [cs348_url]
        self.logger.info(self.start_urls)
        super().__init__(*args, **kwargs)



    def parse(self, response):
        print("im here!")
        for href in response.css('ul li a[href$=".pdf"] ::attr(href)').extract():
            yield Request (
                url = response.urljoin(href),
                callback = self.save_pdf
            )

    def save_pdf(self, response):
        name = response.url.split('/')[-1]
        i = MyItem()
        i['body'] = response.body
        i['url'] = response.url
        number = self.number
        if (number in name):
            i['path'] = desktop + response.url.split('/')[-1]
        return i
