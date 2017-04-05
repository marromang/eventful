# -*- coding: utf-8 -*-
import requests
from lxml import etree

ciudad = raw_input("Introduce una ciudad: ")
tipo = raw_input("Introduce un tipo de evento: ")
key = "JQcrv9s2TtsfKHLG"
payload = {'app_key':key, 'keywords': tipo, 'location':ciudad, 'date':'Future'}

r= requests.get('http://api.eventful.com/rest/events/search', params=payload)

if r.status_code == 200:
	doc = etree.fromstring(r.text.encode('utf-8'))
	for e in doc.xpath("//title"):
		print e.text
else:
	print "Error"