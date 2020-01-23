#!/usr/bin/env python3

print(__name__)

__all__ = [
	"__main__",
	"whois",
]

from . import __main__
from . import whois

from ..config import api
api.register_blueprint(__main__.self, url_prefix="/domains")
