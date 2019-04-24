__author__ = "Bernardet, Coruzzi, Laik, Montfort, Rouby, Trouyet"
__filename__ = "class_point"

from math import sqrt, degrees, acos
import numpy as np


class Point:

    def __init__(self, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee

    def getAbscisse(self):
        """ None --> float """
        return self.abscisse

    def getOrdonnee(self):
        """ None --> float """
        return self.ordonnee

    def setAbscisse(self, value):
        """ float --> None """
        assert isinstance(value, float)
        self.abscisse = value

    def setOrdonnee(self, value):
        """ float --> None """
        assert isinstance(value, float)
        self.ordonnee = value

    def __eq__(self, other):
        """ Point --> Bool """
        assert isinstance(other, Point)
        return self.getAbscisse() == other.getAbscisse() and self.getOrdonnee() == other.getOrdonnee()

    def milieu(self, other):
        """ Point --> Point
         Donne le milieu du segment [self, other] """
        assert isinstance(other, Point)
        x = (self.getAbscisse() + other.getAbscisse())/2
        y = (self.getOrdonnee() + other.getOrdonnee())/2
        return Point(x, y)

    def distance(self, other):
        """ Point, Point --> float
         Renvoie la distance entre deux points """
        assert isinstance(other, Point)
        return sqrt((self.getAbscisse()-other.getAbscisse())**2+(self.getOrdonnee()-other.getOrdonnee())**2)

    def appart_segment(self, segment):
        """ Point, [Point, Point] --> Bool
         Renvoie True si self appartient a droite, False sinon
         Un segment est represente par une liste de 2 points"""
        assert isinstance(segment, list)
        assert len(segment) == 2
        assert isinstance(segment[0], Point)
        assert isinstance(segment[1], Point)
        return self.distance(segment[0]) + self.distance(segment[1]) == segment[0].distance(segment[1])

    def proche_sommet(self, liste):
        """ Point, list -> Point
         liste = liste de points
         Renvoie le point de liste qui est le plus proche de self """
        assert isinstance(liste, list)
        assert isinstance(liste[0], Point)
        mini = self.distance(liste[0])
        ind = 0
        for j in range(len(liste)):
            if self.distance(liste[j]) < mini:
                mini = self.distance(liste[j])
                ind = j
        return liste[ind]

    def angle(self, Point2, Point3):
        """ Point, Point, Point --> float
         Prend en entrée trois points réprésentant deux vecteurs partageant
         un même point, self, et retourne la valeur en degré de l'angle entre les deux"""
        assert isinstance(Point2, Point)
        assert isinstance(Point3, Point)

        x1 = self.getAbscisse()
        y1 = self.getOrdonnee()

        x2 = Point2.getAbscisse()
        y2 = Point2.getOrdonnee()

        x3 = Point3.getAbscisse()
        y3 = Point3.getOrdonnee()

        u = np.array([x2 - x1, y2 - y1])
        v = np.array([x3 - x1, y3 - y1])

        prod_scal = np.dot(u, v)
        norme1 = self.distance(Point2)
        norme2 = self.distance(Point3)

        angle = degrees(acos(prod_scal / (norme1 * norme2)))
        if x2 * y3 - x3 * y2 > 0:
            angle = -angle

        return angle
