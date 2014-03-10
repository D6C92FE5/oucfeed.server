# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import pymongo

from oucfeed.server import config
from oucfeed.server.datastore.base import BaseDatastore


class MongodbDatastore(BaseDatastore):

    # noinspection PyMissingConstructor
    def __init__(self):
        self._db = None

    @property
    def db(self):
        if not self._db:
            client = pymongo.MongoClient(config.DATASTORE_URI)
            self._db = client[config.DATASTORE_NAME]

            if config.PLATFORM == "BAE":
                auth = getattr(config, 'DATASTORE_AUTHENTICATE')
                if auth:
                    self.db.authenticate(**auth)
                else:
                    pass  # FIXME: 提示错误
        return self._db

    def _select(self, table, where=None, **kwargs):
        return self.db[table].find(where, **kwargs)

    def _insert_or_update(self, table, item):
        if isinstance(item, list):
            self.db[table].insert(item)
        else:
            self.db[table].save(item)

    def _get_misc(self, key, default=None):
        item = next(self._select('misc', {'key': key}), {})
        return item.get('value', default)

    def _set_misc(self, key, value):
        item = {'key': key, 'value': value}
        self._insert_or_update('misc', item)

    # news

    def get_news(self, where=None):
        return self._select('news', where=where, sort=[('$natural', pymongo.DESCENDING)])

    def add_news(self, news):
        self._insert_or_update('news', news)

    # history

    def get_history(self):
        return set(self._get_misc('history', []))

    def set_history(self, history):
        self._set_misc('history', list(history))

    # category

    def get_category(self):
        return self._get_misc('category', {})

    def set_category(self, category):
        self._set_misc('category', category)

    # profile

    def get_profile_by_id(self, profile_id):
        item = next(self.get_profile({'id': profile_id}), {})
        return item.get('data', {})
