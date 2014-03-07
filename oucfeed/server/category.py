# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import cherrypy
from cherrypy import request, response

from oucfeed.server.datastore import datastore


class CategoryPage(object):

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self):
        return datastore.get_category()

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        datastore.set_category(request.json)
        return {}


def add(category_iter):
    category_dict = datastore.get_category()
    for category in category_iter:
        category_node = category_dict
        for part in category:
            if part not in category_node:
                category_node[part] = {}
            category_node = category_node[part]
    datastore.set_category(category_dict)
