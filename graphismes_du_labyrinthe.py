# -*- coding: utf-8 -*-
##### Projet 12. Le labyrinthe #####
#### Auteurs : BIZZOZZERO Nicolas, BOUHASTINE Mohamed ####
#### Description du programme ####
# Ce programme contient les images du jeu à afficher

#### Importation des modules / bibliotheques ####
from upemtk import *

### Definition ###
## Definition des fonctions
def profondeur0():
	ligne(0, 0, 100, 50) # Haut gauche
	ligne(0, 450, 100, 400) # Bas gauche
	ligne(900, 50, 1000, 0) # Haut droit
	ligne(900, 400, 1000, 450) # Bas droit
	ligne(100, 50, 900, 50) # Horizontale haute du cadre central
	ligne(100, 400, 900, 400) # Horizontale basse du cadre central
	ligne(100, 50, 100, 400) # Verticale gauche du mur gauche
	ligne(900, 50, 900, 400) # Verticale droite du mur droite
	
def profondeur1():
	ligne(0, 0, 300, 150) # Haut gauche
	ligne(0, 450, 300, 300) # Bas gauche
	ligne(700, 150, 1000, 0) # Haut droit
	ligne(700, 300, 1000, 450) # Bas droit
	ligne(300, 150, 700, 150) # Horizontale haute du cadre central
	ligne(300, 300, 700, 300) # Horizontale basse du cadre central
	ligne(300, 150, 300, 300) # Verticale gauche du cadre central
	ligne(700, 150, 700, 300) # Verticale droite du cadre central
	ligne(100, 50, 100, 400) # Verticale gauche du mur gauche
	ligne(900, 50, 900, 400) # Verticale droite du mur droite

def profondeur2():
	ligne(0, 0, 400, 200) # Haut gauche
	ligne(0, 450, 400, 250) # Bas gauche
	ligne(600, 200, 1000, 0) # Haut droit
	ligne(600, 250, 1000, 450) # Bas droit
	ligne(400, 200, 600, 200) # Horizontale haute du cadre central
	ligne(400, 250, 600, 250) # Horizontale basse du cadre central
	ligne(400, 200, 400, 250) # Verticale gauche du carré central
	ligne(600, 200, 600, 250) # Verticale droite du carré central
	ligne(300, 150, 300, 300) # Verticale gauche du second mur à gauche
	ligne(700, 150, 700, 300) # Verticale droite du second mur à droite
	ligne(100, 50, 100, 400) # Verticale gauche du premier mur à gauche
	ligne(900, 50, 900, 400) # Verticale droite du premier mur à droite


def profondeur3():
	ligne(0, 0, 450, 225) # Haut gauche
	ligne(0, 450, 450, 225) # Bas gauche
	ligne(550, 225, 1000, 0) # Haut droit
	ligne(550, 225, 1000, 450) # Bas droit
	ligne(450, 225, 550, 225) # Horizontale haute du cadre central
	ligne(450, 224, 550, 224) # Horizontale basse du cadre central
	ligne(400, 200, 400, 250) # Verticale gauche du carré central
	ligne(600, 200, 600, 250) # Verticale droite du carré central
	ligne(300, 150, 300, 300) # Verticale gauche du second mur à gauche
	ligne(700, 150, 700, 300) # Verticale droite du second mur à droite
	ligne(100, 50, 100, 400) # Verticale gauche du premier mur à gauche
	ligne(900, 50, 900, 400) # Verticale droite du premier mur à droite

def profondeurn():
	ligne(0, 0, 450, 225) # Haut gauche
	ligne(0, 450, 450, 225) # Bas gauche
	ligne(550, 225, 1000, 0) # Haut droit
	ligne(550, 225, 1000, 450) # Bas droit
	ligne(400, 200, 400, 250) # Verticale gauche du carré central
	ligne(600, 200, 600, 250) # Verticale droite du carré central
	ligne(300, 150, 300, 300) # Verticale gauche du second mur à gauche
	ligne(700, 150, 700, 300) # Verticale droite du second mur à droite
	ligne(100, 50, 100, 400) # Verticale gauche du premier mur à gauche
	ligne(900, 50, 900, 400) # Verticale droite du premier mur à droite

def profondeur0viragegauche():
	ligne(0, 0, 100, 50, couleur = "white") # Haut gauche
	ligne(0, 450, 100, 400, couleur = "white") # Bas gauche
	ligne(0, 50, 100, 50) # Horizontale haute du carré gauche
	ligne(0, 400, 100, 400) # Horizontale basse du carré gauche

def profondeur0viragedroite():
	ligne(900, 50, 1000, 0, couleur = "white") # Haut droit
	ligne(900, 400, 1000, 450, couleur = "white") # Bas droit
	ligne(900, 50, 1000, 50) # Horizontale haute du carré droit
	ligne(900, 400, 1000, 400) # Horizontale basse du carré droit

def profondeur1viragegauche():
	ligne(100, 50, 300, 150, couleur = "white") # Haut gauche
	ligne(100, 400, 300, 300, couleur = "white") # Bas gauche
	ligne(100, 150, 300, 150) # Horizontale haute du carré gauche
	ligne(100, 300, 300, 300) # Horizontale basse du carré gauche

def profondeur1viragedroite():
	ligne(900, 50, 700, 150, couleur = "white") # Haut droit
	ligne(900, 400, 700, 300, couleur = "white") # Bas droit
	ligne(700, 150, 900, 150) # Horizontale haute du carré droit
	ligne(700, 300, 900, 300) # Horizontale basse du carré droit

def profondeur2viragegauche():
	ligne(300, 150, 400, 200, couleur = "white") # Haut gauche
	ligne(300, 300, 400, 250, couleur = "white") # Bas gauche
	ligne(300, 200, 400, 200) # Horizontale haute du carré gauche
	ligne(300, 250, 400, 250) # Horizontale basse du carré gauche

def profondeur2viragedroite():
	ligne(700, 150, 600, 200, couleur = "white") # Haut droit
	ligne(700, 300, 600, 250, couleur = "white") # Bas droit
	ligne(700, 200, 600, 200) # Horizontale haute du carré droit
	ligne(700, 250, 600, 250) # Horizontale basse du carré droit

def profondeur3viragegauche():
	ligne(400, 200, 450, 225, couleur = "white") # Haut gauche
	ligne(400, 250, 450, 225, couleur = "white") # Bas gauche
	ligne(400, 224, 450, 224) # Horizontale haute du carré gauche
	ligne(400, 225, 450, 225) # Horizontale basse du carré gauche

def profondeur3viragedroite():
	ligne(600, 200, 550, 225, couleur = "white") # Haut droit
	ligne(600, 250, 550, 225, couleur = "white") # Bas droit
	ligne(550, 224, 600, 224) # Horizontale haute du carré droit
	ligne(550, 225, 600, 225) # Horizontale basse du carré droit