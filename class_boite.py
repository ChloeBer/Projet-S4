__author__ = "Bernardet, Coruzzi, Laik, Montfort, Rouby, Trouyet"
__filename__ = "class_boite"

from class_point import *


class Boite:
    """ On ne considere ici que des boites rectangulaires ABCD, A étant le point en haut à gauche """
    def __init__(self, liste_sommets):
        self.sommets = liste_sommets

    def getSommets(self):
        return self.sommets

    def setSommets(self, values):
        assert isinstance(values, list)
        for i in values:
            assert isinstance(i, Point)
        self.sommets = values

    def __eq__(self, other):
        assert isinstance(other, Boite)
        return self.sommets == other.sommets

    def decoupe(self):
        """ None --> Liste de 4 boites
         Découpe une boite rectangulaire ABCD, de centre 0 en 4 boites """
        pointA = self.getSommets()[0]
        pointB = self.getSommets()[1]
        pointC = self.getSommets()[2]
        pointD = self.getSommets()[3]
        pointO = pointA.milieu(pointC)
        pointAB = pointA.milieu(pointB)
        pointBC = pointB.milieu(pointC)
        pointCD = pointC.milieu(pointD)
        pointDA = pointD.milieu(pointA)
        boiteA = Boite([pointA, pointAB, pointO, pointDA])
        boiteB = Boite([pointAB, pointB, pointBC, pointO])
        boiteC = Boite([pointO, pointBC, pointC, pointCD])
        boiteD = Boite([pointDA, pointO, pointCD, pointD])
        return [boiteA, boiteB, boiteC, boiteD]

    def dimension(self):
        """ None --> liste (longueur AB, largeur BC) """
        pointA = self.getSommets()[0]
        pointB = self.getSommets()[1]
        pointC = self.getSommets()[2]
        longueur = sqrt((pointB.getAbscisse() - pointA.getAbscisse())**2 + (pointB.getOrdonnee() - pointA.getOrdonnee())**2)
        largeur = sqrt((pointB.getAbscisse() - pointC.getAbscisse())**2 + (pointB.getOrdonnee() - pointC.getOrdonnee())**2)
        return [longueur, largeur]

    def appartenance(self, point):
        """ Boite, Point --> Bool
         Renvoie True si point appartient a self, False sinon"""
        assert isinstance(point, Point)
        x = point.getAbscisse()
        y = point.getOrdonnee()
        if x < self.getSommets()[0].getAbscisse() or \
           x > self.getSommets()[1].getAbscisse() or \
           y < self.getSommets()[0].getOrdonnee() or \
           y > self.getSommets()[2].getOrdonnee():
            return False
        return True

    def adjacence(self, boite):
        """ Boite, Boite --> Bool
         renvoie True si self et boite sont adjacentes, False sinon """
        for i in range(4):
            if self.getSommets()[i % 4].appart_segment([boite.getSommets()[(i + 3) % 4], boite.getSommets()[(i + 2) % 4]]) \
               and self.getSommets()[(i + 1) % 4].appart_segment([boite.getSommets()[(i + 3) % 4], boite.getSommets()[(i + 2) % 4]]):
                return True
            if boite.getSommets()[i % 4].appart_segment([self.getSommets()[(i + 3) % 4], self.getSommets()[(i + 2) % 4]]) \
               and boite.getSommets()[(i + 1) % 4].appart_segment([self.getSommets()[(i + 3) % 4], boite.getSommets()[(i + 2) % 4]]):
                return True
        return False


def boite_deplacement(point, distance):
    """ Point, float --> Boite
     Renvoie une boite de centre point et de longeueur 2*distance """
    assert isinstance(point, Point)
    return Boite([Point(point.getAbscisse() - distance, point.getOrdonnee() - distance),
                  Point(point.getAbscisse() + distance, point.getOrdonnee() - distance),
                  Point(point.getAbscisse() + distance, point.getOrdonnee() + distance),
                  Point(point.getAbscisse() - distance, point.getOrdonnee() + distance)])
