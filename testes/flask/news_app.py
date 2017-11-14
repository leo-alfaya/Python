from flask import Flask, request, url_for

from db import noticias

app = Flask("flask")

base_html = u"""
	<html>
	<head>
		<title>{title}</title>
	</head>
	<body>
		{body}
	</body>
	</html>
"""

@app.route("/noticias/cadastro", methods=["GET", "POST"])
def cadastro():
	if request.method == "POST":
		dados_do_formulario = request.form.to_dict()
		#nova_noticia = noticias.insert(dados_do_formulario)
		return u"""
			<h1>Notícia id {} inserida com sucesso!</h1>
			<a href="{}"> Inserir nova notícia </a>
		""".format(nova_noticia, url_for('cadastro'));
	else:
		formulario = u"""
			<form method="post" action="/noticias/cadastro">
			   <label>Titulo:<br />
					<input type="text" name="titulo" id="titulo" />
			   </label>
			   <br />
			   <label>Texto:<br />
					<textarea name="texto" id="texto"></textarea>
			   </label>
			   <input type="submit" value="Postar" />
		   </form>
		"""
		return base_html.format(title=u"Inserir nova noticia", body=formulario)

if __name__ == "__main__":
	app.run(debug=True, use_reloader=True)