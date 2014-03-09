# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import cherrypy

from oucfeed.server import cors  # 初始化 CORS

from oucfeed.server.root import RootPage
from oucfeed.server.news import NewsPage
from oucfeed.server.category import CategoryPage
from oucfeed.server.profile import ProfilePage
from oucfeed.server.feed import FeedPage


config = {
    b'/': {
        'response.headers.Access-Control-Allow-Origin': "*",  # CORS
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.cors.on': True,
    },
}

root = RootPage()
root.news = NewsPage()
root.category = CategoryPage()
root.profile = ProfilePage()
root.rss = FeedPage('rss')
root.atom = FeedPage('atom')
