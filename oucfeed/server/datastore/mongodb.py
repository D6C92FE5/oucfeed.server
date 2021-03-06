# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import json

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
                # noinspection PyUnresolvedReferences
                self._db.authenticate(config.BAE_API_KEY, config.BAE_SECRET_KEY)
        return self._db

    def _select(self, table, where=None, **kwargs):
        return self.db[table].find(where, **kwargs)

    def _insert_or_update(self, table, item, unique_field=None):
        if isinstance(item, list):
            self.db[table].insert(item)
        elif unique_field is not None:
            self.db[table].find_and_modify({unique_field: item[unique_field]}, item, upsert=True)
        else:
            self.db[table].save(item)

    def _get_misc(self, key, default=None):
        item = next(self._select('misc', {'key': key}), None)
        return json.loads(item['value']) if item is not None else default

    def _set_misc(self, key, value):
        item = {'key': key, 'value': json.dumps(value)}
        self._insert_or_update('misc', item, unique_field='key')

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

    def set_profile(self, profile):
        self._insert_or_update('profile', profile, unique_field='id')

    def get_profile_by_id(self, profile_id):
        item = next(self.get_profile({'id': profile_id}), {})
        return item.get('data', {})
