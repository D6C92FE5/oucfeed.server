# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import cherrypy
from cherrypy import request, response

from oucfeed.server import util
from oucfeed.server.datastore import datastore


class ItemPage(object):

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, *news_id):
        items = datastore.get_news({'id': b"/".join(news_id).decode('utf-8')})
        items = list(util.remove_mongodb_id(items))
        item = items[0] if len(items) > 0 else None
        return item
