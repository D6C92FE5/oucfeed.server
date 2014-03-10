# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals


import os
import json
from io import open

PLATFORM = ""  # 运行于 GAE, SAE, BAE 等平台？

DATASTORE_URI = "mongodb://localhost:27017/"
DATASTORE_NAME = "oucfeed"

EXPORT_COUNT_DEFAULT = 10
EXPORT_COUNT_MIN = 1
EXPORT_COUNT_MAX = 50


def load():
    config_path = "config.json"
    if os.path.exists(config_path):
        with open(config_path, encoding='utf-8') as f:
            config = json.load(f)
        global_ = globals()
        for k in config:
            global_[k] = config[k]
load()


def detect_platform():
    global PLATFORM
    if not PLATFORM:
        try:
            import google.appengine
            PLATFORM = "GAE"
        except ImportError:
            try:
                import bae
                PLATFORM = "BAE"
            except ImportError:
                pass
detect_platform()
