#encoding:UTF-8

#从配置文件里面读取需要更新的网站地址，并以数组形式返回。
def getSpiderPlan():

	#数组
	dictionary = {}

	#读取
	file = open('setting/spiderPlan.txt', 'r')
	while True:
		lines = file.readlines(100000)
		if not lines:
			break

		for line in lines:

			#字符串处理
			lineSplit = line.split('|')
			url = lineSplit[0]
			keyWord = lineSplit[1].replace('\n', '')

			#加入到数组
			dictionary[url] = keyWord

	#释放内存
	file.close()

	#返回结果
	return dictionary

#Test
#print(getSpiderPlan())
