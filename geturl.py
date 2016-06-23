
#!/usr/bin/python

import urllib2

response = urllib2.urlopen('https://www.youtube.com')
print response.info()
html = response.read()
print html
response.close()
