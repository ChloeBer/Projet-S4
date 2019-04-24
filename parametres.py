__author__ = "Bernardet, Coruzzi, Laik, Montfort, Rouby, Trouyet"
__filename__ = "parametres"

# Importation des modules :
from PIL.Image import *  # necessaire au traitement des pixels
from class_boite import *
from class_graph import *
import time
import pygame
from pygame.locals import *
import pygame.draw # necessaire au simulateur


# nom des images :
noma = "blanc_total.png"
nomb = "blanc_rectangle_noir.png"
nomc = "cercle_noir.png"
nomd = "chemin_etroit.png"
nome = "nuage_noir.png"

# initialisation de l'image d'acceuil:
im_accueil = "accueil_pic.png"

# taille de l'image :
image = open(noma)
S = image.size
taille = [S[0], S[1]]

# nom de l'image cree avec les boites:
nom_map = 'creation_map.bmp'

# nom de l'image cree avec le chemin optimal:
nom_map_chemin = 'creation_map_avec_chemin.bmp'

# boite initiale:
box = Boite([Point(0, 0), Point(taille[0], 0), Point(taille[0], taille[1]), Point(0, taille[1])])
# box est une boite aux dimensions de l'image traitee

# position initiale du robot:
car_x = 0
car_y = 0

# nom de l'image de la voiture :
# nom_car="voitureplusgrande.png"
nom_car = "voiture.png"  # ne represente pas la réalité des choses!!!

# on recupere les dimensions de l'image pour avoir le centre :
im = open(nom_car)
s = im.size
dim_robot = [s[0], s[1]]
centre_car = [dim_robot[0]/2, dim_robot[1]/2]

# taille reelle robot :
# dim_robot=[50,57] # pour l'instant c'est en pixel mais il faudra faire la conversion en vrai
m = max(dim_robot[0], dim_robot[1])
dim_robot_max = [m+10, m+10]
