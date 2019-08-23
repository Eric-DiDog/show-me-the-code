import re
import os
from bs4 import BeautifulSoup

def get_mainText(html):
	soup=BeautifulSoup(html,'html.parser')
	article=soup.find_all(attrs={'class':'read-section jsChapterWrapper'})[0].text
	return article

def get_title(html):
	soup=BeautifulSoup(html,'html.parser')
	title=soup.title.text
	return title

if __name__ == '__main__':
	with open('html.txt','rb') as f:
		html=f.read().decode('utf-8')
	print(get_title(html))
	print(get_mainText(html))


# import requests
# from bs4 import BeautifulSoup
# def search_body_urls(path):
#     #path = 'http://mil.news.sina.com.cn/china/2017-04-05/doc-ifycwymx3854291.shtml'
#     page = requests.get(path)
#     page.encoding = 'utf-8'
#     soup = BeautifulSoup(str(page.text),'html.parser')
#     article = soup.select('.content')[0].text
#     urls = soup.findAll('a')
#     for u in urls:
#          print(u['href'])
#     print(article)

# if __name__ == '__main__':
#     search_body_urls(path='http://mil.news.sina.com.cn/china/2017-04-05/doc-ifycwymx3854291.shtml')
