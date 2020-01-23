#!/usr/bin/env python3

print(__name__)

import platform
from redis import Redis
from flask import Flask, Blueprint, escape, jsonify

api = Flask("picapi")

@api.errorhandler(404)
def err_notfound(error):
	return ("404", 404) #error

@api.errorhandler(403)
def err_forbidden(error):
	return ("403", 403) #error

cache = Redis(host="cache")

headers = dict(
	etag=f"{id(api)}:{hash(platform.python_version())}",
	#refresh=5,
)


class ApiPath(Blueprint):
	#api.register_blueprint(app.self, url_prefix="/")
	def register_blueprint(self, blueprint: Blueprint, **options):
		#blueprint.url_prefix
		return
	pass

"""
	def __init__(self, name, import_name, prefix):
		super(ApiPath, self).__init__(name, import_name)
		self.blueprint = blueprint
		self.prefix = f"/{prefix}"

	def route(self, rule, **options):
		rule = f"{self.prefix}{rule}"
		return self.blueprint.route(rule, **options)
	pass
"""

#print("initialized with:", platform.uname())
