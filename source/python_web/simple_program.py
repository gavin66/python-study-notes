from urllib import request
import re

p = re.compile('<a href="(.*?)" .*?>(.*?)</a>')
text = request.urlopen('http://www.dgtle.com/').read().decode('utf-8')
for url, name in p.findall(text):
    print('%s (%s)' % (name, url))
