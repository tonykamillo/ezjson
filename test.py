#!/usr/bin/env python
#-*- coding:utf-8 -*-

import ezjson as json, datetime

class LoremIpsum(object):	
	pass
		
class Page(object):	
	
	def __init__(self, title, text=None, tags=[]):
		self.title = title
		self.text = text
		self.tags = tags
		self.published = False
		self.date_published = None


if __name__ == '__main__':	
	lorem = LoremIpsum()
	lorem.paragraph1 = 'Phasellus nascetur urna rhoncus nisi et. Dignissim turpis tempor et, in, vel mattis'
	lorem.paragraph2 = 'Eros urna lectus, magna cum! Turpis risus turient nunc. Tristique dis? In a facilisis' 

	relpage1 = Page('Some page')
	relpage2 = Page('Another some page')

	page = Page('Master page', lorem, ['#tag1', '#tag2', '#tag3', '#tag4', '#tag5'])
	
	print
	print('################### ezjson test ###################')
	print
	print('         ######## JSON Encoding ########           ')
	print
	print(json.dump(page))
	print
	page.related_pages = (relpage1, relpage2)
	page.published = True
	page.date_published = datetime.datetime.now()
	print(json.dump(page, max_depth=2))
	print
	print
	print('         ######## JSON Decoding ########           ')
	print
	_json = json.dump(page, max_depth=2)
	print('             ####### as dict #######               ')
	print
	print( dir(json.load(_json)) )
	print
	print('            ####### as object #######              ')
	print
	print( dir(json.load(_json, True)) )
	

