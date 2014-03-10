# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

from oucfeed.server import config
from oucfeed.server.datastore.mongodb import MongodbDatastore
from oucfeed.server.datastore.gae import NdbDatastore


if config.PLATFORM == "GAE":
    Datastore = NdbDatastore
else:
    Datastore = MongodbDatastore
datastore = Datastore()
