# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     testRedisClient
   Description :
   Author :        JHao
   date：          2020/6/23
-------------------------------------------------
   Change Activity:
                   2020/6/23:
-------------------------------------------------
"""
from handler.proxyHandler import ProxyHandler
__author__ = 'Gaoxiang'

proxy_handler = ProxyHandler()


def testProxyHandler():
    proxy_handler.ban("103.171.84.215:8080")
    proxy_handler.unban("103.171.84.215:8080")

    proxy_handler.unuseable("116.62.26.183:7890")






if __name__ == '__main__':
    testProxyHandler()
