# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import pymongo

from oucfeed.server import config
from oucfeed.server.datastore.base import BaseDatastore


class MongodbDatastore(BaseDatastore):

    # noinspection PyMissingConstructor
    def __init__(self):
        client = pymongo.MongoClient(config.DATASTORE_URI)
        self.db = client.oucfeed

    def _select(self, table, where=None):
        return self.db[table].find(where)

    def _insert_or_update(self, table, item):
        self.db[table].save(item)

    def _inserts(self, table, items):
        self.db[table].insert(items)

    def _get_misc(self, key):
        item = self._select('misc', {'key': key})
        return item['value']

    def _set_misc(self, key, value):
        item = {'key': key, 'value': value}
        self._insert_or_update('misc', item)

    def add_news(self, news):
        self._inserts('news', news)

    def get_news_history(self, where=None):
        return self._get_misc('news_history')

    def set_news_history(self, news_history):
        self._set_misc('news_history', news_history)

    def get_category(self, where=None):
        return self._get_misc('category')

    def set_category(self, category):
        self._set_misc('category', category)

    def get_profile_by_id(self, profile_id):
        return self.get_profile({'id': profile_id})
