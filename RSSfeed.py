import feedparser, requests, urllib2
from bs4 import BeautifulSoup

def readArticle():
	postNum = 0
	feed = feedparser.parse('http://www.cbc.ca/cmlink/rss-canada')
	print (feed['feed']['title'])
	for post in feed.entries:
		print(str(postNum) + ') ' + post.title + ':' + post.link + '\n')
		postNum += 1
	whichArticle = eval(input('Based on the above links, what article number would you like to view: '))
	article = feed.entries[whichArticle] 
	link = article['link']
	html = urllib2.urlopen(link).read()
	soup = BeatifulSoup(html)
	text = soup.findAll(text=True)
	print(text)



readArticle()