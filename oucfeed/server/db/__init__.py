# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals


try:
    from google.appengine.ext import ndb
except:
    from oucfeed.server.db.sqlite import *
else:
    from oucfeed.server.db.gae import *
