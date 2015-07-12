#encoding:UTF-8
from wordpress_xmlrpc import Client
from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc.methods import posts

def articlePost(url, username, password, dictionary):

	#设置网站地址，用户名，密码
	client = Client(url, username, password)

        #创建提交对象
	post = WordPressPost()

	#构建提交内容
	post.title = dictionary['title']
	content = dictionary['content'] + "<br>" + "<a href='" + dictionary['url'] + "' target='_blank'>原文地址</a>"
	post.content = content
	post.post_status = 'publish'
	post.terms_names = {
                'post_tag': dictionary['articleTag'],
	       'category': dictionary['articleTag']
	}

	#发表
	post.id = client.call(posts.NewPost(post))

	return  post.id

#Test
#我就不Test
