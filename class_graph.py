__author__ = "Bernardet, Coruzzi, Laik, Montfort, Rouby, Trouyet"
__filename__ = "class_graph"

from class_point import *
from class_pile import *
from math import inf
import numpy as np


class Graph:
    """ classe permettant de creer des graphes ponderes mais non orientes
    composes de vertices (liste de sommets) et de edges (liste d'aretes)
    Les sommets et les aretes sont ranges dans l'ordre dans lesquels ils ont ete rentre
    arete = tuple (sommet1, sommet2, poids)
    sommets = entiers
    poids = reel
    On ne peut pas avoir les aretes (sommet1, sommet2, poids) et (sommet2, sommet1, poids) dans un meme graphe
    (memes aretes avec l'ordre des sommets inverses)
    On ne peut pas creer une arete entre/sur un meme sommet (init, setEdges, add_edge)
    On ne peut pas creer des aretes de poids (differents ou egales) entre deux memes sommets (init, setEdges, add_edge)
    """

    def __init__(self, vertices, edges):
        """ cree un graph avec :
         - vertices : liste des sommets (Points) du graphe
         - edges : liste des aretes du graphe
         une arrete est representee par le tuple : (sommet1, sommet2, poids)
         avec sommet1, sommet2 des Points et poids un reel """

        assert isinstance(vertices, list)
        assert isinstance(edges, list)

        # verifie que les sommets sont de la classe Point
        for i in range(len(vertices)):
            assert isinstance(vertices[0], Point)

        # verifie que les arretes sont des tuples composes de 2 Points et 1 reel
        for i in range(len(edges)):
            assert isinstance(edges[i], tuple)
            assert len(edges[i]) == 3
            assert isinstance(edges[i][0], Point)  # sommet1 = Point
            assert isinstance(edges[i][1], Point)  # sommet2 = Point
            assert isinstance(edges[i][2], float)  # poids = reel

            sommet1_i = edges[i][0]
            sommet2_i = edges[i][1]
            poids_i = edges[i][2]

            # verifie que les sommets des aretes sont dans la liste des sommets du graphe
            assert sommet1_i in vertices
            assert sommet2_i in vertices

            # verifie que l'arete n'est pas entre un meme sommet
            assert sommet1_i != sommet2_i

            for j in range(len(edges)):
                if j != i:
                    sommet1_j = edges[j][0]
                    sommet2_j = edges[j][1]
                    poids_j = edges[j][2]
                    # verifie qu'il n'y ait pas 2 fois la meme arete avec sommet1, sommet2 inverses
                    assert (sommet1_i, sommet2_i, poids_i) != (sommet2_j, sommet1_j, poids_j)
                    # verifie qu'il n'y ait pas d'aretes avec les memes sommets mais des poids differents
                    assert (sommet1_i, sommet2_i) != (sommet1_j, sommet2_j)
                    assert (sommet2_i, sommet1_i) != (sommet1_j, sommet2_j)

        self.vertices = vertices
        self.edges = edges

    def getVertices(self):
        """ recupere la liste des sommets du graphes """
        return self.vertices

    def getEdges(self):
        """ recupere la liste des aretes du graphes """
        return self.edges

    def setVertices(self, vertices):
        """ change toute la liste des sommets du graphe par la liste vertices """
        assert isinstance(vertices, list)

        for i in range(len(vertices)):
            assert isinstance(vertices[i], Point)

        self.vertices = vertices

    def setEdges(self, edges):
        """ change toute la liste des aretes du graphe par la liste edges """
        assert isinstance(edges, list)
        # verifie que les arretes sont des tuples composes de 2 Points et 1 reel
        for i in range(len(edges)):
            assert isinstance(edges[i], tuple)
            assert len(edges[i]) == 3
            assert isinstance(edges[i][0], Point)  # sommet1 = Point
            assert isinstance(edges[i][1], Point)  # sommet2 = Point
            assert isinstance(edges[i][2], float)  # poids = reel

            # verifie que les sommets des nouvelles aretes sont dans la liste des sommets du graphe
            assert edges[i][0] in self.getVertices()
            assert edges[i][1] in self.getVertices()

            # verifie que l'arete n'est pas entre un meme sommet
            assert edges[i][0] != edges[i][1]

            sommet1_i = edges[i][0]
            sommet2_i = edges[i][1]
            poids_i = edges[i][2]

            for j in range(len(edges)):
                if j != i:
                    sommet1_j = edges[j][0]
                    sommet2_j = edges[j][1]
                    poids_j = edges[j][2]
                    # verifie qu'il n'y ait pas 2 fois la meme arete avec sommet1, sommet2 inverses
                    assert (sommet1_i, sommet2_i, poids_i) != (sommet2_j, sommet1_j, poids_j)
                    # verifie qu'il n'y ait pas d'aretes avec les memes sommets mais des poids differents
                    assert (sommet1_i, sommet2_i) != (sommet1_j, sommet2_j)
                    assert (sommet2_i, sommet1_i) != (sommet1_j, sommet2_j)

        self.edges = edges

    def add_vertex(self, vertex):
        """ ajoute UN sommet (Point) a la liste des sommets du graphe s'il n'y etait pas """
        assert isinstance(vertex, Point)
        # ajout de vertex a vertices si pas present
        if vertex not in self.getVertices():
            self.getVertices().append(vertex)

    def add_edge(self, sommet1, sommet2, poids):
        """ ajoute UNE arete (sommet1, sommet2, poids) a la liste des aretes du graphe si elle n'y etait pas
        ou s'il n'y a pas une autre arete entre sommet1 et sommet2
        sommet1, sommet2 des Points et poids reel
        si sommet1, sommet2 ne sont pas dans la liste des sommets du graphe, ils sont ajoutes a la liste """

        assert isinstance(sommet1, Point)  # sommet1 = Point
        assert isinstance(sommet2, Point)  # sommet2 = Point
        assert isinstance(poids, float)  # poids = reel
        # verifie que l'arete n'est pas entre un meme sommet
        assert sommet1 != sommet2

        for j in range(len(self.getEdges())):
                sommet1_j = self.getEdges()[j][0]
                sommet2_j = self.getEdges()[j][1]
                # verifie qu'il n'y ait pas d'aretes avec les memes sommets mais des poids differents ou egaux
                assert (sommet1, sommet2) != (sommet1_j, sommet2_j)
                assert (sommet2, sommet1) != (sommet1_j, sommet2_j)

        # ajout sommet1, sommet2 dans liste vertices si pas presents dans vertices
        if sommet1 not in self.getVertices():
            self.add_vertex(sommet1)

        if sommet2 not in self.getVertices():
            self.add_vertex(sommet2)

        # ajout arete
        self.getEdges().append((sommet1, sommet2, poids))

    def supp_edge(self, edge):
        """ supprime l'arete edge = (sommet1, sommet2, poids) de la liste des aretes du graphe """
        assert isinstance(edge, tuple)
        assert edge in self.getEdges()

        self.getEdges().remove(edge)

    def supp_vertex(self, vertex):
        """ supprime le sommet vertex de la liste des sommets du graphe
         supprime aussi les aretes concernant vertex """
        assert vertex in self.getVertices()

        # supprime les aretes concernant vertex
        edges = self.getEdges()
        for i in range(len(edges)):
            if vertex == edges[i][0] or vertex == edges[i][1]:
                self.supp_edge(edges[i])
        # supprime vertex de la liste des sommets
        self.getVertices().remove(vertex)

    def matrice_poids(self):
        """ donne la matrice des poids des aretes
        l'ordre des colonnes et des lignes de la matrices correspondent a l'ordre des sommets
        dans la liste des sommets (la 1e ligne/colonne de la matrice correspond au 1e sommet de vertices)
        valeur coefficient i,j de la matrice :
        - 0 si i = j
        - inf s'il n'y a pas d'aretes entre le i-eme et j-eme sommet
        - le poids de l'arete entre le i-eme et j-eme sommet
        la matrice est symetrique suivant la diagonale"""

        vertices = self.getVertices()
        edges = self.getEdges()

        poids = np.zeros((len(vertices), len(vertices)))

        # remplit la matrice poids de inf partout sauf sur la diagonale de 1
        for i in range(len(vertices)):
            for j in range(len(vertices)):
                if i != j:
                    poids[i, j] = inf

        # remplit la matrice de poids avec les valeurs des poids des aretes
        for ind_vertex in range(len(vertices)):
            vertex = vertices[ind_vertex]
            for j in range(len(edges)):
                # cas ou vertex est le 1e sommet de l'arete
                if edges[j][0] == vertex:
                    ind_sommet2 = vertices.index(edges[j][1])  # recupere la position du 2e sommet de l'arete dans la liste des sommets
                    poids[ind_vertex, ind_sommet2] = edges[j][2]  # recupere le poids de l'arete
                    poids[ind_sommet2, ind_vertex] = edges[j][2]  # pour matrice symetrique
                # cas ou vertex est le 2e sommet de l'arete
                if edges[j][1] == vertex:
                    ind_sommet1 = vertices.index(edges[j][0])  # recupere la position du 1e sommet de l'arete dans la liste des sommets
                    poids[ind_vertex, ind_sommet1] = edges[j][2]  # recupere le poids de l'arete
                    poids[ind_sommet1, ind_vertex] = edges[j][2]  # pour matrice symetrique

        return poids

    def successeurs(self):
        """ renvoie une liste de liste ou la i-eme liste correspond aux successeurs du i-eme sommet
        sous la forme du tuple (sommet, poids) ou :
        sommet represente le successeur du i-eme sommet et poids represente le poids de l'arete entre sommet et le i-eme sommet """
        successeurs = []
        vertices = self.getVertices()
        edges = self.getEdges()

        for i in range(len(vertices)):
            vertex = vertices[i]
            successeurs_vertex = []
            # liste des successeurs pour le sommet vertex / le i-eme sommet sous forme (sommet, poids)
            for j in range(len(edges)):
                # poids de l'arete
                poids = edges[j][2]
                # sommet de l'arete (autre que le i-eme sommet)
                if edges[j][0] == vertex:
                    sommet = edges[j][1]
                    successeurs_vertex.append((sommet, poids))

                if edges[j][1] == vertex:
                    sommet = edges[j][0]
                    successeurs_vertex.append((sommet, poids))

            # ajoute la liste des successeurs du i-eme sommet a la liste des successeurs
            successeurs.append(successeurs_vertex)

        return successeurs

    def successeurs_sans_poids(self):
        """ renvoie une liste de liste ou la i-eme liste correspond a la liste des sommets successeurs du i-eme sommet """
        successeurs = []
        vertices = self.getVertices()
        edges = self.getEdges()

        for i in range(len(vertices)):
            vertex = vertices[i]
            successeurs_vertex = []
            # liste des successeurs pour le sommet vertex / le i-eme sommet sous forme (sommet, poids)
            for j in range(len(edges)):
                # sommet de l'arete (autre que le i-eme sommet)
                if edges[j][0] == vertex:
                    sommet = edges[j][1]
                    successeurs_vertex.append(sommet)

                if edges[j][1] == vertex:
                    sommet = edges[j][0]
                    successeurs_vertex.append(sommet)

            # ajoute la liste des successeurs du i-eme sommet a la liste des successeurs
            successeurs.append(successeurs_vertex)

        return successeurs

    def est_atteint(self, vertex1, vertex2):
        """ renvoie True s'il existe au moins un chemin entre vertex1 et vertex2 (vertex1 et vertex2 sont dans la meme partie connexe du graphe), False sinon """
        vertices = self.getVertices()  # liste des sommets du graphe
        assert vertex1 in vertices
        assert vertex2 in vertices
        index_v1 = vertices.index(vertex1)
        atteint = self.successeurs_sans_poids()[index_v1]  # liste des sommets atteignables a partir de vertex1
        marque = [vertex1]
        a_etudier = Pile(self.successeurs_sans_poids()[index_v1])  # piles des sommets a etudier = sommets qui ne sont pas des successeurs de vertex1

        while not a_etudier.isEmpty():  # tant que la pile de sommets n'est pas vide
            vertex = a_etudier.depiler()  # on depile le 1e sommmet de la pile
            if vertex not in marque:  # si ce sommet n'est pas marque
                index_vertex = vertices.index(vertex)
                successeurs = self.successeurs_sans_poids()[index_vertex]
                # on marque ce sommet
                marque.append(vertex)
                # on ajoute les successeurs de ce sommet a la pile a_etudier et a la liste des sommets atteints depuis vertex1
                for voisin in successeurs:
                    a_etudier.empiler(voisin)
                    atteint.append(voisin)
        # si vertex2 est dans la liste des sommets atteints depuis vertex, on renvoie True sinon False
        for ind in range(len(atteint)):
            if vertex2 == atteint[ind]:
                return True
        return False

    def voyageur(self, dep, arr):
        """ Graphe, Point, Point --> list
         Renvoie une liste de Point correspondant a un plus court chemin de dep a arr """
        # Détermine la distance de chaque sommet du graphe par rapport au sommet de départ, jusqu'à ce que le sommet d'arrivée soit sélectionné
        # Pour faire référence à un sommet, on utilisera son indice dans la liste L_sommets
        L_sommets = self.getVertices()
        if dep not in L_sommets or arr not in L_sommets:
            return "point de départ ou arrivée hors du graphe"
        G = self.successeurs()
        n = len(G)
        inddep = L_sommets.index(dep)
        indarr = L_sommets.index(arr)
        L_MARQUE = [False] * n
        L_DIS = [inf] * inddep + [0] + [inf] * (n - inddep - 1)
        CHEM = [-3] * inddep + [- 1] + [-3] * (n - inddep - 1)
        cont = True
        while cont:
            cont = actualisation(G, L_sommets, L_MARQUE, L_DIS, CHEM, indarr)

        # retrouve le chemin le plus court en partant du sommet d'arrivée et en allant jusqu'au sommet de départ
        # (CHEM donne l'indice du sommet précédent de chaque sommet dans le chemin)
        res = [arr]
        k = indarr
        while k != inddep:
            res = [L_sommets[CHEM[k]]] + res
            k = CHEM[k]
        return res


def recherche_plus_proche(L_mark, L_dis):
    """ list, list --> Point
     Cherche le sommet le plus proche du depart parmi ceux non marques
     L_dis = liste des distances au point de depart
     L_mark = liste des marques """
    dmin = inf
    plus_proche = -1
    for i, d in enumerate(L_dis):
        if L_mark[i] == False and d < dmin:
            plus_proche = i
            dmin = d
    return plus_proche


def actualisation(successeurs, L_sommets, L_marques, L_dis, chem, arrive):
    """ list, list, list, list, list, Point --> Bool
     Sélectionne le sommet le plus proche du point de départ (indpp) et met à jour les distances de ses voisins non marqués, puis marque indpp
     si indpp est le sommet d'arrivée, met fin à la boucle de la fonction algo
     successeurs correspond au resultat de graph.successeurs """
    n = len(L_sommets)
    indpp = recherche_plus_proche(L_marques, L_dis)

    if indpp != -1 and indpp != arrive:
        dis_som_origine = L_dis[indpp]
        for a in successeurs[indpp]:
            sp, dis_sommet_sp = a
            idsp = L_sommets.index(sp)
            if not L_marques[idsp]:
                if L_dis[idsp] > dis_sommet_sp + dis_som_origine:
                    L_dis[idsp] = dis_sommet_sp + dis_som_origine
                    chem[idsp] = indpp
        L_marques[indpp] = True
        return True
    else:
        return False
