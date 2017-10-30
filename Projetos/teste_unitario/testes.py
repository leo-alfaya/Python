from unittest import TestCase, main

class Calc:
	def soma(self, x, y):
		return x + y

	def sub(self, x, y):
		return x - y

class Testes_calculadora(TestCase):
	def setUp(self):
		self.calc = Calc()

	def teste_soma(self):
		self.assertEqual(self.calc.soma(2, 2), 4)

	def teste_soma_neg(self):
		self.assertEqual(self.calc.soma(-2, -3), -5)

	def teste_soma_float(self):
		self.assertEqual(self.calc.soma(2.0, 1.0), 3.0)

	def teste_sub(self):
		self.assertEqual(self.calc.sub(2, 2), 0)

	def teste_sub_float(self):
		self.assertEqual(self.calc.sub(2.0, 2.0), 0)

	def teste_soma_string(self):
		self.assertEqual(self.calc.soma('eduardo', 'jaber'), 0)

if __name__ == '__main__':
	main()