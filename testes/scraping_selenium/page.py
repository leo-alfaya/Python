class Page:
	def __init__(self, browser):
		self.browser = browser	

	def get(self, url):
		self.browser.get(url)

	def find(self, type, element_name):
		if type == "id":
			return self.browser.find_elements_by_id(element_name)
		elif type == "class":
			return self.browser.find_elements_by_class_name(element_name)
		else:
			return self.browser.find_elements_by_name(element_name)

	def fill_input(self, type, element_name, word="None"):
		if type == "id":
			self.browser.find_element_by_id(element_name).send_keys(word)
		elif type == "class":
			self.browser.find_element_by_class_name(element_name).send_keys(word)
		else:
			self.browser.find_element_by_name(element_name).send_keys(word)

	def submit(self, type, element_name):
		if type == "id":
			self.browser.find_element_by_id(element_name).click()
		elif type == "class":
			self.browser.find_element_by_class_name(element_name).click()
		else:
			self.browser.find_element_by_name(element_name).click()