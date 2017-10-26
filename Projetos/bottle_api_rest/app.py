"""
Loja de Cds.
"""

from bottle import Bottle, request
from json import dumps
from core import search_all_artists

app = Bottle()

@app.get('/')
def index_map():
	"""
	Retornar um mapa completo da API.
	"""
	return dumps({"artistas": "url/artistas",
				  "albuns": "url/albuns"})

@app.get('/artistas')
def artistas_map():
	"""Retornar todos os artistas."""
	return search_all_artists()
@app.post('/artistas'):
def artistas_include
	"""


if __name__ == '__main__':
	app.run(port=8081)