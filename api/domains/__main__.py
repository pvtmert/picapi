#!/usr/bin/env python3

print(__name__)

from os import listdir, path, walk
# from json import dumps, loads

from ..config import *

self = ApiPath("domains", __name__)

"""
data = {
	path.relpath(pathname, path.dirname(__file__)): [
		#*[ f"{path.basename(n)}/" for n in dirnames ],
		*[
			f"{n.replace(extension, '', -1)}"
			for n in filenames if n.endswith(extension)
		],
	]
	for pathname, dirnames, filenames in walk(path.dirname(__file__))
	if "__pycache__" not in pathname
}
"""

@self.route("/")
def api_route_domains(extension=".txt"):
	return jsonify(
		list(
			map(
				lambda x: x.replace(extension, "", -1),
				filter(
					lambda x: x.endswith(".txt"),
					listdir(path.dirname(__file__)),
				)
			)
		)
	)

@self.route("/<filename>")
def api_route_domains_textfile(filename="main.py"):
	fileloc = path.join(path.dirname(__file__), escape(filename))
	try:
		with open(f"{fileloc}.txt", "r") as file:
			return (file.read(), 200, {
				"content-type": "text/plain",
				**headers,
			})
		pass
	except Exception as e:
		return (dict(error=str(e)), 400, { **headers, })
	return (dict(error=__name__), 500, { **headers, })
