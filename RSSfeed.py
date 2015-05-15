import feedparser

def readArticle():
	postNum = 0
	feed = feedparser.parse('http://www.cbc.ca/cmlink/rss-canada')
	print (feed['feed']['title'])
	for post in feed.entries:
		print(str(postNum) + ') ' + post.title + ': ' + post.link + '\n')
		postNum += 1


readArticle()