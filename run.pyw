#encoding:UTF-8

#引用模块
import getSpiderPlan
import getAccount
import getArticleLinkCollection
import checkPosted
import getArticleAll
import articlePost
import setPosted

from apscheduler.schedulers.background import BackgroundScheduler

#获取采集计划，即不同网站的不同关键词
spiderPlan = getSpiderPlan.getSpiderPlan()
print(spiderPlan)

for (key, value) in spiderPlan.items():

	#根据不同网站获取后台账号密码
	account = getAccount.getAccount(key)
	print(account)

	#如果获取到了账号密码
	if(account != 'false'):

		#设置网站地址，用户名，密码
		url = key + 'xmlrpc.php'
		userName = account['userName']
		passWord = account['passWord']

		#根据关键词获取文章地址列表
		linkCollection = getArticleLinkCollection.getArticleLinkCollection(value)

		for link in linkCollection:

			#根据地址判断文章是否发表过
			check = checkPosted.checkPosted(link)

			#未发表
			if(check == 'noPosted'):

				#获取文章所有相关内容
				dictionary = getArticleAll.getArticleAll(link)

				#发表文章并记录
				postId = articlePost.articlePost(url, userName, passWord, dictionary)

				if(int(postId) > 0):

					setPosted.setPosted(link)
					print(dictionary['title'] + '\n')

				break
