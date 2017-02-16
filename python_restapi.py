#!/usr/bin/python

import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/posts')
print "Status code:", r.status_code
#print "Headers:", r.headers
#print "Content:", r.content
data = json.loads(r)
"""
r = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
print "Status code:", r.status_code
print "Headers:", r.headers
print "Content:", r.content


headers = {
    'Content-Type': 'application/json',
}

data = open('gtt.json')
r = requests.post('https://jsonplaceholder.typicode.com/posts', headers=headers, data=data)
print "Status code:", r.status_code
print "Headers:", r.headers
print "Content:", r.content
"""
