#!/usr/bin/python
# coding:utf-8

import urllib
import urllib2
import re

if __name__ == '__main__':
    url = 'https://www.qiushibaike.com/8hr/page/2/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
	try:
	    request = urllib2.Request(url=url, headers = headers)
	    response = urllib2.urlopen(request)
	    content = response.read()
	except urllib2.HTTPError as e:
		print e
		exit()
	except urllib2.URLError as e:
		print e
		exit() #return 只能用在function里
	#根据抓取的网页源代码提取正则表达式匹配的数据
    pattern = re.complie('<div ')
    items = re.findall(pattern, content)
    for item in items:
    	item_new = item[0].replace('\n','').replace('<br/>','\n')
    	#save data
    	path = 'webdata'
    	if not os.path.exists(path):
    		os.makedirs(path)
    	file_path = path + '/'+item[1]+'..txt'
    	f = open(file_path,'w')
    	f.write(item_new)
    	f.close()
    	
