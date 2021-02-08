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
LARGEUR = 800
HAUTEUR = 800
DUREE_FEU = 5
DUREE_CENDRE = 5
#########################################



#########################################
#DEFINITION DES VARIABLES GLOBALES
couleurInitiale=""

#########################################


#########################################
#DEFINITION DES FONCTIONS

def couleurTerrain() :
    global couleurInitiale
    a=rd.randint(1,3)
    if a==1 :
        couleurInitiale="blue"
    elif a==2 :
        couleurInitiale="yellow"
    elif a==3 :
        couleurInitiale="green"

def generationTerrains () :
    global couleurInitiale
    couleurTerrain()
    for i in range(0,LARGEUR,25) :
        for j in range(0,HAUTEUR,25) :
            canvas.create_rectangle((i,j), (i+25,j+25), outline = "black", fill=couleurInitiale)
#########################################

#########################################
#PROGRAMME PRINCIPAL 

racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", width = LARGEUR, height = HAUTEUR)
canvas.grid(column=0,row=0)
for i in range(0,LARGEUR,25) :
    for j in range(0,HAUTEUR,25) :
        canvas.create_rectangle((i,j), (i+25,j+25), outline = "black")
button = tk.Button(racine, text="générer des terrains", command = generationTerrains)
button.grid(column=0, row=1)


racine.mainloop()