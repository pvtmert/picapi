#!/usr/bin/env python3

print(__name__)

import platform

from api import __main__ as application

def main():
	print(platform.python_version())
	return application.main()

if __name__ == '__main__':
	main()
