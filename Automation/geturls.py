#Get all urls from a webpage
#Code courtesy http://python.zirael.org/oop-emul1-1.py


import urllib2
import re

class Links( object):
  """provides an iterator over links from a HTML page"""

  def __init__( self, text=""):
    self.text = ""
    self._index = 0

  def read_url( self, url):
    try:
      f = urllib2.urlopen( url)
    except urllib2.URLError:
      return False
    self.text = f.read()
    f.close()
    return True

  def __iter__( self):
    return self

  def next( self):
    """next step of the iterator"""
    regexp = re.compile( '<a\s+href="(.*?)".*?>', re.I)
    m = regexp.search( self.text, pos=self._index)
    if m:
      self._index = m.end( 1) #@+ end position of the match
      return m.group( 1)
    else:
      raise StopIteration

l = Links()
l.read_url( "http://www.intel.com")
for link in l:
  print link
