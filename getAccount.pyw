#encoding:UTF-8

#从配置文件里面读取需要更新的网站的账号密码，并以数组形式返回。
def getAccount(targetUrl):

	#读取
	file = open('setting/account.txt', 'r')
	while True:
		lines = file.readlines(100000)
		if not lines:
			break

		for line in lines:

			#字符串处理
			lineSplit = line.split('|')
			url = lineSplit[0]

			if(targetUrl == url):

				#数组
				dictionary = {}

				userName = lineSplit[1]
				passWord = lineSplit[2].replace('\n', '')

				#加入到数组
				dictionary['userName'] = userName
				dictionary['passWord'] = passWord

				#返回结果
				return dictionary

	return 'false'

	#释放内存
	file.close()



#Test
#print(getAccount('http://weixinchoujiang.sinaapp.com/'))
#print(getAccount('http://yishengjiaowo.sinaapp.com/'))
