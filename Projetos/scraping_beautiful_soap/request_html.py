import requests
from bs4 import BeautifulSoup as bs

req  = requests.get('https://www.youtube.com/?hl=pt&gl=BR')
page = req.text

youtube = bs(page, 'lxml')