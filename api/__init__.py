#!/usr/bin/env python3

print(__name__)

__all__ = [
	"app",
	"config",
	"domains",
	"health",
]

#from . import config
#from .domains import *

from . import app
from . import config
from . import domains
from . import health

from .config import api
api.register_blueprint(app.self, url_prefix="/")
