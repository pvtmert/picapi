#!/usr/bin/env python3

print(__name__)

from whois import whois

from ...config import *

self = ApiPath("whois", __name__)

@self.route("/<domain>")
def api_route_domains_whois(domain="n0pe.me"):
	try:
		return (whois(domain), 200, { **headers, })
	except Exception as e:
		return (dict(error=str(e)), 400, { **headers, })
	return (dict(error=__name__), 500, { **headers, })
