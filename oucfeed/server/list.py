# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from itertools import islice

import cherrypy
from cherrypy import request, response

from oucfeed.server import util, news
from oucfeed.server.datastore import datastore


class ListPage(object):

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, profile_id='all', count=None):
        count = util.parse_output_count(count)
        items = list(islice(util.remove_mongodb_id(news.filtered_by_profile(profile_id)), count))
        for item in items:
            del item['content']
        return items
