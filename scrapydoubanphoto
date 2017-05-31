#!/usr/bin/env python3
#-*- coding:utf-8 -*-
'''
爬豆瓣相册
需要导入的模块： os urllib.request bs4.BeautifulSoup re
------------------------------------------------------------
1创建request 包括url headers
2url管理  root_url一开始访问的根url new_urls新的url crawed——urls记录已爬过的url
3destFile 处理图片保存名字
4destLink 豆瓣图片一般是压缩过的，重定向到高清大图链接
'''
import os
import urllib.request
from bs4 import BeautifulSoup
import re
#visit url 
root_url = "https://www.douban.com/people/142796332/photos"
webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'} 

#urls management
new_urls = set()
crawed_urls = set()
#dir 放照片的文件夹路径
targetDir = r'C://Users/naganohabara/documents/PythonWorkData/py/scrapy/test'
#
new_urls.add(root_url)#添加待爬取的起始url
#
def destFile(path):
	'''
	return a path in targetDir
	'''

	if not os.path.isdir(targetDir):
		os.mkdir(targetDir)
	pos = path.rindex('/')
	t = targetDir+'/'+path[pos+1:]
	return t
#----------------------------------------------------------------------------------------
str1=re.compile(r'https://img3.doubanio.com/view/photo/(lphoto)|(thumb)|(albumcover)|(lthumb)/public/p[\d]{6,20}.jpg')
#--------------------------------------------------------------------------------------------
def destLink(link):
	'''
	在函数外编译re str1以免每次调用函数都编译
	切换到高清大图链接
	'''
	s1 = re.search(str1,link)
	
	if s1:
		print('match')
		snum = re.search(r'[\d]{6,20}',link)
		s='https://img3.doubanio.com/view/photo/large/public/p'+snum.group()+'.jpg'
		print('reurl:%s'%s)
		return s
	return link

urls_count = 1
while len(new_urls) != 0:
		new_url = new_urls.pop()
		crawed_urls.add(new_url)
		print ('begin %s'%new_url)
		req = urllib.request.Request(url = new_url,headers = webheaders)
		try:
			response = urllib.request.urlopen(req)
			if response.getcode() == 200:
				contentBytes = response.read()
				soup = BeautifulSoup(contentBytes, 'html.parser', from_encoding='utf-8')
				contentBytesDecode = contentBytes.decode('utf-8')
				urls = soup.find_all('a', href=re.compile(r"https://www.douban.com/photos/album/\d*/\?start=\d+$"))
				urls += soup.find_all('a', href=re.compile(r'https://www.douban.com/photos/album/\d*'))
				print('end research urls')

				for url in urls:
					#print (url['href'])
					if url['href'] not in new_urls and url['href'] not in crawed_urls:
						print(url['href'])
						new_urls.add(url['href'])

				cinfo = re.findall(r'(https:[^s]*?(jpg|png|gif))',str(contentBytesDecode))
				
				for link,t in set(cinfo):
					print(link)
					try:						
						urllib.request.urlretrieve(destLink(link),destFile(link))
					except:
						print('failed')
				
				print ('end %s'%new_url)
				urls_count+=1
				if urls_count>100:
					#爬到累了
					break
		except urllib.request.URLError as e:
			print(e)
