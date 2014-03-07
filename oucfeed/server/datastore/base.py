# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals


class BaseDatastore(object):

    def __init__(self):
        raise NotImplementedError()

    def _select(self, table, where=None):
        raise NotImplementedError()

    def _insert_or_update(self, table, item):
        raise NotImplementedError()

    def get_news(self, where=None):
        return self._select('news', where=where)

    def add_news(self, news):
        for item in news:
            self._insert_or_update('news', item)

    def get_news_history(self, where=None):
        return self._select('news_history', where=where)

    def set_news_history(self, news_history):
        self._insert_or_update('news_history', news_history)

    def get_category(self, where=None):
        return self._select('category', where=where)

    def set_category(self, category):
        self._insert_or_update('category', category)

    def get_profile(self, where=None):
        return self._select('profile', where=where)

    def set_profile(self, profile):
        self._insert_or_update('profile', profile)

    def get_profile_by_id(self, profile_id):
        for item in self._select('profile'):
            if item['id'] == profile_id:
                return item
        return None
