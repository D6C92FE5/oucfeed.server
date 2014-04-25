# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import os

import cherrypy

from oucfeed.server import cors  # 初始化 CORS

from oucfeed.server.root import RootPage
from oucfeed.server.news import NewsPage
from oucfeed.server.list import ListPage
from oucfeed.server.item import ItemPage
from oucfeed.server.category import CategoryPage
from oucfeed.server.profile import ProfilePage
from oucfeed.server.feed import FeedPage


config = {
    b'/': {
        'response.headers.Access-Control-Allow-Origin': "*",  # CORS
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.encode.on': True,
        'tools.encode.encoding': 'utf-8',
        'tools.cors.on': True,
    },
    b'/oucfeed.js': {
        'tools.staticfile.on': True,
        'tools.staticfile.filename': os.path.abspath("oucfeed.js"),
    },
}

root = RootPage()
root.news = NewsPage()
root.list = ListPage()
root.item = ItemPage()
root.category = CategoryPage()
root.profile = ProfilePage()
root.rss = FeedPage('rss')
root.atom = FeedPage('atom')
