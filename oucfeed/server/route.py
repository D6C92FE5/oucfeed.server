# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

import cherrypy

from oucfeed.server import cors

from oucfeed.server.root import Root
from oucfeed.server.news import News
from oucfeed.server.category import Category
from oucfeed.server.profile import Profile
from oucfeed.server.feed import Feed


config = {
    '/': {
        'response.headers.Access-Control-Allow-Origin': "*",  # CORS
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
        'tools.cors.on': True,
    },
}

root = Root()
root.news = News()
root.category = Category()
root.profile = Profile()
root.rss = Feed('rss')
root.atom = Feed('atom')
