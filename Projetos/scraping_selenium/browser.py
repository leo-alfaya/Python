from selenium import webdriver

def getFirefox():
	"""
	Return Firefox Browser instance.

	Sample usage:
		firefox = getFirefox()
	"""
	firefox = webdriver.Firefox()
	firefox.maximize_window()
	return firefox	

def getPhantom():
	"""
	Return Phantom JS instance.

	Sample usage:
		phantom = getPhantom()
	"""
	return webdriver.PhantomJS()
	