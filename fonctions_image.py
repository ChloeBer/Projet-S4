__author__ = "Bernardet, Coruzzi, Laik, Montfort, Rouby, Trouyet"
__filename__ = "fonctions_image"

from parametres import *


def position_acceptable(image, boite):
    """ image, Boite --> Bool
     Renvoie False si un obstacle (= pixel(s) noir(s)) est présent sur la partie de
     l'image delimitee par la boite, sinon True
     ATTENTION un seul pixel noir constitue aussi un obstacle """
    assert isinstance(boite, Boite)
    x1 = boite.getSommets()[0].getAbscisse()
    x2 = boite.getSommets()[1].getAbscisse()

    y1 = boite.getSommets()[0].getOrdonnee()
    y4 = boite.getSommets()[3].getOrdonnee()

    X1 = round(x1)
    X2 = round(x2)

    Y1 = round(y1)
    Y4 = round(y4)
    # le pixel a la position (i,j) est noir si la valeur du pixel en (i,j) est 0
    # on parcourt ici les pixels de l'image compris entre l'abscisse
    # de l'angle supérieur gauche de la boite et l'angle inférieur droit de l'image
    for i in range(X1, X2):
        for j in range(Y1, Y4):
            if Image.getpixel(image, (i, j)) == 0:
                return False
    return True


def decouper_accept(image, boite, liste):
    """ image, Boite, list --> list
     Prend en argument une image, une boite et une liste intialement vide
     et decoupe l'image en quatre boites si un obstacle est présent dans les limites
     de la boite et si la dimension de la boite est superieure a celle du robot et recommence
     tant qu'il y a un obstacle ou que la boite est assez grande
     Renvoie la liste des boites sans obstacle """
    assert isinstance(boite, Boite)
    assert isinstance(liste, list)
    if position_acceptable(image, boite) and boite.dimension() > dim_robot_max:
        liste = liste+[boite]
        return liste
    elif boite.dimension() > dim_robot_max:
        B1, B2, B3, B4 = boite.decoupe()
        return decouper_accept(image, B1, liste) + decouper_accept(image, B2, liste) + \
               decouper_accept(image, B3, liste) + decouper_accept(image, B4, liste)
    return liste


def cree_map(image, box, name_image, point_depart, point_arrivee):
    """ image, Boite, str, Point, Point --> Graph
     Renvoie un graphe où les sommets représentent les milieux des boites crées par la fonction decouper,
     il y a une arête entre les sommets si leurs boites sont adjacentes
    Modifie l’image de départ sur laquelle est tracée graphe et les boites crées par la fonction decouper """
    pygame.init()

    resVrai = decouper_accept(image, box, [])  # on recupere la liste de toutes les boites une fois l'image decoupee
    resMil = []
    # Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode(taille)
    # Chargement et collage du fond
    fond = pygame.image.load(name_image)
    fenetre.blit(fond, (0, 0))

    # Rafraîchissement de l'écran
    pygame.display.flip()
    for i in range(len(resVrai)):
        # Affiche les boites sur l'image
        pygame.draw.rect(fenetre, (50, 250, 50), [resVrai[i].getSommets()[0].getAbscisse(),
                                                  resVrai[i].getSommets()[0].getOrdonnee(),
                                                  resVrai[i].dimension()[0],
                                                  resVrai[i].dimension()[1]], 4)
        # Cree les sommets
        resMil += [resVrai[i].getSommets()[0].milieu(resVrai[i].getSommets()[2])]
        # Affiche les sommets sur l'image
        pygame.draw.circle(fenetre, (255, 127, 0), [round(resMil[i].getAbscisse()), round(resMil[i].getOrdonnee())], 8)

    # Point le plus proche de point_depart
    point_de_contact_dep = point_depart.proche_sommet(resMil)
    # Trace une arete entre point_de_contact_dep et point_depart
    pygame.draw.line(fenetre, (255, 127, 0), [round(point_de_contact_dep.getAbscisse()), round(point_de_contact_dep.getOrdonnee())],
                     [round(point_depart.getAbscisse()), round(point_depart.getOrdonnee())], 5)
    # Point le plus proche de point_arr
    point_de_contact_arr = point_arrivee.proche_sommet(resMil)
    # Trace une arete entre point_de_contact_arr et point_arrivee
    pygame.draw.line(fenetre, (255, 127, 0), [round(point_de_contact_arr.getAbscisse()), round(point_de_contact_arr.getOrdonnee())],
                     [round(point_arrivee.getAbscisse()), round(point_arrivee.getOrdonnee())], 5)
    # Affiche point_arrivee et point_depart sur l'image
    pygame.draw.circle(fenetre, (0, 0, 255), [point_depart.getAbscisse(), point_depart.getOrdonnee()], 8)
    pygame.draw.circle(fenetre, (0, 0, 255), [point_arrivee.getAbscisse(), point_arrivee.getOrdonnee()], 8)
    aretes = []
    # Ajoute les aretes
    for j in range(len(resVrai)):
        for k in range(len(resVrai)):
            if resVrai[j].adjacence(resVrai[k]):
                pygame.draw.line(fenetre, (255, 127, 0), [round(resMil[j].getAbscisse()), round(resMil[j].getOrdonnee())], [round(resMil[k].getAbscisse()), round(resMil[k].getOrdonnee())], 5)
                if (resMil[j], resMil[k], resMil[j].distance(resMil[k])) and (resMil[k], resMil[j], resMil[j].distance(resMil[k])) not in aretes:
                    aretes += (resMil[j], resMil[k], resMil[j].distance(resMil[k])),
    graphe = Graph(resMil, aretes)
    # Ajoute les aretes entre point_depart et point_de_contact_dep et entre point_arrivee et point_de_contact_arr
    graphe.add_edge(point_depart, point_de_contact_dep, point_depart.distance(point_de_contact_dep))
    graphe.add_edge(point_arrivee, point_de_contact_arr, point_arrivee.distance(point_de_contact_arr))
    # Rafraichissement et sauvegarde de l'image
    pygame.display.flip()
    pygame.image.save(fenetre, nom_map)
    return graphe


def cree_map_avec_chemin(liste, point_arr):
    """ list, point_arr --> None
     liste = chemin renvoye par l'algo des voyageurs
     Trace un plus court chemin sur l'image
     nom_map = nom de l'image avec les boites et le graphe deja dessiné """
    pygame.init()

    # Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode(taille)
    # Chargement et collage du fond
    fond = pygame.image.load(nom_map)
    fenetre.blit(fond, (0, 0))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Trace le plus court chemin dans une couleur differente
    for i in range(len(liste)-1):
        pygame.draw.line(fenetre, (0, 0, 255), [round(liste[i].getAbscisse()), round(liste[i].getOrdonnee())],
                         [round(liste[i + 1].getAbscisse()), round(liste[i + 1].getOrdonnee())], 5)
        pygame.draw.circle(fenetre, (0, 0, 255), [round(liste[i].getAbscisse()), round(liste[i].getOrdonnee())], 8)

    # Rafraichissement et sauvegarde de l'image
    pygame.display.flip()
    pygame.image.save(fenetre, nom_map_chemin)
