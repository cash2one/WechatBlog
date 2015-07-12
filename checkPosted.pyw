#encoding:UTF-8
import re

#从配置文件里面读取已经发表过的文章ID，并以数组形式返回。
def checkPosted(targetUrl):

	#正则匹配获取文章MID
	m = re.match(r'(.*)mid=(\d*)(.*)', targetUrl)
	targetId = m.group(2)

	#读取
	file = open('data/postedArticle.txt', 'r')
	while True:
		lines = file.readlines(100000)
		if not lines:
			break

		#判断是否已发表
		for line in lines:

			#根据文章ID判断
			if targetId in line:
				file.close()
				return  'posted'

	file.close()
	return 'noPosted'

#Test
#print(checkPosted('http://mp.weixin.qq.com/s?__biz=MzAwNTE4MzQyMQ==&mid=213054266&idx=8&sn=ca1a634aac5b9b4e5e492d7ac3825660&3rd=MzA3MDU4NTYzMw==&scene=6#rd'))
