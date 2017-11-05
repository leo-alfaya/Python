from bottle import jinja2_view, route, run, request, response, static_file

links = ['Home', 'About', 'Help']

"""
Rotas para arquivos estáticos
"""
@route("/static/css/<filepath:path>", method="GET")
def css(filepath):
    return static_file(filepath, root="static/css")

"""
Rotas para as páginas
"""
@route('/', method='GET')
@jinja2_view('paginas/login.html')
def form_login():
	if request.get_cookie('logado') == 'true':
		username = request.get_cookie('username')
		return dict(links=links, logado=True, username=username)
	return dict(links=links, logado=False)

@route('/user', method='POST')
@jinja2_view('paginas/login.html')
def form_login_post():
	username = request.forms.get("username")
	password = request.forms.get("password")

	if username == "Leonardo" and password == "1234":
		response.set_cookie('logado', 'true')
		response.set_cookie('username', 'Leonardo')
		return dict(links=links, username=username, logado=True)
	return dict(links=links, logado=False)

@route('/logout', method='GET')
@jinja2_view('paginas/login.html')
def form_login_post():	
	response.set_cookie('logado','')		
	return dict(links=links, logado=False)


@route('/<area>', method="GET")
@jinja2_view('paginas/not_found.html')
def not_found(area):
	return dict(links=links, nome=area)

run(port=8081, reloader=True, debug=True)