import urllib
import urllib2

DUOSHUO_LIST_TOP_URL = 'http://api.duoshuo.com/sites/listTopThreads.json'
DUOSHUO_SHORT_NAME = 'yasir'

def duoshuo_comments():
    params = {"short_name":DUOSHUO_SHORT_NAME}
    #headers = {"Content-type":"application/x-www-from-urlencoded","Accept":"text/json",
    #"User-Agent":"mozilla/5.0 (windows nt 6.1; wow64) applewebkit/537.36 (khtml, like gecko) chrome/31.0.1650.63 safari/537.36"
    #}
    ret = urllib2.urlopen(DUOSHUO_LIST_TOP_URL,urllib.urlencode(params))
    return ret

print duoshuo_comments()