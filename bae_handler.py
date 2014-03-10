#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import os
import sys

app_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, app_root)
os.chdir(app_root)


# noinspection PyUnresolvedReferences
from oucfeed.server import application
