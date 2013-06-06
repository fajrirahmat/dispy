def getFeed(url):
	import feedparser
	d = feedparser.parse(url)
	return d

if __name__ == '__main__':
	import dispy, random
	cluster = dispy.JobCluster(getFeed,nodes=['10.151.32.*','10.151.38.72'],ip_addr='10.151.32.123')
	links = ['http://if.its.ac.id/feed','http://kbj.if.its.ac.id/feed/','http://ajk.if.its.ac.id/feed/','http://rpl.if.its.ac.id/feed/']
	i = 1
	for url in links:
		job = cluster.submit(url)
		job.id = i
		i = i + 1
		for item in job().entries:
			print item.title +'\n\n'+item.summary+'\n\n\n'
	cluster.stats()
