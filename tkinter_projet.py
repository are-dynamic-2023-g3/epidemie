
# -*- coding: utf-8 -*-

import numpy as np
import tkinter as Tk
from matplotlib import pyplot as plt



monde_test=[[1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
 [3, 1, 1, 1, 1, 0, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 3, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [0, 1, 1, 1, 0, 1, 1, 0, 1, 1],
 [0, 1, 1, 1, 1, 1, 1, 2, 1, 0],
 [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
 [0, 1, 1, 1, 0, 0, 1, 1, 0, 1]]



def number_to_color(world:list)->list:
    """
    On crée un nouveau tableau "str_world" de dimensions identiques à "world"
    On parcourt ensuite "world" et, selon les types des individus, on les identifie à une couleur que l'on place dans
    "str_world", aux mêmes coordonnées de l'individu en question
    
    Par exemple :
    
    monde=[[0, 3, 1, 1, 2, 2],
       [2, 3, 0, 2, 3, 0],
       [4, 0, 1, 3, 0, 1],
       [2, 2, 3, 1, 2, 3],
       [1, 3, 0, 2, 2, 2],
       [2, 3, 3, 2, 2, 4]]

    str_world=[['white', 'orange', 'blue', 'blue', 'green', 'green'],
     ['green', 'orange', 'white', 'green', 'orange', 'white'],
     ['red', 'white', 'blue', 'orange', 'white', 'blue'],
     ['green', 'green', 'orange', 'blue', 'green', 'orange'],
     ['blue', 'red', 'white', 'green', 'green', 'green'],
     ['green', 'orange', 'orange', 'green', 'green', 'red']]
     
    """
    str_world=[]
    
    for y in range(len(world)):
        str_world.append([])
        for x in range(len(world[0])):
            
            if world[y][x]==0:
                str_world[y].append("white")
            elif world[y][x]==1:
                str_world[y].append("blue")
            elif world[y][x]==2:
                str_world[y].append("green")
            elif world[y][x]==3:
                str_world[y].append("orange")
            elif world[y][x]==4:
                str_world[y].append("red")            

    
    return str_world



def delete_grille():
    """
    Utilisé à chaque création de monde pour détruire la grille de la fenetre Tkinter et les elements y étant 
    """
    for widget in fenetre.winfo_children():
        widget.grid_forget()
        widget.destroy()



def generer_world(aleatoire:bool,nb_S, nb_E, nb_I, nb_R):
    """
    Permet de setup la représentation du monde
    """
    
    delete_grille()
    
    if (aleatoire==True):
        world=generate_random_world_SEIR()
    else:
        world=generate_world_SEIR(nb_S, nb_E, nb_I, nb_R)
    
    afficher_monde_tkinter(world,0,0,0,0)


# On cree notre fenetre Tkinter

def setup_tkinter():

    fenetre = Tk.Tk()
    
    fenetre.title("Etude d'évolution d'épidémie")
    fenetre.config(bg = "#87CEEB") 
    fenetre.geometry("1000x400+500+300")
    
    
    
    for i in range(4):
        fenetre.columnconfigure(i, weight=1)

    
    for j in range(6):
        fenetre.rowconfigure(j, weight=1)
    
    
    
    
    
    
    nb_S=Tk.IntVar()
    nb_E=Tk.IntVar()
    nb_I=Tk.IntVar()
    nb_R=Tk.IntVar()
    
    
    Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus \n sains : ",font=("Arial",20,"bold")).grid(row=0, column=0,sticky='nesw',columnspan=2)
    Tk.Scale(fenetre,variable=nb_S,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=0, column=2,sticky='nesw',columnspan=2)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus infectés \n non infectieux : ",font=("Arial",20,"bold")).grid(row=1, column=0,sticky='nesw',columnspan=2)
    Tk.Scale(fenetre,variable=nb_E,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=1, column=2,sticky='nesw',columnspan=2)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus infectés \n infectieux : ",font=("Arial",20,"bold")).grid(row=2, column=0,sticky='nesw',columnspan=2)
    Tk.Scale(fenetre,variable=nb_I,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=2, column=2,sticky='nesw',columnspan=2)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus retirés \n (guéris ou morts) : ",font=("Arial",20,"bold")).grid(row=3, column=0,sticky='nesw',columnspan=2)
    Tk.Scale(fenetre,variable=nb_R,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=3, column=2,sticky='nesw',columnspan=2)
    
    
    
    
    Tk.Button(fenetre, text = "Générer un monde \n selon paramètres",font=("Arial",30),command=lambda:generer_world(False,0,0,0,0)).grid(row=4, column=2,columnspan=2,rowspan=2)
    
    Tk.Button(fenetre, text = "Générer un monde \n aléatoire",font=("Arial",30),command=lambda:generer_world(True,0,0,0,0)).grid(row=4, column=0,columnspan=2,rowspan=2)
    
    
    fenetre.mainloop()
    
 
setup_tkinter()



def afficher_monde_tkinter(world,old_incubation,old_transmission,old_guerison,old_mortalite):
    
    pass