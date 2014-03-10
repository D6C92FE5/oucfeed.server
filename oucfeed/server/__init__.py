#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.server import config


# GAE 用的 site-packages
if config.PLATFORM in ("GAE",):
    import sys
    sys.path.insert(0, 'site-packages')


import cherrypy

from oucfeed.server import route


application = cherrypy.tree.mount(route.root, "", route.config)

if config.PLATFORM == "BAE":
    # noinspection PyUnresolvedReferences, PyPackageRequirements
    from bae.core.wsgi import WSGIApplication
    application = WSGIApplication(application)

if __name__ == '__main__':
    if not config.PLATFORM:
        cherrypy.engine.start()
        cherrypy.engine.block()
