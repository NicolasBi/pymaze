# -*- coding: utf-8 -*-
##### Projet 12. Le labyrinthe #####
#### Auteurs : BIZZOZZERO Nicolas, BOUHASTINE Mohamed ####
#### Description du programme ####
# Ce programme permet de lancer le jeu

#### Importation des modules / bibliotheques #####
from fonctions_du_labyrinthe import *
from graphismes_du_labyrinthe import *
from upemtk import *
from time import *

### Definitions ###
## Definition des variables
niveau_du_labyrinthe = 0
coordonnees_du_personnage = [1, 1]
coordonnees_de_la_sortie = [15, 1]
action = 'none'
profondeur_vision = 0
orientation_du_personnage = 'nord'

## Definition des listes
liste_plan_du_labyrinthe = []
liste_positions_virages_gauche = []
liste_positions_virages_droite = []

## Definition des tuples
coordonnees_du_clic = (0, 0)

### Debut du programme ###
cree_fenetre(1000, 600)

### Menu principal
coordonnees_du_clic = affichage_menu_principal()
# Boucle permettant à l'utilisateur de cliquer ailleurs que sur les boutons sans créer d'erreur
while (coordonnees_du_clic[0] < 350) or (coordonnees_du_clic[0] > 650) or (coordonnees_du_clic[1] < 330) or (coordonnees_du_clic[1] > 445 and coordonnees_du_clic[1] < 460) or (coordonnees_du_clic[1] > 575):
	coordonnees_du_clic = attente_clic()
# Si l'utilisateur clique sur le bouton 'Lancer le jeu'
if coordonnees_du_clic[0] >= 350 and coordonnees_du_clic[0] <= 650 and coordonnees_du_clic[1] >= 330 and coordonnees_du_clic[1] <= 445:
	### Menu de choix du niveau
	coordonnees_du_clic, niveau_du_labyrinthe, coordonnees_de_la_sortie, orientation_du_personnage = affichage_choix_du_niveau(niveau_du_labyrinthe, coordonnees_de_la_sortie, orientation_du_personnage)
	# Boucle permettant à l'utilisateur de cliquer ailleurs que sur les boutons sans créer d'erreur
	while (coordonnees_du_clic[0] < 90) or (coordonnees_du_clic[0] > 190 and coordonnees_du_clic[0] < 240) or (coordonnees_du_clic[0] > 340 and coordonnees_du_clic[0] < 390) or (coordonnees_du_clic[0] > 490 and coordonnees_du_clic[0] < 540) or (coordonnees_du_clic[0] > 640 and coordonnees_du_clic[0] < 690) or (coordonnees_du_clic[0] > 790 and coordonnees_du_clic[0] < 840) or (coordonnees_du_clic[0] > 940) or (coordonnees_du_clic[1] < 300) or (coordonnees_du_clic[1] > 400):
		coordonnees_du_clic, niveau_du_labyrinthe, coordonnees_de_la_sortie, orientation_du_personnage = affichage_choix_du_niveau(niveau_du_labyrinthe, coordonnees_de_la_sortie, orientation_du_personnage)
	# Chargement du labyrinthe et démarrage du chronomètre
	liste_plan_du_labyrinthe = chargement_labyrinthe(niveau_du_labyrinthe)
	debut_du_chrono = time()
	### Boucle principale faisant tourner le jeu
	while coordonnees_du_personnage != coordonnees_de_la_sortie:
		point_de_passage_du_chrono = round(time() - debut_du_chrono, 3)
		action, coordonnees_du_personnage, orientation_du_personnage, liste_plan_du_labyrinthe, profondeur_vision, liste_positions_virages_gauche, liste_positions_virages_droite, niveau_du_labyrinthe, point_de_passage_du_chrono = boucle_du_jeu(action, coordonnees_du_personnage, orientation_du_personnage, liste_plan_du_labyrinthe, profondeur_vision, liste_positions_virages_gauche, liste_positions_virages_droite, niveau_du_labyrinthe, point_de_passage_du_chrono)
	### Fin du jeu et arret du chronomètre
	fin_du_chrono = time()
	temps_total = round(fin_du_chrono - debut_du_chrono, 3)
	# Sii l'utilisateur a battu un record associé à un niveau, son fichier de record sera modifié en conséquences
	nouveau_record = verification_nouveau_record(niveau_du_labyrinthe, temps_total)
	### Ecran de victoire
	efface_tout()
	# Background
	rectangle(0, 0, 1000, 600, epaisseur = "1", remplissage = 'black')
	# Message de victoire
	texte(500, 200, "FELICITATIONS !", couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 18)
	if niveau_du_labyrinthe == 1:
		texte(500, 250, "Vous avez terminé le niveau 1 en :", couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 18)
	elif niveau_du_labyrinthe == 2:
		texte(500, 250, "Vous avez terminé le niveau 2 en :", couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 18)
	elif niveau_du_labyrinthe == 3:
		texte(500, 250, "Vous avez terminé le niveau 3 en :", couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 18)
	elif niveau_du_labyrinthe == 4:
		texte(500, 250, "Vous avez terminé le niveau 4 en :", couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 18)
	elif niveau_du_labyrinthe == 5:
		texte(500, 250, "Vous avez terminé le niveau 5 en :", couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 18)
	elif niveau_du_labyrinthe == 6:
		texte(500, 250, "Vous avez terminé le niveau 6 en :", couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 18)
	# Petit logo s'affichant si l'utilisateur bat un record
	if nouveau_record == True:
		image(150, 150, "img/nouveau_record.gif", ancrage='center')
	# Affichage du temps de l'utilisateur
	texte(500, 275, temps_total, couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 18)
	texte(500, 300, "secondes", couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 18)
	# Affichage des records du niveau
	affichage_meilleurs_scores(niveau_du_labyrinthe)
	coordonnees_du_clic = attente_clic()
	# Boucle permettant à l'utilisateur de cliquer ailleurs que sur le bouton 'Quitter' sans créer d'erreur
	while (coordonnees_du_clic[0] < 400) or (coordonnees_du_clic[0] > 600) or (coordonnees_du_clic[1] < 490) or (coordonnees_du_clic[1] > 530):
		coordonnees_du_clic = attente_clic()
	ferme_fenetre()
# Si l'utilisateur clique le bouton 'Quitter'
elif coordonnees_du_clic[0] >= 350 and coordonnees_du_clic[0] <= 650 and coordonnees_du_clic[1] >= 460 and coordonnees_du_clic[1] <= 575:
	ferme_fenetre()