#encoding:UTF-8
from pyquery import PyQuery as pq
import filterHtml
import getTag

#根据文章地址返回文章标题、文章内容、文章摘要、文章标签、原文地址等，并以数组形式返回。
def getArticleAll(articleUrl):

	dictionary = {}

	#获取源代码
	articleSource = pq(url = articleUrl)

	#文章标题
	title = articleSource('title').text()
	dictionary['title'] = title

	#正文源码
	contentSource = str(articleSource('#js_content').html())

	#文章内容
	content = str(filterHtml.filterHtml(contentSource))
	dictionary['content'] = content

	#文章摘要

	#文章标签
	articleTag = getTag.getTag(content)
	dictionary['articleTag'] = articleTag

	#原文地址
	dictionary['url'] = articleUrl

	return dictionary

#Test
#print(getArticleAll('http://mp.weixin.qq.com/s?__biz=MjM5OTQ2NjU4NQ==&mid=211364691&idx=3&sn=daa86d7ea6527069b235317e59fdf06c&3rd=MzA3MDU4NTYzMw==&scene=6#rd'))