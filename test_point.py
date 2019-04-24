

import unittest
from class_point import *
from copy import deepcopy


class testPoint(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(-1.0, 1.0)
        self.point2 = Point(1.0, 1.0)
        self.point3 = Point(1.0, -1.0)
        self.point4 = Point(-1.0, -1.0)
        self.point5 = Point(0.0, 0.0)

    def testGetAbscisse(self):
        point = deepcopy(self.point1)
        value = point.getAbscisse()
        expected = -1.0
        self.assertTrue(value == expected)

    def testGetOrdonnee(self):
        point = deepcopy(self.point1)
        value = point.getOrdonnee()
        expected = 1.0
        self.assertTrue(value == expected)

    def testTrySetAbscisseStr(self):
        point = deepcopy(self.point1)
        try:
            point.setAbscisse('Tagazoc !')
        except:
            self.assertRaises(AssertionError)

    def testSetAbscisse(self):
        point = deepcopy(self.point1)
        point.setAbscisse(1.0)
        value = point.getAbscisse()
        expected = 1.0
        self.assertTrue(value == expected)

    def testTrySetOrdonneeStr(self):
        point = deepcopy(self.point1)
        try:
            point.setOrdonnee('Baston !')
        except:
            self.assertRaises(AssertionError)

    def testTryEqNotPoint(self):
        point = deepcopy(self.point1)
        other = 'Tagazoc !'
        try:
            point == other
        except:
            self.assertRaises(AssertionError)

    def testEq(self):
        point1 = deepcopy(self.point1)
        point2 = deepcopy(self.point1)
        self.assertTrue(point1 == point2)

    def testNotEq(self):
        point1 = deepcopy(self.point1)
        point2 = deepcopy(self.point2)
        self.assertFalse(point1 == point2)

    def testMilieu(self):
        point1 = deepcopy(self.point2)
        point2 = deepcopy(self.point4)
        value = point1.milieu(point2)
        expected = self.point5
        self.assertTrue(value == expected)
