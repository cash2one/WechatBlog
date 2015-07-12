#encoding:UTF-8
from pyquery import PyQuery as pq

import urllib.parse as parse

#通过关键词来获取微信公众号文章，返回网页源代码

def getArticleLinkCollection(keyWord):

	#请求字段
	query = {'type': '2', 'query': keyWord, 'page': 1}
	queryStr = parse.urlencode(query)

	#文章列表页源码
	url = 'http://weixin.sogou.com/weixin?' + queryStr
	pageSource = pq(url = url)

	#数组
	list = []

	#获取链接
	linkCollection = pageSource('h4 a')
	for link in linkCollection:
		articleUrl = (pq(link).attr('href'))

		#存入数组
		list.append(articleUrl)

	#返回数组
	return list

#Test
#print(getArticleLinkCollection('抽奖'))
