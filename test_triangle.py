import unittest

import triangle

class TriangleAreaTestCase(unittest.TestCase):
	def test_base_zero(self):
		res = triangle.area(0, 10)
		self.assertEqual(res, 0)
	
	def test_height_zero(self):
		res = triangle.area(5, 0)
		self.assertEqual(res, 0)
	
	def test_area_one(self):
		res = triangle.area(1, 2)
		self.assertEqual(res, 1)
	
	def test_area_float(self):
		res = triangle.area(3, 5)
		self.assertEqual(res, 7.5)
	
	def test_negative_height(self):
		res = triangle.area(-3, 4)
		self.assertIsNone(res)
	
	def test_negative_base(self):
		res = triangle.area(6, -5)
		self.assertIsNone(res)

class TrianglePerimeterTestCase(unittest.TestCase):
	def test_equal_sides(self):
		res = triangle.perimeter(1, 1, 1)
		self.assertEqual(res, 3)
	
	def test_right_triangle(self):
		res = triangle.perimeter(3, 4, 5)
		self.assertEqual(res, 12)
	
	def test_negative_side(self):
		res = triangle.perimeter(-2, -3, 4)
		self.assertIsNone(res)