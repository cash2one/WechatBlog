#encoding:UTF-8
import re

def filterHtml(htmlstr):

	re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I) #匹配CDATA
	re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)#Script
	re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)#style
	re_br = re.compile('<br\s*?/?>')#处理换行
	re_span = re.compile('<span[^>]*>')#去掉span
	re_comment = re.compile('<!--[^>]*-->')#HTML注释

	s = re_cdata.sub('', htmlstr)#去掉CDATA
	s = re_script.sub('', s) #去掉SCRIPT
	s = re_style.sub('', s)#去掉style
	s = re_br.sub('<br>', s)#将br转换为换行
	s = re_span.sub('', s)#去掉span
	s = re_comment.sub('', s)#去掉HTML注释

	re_h = re.compile('</?\w+[^>]*>')#HTML标签
	s = re_h.sub('<br>', s) #去掉HTML 标签

	blank_line = re.compile('(<br>)+')#去掉多余的空行
	s = blank_line.sub('<br>', s)

	#s = replaceCharEntity(s)#替换实体
	return s
