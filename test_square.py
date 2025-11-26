import unittest

import square

class SquareAreaTestCase(unittest.TestCase):
	def test_zero_area(self):
		res = square.area(0)
		self.assertEqual(res, 0)
	
	def test_one_area(self):
		res = square.area(1)
		self.assertEqual(res, 1)
	
	def test_float_area(self):
		res = square.area(2.5)
		self.assertEqual(res, 6.25)
	
	def test_big_area(self):
		res = square.area(100)
		self.assertEqual(res, 10000)

class SquarePerimeterTestCase(unittest.TestCase):
	def test_side_zero(self):
		res = square.perimeter(0)
		self.assertEqual(res, 0)
	
	def test_side_one(self):
		res = square.perimeter(1)
		self.assertEqual(res, 4)
	
	def test_side_float(self):
		res = square.perimeter(0.25)
		self.assertEqual(res, 1)
	
	def test_side_big(self):
		res = square.perimeter(1000)
		self.assertEqual(res, 4000)