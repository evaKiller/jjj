import urllib2
import urllib
import os
from BeautifulSoup import BeautifulSoup
def getAllImageLink():
	html = urllib2.urlopen('https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&hs=3&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A4%9A%E8%82%89%E6%A4%8D%E7%89%A9&f=3&oq=duorou&rsp=1').read()
	soup = BeautifulSoup(html);
	liResult = soup.findAll('div',{'id':'wrapper'}).findAll('div',{'id':'imgContainer'});
	print "find result";
	print liResult;
	
	count = 0;
	for image in liResult:
		count += 1
		link = image.get('data-thumburl');
		imageName = count
		filesavepath = '/home/cdyf/my/mypython/%s.jpg' % imageName
		urllib.urlretrieve(link,filesavepath)
       		print filesavepath
if __name__ == '__main__':
    getAllImageLink()
