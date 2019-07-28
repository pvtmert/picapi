#!/usr/bin/env python3

import re, io, os, sys, time, json, socket, struct, threading

from config import *


# TODO: impl;
# - /location/<float:lat>/<float:lng>
#   GET   -> return list of items
#   POST  -> upload image to location -> returns id
# - /images/<string:id>/large
#   GET   -> return original image
# - /images/<string:id>/thumb
#   GET   -> return smaller image

@app.route('/')
def hello_world():
	return ({
		"/item": [ "GET", "POST", ],
		"/auth": None,
		"/env": dict(os.environ),
	}, 200, { "refresh": 5, })

#############################################################

def main():
	return app.run(
		host="0.0.0.0",
		port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000,
		use_evalex=False,
		debug=True,
	)

if __name__ == '__main__':
	main()
