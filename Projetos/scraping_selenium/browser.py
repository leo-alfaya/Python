from selenium import webdriver

class Browser:
	def create(browser):
		if browser == "Firefox":
			return webdriver.Firefox()
		elif browser == "Phantom":
			return webdriver.PhantomJS()

def getFirefox():
		firefox = Browser.create("Firefox")
		firefox.maximize_window()
		return firefox	

def getPhantom():
		phantom = Browser.create("Phantom")
		return phantom