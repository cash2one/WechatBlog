#encoding:UTF-8
import urllib
import urllib.parse as parse
import urllib.request as request
import re

from pyquery import PyQuery as pq

def getTag(article):

	url = "http://lietu.com/demo/KeyWords.jsp"
	postData = parse.urlencode({'doc1': article}).encode('utf-8')
	result = request.urlopen(url, postData).read().decode('utf-8')
	pageSource = pq(result)
	typeCollection = pageSource('.bg:eq(1)').text()

	pattern = re.compile(r'(?<=\s)\D+(?=:)')
	match = pattern.findall(typeCollection)

	return match
