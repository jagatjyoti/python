#!/usr/bin/python

import requests

r = requests.get('https://jsonplaceholder.typicode.com/posts')
print "Status code:", r.status_code
print "Headers:", r.headers
print "Content:", r.content


r = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
print "Status code:", r.status_code
print "Headers:", r.headers
print "Content:", r.content
