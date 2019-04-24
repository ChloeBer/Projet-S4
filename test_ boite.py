

import unittest
from class_boite import *
from copy import deepcopy


class testBoite(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(-1.0, 1.0)
        self.point2 = Point(1.0, 1.0)
        self.point3 = Point(1.0, -1.0)
        self.point4 = Point(-1.0, -1.0)
        self.pointO = Point(0.0, 0.0)
        self.point12 = Point(0.0, 1.0)
        self.point23 = Point(1.0, 0.0)
        self.point34 = Point(0.0, -1.0)
        self.point41 = Point(-1.0, 0.0)

        self.boite1234 = Boite([point1, point2, point3, point4])
        self.boiteA = Boite([self.point1, self.point12, self.pointO, self.point41])
        self.boiteB = Boite([self.point12, self.point2, self.point23, self.pointO])
        self.boiteC = Boite([self.pointO, self.point23, self.point3, self.point34])
        self.boiteD = Boite([self.point41, self.pointO, self.point34, self.point4])

    def testGetSommets(self):
        boite = deepcopy(self.boite1234)
        value = boite.getSommets()
        expected = [point1, point2, point3, point4]
        self.assertTrue(value == expected)

    def testTrySetSommetsNotList(self):
        boite = deepcopy(self.boite1234)
        try:
            boite.setSommets('Baston !')
        except:
            self.assertRaises(AssertionError)

    def testTrySetSommetsListNotPoints(self):
        boite = deepcopy(self.boite1234)
        try:
            boite.setSommets(['Baston', 'Tagazoc', 'Autre'])
        except:
            self.assertRaises(AssertionError)

    def testSetSommets(self):
        boite = deepcopy(self.boite1234)
        boite.setSommets([self.point4, self.point3, self.point2, self.point1])
        value = boite.getSommets
        expected = [self.point4, self.point3, self.point2, self.point1]
        self.assertTrue(value == expected)

    def testEqNotBoite(self):
        boite = deepcopy(self.boite1234)
        try:
            boite == 'Baston !'
        except:
            self.assertRaises(AssertionError)

    def testEq(self):
        boite = deepcopy(self.boite1234)
        expected = self.boite1234
        self.assertTrue(boite == expected)

    def testDecoupe(self):
        boite = deepcopy(self.boite1234)
        value = boite.decoupe()
        expected = [self.boiteA, self.boiteB, self.boiteC, self.boiteD]
        self.assertTrue(value == expected)

    def testDimension(self):
        boite = deepcopy(self.boite1234)
        value = boite.dimension()
        expected = [2,2]
        self.assertTrue(value == expected)
