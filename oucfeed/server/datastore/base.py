# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals


class BaseDatastore(object):

    def __init__(self):
        raise NotImplementedError()

    def _select(self, table, where=None, **kwargs):
        raise NotImplementedError()

    def _insert_or_update(self, table, item):
        raise NotImplementedError()

    # news

    def get_news(self, where=None):
        return self._select('news', where=where)

    def add_news(self, news):
        for item in news:
            self._insert_or_update('news', item)

    # history

    def get_history(self):
        return self._select('history')

    def set_history(self, history):
        self._insert_or_update('history', history)

    # category

    def get_category(self):
        return self._select('category')

    def set_category(self, category):
        self._insert_or_update('category', category)

    # profile

    def get_profile(self, where=None):
        return self._select('profile', where=where)

    def set_profile(self, profile):
        self._insert_or_update('profile', profile)

    def get_profile_by_id(self, profile_id):
        for item in self._select('profile'):
            if item['id'] == profile_id:
                return item['data']
        return {}

    def set_profile_by_id(self, profile_id, profile):
        item = {'id': profile_id, 'data': profile}
        self.set_profile(item)
