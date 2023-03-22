
# -*- coding: utf-8 -*-

import numpy as np
import tkinter as Tk
from matplotlib import pyplot as plt
from main import *



def center_window(w):
    eval_ = w.nametowidget('.').eval
    eval_('tk::PlaceWindow %s center' % w)




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



def delete_grille(fenetre):

    for widget in fenetre.winfo_children():
        widget.grid_forget()
        widget.destroy()



def generer_world(fenetre,aleatoire:bool,nb_S, nb_E, nb_I, nb_R,somme):
    """
    Permet de setup la représentation du monde
    """
    
    if (aleatoire==True):
        delete_grille(fenetre)
        world=generate_random_world_SEIR()
        afficher_monde_tkinter(fenetre,world,0,0,0,0,0)
        
    elif (aleatoire==False and somme <=100):
        delete_grille(fenetre)
        world=generate_world_SEIR(nb_S, nb_E, nb_I, nb_R)
        afficher_monde_tkinter(fenetre,world,0,0,0,0,0)
    
    elif (aleatoire==False and somme >100): 
        setup_tkinter(False,fenetre)
    
    


# On cree notre fenetre Tkinter

def setup_tkinter(first_time:bool,fenetre):

    
    if (first_time==True):
        
        if (fenetre!=False):
            fenetre.destroy()

        fenetre = Tk.Tk()
        
        fenetre.title("Paramètres évolution d'épidémie")
        fenetre.config(bg = "#87CEEB") 
        
        #fenetre.geometry("1000x400+500+300")
        fenetre.geometry("1000x600")
        center_window(fenetre)
        
        
        
        for i in range(4):
            fenetre.columnconfigure(i, weight=1)
    
        
        for j in range(7):
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
        
        
        
        Tk.Button(fenetre, text = "Générer un monde \n selon paramètres",font=("Arial",30),command=lambda:generer_world(fenetre,False,int(nb_S.get()),int(nb_E.get()),int(nb_I.get()),int(nb_R.get()),somme=int(nb_S.get())+int(nb_E.get())+int(nb_I.get())+int(nb_R.get()))).grid(row=5, column=2,columnspan=2,rowspan=2)
        
        Tk.Button(fenetre, text = "Générer un monde \n aléatoire",font=("Arial",30),command=lambda:generer_world(fenetre,True,0,0,0,0,somme=int(nb_S.get())+int(nb_E.get())+int(nb_I.get())+int(nb_R.get()))).grid(row=5, column=0,columnspan=2,rowspan=2) 
        
        fenetre.mainloop()
        
    else:
        
        Tk.Label(fenetre,bg="#87CEEB",text="Sélectionnez une somme d'individus ne dépassant pas 100",font=("Arial",20,"bold"),fg="Red").grid(row=4, column=0,sticky='nesw',columnspan=4)






def afficher_monde_tkinter(fenetre,world,old_incubation,old_transmission,old_guerison,old_mortalite,nb_tours):
    
    delete_grille(fenetre)
    
    fenetre.geometry("1000x600+200+150")
    fenetre.title("Modélisation évolution d'épidémie")
    
    
    
    # Setup la fenêtre en grille
    
    for i in range(16):
        fenetre.columnconfigure(i, weight=1)
    for j in range(20):
        fenetre.rowconfigure(j, weight=1)
    
    
    world_color=number_to_color(world)
    
    # Sert à attribuer les couleurs aux cases de la grille selon les types
    
    for y in range(10):
        for x in range(10):
            Tk.Label(fenetre,bg=world_color[y][x]).grid(row=y, column=x,sticky='nesw',padx=5, pady=5)
    
    
    
    
    # Partie affichée des paramètres à droite du monde
    
    text_nb_tours=str(nb_tours)
    Tk.Label(fenetre,bg="#87CEEB",text="Tours : "+text_nb_tours,font=("Arial",30,"bold")).grid(row=0, column=10,sticky='nesw',columnspan=2,rowspan=2)
    
    incubation = Tk.IntVar()
    transmission = Tk.IntVar()
    guerison = Tk.IntVar()
    mortalite = Tk.IntVar()
    
    
    incubation.set(old_incubation)
    transmission.set(old_transmission)
    guerison.set(old_guerison)
    mortalite.set(old_mortalite)
    
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage \nd'incubation :",font=("Arial",14,"bold")).grid(row=2, column=10,sticky='nesw',rowspan=2)
    Tk.Scale(fenetre,variable=incubation,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=2, column=11,rowspan=2)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage de \ntransmission :",font=("Arial",14,"bold")).grid(row=4, column=10,sticky='nesw',rowspan=2)
    Tk.Scale(fenetre,variable=transmission,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=4, column=11,rowspan=2)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage de \nguérison :",font=("Arial",14,"bold")).grid(row=6, column=10,sticky='nesw',rowspan=2)
    Tk.Scale(fenetre,variable=guerison,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=6, column=11,rowspan=2)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage de \nmortalité :",font=("Arial",14,"bold")).grid(row=8, column=10,sticky='nesw',rowspan=2)
    Tk.Scale(fenetre,variable=mortalite,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=8, column=11,rowspan=2)
    
    
    Tk.Button(fenetre, text = "Itérer 1 fois le monde",font=("Arial",20),command=lambda:afficher_monde_tkinter(fenetre,evolution_world_SEIR(world,int(incubation.get()),int(transmission.get()),int(guerison.get()),int(mortalite.get())),int(incubation.get()),int(transmission.get()),int(guerison.get()),int(mortalite.get()),nb_tours+1)).grid(row=10, column=10,columnspan=2,rowspan=2)
    
    
    
    
    
    
    
    # Partie affichée sous le monde
    
    Tk.Label(fenetre,bg="#87CEEB",text="Légende :",font=("Arial",20,"bold")).grid(row=10, column=0,sticky='nesw',columnspan=10)
    
    Tk.Label(fenetre,bg="#87CEEB",text="S",font=("Arial",16,"bold")).grid(row=11, column=0,sticky='nesw',columnspan=1)
    Tk.Label(fenetre,bg="blue").grid(row=11, column=1,sticky='nesw',padx=5, pady=5)

    Tk.Label(fenetre,bg="#87CEEB",text="E",font=("Arial",16,"bold")).grid(row=11, column=2,sticky='nesw',columnspan=1)
    Tk.Label(fenetre,bg="green").grid(row=11, column=3,sticky='nesw',padx=5, pady=5)

    Tk.Label(fenetre,bg="#87CEEB",text="I",font=("Arial",16,"bold")).grid(row=11, column=4,sticky='nesw',columnspan=1)
    Tk.Label(fenetre,bg="orange").grid(row=11, column=5,sticky='nesw',padx=5, pady=5)
    
    Tk.Label(fenetre,bg="#87CEEB",text="R",font=("Arial",16,"bold")).grid(row=11, column=6,sticky='nesw',columnspan=1)
    Tk.Label(fenetre,bg="red").grid(row=11, column=7,sticky='nesw',padx=5, pady=5)
    
    Tk.Button(fenetre, text = "Générer un nouveau monde",font=("Arial",20),command=lambda:setup_tkinter(True,fenetre)).grid(row=12, column=0,columnspan=10,pady=10) 
    
    
    
    
    
setup_tkinter(True,False)