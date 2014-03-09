# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import pymongo
import cherrypy
from bson import json_util

from oucfeed.server import config
from oucfeed.server.datastore.base import BaseDatastore


class MongodbDatastore(BaseDatastore):

    # noinspection PyMissingConstructor
    def __init__(self):
        client = pymongo.MongoClient(config.DATASTORE_URI)
        self.db = client.oucfeed

    def _select(self, table, where=None, **kwargs):
        return self.db[table].find(where, **kwargs)

    def _insert_or_update(self, table, item):
        self.db[table].save(item)

    def _inserts(self, table, items):
        self.db[table].insert(items)

    def _get_misc(self, key, default=None):
        item = next(self._select('misc', {'key': key}), {})
        return item.get('value', default)

    def _set_misc(self, key, value):
        item = {'key': key, 'value': value}
        self._insert_or_update('misc', item)

    def get_news(self, where=None):
        return self._select('news', where=where, sort=[('$natural', pymongo.DESCENDING)])

    def add_news(self, news):
        self._inserts('news', news)

    def get_news_history(self, where=None):
        return set(self._get_misc('news_history', []))

    def set_news_history(self, news_history):
        self._set_misc('news_history', list(news_history))

    def get_category(self, where=None):
        return self._get_misc('category', {})

    def set_category(self, category):
        self._set_misc('category', category)

    def get_profile_by_id(self, profile_id):
        item = next(self.get_profile({'id': profile_id}), {})
        return item.get('data', {})

    def set_profile_by_id(self, profile_id, profile):
        item = {'id': profile_id, 'data': profile}
        self.set_profile(item)
