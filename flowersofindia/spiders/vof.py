# -*- coding: utf-8 -*-
import scrapy

class VofSpider(scrapy.Spider):
    name = "vof"
    allowed_domains = ["flowersofindia.net"]

    def start_requests(self):
	urls = [
		'http://www.flowersofindia.net/catalog/vof-frame.html',
		'http://www.flowersofindia.net/catalog/vof-frame2.html',
		'http://www.flowersofindia.net/catalog/vof-frame3.html',
		'http://www.flowersofindia.net/catalog/vof-frame4.html',
		'http://www.flowersofindia.net/catalog/vof-frame5.html',
		'http://www.flowersofindia.net/catalog/vof-frame6.html',
		'http://www.flowersofindia.net/catalog/vof-frame7.html',
		'http://www.flowersofindia.net/catalog/vof-frame8.html',
		'http://www.flowersofindia.net/catalog/vof-frame9.html',
		'http://www.flowersofindia.net/catalog/vof-frame10.html',
		'http://www.flowersofindia.net/catalog/vof-frame11.html',
	]
	for url in urls:
		yield scrapy.Request(url = url, callback = self.parse_pages)

    def parse_pages(self, response):
	for link in response.selector.xpath('//table')[3].xpath('//a[@target="slide"]').xpath('@href').extract():
		yield scrapy.Request(url = 'http://www.flowersofindia.net/catalog/' + link, callback = self.parse_inner_pages)

    def parse_inner_pages(self, response):
	yield {
		'Common name': response.selector.xpath('//table[@class="rubber"]').xpath('//td[@id="maintext"]').xpath('//div[@id="title"]/text()').extract(),
		'Botanical Name': response.selector.xpath('//table[@class="rubber"]').xpath('//td[@id="maintext"]').xpath('//div[@id="botname"]/span[@id="genus"][1]/text()').extract(),
		'Family': response.selector.xpath('//table[@class="rubber"]').xpath('//td[@id="maintext"]').xpath('//div[@id="botname"]/span[@id="genus"][2]/text()').extract(),
		'Description': response.selector.xpath('//table[@class="rubber"]').xpath('//td[@id="maintext"]').xpath('//div[@id="descr"]/text()').extract(), 
		'image_urls': ['http://www.flowersofindia.net/catalog/slides/' + response.selector.xpath('//img[@class="rubber"]').xpath('@src').extract_first()] }

