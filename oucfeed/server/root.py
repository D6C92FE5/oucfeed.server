# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import cherrypy


class RootPage(object):

    exposed = True

    def GET(self):
        return "OUC Feed"
