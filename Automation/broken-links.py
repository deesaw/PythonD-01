#connect to cisco
import urllib2
content=''
for line in urllib2.urlopen('http://www.plateletdonors.org'):
    content+=line
import re
urls=re.findall('(?i)<a([^>]+)>(.+?)</a>',content)
a=[]
for url in urls:
    url_to_check=url[0].split('"')[1]
    if url_to_check.startswith('http'):
        a.append(url_to_check)
for url in a:
    try:
        request = urllib2.Request(url)
        request.get_method = lambda : 'HEAD'
        response = urllib2.urlopen(request)
        print url + ' is fine'
    except urllib2.URLError:
        print url + 'is broken'

        


