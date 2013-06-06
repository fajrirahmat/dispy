import sys
import xml.etree.ElementTree as ET
def getFeed(code):
	from suds.client import Client
	import urllib2
	url = 'http://www.webservicex.net/stockquote.asmx?WSDL'
	p = dict(http='http://fajri@its.ac.id:j4ckth3r1p@proxy.its.ac.id:8080')
	client = Client(url, proxy=p)
	result = '<?xml version="1.0"?>\n' + client.service.GetQuote(code)
	return result


if __name__ == '__main__':
	import dispy, random
	cluster = dispy.JobCluster(getFeed,nodes=['10.151.32.*','10.151.38.72'],ip_addr='10.151.32.123')
	codes = ['TLK','INDFY']
	i = 1
	for code in codes:
		job = cluster.submit(code)
		job.id = i
		i = i + 1
		parser = ET.XMLParser(encoding='utf-8')
		data = ET.fromstring(job(),parser = parser)
		for quote in data[0]:
			print quote.tag +"\t\t :"+str(quote.text)
		
		print "\n"
	cluster.stats()
