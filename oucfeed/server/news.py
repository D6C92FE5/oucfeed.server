# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from itertools import islice

import cherrypy
from cherrypy import request, response

from oucfeed.server import util, category, profile
from oucfeed.server.datastore import datastore


class NewsPage(object):

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, profile_id='all', count=None):
        count = util.parse_output_count(count)
        news = islice(util.remove_mongodb_id(filtered_by_profile(profile_id)), count)
        return list(news)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        add(request.json)
        return {}


def add(news_list):
    history = datastore.get_history()

    news_list = [x for x in news_list if x['id'] not in history]
    for item in news_list:
        item['category'] = item['category'].split("/")
        history.add(item['id'])

    datastore.add_news(news_list)
    datastore.set_history(history)
    category.add(x['category'] for x in news_list)


def filtered_by_profile(profile_id):
    profile_ = profile.get_by_id(profile_id)
    for news in datastore.get_news():
        if profile_id == 'all' or profile.match(profile_, news['category']):
            yield news
