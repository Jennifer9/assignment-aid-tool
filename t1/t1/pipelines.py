# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from sys import *
import urllib.request
import os
import argparse
import requests
from urllib.parse  import *

from scrapy.http import Request

desktop = os.path.expanduser("~/Desktop")
desktop += "/"


class T1Pipeline(object):
    def process_item(self, item, spider):
        path = item['path']
        with open(path, 'wb') as f:
            f.write(item['body'])
        del item['body']
        item['path'] = path
        return item
