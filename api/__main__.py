#!/usr/bin/env python3

print(__name__, __package__)

import sys, os.path

if not __package__:
	__package__ = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
	sys.path.insert(0, os.path.dirname(
		os.path.dirname(
			os.path.abspath(__file__)
		)
	))

from . import *

api = app.api

def main():
	import sys
	print(api.url_map)
	return api.run(
		host="0.0.0.0",
		port=int(sys.argv[1]) if len(sys.argv) > 1 else 8080,
		use_reloader=True,
		use_debugger=True,
		use_evalex=False,
		debug=True,
	)

if __name__ == '__main__':
	main()
else:
	print(app.url_map, f"""
		name: {__name__}
		pkg : {__package__}
		path: {sys.path}
	""")

"""
app = config.Flask(__name__)
@app.route("/hello")
def hello():
	return "world"
"""
