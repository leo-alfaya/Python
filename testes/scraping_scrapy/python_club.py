from scrapy import Request, Spider

class PyJobsSpider(Spider):
	name = "python_club"    

	def start_requests(self):
		urls = [
			'http://pythonclub.com.br/',
			'http://pythonclub.com.br/index2.html',
			'http://pythonclub.com.br/index3.html',
			'http://pythonclub.com.br/index4.html',
			'http://pythonclub.com.br/index5.html',
			'http://pythonclub.com.br/index6.html',
			'http://pythonclub.com.br/index7.html',
			'http://pythonclub.com.br/index8.html',
			'http://pythonclub.com.br/index9.html',
		   ]

		for url in urls:			
			yield Request(url=url, callback=self.parse)

	def parse(self, response):		
		field = getattr(self, 'field', None)
		element = getattr(self, 'element', None)

		posts = response.css(".posts .post")
		
		for post in posts:
			yield {
				field: post.css(element).extract()
			}
			
"""
Example of usage:
	scrapy runspider python_club.py -a field="title" -a element="p > a .pute-button" -L ERROR -t jl -o -
"""