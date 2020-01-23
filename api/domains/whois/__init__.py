#!/usr/bin/env python3

print(__name__)

__all__ = [
	"__main__",
]

from . import __main__

from ...config import api
api.register_blueprint(__main__.self, url_prefix="/domains/whois")
