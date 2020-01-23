#!/usr/bin/env python3

print(__name__)

from ..config import *

self = ApiPath("health", __name__)

@self.route("/")
def health_check_all():
	return (dict(ok=True), 200, { **headers, })
