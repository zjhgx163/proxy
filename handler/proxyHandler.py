# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ProxyHandler.py
   Description :
   Author :       JHao
   date：          2016/12/3
-------------------------------------------------
   Change Activity:
                   2016/12/03:
                   2020/05/26: 区分http和https
-------------------------------------------------
"""
__author__ = 'JHao'

from helper.proxy import Proxy
from db.dbClient import DbClient
from handler.configHandler import ConfigHandler
import json


class ProxyHandler(object):
    """ Proxy CRUD operator"""

    def __init__(self):
        self.conf = ConfigHandler()
        self.db = DbClient(self.conf.dbConn)
        self.db.changeTable(self.conf.tableName)

    def get(self, https=False):
        """
        return a proxy
        Args:
            https: True/False
        Returns:
        """
        proxy = self.db.get(https)
        return Proxy.createFromJson(proxy) if proxy else None

    def pop(self, https):
        """
        return and delete a useful proxy
        :return:
        """
        proxy = self.db.pop(https)
        if proxy:
            return Proxy.createFromJson(proxy)
        return None

    def put(self, proxy):
        """
        put proxy into use proxy
        :return:
        """
        self.db.put(proxy)

    def delete(self, proxy):
        """
        delete useful proxy
        :param proxy:
        :return:
        """
        return self.db.delete(proxy.proxy)

    def getAll(self, https=False):
        """
        get all proxy from pool as Proxy list
        :return:
        """
        proxies = self.db.getAll(https)
        return [Proxy.createFromJson(_) for _ in proxies]

    def exists(self, proxy):
        """
        check proxy exists
        :param proxy:
        :return:
        """
        return self.db.exists(proxy.proxy)

    def getCount(self):
        """
        return raw_proxy and use_proxy count
        :return:
        """
        total_use_proxy = self.db.getCount()
        return {'count': total_use_proxy}

    def ban(self, proxy):
        """
        ban forbidden proxy
        :param proxy:
        :return:
        """
        proxy_json = self.db.getValueByField(proxy)
        if proxy_json is not None:
            proxy_obj = Proxy.createFromJson(proxy_json)
            proxy_obj.ban = True
            # _dict = json.loads(proxy_json)
            # _dict['ban'] = True
            return self.db.update(proxy_obj)
            # return self.db.updateValueByField(proxy,json.dumps(_dict, ensure_ascii=False))
        else:
            return -1

    def unuseable(self, proxy):
        """
        tag a proxy is unuseable
        :param proxy:
        :return:
        """
        proxy_json = self.db.getValueByField(proxy)
        if proxy_json is not None:
            proxy_obj = Proxy.createFromJson(proxy_json)
            proxy_obj.is_useable = False
            return self.db.update(proxy_obj)
        else:
            return -1