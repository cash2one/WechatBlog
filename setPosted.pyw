#encoding:UTF-8

#将已经发表成功的文章地址写入配置文件。
def setPosted(url):

	#打开文件
	file = open('data/postedArticle.txt', 'a')

	#写入文件
	file.write(url + '\n')

	#关闭文件
	file.close()


#Test
#setPosted("test")
