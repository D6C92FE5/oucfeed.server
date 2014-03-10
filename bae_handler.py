#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import os
import sys


os.chdir(os.path.dirname(__file__))
sys.path.insert(0, '.')


from bae.core.wsgi import WSGIApplication
from oucfeed.server import app


application = WSGIApplication(app)
