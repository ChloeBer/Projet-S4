__author__ = "Bernardet, Coruzzi, Laik, Montfort, Rouby, Trouyet"
__filename__ = "interface"

from fonctions_image import *
from parametres import *

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode(taille)
# Titre de la fenetre
pygame.display.set_caption("simulateur projet S4")

pygame.key.set_repeat(300, 15)

# texte à écrire pour choisir le sommet de départ et de fin sur pygame
font = pygame.font.Font(None, 50)
message_end = font.render("Choix du point d'arrivée (clic gauche)", 1, (219, 23, 2))
message_start = font.render("Choix du point de départ (touche g lorsque le curseur est en position)", 1, (219, 23, 2))
message_erreur_start = font.render("Le départ n'est pas à choisir sur un obstacle", 1, (219, 23, 2))
message_erreur_end = font.render("L'arrivée n'est pas à choisir sur un obstacle", 1, (219, 23, 2))
message_erreur_graphe = font.render("Il n'existe pas de tel chemin, choisir à nouveau le départ et l'arrivée", 1, (219, 23, 2))

# BOUCLE PRINCIPALE
continuer = 1
continuer_accueil = 1
while continuer:
    # Chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(im_accueil).convert()
    if continuer_accueil != 0:
        fenetre.blit(accueil, (0, 0))
    # Rafraichissement
    pygame.display.flip()

    # On remet ces variables à 1 à chaque tour de boucle
    continuer_choix = 1
    continuer_erreurStart = 1
    continuer_erreurEnd = 1
    continuer_erreurGraphe = 1

    # BOUCLE D'ACCUEIL
    while continuer_accueil:
        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

            # Si l'utilisateur quitte, on met les variables de boucle à 0 pour n'en parcourir aucune et fermer
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                continuer_accueil = 0
                continuer_jeu = 0
                continuer_choix = 0
                continuer = 0
                # Variable de choix du niveau
                image = 0

            elif event.type == KEYDOWN:

                if event.key == K_a:
                    continuer_accueil = 0
                    name = noma
                    image = open(noma)
                if event.key == K_b:
                    continuer_accueil = 0
                    name = nomb
                    image = open(nomb)
                if event.key == K_c:
                    continuer_accueil = 0
                    name = nomc
                    image = open(nomc)
                if event.key == K_d:
                    continuer_accueil = 0
                    name = nomd
                    image = open(nomd)
                if event.key == K_e:
                    continuer_accueil = 0
                    name = nome
                    image = open(nome)
    if image != 0:
        # Chargement et collage du fond
        fond1 = pygame.image.load(name)
        # Chargement et collage de la voiture
        # Rafraîchissement de l'écran
        pygame.display.flip()
        start_posx = 0
        start_posy = 0
        end_posx = 0
        end_posy = 0
    # BOUCLE DE CHOIX
    while continuer_choix:
        continuer_jeu = 1
        # Limitation de vitesse de la boucle
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # Si l'utilisateur quitte, on met la variable qui continue le jeu,
            # la variable générale et la variable de choix à 0 pour fermer la fenêtre
            if event.type == QUIT:
                continuer_choix = 0
                continuer_jeu = 0
                continuer = 0
            elif event.type == KEYDOWN:
                # Si l'utilisateur presse Echap ici, on revient seulement au menu
                if event.key == K_ESCAPE:
                    continuer_jeu = 0
                    continuer_choix = 0
                    continuer_accueil = 1

            if event.type == MOUSEBUTTONDOWN:  # si on utilise les boutons de la souris
                if event.button == 1:
                    if end_posx == 0 and end_posy == 0:
                        end_posx = event.pos[0]
                        end_posy = event.pos[1]
                        if Image.getpixel(image, (end_posx, end_posy)) == 0:
                            fenetre.blit(fond1, (0, 0))
                            fenetre.blit(message_erreur_end, (300, 200))
                            fenetre.blit(message_end, (300, 100))
                            # Rafraichissement
                            pygame.display.flip()
                            while continuer_erreurEnd:
                                # Limitation de vitesse de la boucle
                                pygame.time.Clock().tick(30)

                                for event in pygame.event.get():
                                    # Si l'utilisateur quitte, on met la variable qui continue le jeu,
                                    # la variable générale et la variable de choix à 0 pour fermer la fenêtre
                                    if event.type == QUIT:
                                        continuer_choix = 0
                                        continuer_jeu = 0
                                        continuer_erreurEnd = 0
                                        continuer = 0
                                    elif event.type == KEYDOWN:
                                        # Si l'utilisateur presse Echap ici, on revient seulement au menu
                                        if event.key == K_ESCAPE:
                                            continuer_jeu = 0
                                            continuer_choix = 0
                                            continuer_erreurEnd = 0
                                            continuer_accueil = 1

                                    if event.type == MOUSEBUTTONDOWN:  # si on utilise les boutons de la souris
                                        if event.button == 1:
                                            end_posx = event.pos[0]
                                            end_posy = event.pos[1]

                                    if Image.getpixel(image, (end_posx, end_posy)) != 0:
                                        continuer_erreurEnd = 0
                                    else:
                                        fenetre.blit(fond1, (0, 0))
                                        fenetre.blit(message_erreur_end, (300, 200))
                                        fenetre.blit(message_end, (300, 100))
                                        # Rafraichissement
                                        pygame.display.flip()
            if event.type == KEYDOWN and end_posx != 0 and end_posy != 0:
                if event.key == K_g:
                    if start_posx == 0 and start_posy == 0:
                        start_posx = pygame.mouse.get_pos()[0]
                        start_posy = pygame.mouse.get_pos()[1]
                        if Image.getpixel(image, (start_posx, start_posy)) == 0:
                            fenetre.blit(fond1, (0, 0))
                            fenetre.blit(message_erreur_start, (300, 200))
                            fenetre.blit(message_start, (300, 100))
                            pygame.draw.circle(fenetre, (0, 0, 255), [end_posx, end_posy], 8)
                            # Rafraichissement
                            pygame.display.flip()
                            while continuer_erreurStart:
                                # Limitation de vitesse de la boucle
                                pygame.time.Clock().tick(30)
                                for event in pygame.event.get():
                                    # Si l'utilisateur quitte, on met la variable qui continue le jeu,
                                    # la variable générale et la variable de choix à 0 pour fermer la fenêtre
                                    if event.type == QUIT:
                                        continuer_choix = 0
                                        continuer_jeu = 0
                                        continuer_erreurEnd = 0
                                        continuer_erreurStart = 0
                                        continuer = 0
                                    elif event.type == KEYDOWN:
                                        # Si l'utilisateur presse Echap ici, on revient seulement au menu
                                        if event.key == K_ESCAPE:
                                            continuer_jeu = 0
                                            continuer_choix = 0
                                            continuer_erreurEnd = 0
                                            continuer_erreurStart = 0
                                            continuer_accueil = 1
                                    if event.type == KEYDOWN:  # si on utilise les boutons de la souris
                                        if event.key == K_g:
                                            start_posx = pygame.mouse.get_pos()[0]
                                            start_posy = pygame.mouse.get_pos()[1]
                                    if Image.getpixel(image, (start_posx, start_posy)) != 0:
                                        continuer_erreurStart = 0
                                    else:
                                        fenetre.blit(fond1, (0, 0))
                                        fenetre.blit(message_erreur_start, (300, 200))
                                        fenetre.blit(message_start, (300, 100))
                                        pygame.draw.circle(fenetre, (0, 0, 255), [end_posx, end_posy], 8)
                                        # Rafraichissement
                                        pygame.display.flip()

        # Re-collage
        fenetre.blit(fond1, (0, 0))
        if end_posx == 0 and end_posy == 0:
            fenetre.blit(message_end, (300, 100))
        elif start_posx == 0 and start_posy == 0:
            fenetre.blit(message_start, (300, 100))
        pygame.draw.circle(fenetre, (0, 0, 255), [start_posx, start_posy], 8)
        pygame.draw.circle(fenetre, (0, 0, 255), [end_posx, end_posy], 8)
        # Rafraichissement
        pygame.display.flip()
        if start_posx != 0 and start_posy != 0 and end_posx != 0 and end_posy != 0:
            continuer_choix = 0
            # Re-collage
            fenetre.blit(fond1, (0, 0))
            pygame.draw.circle(fenetre, (0, 0, 255), [start_posx, start_posy], 8)
            pygame.draw.circle(fenetre, (0, 0, 255), [end_posx, end_posy], 8)
            # Rafraichissement
            pygame.display.flip()

    if continuer_jeu != 0:
        point_depart = Point(start_posx, start_posy)
        point_arrivee = Point(end_posx, end_posy)
        graphe = cree_map(image, box, name, point_depart, point_arrivee)  # appelle la fonction qui fait la carte

        if not (graphe.est_atteint(point_depart, point_arrivee)):
            continuer_jeu = 0
            continuer_accueil = 0
            fenetre.blit(fond1, (0, 0))
            fenetre.blit(message_erreur_graphe, (300, 200))
            # Rafraîchissement de l'écran
            pygame.display.flip()
            time.sleep(3)
        if continuer_jeu != 0:
            chemin = graphe.voyageur(point_depart, point_arrivee)
            print(chemin)
            chemin_effectif = []
            for elt in chemin:
                chemin_effectif += [tuple((elt.getAbscisse(), elt.getOrdonnee()))]
            print(chemin_effectif)
            cree_map_avec_chemin(chemin, point_arrivee)
            # Chargement et collage du fond
            fond = pygame.image.load(nom_map_chemin)
            # Chargement et collage de la voiture
            car = pygame.image.load(nom_car).convert_alpha()
            fenetre.blit(car, (car_x, car_y))
            # Rafraîchissement de l'écran
            pygame.display.flip()
            
        # BOUCLE DE JEU
        while continuer_jeu:

            # Limitation de vitesse de la boucle
            pygame.time.Clock().tick(30)
            for event in pygame.event.get():

                # Si l'utilisateur quitte, on met la variable qui continue le jeu
                # ET la variable générale à 0 pour fermer la fenêtre
                if event.type == QUIT:
                    continuer_jeu = 0
                    continuer = 0
                elif event.type == KEYDOWN:
                    # Si l'utilisateur presse Echap ici, on revient seulement au menu
                    if event.key == K_ESCAPE:
                        continuer_jeu = 0
                        continuer_accueil = 1

                if event.type == MOUSEMOTION:  # si on utilise les mouvements de la souris
                    # si je veux que l'image de la voiture suive ma souris
                    car_x = event.pos[0] - centre_car[0]
                    car_y = event.pos[1] - centre_car[1]
            # Re-collage
            fenetre.blit(fond, (0, 0))
            fenetre.blit(car, (car_x, car_y))
            # Rafraichissement
            pygame.display.flip()
