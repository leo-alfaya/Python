from bottle import jinja2_view, route, run, static_file
	
"""
Rotas para arquivos estáticos
"""
@route("/static/css/<filepath:path>", method="GET")
def get_css(filepath):
    return static_file(filepath, root="static/css")

@route("/static/js/<filepath:path>", method="GET")
def get_js(filepath):
    return static_file(filepath, root="static/js")

"""
Rotas para as páginas
"""
@route('/', method='GET')
@jinja2_view('paginas/camera.html')
def render_camera():
	pass	

run(host='0.0.0.0', port=8081, reloader=True, debug=True)