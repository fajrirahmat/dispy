import sys
def getFeed(code):
	from suds.client import Client
	import urllib2
	url = 'http://www.webservicex.net/CurrencyConvertor.asmx?WSDL'
	p = dict(http='http://fajri@its.ac.id:j4ckth3r1p@proxy.its.ac.id:8080')
	client = Client(url, proxy=p)
	return client.service.ConversionRate(code,'IDR')


if __name__ == '__main__':
	import dispy, random
	cluster = dispy.JobCluster(getFeed,nodes=['10.151.32.*','10.151.38.72'],ip_addr='10.151.32.123')
	codes = ['USD','KRW','JPY','AFA','CNY','EUR','MYR']
	i = 1
	for code in codes:
		job = cluster.submit(code)
		job.id = i
		i = i + 1
		print 'Konversi dari '+code+' ke IDR = '+str(job())+' rupiah'
	cluster.stats()
