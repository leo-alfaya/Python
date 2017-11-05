import browser
from page import

packt_pub = Page(browser.getFirefox())

def claim_free_book(packt_pub):
	packt_pub.get('https://www.packtpub.com/packt/offers/free-learning')
	# packt_pub.submit('id', 'free-learning-claim')
	# email = packt_pub.find('id', 'email')
	
	# popup

	# for i in email:
	# 	try:
	# 		i.send_keys('leonardo.alfaya@gmail.com')
	# 	except:
	# 		''

claim_free_book(packt_pub)
