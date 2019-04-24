__author__ = "Bernardet, Coruzzi, Laik, Montfort, Rouby, Trouyet"
__filename__ = "test_pile"

from pile import *
import unittest
from copy import *


class PileTest(unittest.TestCase):
    def setUp(self):
        # Listes
        self.liste1 = [1]
        self.liste2 = [1, 2]
        self.liste3 = [1, 2, 3]
        self.liste4 = [1, 2, 3, 4]

        # Piles
        self.pileempty = Pile([])
        self.pile1 = Pile(copy(self.liste1))
        self.pile2 = Pile(copy(self.liste2))
        self.pile3 = Pile(copy(self.liste3))
        self.pile4 = Pile(copy(self.liste4))

    def testGetListe(self):
        pile = copy(self.pile1)
        value = pile.getListe()
        expected = copy(self.liste1)
        self.assertEqual(value, expected)

    def testSetListe(self):
        pile = copy(self.pile1)
        pile.setListe(copy(self.liste2))
        value = pile.getListe()
        expected = copy(self.liste2)
        self.assertEqual(value, expected)

    def testSetListeErrorListNotList(self):
        pile = copy(self.pile1)
        try:
            value = pile.setListe("1, 2, 3")
        except:
            self.assertRaises(AssertionError)

    def testIsEmpty(self):
        pile = copy(self.pileempty)
        value = pile.isEmpty()
        self.assertTrue(value)

    def testIsNotEmpty(self):
        pile = copy(self.pile1)
        value = pile.isEmpty()
        self.assertFalse(value)

    def testEmpiler(self):
        pile = copy(self.pile1)
        pile.empiler(2)
        value = pile.getListe()
        expected = copy(self.liste2)
        self.assertEqual(value, expected)

    def testDepiler(self):
        pile = copy(self.pile4)
        value_haut = pile.depiler()
        expected_haut = copy(self.liste4[-1])
        value_list = pile.getListe()
        expected_list = copy(self.liste3)
        self.assertEqual(value_haut, expected_haut)
        self.assertEqual(value_list, expected_list)

    def testDepilerErrorPileIsEmpty(self):
        pile = copy(self.pileempty)
        try:
            value = pile.depiler()
        except:
            self.assertRaises(AssertionError)

    def testHaut(self):
        pile = copy(self.pile4)
        value = pile.haut()
        expected = copy(self.liste4[-1])
        self.assertEqual(value, expected)

    def testHautErrorPileIsEmpty(self):
        pile = copy(self.pileempty)
        try:
            value = pile.haut()
        except:
            self.assertRaises(AssertionError)

    def testRetirer(self):
        pile = copy(self.pile4)
        pile.retirer(3)
        value = pile.getListe()
        expected = [1, 2, 4]
        self.assertEqual(value, expected)

    def testRetirerErrorElementNotInPile(self):
        pile = copy(self.pile3)
        try:
            value = pile.retirer(4)
        except:
            self.assertRaises(AssertionError)

    def testPosition(self):
        pile = copy(self.pile4)
        value = pile.position(3)
        expected = 2
        self.assertEqual(value, expected)

    def testPositionErrorElementNotInPile(self):
        pile = copy(self.pile3)
        try:
            value = pile.position(4)
        except:
            self.assertRaises(AssertionError)
