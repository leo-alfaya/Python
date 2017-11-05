import browser
import page

def yetz():
	firefox = browser.getFirefox()
	yetz = page.Page(firefox, "http://172.20.156.202/yetz-novo/view/login/index.php")	
	yetz.navigate()
	return yetz

def verificaLoginYetz(yetz):
	yetz.submit("class", "btn-minha-area")
	yetz.fill_input("id", "chave-cliente", "teste")
	yetz.submit("id", "btn-buscar-chave")
	yetz.fill_input("id", "cpf-primeiro-acesso", "11111111111")
	yetz.submit("id", "btn-verificar-cadastro")
	yetz.fill_input("name", "senha", "1234")
	yetz.submit("id", "btn-entrar")

