import unittest

import rectangle

class RectangleAreaTestCase(unittest.TestCase):
	def test_area_zero(self):
		res = rectangle.area(10, 0)
		self.assertEqual(res, 0)
	
	def test_square(self):
		res = rectangle.area(10, 10)
		self.assertEqual(res, 100)
	
	def test_negative_side(self):
		res = rectangle.area(-10, 5)
		self.assertIsNone(res)


class RectanglePerimeterTestCase(unittest.TestCase):
	def test_perimeter_zero(self):
		res = rectangle.perimeter(0, 0)
		self.assertEqual(res, 0)
	
	def test_one_side_zero(self):
		res = rectangle.perimeter(10, 0)
		self.assertEqual(res, 20)
	
	def test_square(self):
		res = rectangle.perimeter(10, 10)
		self.assertEqual(res, 40)
	
	def test_negative_side(self):
		res = rectangle.perimeter(-6, 4)
		self.assertIsNone(res)