#!/usr/bin/env python3

import platform
import flask, redis

app = flask.Flask(__name__)

@app.errorhandler(404)
def err_notfound(error):
	return "404" #error

@app.errorhandler(403)
def err_forbidden(error):
	return "403" #error

cache = redis.Redis(host="cache")
