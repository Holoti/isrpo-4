import math
import unittest

import circle

class CircleAreaTestCase(unittest.TestCase):
	def test_radius_zero(self):
		res = circle.area(0)
		self.assertEqual(res, 0)
	
	def test_radius_one(self):
		res = circle.area(1)
		self.assertEqual(res, math.pi)
	
	def test_area_one(self):
		res = circle.area(1 / math.pi ** 0.5)
		self.assertAlmostEqual(res, 1)
	
	def test_radius_negative(self):
		res = circle.area(-1)
		self.assertIsNone(res)


class CirclePerimeterTestCase(unittest.TestCase):
	def test_radius_zero(self):
		res = circle.perimeter(0)
		self.assertEqual(res, 0)
	
	def test_radius_one(self):
		res = circle.perimeter(1)
		self.assertEqual(res, 2 * math.pi)
	
	def test_perimeter_one(self):
		res = circle.perimeter(1 / (2 * math.pi))
		self.assertEqual(res, 1)
	
	def test_radius_negative(self):
		res = circle.perimeter(-1)
		self.assertIsNone(res)