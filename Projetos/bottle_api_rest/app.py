"""
Loja de Cds.
"""

from bottle import Bottle, request, response
from json import dumps
from core import search_all_artists, insert_artist, insert_album

app = Bottle()

@app.get('/')
def index_map():
	"""
	Retornar um mapa completo da API.
	"""
	return dumps({"artistas": "url/artistas",
				  "albuns": "url/albuns"})

@app.get('/artistas')
def artists_map():
	"""
	Retornar todos os artistas.
	"""
	return search_all_artists()

@app.post('/artistas')
def post_artist():
	"""
	Insere um artista na API.

	Formato do input.
	Content-Type: application/json
	{"nome": "Zimbra"}
	"""
	artista = request.json
	response.headers['Content-Type'] = 'application/json'

	if not artista:
		response.status = 400
		return {response.status:artista}

	if insert_artist(artista['nome'].lower()):
		response.status = 201 #Created
	else:
		response.status = 409 #Conflict

	return dumps({response.status: artista})

@app.post('/album')
def post_album():
	"""
	Insere um album na API.

	Formato do input.
	Content-Type: application/json
	{"nome": "Zimbra"}
	"""
	album = request.json
	response.headers['Content-Type'] = 'application/json'

	if not album:
		response.status = 400
		return {response.status:album}

	if insert_album(album['nome'].lower()):
		response.status = 201 #Created
	else:
		response.status = 409 #Conflict

	return dumps({response.status: album})

if __name__ == '__main__':
	app.run(port=8081)