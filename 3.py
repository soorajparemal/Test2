#!/usr/bin/python

#demo of requests library

import requests

r = requests.get('http://http://code.google.com')
print r.content
