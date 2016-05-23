# -*- coding: utf-8 -*-
##### Projet 12. Le labyrinthe #####
#### Auteurs : BIZZOZZERO Nicolas, BOUHASTINE Mohamed ####
#### Description du programme ####
# Ce programme contient les fonctions du jeu

#### Importation des modules / bibliotheques ####
from upemtk import *
from graphismes_du_labyrinthe import *
from random import randint

### Definition ###
## Definition des fonctions
def chargement_labyrinthe(niveau_du_labyrinthe):
	"""
		Prends en argument un entier correspondant au niveau du labyrinthe a charger, 'niveau_du_labyrinthe'.
		Charge le niveau du labyrinthe depuis le fichier texte correspondant.
		Insère le contenu du fichier texte dans une liste 'liste_plan_du_labyrinthe'.
		Modifie la liste 'liste_plan_du_labyrinthe' de manière à ce qu'elle soit facilement utilisable pour d'ultérieures modifications.
		Retourne la liste 'liste_plan_du_labyrinthe' correspondant au plan du labyrinthe.
	"""
	compteur = 0
	# Choix du niveau à charger
	if niveau_du_labyrinthe == 1:
		fichier = open("niveaux_du_labyrinthe/niveau_1.txt", "r")
	elif niveau_du_labyrinthe == 2:
		fichier = open("niveaux_du_labyrinthe/niveau_2.txt", "r")
	elif niveau_du_labyrinthe == 3:
		fichier = open("niveaux_du_labyrinthe/niveau_3.txt", "r")
	elif niveau_du_labyrinthe == 4:
		fichier = open("niveaux_du_labyrinthe/niveau_4.txt", "r")
	elif niveau_du_labyrinthe == 5:
		fichier = open("niveaux_du_labyrinthe/niveau_5.txt", "r")
	elif niveau_du_labyrinthe == 6:
		fichier = open("niveaux_du_labyrinthe/niveau_6.txt", "r")
	# Insertion du contenu du fichier texte dans la liste 'liste_plan_du_labyrinthe'
	liste_plan_du_labyrinthe = fichier.readlines()
	fichier.close()
	# Boucle de modification de la liste 'liste_plan_du_labyrinthe'
	while compteur != len(liste_plan_du_labyrinthe):
		# Suppression du saut de ligne
		liste_plan_du_labyrinthe[compteur] = liste_plan_du_labyrinthe[compteur].strip("\n")
		# Insertion de chaque élement de la ligne dans une liste interne à la liste 'liste_plan_du_labyrinthe'
		liste_plan_du_labyrinthe[compteur] = liste_plan_du_labyrinthe[compteur].split(' ')
		compteur += 1
	return liste_plan_du_labyrinthe

def attribution_des_actions(coordonnees_du_clic):
	"""
		Prends un tuple contenant deux coordonnées en argument.
		Verifie que ces coordonnées sont inclues dans une zone correspondant à un bouton de la fenêtre.
		Renvoie une chaîne de caractères correspondant à l'action de ce bouton.
		Cette chaîne de caractères renvoyée peut etre *'haut'*'gauche'*'bas'*'droite'*'rotationgauche'*'rotationdroite'*'none'.
	"""
	# Clic sur le bouton pour effectuer une rotation à gauche
	if (coordonnees_du_clic[0] >= 333 and coordonnees_du_clic[0] <= 444) and (coordonnees_du_clic[1] >= 451 and coordonnees_du_clic[1] <= 525):
		return 'rotationgauche'
	# Clic sur le bouton pour aller tout droit
	if (coordonnees_du_clic[0] >= 444 and coordonnees_du_clic[0] <= 555) and (coordonnees_du_clic[1] >= 451 and coordonnees_du_clic[1] <= 525):
		return 'haut'
	# Clic sur le bouton pour effectuer une rotation à droite
	if (coordonnees_du_clic[0] >= 555 and coordonnees_du_clic[0] <= 666) and (coordonnees_du_clic[1] >= 451 and coordonnees_du_clic[1] <= 525):
		return 'rotationdroite'
	# Clic sur le bouton pour tourner à gauche
	if (coordonnees_du_clic[0] >= 333 and coordonnees_du_clic[0] <= 444) and (coordonnees_du_clic[1] >= 525 and coordonnees_du_clic[1] <= 599):
		return 'gauche'
	# Clic sur le bouton pour aller en arrière
	if (coordonnees_du_clic[0] >= 444 and coordonnees_du_clic[0] <= 555) and (coordonnees_du_clic[1] >= 525 and coordonnees_du_clic[1] <= 599):
		return 'bas'
	# Clic sur le bouton pour tourner à droite
	if (coordonnees_du_clic[0] >= 555 and coordonnees_du_clic[0] <= 666) and (coordonnees_du_clic[1] >= 525 and coordonnees_du_clic[1] <= 599):
		return 'droite'
	# Clic ailleurs que sur un bouton possédant une action
	return 'none'

def deplacement_personnage(action, coordonnees_du_personnage, orientation_du_personnage, liste_plan_du_labyrinthe):
	"""
		Prends en argument : 
		- Une chaîne de caractères correspondant à une action, 'action'; 
		- Une liste correspondant aux coordonnées du personnage, 'coordonnees_du_personnage'; 
		- Une chaîne de caractères correspondant à l'orientation du personnage, 'orientation_du_personnage';
		- Une liste correspondant à la liste du plan du labyrinthe, 'liste_plan_du_labyrinthe'.
		Modifie la liste 'liste_plan_du_labyrinthe' ainsi que les coordonnées du personnage si l'action choisie est 'haut', 'gauche', 'bas' ou 'droite'.
		Empêche le personnage de traverser les murs
		Modifie l'orientation du personnage 'orientation_du_personnage' si l'action choisie est 'rotationgauche' ou 'rotationdroite'.
		Renvoie :
		- La liste des coordonnées du personnage 'coordonnees_du_personnage';
		- La chaîne de caractères correspondant à l'orientation du personnage, 'orientation_du_personnage';
		- La liste du plan du labyrinthe 'liste_plan_du_labyrinthe'.
	"""
	x_personnage = coordonnees_du_personnage[0]
	y_personnage = coordonnees_du_personnage[1]
	if (orientation_du_personnage == 'nord' and action == 'haut') or (orientation_du_personnage == 'est' and action == 'gauche') or (orientation_du_personnage == 'sud' and action == 'bas') or (orientation_du_personnage == 'ouest' and action == 'droite'):
		# Si l'element au dessus de '@' n'est pas un mur, on effectue le deplacement. Sinon, on ne fait rien.
		if liste_plan_du_labyrinthe[y_personnage - 1][x_personnage] != '*':
			liste_plan_du_labyrinthe[y_personnage - 1][x_personnage] = '@'
			liste_plan_du_labyrinthe[y_personnage][x_personnage] = '.'
			y_personnage -= 1
	elif (orientation_du_personnage == 'nord' and action == 'droite') or (orientation_du_personnage == 'est' and action == 'haut') or (orientation_du_personnage == 'sud' and action == 'gauche') or (orientation_du_personnage == 'ouest' and action == 'bas'):
		# Si l'element a droite de '@' n'est pas un mur, on effectue le deplacement. Sinon, on ne fait rien.
		if liste_plan_du_labyrinthe[y_personnage][x_personnage + 1] != '*':
			liste_plan_du_labyrinthe[y_personnage][x_personnage + 1] = '@'
			liste_plan_du_labyrinthe[y_personnage][x_personnage] = '.'
			x_personnage += 1
	elif (orientation_du_personnage == 'nord' and action == 'bas') or (orientation_du_personnage == 'est' and action == 'droite') or (orientation_du_personnage == 'sud' and action == 'haut') or (orientation_du_personnage == 'ouest' and action == 'gauche'):
		# Si l'element en dessous de '@' n'est pas un mur, on effectue le deplacement. Sinon, on ne fait rien.
		if liste_plan_du_labyrinthe[y_personnage + 1][x_personnage] != '*':
			liste_plan_du_labyrinthe[y_personnage + 1][x_personnage] = '@'
			liste_plan_du_labyrinthe[y_personnage][x_personnage] = '.'
			y_personnage += 1
	elif (orientation_du_personnage == 'nord' and action == 'gauche') or (orientation_du_personnage == 'est' and action == 'bas') or (orientation_du_personnage == 'sud' and action == 'droite') or (orientation_du_personnage == 'ouest' and action == 'haut'):
		# Si l'element à gauche de de '@' n'est pas un mur, on effectue le deplacement. Sinon, on ne fait rien.
		if liste_plan_du_labyrinthe[y_personnage][x_personnage - 1] != '*':
			liste_plan_du_labyrinthe[y_personnage][x_personnage - 1] = '@'
			liste_plan_du_labyrinthe[y_personnage][x_personnage] = '.'
			x_personnage -= 1
	# Si l'action choisie est 'rotationdroite'
	elif action == 'rotationdroite':
		if orientation_du_personnage == 'nord':
			orientation_du_personnage = 'est'
		elif orientation_du_personnage == 'est':
			orientation_du_personnage = 'sud'
		elif orientation_du_personnage == 'sud':
			orientation_du_personnage = 'ouest'
		elif orientation_du_personnage == 'ouest':
			orientation_du_personnage = 'nord'
	# Si l'action choisie est 'rotationgauche'
	elif action == 'rotationgauche':
		if orientation_du_personnage == 'nord':
			orientation_du_personnage = 'ouest'
		elif orientation_du_personnage == 'ouest':
			orientation_du_personnage = 'sud'
		elif orientation_du_personnage == 'sud':
			orientation_du_personnage = 'est'
		elif orientation_du_personnage == 'est':
			orientation_du_personnage = 'nord'
	coordonnees_du_personnage = [x_personnage, y_personnage]
	return coordonnees_du_personnage, orientation_du_personnage, liste_plan_du_labyrinthe

def affichage_menu_principal():
	""" 
		Utilise les fonctions prédéfinies du module 'upemtk' pour dessiner le menu principal. 
		Renvoie un tuple correspondant aux coordonnées du clic, 'coordonnees_du_clic'.
	"""
	# Background
	rectangle(0, 0, 1000, 600, couleur = 'black', remplissage = 'black')
	# Titre
	texte(500, 150, "LE LABYRINTHE", couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 17)
	# Bouton 'Lancer le jeu'
	rectangle(350, 330, 650, 445, couleur = '#708090', remplissage = '#868686')
	texte(500, 387, "Lancer le jeu", couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 17)
	# Bouton 'Quitter'
	rectangle(350, 460, 650, 575, couleur = '#708090', remplissage = '#868686')
	texte(500, 517, "Quitter", couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 17)
	coordonnees_du_clic = attente_clic()
	return coordonnees_du_clic

def affichage_choix_du_niveau(niveau_du_labyrinthe, coordonnees_de_la_sortie, orientation_du_personnage):
	""" 
		Prends en arguments:
		- L'entier correspondant au niveau du labyrinthe a charger, 'niveau_du_labyrinthe';
		- Une liste contenant les coordonnées de la sortie, 'coordonnees_de_la_sortie';
		- Une chaune de caractères correspondant à l'orientation du personnage, 'orientation_du_personnage'.
		Utilise les fonctions prédéfinies du module 'upemtk' pour dessiner le menu de choix du niveau. 
		Renvoie:
		- Un tuple correspondant aux coordonnées du clic, 'coordonnees_du_clic';
		- Un entier correspondant au niveau du labyrinthe, 'niveau_du_labyrinthe';
		- Une liste correspondant aux coordonnées de la sortie, 'coordonnees_de_la_sortie'.
	"""
	efface_tout()
	# Background
	rectangle(0, 0, 1000, 600, couleur = 'black', remplissage = 'black')
	# Texte 'Choix du niveau'
	texte(500, 200, "Choix Du Niveau", couleur = 'white', ancrage = CENTER, police = 'Purisa', taille = 30)
	# Bouton 'Niveau 1'
	rectangle(90, 300, 190, 400, couleur = '#708090', remplissage = '#868686')
	texte(140, 350, "Niveau 1", couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 17)
	# Bouton 'Niveau 2'
	rectangle(240, 300, 340, 400, couleur = '#708090', remplissage = '#868686')
	texte(290, 350, "Niveau 2", couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 17)
	# Bouton 'Niveau 3'
	rectangle(390, 300, 490, 400, couleur = '#708090', remplissage = '#868686')
	texte(440, 350, "Niveau 3", couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 17)
	# Bouton 'Niveau 4'
	rectangle(540, 300, 640, 400, couleur = '#708090', remplissage = '#868686')
	texte(590, 350, "Niveau 4", couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 17)
	# Bouton 'Niveau 5'
	rectangle(690, 300, 790, 400, couleur = '#708090', remplissage = '#868686')
	texte(740, 350, "Niveau 5", couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 17)
	# Bouton 'Niveau 6'
	rectangle(840, 300, 940, 400, couleur = '#708090', remplissage = '#868686')
	texte(890, 350, "Niveau 6", couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 17) 
	coordonnees_du_clic = attente_clic()
	## Chaque 'if' va indiquer quel niveau du labytinthe charger
	if coordonnees_du_clic[0] >= 90 and coordonnees_du_clic[0] <= 190 and coordonnees_du_clic[1] >= 300 and coordonnees_du_clic[1] <= 400:
		niveau_du_labyrinthe = 1
		coordonnees_de_la_sortie = [15, 1]
		orientation_du_personnage = 'est'
	elif coordonnees_du_clic[0] >= 240 and coordonnees_du_clic[0] <= 340 and coordonnees_du_clic[1] >= 300 and coordonnees_du_clic[1] <= 400:
		niveau_du_labyrinthe = 2
		coordonnees_de_la_sortie = [17, 1]
		orientation_du_personnage = 'est'
	elif coordonnees_du_clic[0] >= 390 and coordonnees_du_clic[0] <= 490 and coordonnees_du_clic[1] >= 300 and coordonnees_du_clic[1] <= 400:
		niveau_du_labyrinthe = 3
		coordonnees_de_la_sortie = [18, 5]
		orientation_du_personnage = 'sud'
	elif coordonnees_du_clic[0] >= 540 and coordonnees_du_clic[0] <= 640 and coordonnees_du_clic[1] >= 300 and coordonnees_du_clic[1] <= 400:
		niveau_du_labyrinthe = 4
		coordonnees_de_la_sortie = [1, 8]
		orientation_du_personnage = 'est'
	elif coordonnees_du_clic[0] >= 690 and coordonnees_du_clic[0] <= 790 and coordonnees_du_clic[1] >= 300 and coordonnees_du_clic[1] <= 400:
		niveau_du_labyrinthe = 5
		coordonnees_de_la_sortie = [1, 5]
		orientation_du_personnage = 'sud'
	elif coordonnees_du_clic[0] >= 840 and coordonnees_du_clic[0] <= 940 and coordonnees_du_clic[1] >= 300 and coordonnees_du_clic[1] <= 400:
		niveau_du_labyrinthe = 6
		coordonnees_de_la_sortie = [20, 7]
		orientation_du_personnage = 'est'
	return coordonnees_du_clic, niveau_du_labyrinthe, coordonnees_de_la_sortie, orientation_du_personnage

def affichage_HUD(niveau_du_labyrinthe, temps):
	"""
		Prends en arguments un entier correspondant au niveau du labyrinthe, 'niveau_du_labyrinthe' ainsi qu'un
		flottant correspondant au temps écoulé depuis le lancement de la partie, 'temps'.
		Utilise les fonctions prédéfinies du module 'upemtk' pour dessiner l'HUD du jeu. 
	"""
	# Background de la fenêtre
	rectangle(0, 0, 1000, 450, epaisseur = "3", remplissage = 'white')
	rectangle(0, 450, 1000, 600, epaisseur = "3")
	# Affichage du temps
	texte(3, 451, "Temps :", taille = "18")
	texte(95, 451, temps, taille = "18")
	# Affichage du visage du personnage
	rectangle(224, 476, 326, 578)
	visage_personnage = randint(1, 6)
	if visage_personnage == 1:
		image(225, 477, "img/visages_personnage/confus.gif", ancrage= NW)
	if visage_personnage == 2:
		image(225, 477, "img/visages_personnage/heureux.gif", ancrage= NW)
	if visage_personnage == 3:
		image(225, 477, "img/visages_personnage/neutre.gif", ancrage= NW)
	if visage_personnage == 4:
		image(225, 477, "img/visages_personnage/souriant.gif", ancrage= NW)
	if visage_personnage == 5:
		image(225, 477, "img/visages_personnage/surpris.gif", ancrage= NW)
	if visage_personnage == 6:
		image(225, 477, "img/visages_personnage/triste.gif", ancrage= NW)
	# Bouton rotation gauche
	rectangle(333, 451, 444, 525)
	image(334, 452, 'img/rotationgauche.gif', ancrage = NW)
	# Bouton avant
	rectangle(444, 451, 555, 525)
	image(445, 452, 'img/flechehaut.gif', ancrage = NW)
	# Bouton rotation droite
	rectangle(555, 451, 666, 525)
	image(556, 452, 'img/rotationdroite.gif', ancrage = NW)
	# Bouton gauche
	rectangle(333, 525, 444, 599)
	image(334, 526, 'img/flechegauche.gif', ancrage = NW)
	# Bouton arrière
	rectangle(444, 525, 555, 599)
	image(445, 526, 'img/flechebas.gif', ancrage = NW)
	# Bouton droite
	rectangle(555, 525, 666, 599)
	image(556, 526, 'img/flechedroite.gif', ancrage = NW)
	# Carte
	if niveau_du_labyrinthe == 1:
		image(667, 451, 'img/plans_labyrinthes/niveau_1.gif', ancrage = NW)
	if niveau_du_labyrinthe == 2:
		image(667, 451, 'img/plans_labyrinthes/niveau_2.gif', ancrage = NW)
	if niveau_du_labyrinthe == 3:
		image(667, 451, 'img/plans_labyrinthes/niveau_3.gif', ancrage = NW)
	if niveau_du_labyrinthe == 4:
		image(667, 451, 'img/plans_labyrinthes/niveau_4.gif', ancrage = NW)
	if niveau_du_labyrinthe == 5:
		image(667, 451, 'img/plans_labyrinthes/niveau_5.gif', ancrage = NW)
	if niveau_du_labyrinthe == 6:
		image(667, 451, 'img/plans_labyrinthes/niveau_6.gif', ancrage = NW)

def affichage_graphismes(profondeur_vision, liste_positions_virages_gauche, liste_positions_virages_droite):
	"""
		Prends en arguments:
		- Un entier correspondant à l'espace entre le personnage et le prochain mur, 'profondeur_vision';
		- Une liste contenant les emplacements de tous les virages à gauche en face du personnage, 'liste_positions_virages_gauche';
		- Une liste contenant les emplacements de tous les virages à droite en face du personnage, 'liste_positions_virages_droite'.
		Utilise les fonctions prédéfinies du module 'upemtk' ainsi que les fonctions sans arguments contenues
		dans le fichier 'graphismes_du_labyrinthe.py' pour dessiner les graphismes du jeu.
	"""
	# Si la profondeur de la vision est égale à 0
	if profondeur_vision == 0:
		# Affichage du bloc de profondeur 0 en face du personnage
		profondeur0()
		# Affichage des virages à gauche du personnage
		if len(liste_positions_virages_gauche) > 0:
			profondeur0viragegauche()
		# Affichage des virages à droite du personnage
		if len(liste_positions_virages_droite) > 0:
			profondeur0viragedroite()
	# Si la profondeur de la vision est égale à 1
	elif profondeur_vision == 1:
		# Affichage du bloc de profondeur 1 en face du personnage
		profondeur1()
		# Affichage des virages à gauche du personnage
		if len(liste_positions_virages_gauche) > 0:
			if liste_positions_virages_gauche[0] == 0:
				profondeur0viragegauche()
			if liste_positions_virages_gauche[0] == 1:
				profondeur1viragegauche()
		# Affichage des virages à droite du personnage
		if len(liste_positions_virages_droite) > 0:
			if liste_positions_virages_droite[0] == 0:
				profondeur0viragedroite()
			if liste_positions_virages_droite[0] == 1:
				profondeur1viragedroite()
	# Si la profondeur de la vision est égale à 2
	elif profondeur_vision == 2:
		# Affichage du bloc de profondeur 2 en face du personnage
		profondeur2()
		# Affichage des virages à gauche du personnage
		if len(liste_positions_virages_gauche) > 0:
			if liste_positions_virages_gauche[0] == 0:
				profondeur0viragegauche()
			if liste_positions_virages_gauche[0] == 1:
				profondeur1viragegauche()
			if liste_positions_virages_gauche[0] == 2:
				profondeur2viragegauche()
		if len(liste_positions_virages_gauche) > 1:
			if liste_positions_virages_gauche[1] == 0:
				profondeur0viragegauche()
			if liste_positions_virages_gauche[1] == 1:
				profondeur1viragegauche()
			if liste_positions_virages_gauche[1] == 2:
				profondeur2viragegauche()
		# Affichage des virages à droite du personnage
		if len(liste_positions_virages_droite) > 0:
			if liste_positions_virages_droite[0] == 0:
				profondeur0viragedroite()
			if liste_positions_virages_droite[0] == 1:
				profondeur1viragedroite()
			if liste_positions_virages_droite[0] == 2:
				profondeur2viragedroite()
		if len(liste_positions_virages_droite) > 1:
			if liste_positions_virages_droite[1] == 0:
				profondeur0viragedroite()
			if liste_positions_virages_droite[1] == 1:
				profondeur1viragedroite()
			if liste_positions_virages_droite[1] == 2:
				profondeur2viragedroite()
	# Si la profondeur de la vision est égale à 3
	elif profondeur_vision == 3:
		# Affichage du bloc de profondeur 3 en face du personnage
		profondeur3()
		# Affichage des virages à gauche du personnage
		if len(liste_positions_virages_gauche) > 0:
			if liste_positions_virages_gauche[0] == 0:
				profondeur0viragegauche()
			if liste_positions_virages_gauche[0] == 1:
				profondeur1viragegauche()
			if liste_positions_virages_gauche[0] == 2:
				profondeur2viragegauche()
			if liste_positions_virages_gauche[0] == 3:
				profondeur3viragegauche()
		if len(liste_positions_virages_gauche) > 1:
			if liste_positions_virages_gauche[1] == 0:
				profondeur0viragegauche()
			if liste_positions_virages_gauche[1] == 1:
				profondeur1viragegauche()
			if liste_positions_virages_gauche[1] == 2:
				profondeur2viragegauche()
			if liste_positions_virages_gauche[1] == 3:
				profondeur3viragegauche()
		if len(liste_positions_virages_gauche) > 2:
			if liste_positions_virages_gauche[2] == 0:
				profondeur0viragegauche()
			if liste_positions_virages_gauche[2] == 1:
				profondeur1viragegauche()
			if liste_positions_virages_gauche[2] == 2:
				profondeur2viragegauche()
			if liste_positions_virages_gauche[2] == 3:
				profondeur3viragegauche()
		# Affichage des virages à droite du personnage
		if len(liste_positions_virages_droite) > 0:
			if liste_positions_virages_droite[0] == 0:
				profondeur0viragedroite()
			if liste_positions_virages_droite[0] == 1:
				profondeur1viragedroite()
			if liste_positions_virages_droite[0] == 2:
				profondeur2viragedroite()
			if liste_positions_virages_droite[0] == 3:
				profondeur3viragedroite()
		if len(liste_positions_virages_droite) > 1:
			if liste_positions_virages_droite[1] == 0:
				profondeur0viragedroite()
			if liste_positions_virages_droite[1] == 1:
				profondeur1viragedroite()
			if liste_positions_virages_droite[1] == 2:
				profondeur2viragedroite()
			if liste_positions_virages_droite[1] == 3:
				profondeur3viragedroite()
		if len(liste_positions_virages_droite) > 2:
			if liste_positions_virages_droite[2] == 0:
				profondeur0viragedroite()
			if liste_positions_virages_droite[2] == 1:
				profondeur1viragedroite()
			if liste_positions_virages_droite[2] == 2:
				profondeur2viragedroite()
			if liste_positions_virages_droite[2] == 3:
				profondeur3viragedroite()
	# Si la profondeur de la vision est superieure à 3
	else:
		# Affichage du bloc de profondeur n en face du personnage
		profondeurn()
		# Affichage des virages à gauche du personnage
		if len(liste_positions_virages_gauche) > 0:
			if liste_positions_virages_gauche[0] == 0:
				profondeur0viragegauche()
			if liste_positions_virages_gauche[0] == 1:
				profondeur1viragegauche()
			if liste_positions_virages_gauche[0] == 2:
				profondeur2viragegauche()
			if liste_positions_virages_gauche[0] == 3:
				profondeur3viragegauche()
		if len(liste_positions_virages_gauche) > 1:
			if liste_positions_virages_gauche[1] == 0:
				profondeur0viragegauche()
			if liste_positions_virages_gauche[1] == 1:
				profondeur1viragegauche()
			if liste_positions_virages_gauche[1] == 2:
				profondeur2viragegauche()
			if liste_positions_virages_gauche[1] == 3:
				profondeur3viragegauche()
		if len(liste_positions_virages_gauche) > 2:
			if liste_positions_virages_gauche[2] == 0:
				profondeur0viragegauche()
			if liste_positions_virages_gauche[2] == 1:
				profondeur1viragegauche()
			if liste_positions_virages_gauche[2] == 2:
				profondeur2viragegauche()
			if liste_positions_virages_gauche[2] == 3:
				profondeur3viragegauche()
		# Affichage des virages à droite du personnage
		if len(liste_positions_virages_droite) > 0:
			if liste_positions_virages_droite[0] == 0:
				profondeur0viragedroite()
			if liste_positions_virages_droite[0] == 1:
				profondeur1viragedroite()
			if liste_positions_virages_droite[0] == 2:
				profondeur2viragedroite()
			if liste_positions_virages_droite[0] == 3:
				profondeur3viragedroite()
		if len(liste_positions_virages_droite) > 1:
			if liste_positions_virages_droite[1] == 0:
				profondeur0viragedroite()
			if liste_positions_virages_droite[1] == 1:
				profondeur1viragedroite()
			if liste_positions_virages_droite[1] == 2:
				profondeur2viragedroite()
			if liste_positions_virages_droite[1] == 3:
				profondeur3viragedroite()
		if len(liste_positions_virages_droite) > 2:
			if liste_positions_virages_droite[2] == 0:
				profondeur0viragedroite()
			if liste_positions_virages_droite[2] == 1:
				profondeur1viragedroite()
			if liste_positions_virages_droite[2] == 2:
				profondeur2viragedroite()
			if liste_positions_virages_droite[2] == 3:
				profondeur3viragedroite()

def boucle_du_jeu(action, coordonnees_du_personnage, orientation_du_personnage, liste_plan_du_labyrinthe, profondeur_vision, liste_positions_virages_gauche, liste_positions_virages_droite, niveau_du_labyrinthe, temps):
	""" 
		Prends en argument : 
		- La chaîne de caractères correspondant à une action, 'action'; 
		- La liste correspondant aux coordonnées du personnage, 'coordonnees_du_personnage'; 
		- La chaîne de caractères correspondant à l'orientation du personnage, 'orientation_du_personnage';
		- La liste correspondant à la liste du plan du labyrinthe, 'liste_plan_du_labyrinthe';
		- L'entier correspondant à l'espace entre le personnage et le prochain mur, 'profondeur_vision';
		- La liste contenant les emplacements de tous les virages à gauche en face du personnage, 'liste_positions_virages_gauche';
		- La liste contenant les emplacements de tous les virages à droite en face du personnage, 'liste_positions_virages_droite';
		- L'entier correspondant au niveau du labyrinthe, 'niveau_du_labyrinthe';
		- Le flottant correspondant au temps écoulé depuis le lancement de la partie, 'temps'.
		Utilise les fonctions du labyrinthe pour faire tourner le jeu.
		Renvoie :
		- La chaîne de caractères correspondant à une action, 'action'; 
		- La liste correspondant aux coordonnées du personnage, 'coordonnees_du_personnage'; 
		- La chaîne de caractères correspondant à l'orientation du personnage, 'orientation_du_personnage';
		- La liste correspondant à la liste du plan du labyrinthe, 'liste_plan_du_labyrinthe';
		- L'entier correspondant à l'espace entre le personnage et le prochain mur, 'profondeur_vision';
		- La liste contenant les emplacements de tous les virages à gauche en face du personnage, 'liste_positions_virages_gauche';
		- La liste contenant les emplacements de tous les virages à droite en face du personnage, 'liste_positions_virages_droite';
		- L'entier correspondant au niveau du labyrinthe, 'niveau_du_labyrinthe';
		- Le flottant correspondant au temps écoulé depuis le lancement de la partie, 'temps'.
	"""
	efface_tout()
	# Affichage de l'HUD
	affichage_HUD(niveau_du_labyrinthe, temps)
	# Calculs de l'affichage des graphismes
	profondeur_vision = calcul_profondeur_vision(coordonnees_du_personnage, orientation_du_personnage, liste_plan_du_labyrinthe)
	liste_positions_virages_gauche, liste_positions_virages_droite = calcul_positions_virages(coordonnees_du_personnage, orientation_du_personnage, profondeur_vision, liste_plan_du_labyrinthe)
	# Affichage des graphismes
	affichage_graphismes(profondeur_vision, liste_positions_virages_gauche, liste_positions_virages_droite)
	coordonnees_du_clic = attente_clic()
	# Décisions de l'action à effectuer par le personnage
	action = attribution_des_actions(coordonnees_du_clic)
	# Boucle permettant à l'utilisateur de cliquer ailleurs que sur les boutons sans provoquer d'erreur
	while action == 'none':
		coordonnees_du_clic = attente_clic()
		action = attribution_des_actions(coordonnees_du_clic)
	# Déplacement du personnage
	coordonnees_du_personnage, orientation_du_personnage, liste_plan_du_labyrinthe = deplacement_personnage(action, coordonnees_du_personnage, orientation_du_personnage, liste_plan_du_labyrinthe)
	return action, coordonnees_du_personnage, orientation_du_personnage, liste_plan_du_labyrinthe, profondeur_vision, liste_positions_virages_gauche, liste_positions_virages_droite, niveau_du_labyrinthe, temps

def calcul_profondeur_vision(coordonnees_du_personnage, orientation_du_personnage, liste_plan_du_labyrinthe):
	"""
		Prends en argument :  
		- La liste correspondant aux coordonnées du personnage, 'coordonnees_du_personnage'; 
		- La chaîne de caractères correspondant à l'orientation du personnage, 'orientation_du_personnage';
		- La liste correspondant à la liste du plan du labyrinthe, 'liste_plan_du_labyrinthe'.
		Calcule l'espace se trouvant entre le personnage et le mur devant lui.
		Retourne un entier correspondant à la profondeur de sa vision, 'profondeur_vision'.
	"""
	x_personnage = coordonnees_du_personnage[0]
	y_personnage = coordonnees_du_personnage[1]
	profondeur_vision = 0
	## Calcul de l'espace se trouvant entre le personnage et le mur devant lui
	# Si le personnage est orienté vers le Nord
	if orientation_du_personnage == 'nord':
		while liste_plan_du_labyrinthe[y_personnage - profondeur_vision][x_personnage] != '*':
			profondeur_vision += 1
	# Si le personnage est orienté vers l'Est
	elif orientation_du_personnage == 'est':
		while liste_plan_du_labyrinthe[y_personnage][x_personnage + profondeur_vision] != '*':
			profondeur_vision += 1
	# Si le personnage est orienté vers le Sud
	elif orientation_du_personnage == 'sud':
		while liste_plan_du_labyrinthe[y_personnage + profondeur_vision][x_personnage] != '*':
			profondeur_vision += 1
	# Si le personnage est orienté vers l'Ouest
	elif orientation_du_personnage == 'ouest':
		while liste_plan_du_labyrinthe[y_personnage][x_personnage - profondeur_vision] != '*':
			profondeur_vision += 1
	# Réajustement de la profondeur (La variable était toujours d'une valeur entière au dessus de ce qu'elle devait être)
	profondeur_vision -= 1
	return profondeur_vision

def calcul_positions_virages(coordonnees_du_personnage, orientation_du_personnage, profondeur_vision, liste_plan_du_labyrinthe):
	"""
		Prends en argument :  
		- La liste correspondant aux coordonnées du personnage, 'coordonnees_du_personnage'; 
		- La chaîne de caractères correspondant à l'orientation du personnage, 'orientation_du_personnage';
		- L'entier correspondant à la profondeur de la vision du personnage, 'profondeur_vision';
		- La liste correspondant à la liste du plan du labyrinthe, 'liste_plan_du_labyrinthe'.
		Calcule les positions des virages se trouvant à gauche et à droite du personnage.
		Renvoie:
		- Une liste contenant les positions des virages à gauche du personnage, 'liste_positions_virages_gauche';
		- Une liste contenant les positions des virages à droite du personnage, 'liste_positions_virages_droite'.
	"""
	x_personnage = coordonnees_du_personnage[0]
	y_personnage = coordonnees_du_personnage[1]
	profondeur_vision += 1
	compteur = 0
	liste_positions_virages_gauche = []
	liste_positions_virages_droite = []
	## Calcul des positions des virages à droite et à gauche du personnage
	# Si le personnage est orienté vers le Nord
	if orientation_du_personnage == 'nord':
		while compteur != profondeur_vision:
			if liste_plan_du_labyrinthe[y_personnage - compteur][x_personnage - 1] == '.':
				liste_positions_virages_gauche.append(compteur)
			if liste_plan_du_labyrinthe[y_personnage - compteur][x_personnage + 1] == '.':
				liste_positions_virages_droite.append(compteur)
			compteur += 1
	# Si le personnage est orienté vers l'Est
	elif orientation_du_personnage == 'est':
		while compteur != profondeur_vision:
			if liste_plan_du_labyrinthe[y_personnage - 1][x_personnage + compteur] == '.':
				liste_positions_virages_gauche.append(compteur)
			if liste_plan_du_labyrinthe[y_personnage + 1][x_personnage + compteur] == '.':
				liste_positions_virages_droite.append(compteur)
			compteur += 1
	# Si le personnage est orienté vers le Sud
	elif orientation_du_personnage == 'sud':
		while compteur != profondeur_vision:
			if liste_plan_du_labyrinthe[y_personnage + compteur][x_personnage + 1] == '.':
				liste_positions_virages_gauche.append(compteur)
			if liste_plan_du_labyrinthe[y_personnage + compteur][x_personnage - 1] == '.':
				liste_positions_virages_droite.append(compteur)
			compteur += 1
	# Si le personnage est orienté vers l'Ouest
	elif orientation_du_personnage == 'ouest':
		while compteur != profondeur_vision:
			if liste_plan_du_labyrinthe[y_personnage + 1][x_personnage - compteur] == '.':
				liste_positions_virages_gauche.append(compteur)
			if liste_plan_du_labyrinthe[y_personnage - 1][x_personnage - compteur] == '.':
				liste_positions_virages_droite.append(compteur)
			compteur += 1
	return liste_positions_virages_gauche, liste_positions_virages_droite

def verification_nouveau_record(niveau_du_labyrinthe, temps):
	"""
		Prends en argument un entier correspondant au niveau du labyrinthe 'niveau_du_labyrinthe', et
		un flottant correspondant au temps mit par le joueur pour finir le labyrinthe, 'temps'.
		Teste si le 'temps' est meilleur que ceux des records du 'niveau_du_labyrinthe'.
		Si oui, le fichier texte est modifié en conséquence et la fonction retourne True.
		Sinon, la fonction retourne False.
	"""
	nouveau_record = False
	# Ouverture du fichier de records correspondant au niveau du labyrinthe
	if niveau_du_labyrinthe == 1:
		fichier = open("meilleurs_temps/niveau_1.txt", "r")
	if niveau_du_labyrinthe == 2:
		fichier = open("meilleurs_temps/niveau_2.txt", "r")
	if niveau_du_labyrinthe == 3:
		fichier = open("meilleurs_temps/niveau_3.txt", "r")
	if niveau_du_labyrinthe == 4:
		fichier = open("meilleurs_temps/niveau_4.txt", "r")
	if niveau_du_labyrinthe == 5:
		fichier = open("meilleurs_temps/niveau_5.txt", "r")
	if niveau_du_labyrinthe == 6:
		fichier = open("meilleurs_temps/niveau_6.txt", "r")
	# Attribution des variables des records de ce fichier à leur valeur correspondante
	premier_record = float(fichier.readline())
	deuxieme_record = float(fichier.readline())
	troisieme_record = float(fichier.readline())
	fichier.close()
	# Comparaison entre les records et le temps de l'utilisateur
	# Si l'utilisateur a battu le meilleur record
	if temps < premier_record:
		troisieme_record = deuxieme_record
		deuxieme_record = premier_record
		premier_record = temps
		nouveau_record = True
	# Si l'utilisateur a battu le second meilleur record
	elif temps < deuxieme_record:
		troisieme_record = deuxieme_record
		deuxieme_record = temps
		nouveau_record = True
	# Si l'utilisateur a battu le troisième meilleur record
	elif temps < troisieme_record:
		troisieme_record = temps
		nouveau_record = True
	## Réécriture du nouveau record dans le fichier de records du niveau du labyrinthe correspondant
	# Ouverture du fichier de records correspondant au niveau du labyrinthe
	if niveau_du_labyrinthe == 1:
		fichier = open("meilleurs_temps/niveau_1.txt", "w")
	if niveau_du_labyrinthe == 2:
		fichier = open("meilleurs_temps/niveau_2.txt", "w")
	if niveau_du_labyrinthe == 3:
		fichier = open("meilleurs_temps/niveau_3.txt", "w")
	if niveau_du_labyrinthe == 4:
		fichier = open("meilleurs_temps/niveau_4.txt", "w")
	if niveau_du_labyrinthe == 5:
		fichier = open("meilleurs_temps/niveau_5.txt", "w")
	if niveau_du_labyrinthe == 6:
		fichier = open("meilleurs_temps/niveau_6.txt", "w")
	# Réécriture
	fichier.write(str(premier_record) + "\n")
	fichier.write(str(deuxieme_record) + "\n")
	fichier.write(str(troisieme_record) + "\n")
	fichier.close()
	return nouveau_record

def affichage_meilleurs_scores(niveau_du_labyrinthe):
	"""
		Lit le fichier texte correspondant aux records du niveau du labyrinthe 'niveau_du_labyrinthe'.
		Affiche ces records grâce aux fonctions du moudle 'upemtk'
	"""
	# Ouverture du fichier de records correspondant au niveau du labyrinthe
	if niveau_du_labyrinthe == 1:
		fichier = open("meilleurs_temps/niveau_1.txt", "r")
	if niveau_du_labyrinthe == 2:
		fichier = open("meilleurs_temps/niveau_2.txt", "r")
	if niveau_du_labyrinthe == 3:
		fichier = open("meilleurs_temps/niveau_3.txt", "r")
	if niveau_du_labyrinthe == 4:
		fichier = open("meilleurs_temps/niveau_4.txt", "r")
	if niveau_du_labyrinthe == 5:
		fichier = open("meilleurs_temps/niveau_5.txt", "r")
	if niveau_du_labyrinthe == 6:
		fichier = open("meilleurs_temps/niveau_6.txt", "r")
	# Attribution des variables des records de ce fichier à leur valeur correspondante
	premier_record = float(fichier.readline())
	deuxieme_record = float(fichier.readline())
	troisieme_record = float(fichier.readline())
	fichier.close()
	## Affichage
	# Background
	rectangle(370, 335, 630, 405, remplissage = "#868686")
	# Affichage du premier record
	texte(500, 350, "Premier :" + str(premier_record), couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 18)
	# Affichage du second record
	texte(500, 370, "Deuxième :" + str(deuxieme_record), couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 18)
	# Affichage du troisième record
	texte(500, 390, "Troisième :" + str(troisieme_record), couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 18)
	# Bouton de sortie du jeu
	rectangle(400, 490, 600, 530, couleur = '#708090', remplissage = "#868686")
	texte(500, 510, "Quitter", couleur = 'black', ancrage = CENTER, police = 'Purisa', taille = 18)