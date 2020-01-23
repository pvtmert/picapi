#!/usr/bin/env python3

import sys, os.path

if not __package__:
	__package__ = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
	sys.path.insert(0, os.path.dirname(
		os.path.dirname(
			os.path.abspath(__file__)
		)
	))

from .config import api as application

print(application.url_map, f"""
	name: {__name__}
	pkg : {__package__}
	path: {sys.path}
""")

