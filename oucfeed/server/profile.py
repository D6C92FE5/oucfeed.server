# -*- coding: utf-8 -*-

from __future__ import division, absolute_import, print_function, unicode_literals

import json
import hashlib

import cherrypy
from cherrypy import request, response

from oucfeed.server import util
from oucfeed.server.datastore import datastore


class ProfilePage(object):

    exposed = True

    @cherrypy.tools.json_out()
    def GET(self, id_):
        return get_by_id(id_)

    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def POST(self):
        id_ = generate_profile_id(request.json)
        datastore.set_profile(id_, request.json)
        return {'id': id_}


generate_profile_id = util.json_sha1_base64


def get_by_id(profile_id):
    return datastore.get_profile(profile_id)


def match(profile, category):
    for part in category:
        profile = profile.get(part)
        if profile == {}:
            return True
        if not profile:
            break
    return bool(profile)
