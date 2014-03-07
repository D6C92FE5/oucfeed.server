# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals


import os


DATASTORE_URI = "mongodb://localhost:27017/"

GAE = "APPLICATION_ID" in os.environ

EXPORT_COUNT_DEFAULT = 10
EXPORT_COUNT_MIN = 1
EXPORT_COUNT_MAX = 50
