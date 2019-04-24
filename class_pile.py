__author__ = "Bernardet, Coruzzi, Laik, Montfort, Rouby, Trouyet"
__filename__ = "class_pile"


class Pile:
    """ classe permettant de creer des piles composees d'une liste
    Pile = dernier arrive, premier sorti
    On manipule des listes donc dernier element a la position -1 et c'est celui qui sortira en 1e de la pile
    (et 1e element, celui qui sortira de la pile en dernier, en position 0)
    Il n'y a aucune restriction sur les elements (presents initialement ou ajoutes) de la pile """

    def __init__(self, liste):
        """ cree une pile avec :
         - list : la liste des elements contenus dans la pile"""
        assert isinstance(liste, list)
        self.liste = liste

    def getListe(self):
        """ recupere la liste de la pile """
        return self.liste

    def setListe(self, liste):
        """ change toute la liste de la pile """
        assert isinstance(liste, list)
        self.liste = liste

    def isEmpty(self):
        """ renvoie True si la pile et vide, False sinon """
        if self.getListe() == []:
            return True
        else:
            return False

    def empiler(self, element):
        """ ajoute element en haut de la pile """
        self.getListe().append(element)

    def depiler(self):
        """ enleve de la pile et renvoie l'element du haut de la pile (le dernier rentre dans la pile) """
        assert not self.isEmpty()
        haut = self.getListe()[-1]
        self.getListe().remove(haut)
        return haut

    def haut(self):
        """ donne l'element en haut de la pile sans l'enlever de la pile """
        assert not self.isEmpty()
        return self.getListe()[-1]

    def retirer(self, element):
        """ enleve element de la pile """
        assert element in self.getListe()
        self.getListe().remove(element)

    def position(self, element):
        """ donne la position de element dans la liste de la pile """
        assert element in self.getListe()
        return self.getListe().index(element)