from unittest import TestCase, main
from numbers import Number

def validate_cache(func, cache={}):
	def validate_apply_cache(self, x, y=None):
		chave = False

		if y == None:
			y = cache['value']
			chave = True


		if isinstance(x, Number) and isinstance(y, Number):
			if chave:
				cache['value'] = func(self, y, x)
			else:	
				cache['value'] = func(self, x, y)
			return cache['value']
		else:
			raise Exception('insira somente números:')
	return validate_apply_cache

class Calc:
	@validate_cache
	def soma(self, x, y=None):
		return x + y

	@validate_cache	
	def mul(self, x, y):
		return x * y

	@validate_cache	
	def sub(self, x, y=None):
		return x - y

	@validate_cache
	def div(self, x, y):
		return x / y

	def clear_cache(self):
		self.cache = 0

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
		self.assertEqual(self.calc.sub(3, 2), 1)

	def teste_sub_float(self):
		self.assertEqual(self.calc.sub(3.0, 2.0), 1.0)

	def teste_soma_string(self):
		with self.assertRaises(Exception):
			self.calc.soma('eduardo', 'jaber')

	def teste_sub_string(self):
		with self.assertRaises(Exception):
			self.calc.sub('eduardo', 'jaber')

	def teste_mul(self):
		self.assertEqual(self.calc.mul(3, 3),9)

	def teste_mul_string(self):
		with self.assertRaises(Exception):
			self.calc.mul('eduardo', 'jaber')

	def teste_div(self):
		self.assertEqual(self.calc.div(3, 3),1)

	def teste_div_string(self):
		with self.assertRaises(Exception):
			self.calc.div(3, 'eduardo')

	def teste_soma_cache(self):		
		self.assertEqual(self.calc.soma(self.calc.soma(2, 2)),8)

	def teste_sub_cache(self):
		self.assertEqual(self.calc.sub(self.calc.sub(10, 5)),0)

	def teste_sub_resultado_negativo_mul_cache(self):
		self.assertEqual(self.calc.sub(3, 10), -7)
		self.assertEqual(self.calc.mul(3), -21)

	def teste_sub_resultado_negativo_soma_cache(self):
		self.assertEqual(self.calc.sub(3, 10), -7)
		self.assertEqual(self.calc.soma(3), -4)

	def teste_soma_resultado_positivo_sub_cache(self):
		self.assertEqual(self.calc.soma(1, 1), 2)
		self.assertEqual(self.calc.sub(3), -1)

if __name__ == '__main__':
	main() 