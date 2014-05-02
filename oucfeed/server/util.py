# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import json
import hashlib
import base64
import threading
import urllib

from oucfeed.server import config


def json_sha1_base64(obj):
    s = json.dumps(obj, sort_keys=True)
    h = hashlib.sha1(s).digest()
    b = base64.urlsafe_b64encode(h)
    return b.strip('=')


def try_parse_int(string, default):
    try:
        ret = int(string)
    except (TypeError, ValueError):
        ret = default
    return ret


def parse_output_count(string):
    ret = try_parse_int(string, config.EXPORT_COUNT_DEFAULT)
    ret = max(ret, config.EXPORT_COUNT_MIN)
    ret = min(ret, config.EXPORT_COUNT_MAX)
    return ret


def parse_datetime(datetime_string):
    with lock:
        from datetime import datetime
        return datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")
lock = threading.Lock()


def remove_mongodb_id(items):
    for item in items:
        del item['_id']
        yield item


def url_decode(url):
    return urllib.unquote(url)
