#!/usr/bin/env python3

print(__name__)

import re, io, os, sys, time, json, socket, struct, threading

from .config import *

# TODO: impl;
# - /location/<float:lat>/<float:lng>
#   GET   -> return list of items
#   POST  -> upload image to location -> returns id
# - /images/<string:id>/large
#   GET   -> return original image
# - /images/<string:id>/thumb
#   GET   -> return smaller image

self = ApiPath("app", __name__)

@self.route("/")
def api_route_root():
	return ({
		"/item": [ "GET", "POST", ],
		"/auth": None,
		"/env": dict(os.environ),
	}, 200, { **headers, })
