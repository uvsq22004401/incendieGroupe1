#########################################
# Informations liées au groupe :
# groupe LDDMP 1
# Nikita DE LA FOURNIERE
# Malek WALLIER
# Theotime MAMOU
# Auguste MAJOU
# Gregoire DUNGLAS
# Keli xaviera DZOUOSSIA MOZIE
#########################################



#########################################
#Import des librairies
import random as rd
import tkinter as tk
#########################################



#########################################
#DEFINITION DES CONSTANTES
LARGEUR = 600
HAUTEUR = 600
DUREE_FEU = 5
DUREE_CENDRE = 5
#########################################



#########################################
#DEFINITION DES VARIABLES GLOBALES
couleurInitiale=""
listeCases = []
listeCouleur = []

#########################################


#########################################
#DEFINITION DES FONCTIONS

def couleurTerrain() :
    global couleurInitiale
    a=rd.randint(1,100)
    if a<21 :
        couleurInitiale="blue"
    elif a<56 :
        couleurInitiale="yellow"
    elif a>55 :
        couleurInitiale="green"

def generationTerrains () :
    global couleurInitiale, listeCases  
    for j in range(0,HAUTEUR,15) :
        for i in range(0,LARGEUR,15) :
            couleurTerrain()
            canvas.create_rectangle((i,j), (i+15,j+15), outline = "black", fill=couleurInitiale)
            identitéCase= [couleurInitiale,j//15,i//15]
            listeCases.append(identitéCase)
            listeCouleur.append(couleurInitiale)
    print(listeCases)
    print(listeCouleur)

#########################################

#########################################
#PROGRAMME PRINCIPAL 

racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", width = LARGEUR, height = HAUTEUR)
canvas.grid(column=0,row=0)
for i in range(0,HAUTEUR,15) :
    for j in range(0,LARGEUR,15) :
        canvas.create_rectangle((i,j), (i+15,j+15), outline = "black")
button = tk.Button(racine, text="générer des terrains", command = generationTerrains)
button.grid(column=0, row=1)


racine.mainloop()