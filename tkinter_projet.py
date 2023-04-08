# -*- coding: utf-8 -*-

import numpy as np
import tkinter as Tk
from tkinter import ttk
from matplotlib import pyplot as plt
from main import *
import copy


from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure



# Utilisé pour les dégradés de couleurs des infections d'individus
code_couleur=["white","#F7FF86","#FFDC00","#FFAA00","#FF7B00","#FF4800",
              "#D90025","#B4004A","#8F006F","#63009B"]


def center_window(fenetre):
    '''
    Fonction qui en étant appellée est censée centrer la fenêtre passée en paramètre.
    '''
    
    eval_ = fenetre.nametowidget('.').eval
    eval_('tk::PlaceWindow %s center' % fenetre)




def number_to_color(world:list)->list:
    '''
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
     
    '''
    str_world=[]
    
    for y in range(len(world)):
        str_world.append([])
        for x in range(len(world[y])):
            
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

def number_to_color2(matrice_infection:list,nb_fenetre)->list:
    """
    Même principe que pour number_to_color, la seule différence est le code couleur
    Fonction appelée pour attribuer les couleurs à la matrice d'infections
    """
    str_world_infections=[]
    
    for y in range(len(matrice_infection)):
        str_world_infections.append([])
        for x in range(len(matrice_infection[y])):
            
            if (len(matrice_infection)==10):
            
                if (nb_fenetre==1):
            
                    if matrice_infection[y][x]==0:
                        str_world_infections[y].append(code_couleur[0])
                    elif matrice_infection[y][x]==1:
                        str_world_infections[y].append(code_couleur[1])
                    elif matrice_infection[y][x]==2:
                        str_world_infections[y].append(code_couleur[2])
                    elif matrice_infection[y][x]==3:
                        str_world_infections[y].append(code_couleur[3])
                    elif matrice_infection[y][x]==4:
                        str_world_infections[y].append(code_couleur[4])
                    elif matrice_infection[y][x]==5:
                        str_world_infections[y].append(code_couleur[5])
                    elif matrice_infection[y][x]>5:
                            str_world_infections[y].append(code_couleur[6])
                            
                elif (nb_fenetre==2):
                    
                    if matrice_infection[y][x]==0:
                        str_world_infections[y].append(code_couleur[0])
                    elif 0<matrice_infection[y][x]<=0.25:
                        str_world_infections[y].append(code_couleur[1])
                    elif 0.25<matrice_infection[y][x]<=0.50:
                        str_world_infections[y].append(code_couleur[2])
                    elif 0.50<matrice_infection[y][x]<=0.75:
                        str_world_infections[y].append(code_couleur[3])
                    elif 0.75<matrice_infection[y][x]<=1:
                        str_world_infections[y].append(code_couleur[4])
                    elif 1<matrice_infection[y][x]<=1.25:
                        str_world_infections[y].append(code_couleur[5])
                    elif matrice_infection[y][x]>1.25:
                            str_world_infections[y].append(code_couleur[6])
            
            elif (len(matrice_infection)==30):

                if matrice_infection[y][x]==0:
                    str_world_infections[y].append(code_couleur[0])
                elif matrice_infection[y][x]==1:
                    str_world_infections[y].append(code_couleur[1])
                elif matrice_infection[y][x]==2:
                    str_world_infections[y].append(code_couleur[2])
                elif matrice_infection[y][x]==3:
                    str_world_infections[y].append(code_couleur[3])
                elif matrice_infection[y][x]==4:
                    str_world_infections[y].append(code_couleur[4])
                elif matrice_infection[y][x]==5:
                    str_world_infections[y].append(code_couleur[5])
                elif matrice_infection[y][x]==6:
                    str_world_infections[y].append(code_couleur[6])
                elif matrice_infection[y][x]==7:
                    str_world_infections[y].append(code_couleur[7])    
                elif matrice_infection[y][x]==8:
                    str_world_infections[y].append(code_couleur[8])  
                elif matrice_infection[y][x]>=9:
                    str_world_infections[y].append(code_couleur[9])    
    
    return str_world_infections



def number_types(world,tab_nb):
    '''
    Renvoit un tableau mis à jour qui contient l'historique du nombre d'individus au fil des tours
    tab_nb[0] -> historique des S
    tab_nb[1] -> historique des E
    tab_nb[2] -> historique des I
    tab_nb[3] -> historique des R
    '''
    
    nb_S=0
    nb_E=0
    nb_I=0
    nb_R=0
    for y in range(len(world)):
        for x in range(len(world[y])):
            
            if world[y][x]==1:
                nb_S=nb_S+1
            elif world[y][x]==2:
                nb_E=nb_E+1
            elif world[y][x]==3:
                nb_I=nb_I+1
            elif world[y][x]==4:
                nb_R=nb_R+1
    
    tab_nb[0].append(nb_S)
    tab_nb[1].append(nb_E)
    tab_nb[2].append(nb_I)
    tab_nb[3].append(nb_R)
    
    return tab_nb


def number_types_en_deplacement(world,tab_nb_deplacement,matrice_infos_deplacement):
    '''
    Renvoit un tableau mis à jour qui contient l'historique du nombre d'individus 
    en déplacement au fil des tours
    tab_nb_deplacement[0] -> historique des S en déplacement
    tab_nb_deplacement[1] -> historique des E en déplacement
    tab_nb_deplacement[2] -> historique des I en déplacement
    tab_nb_deplacement[3] -> historique des R en déplacement
    '''
    
    coordonnees_cible=matrice_infos_deplacement[1]
    
    # Rappel : coordonnees_cible est un tableau de couples (x,y)
    # Ces (x,y) représentent les coordonnées dun indivdus actuellement 
    # en déplacement à ces ccordonnées
    
    nb_S=0
    nb_E=0
    nb_I=0
    nb_R=0
    
    if (len(coordonnees_cible)>0):
        for i in range(len(coordonnees_cible)):
            
            x=coordonnees_cible[i][0]
            y=coordonnees_cible[i][1]
    
            if world[y][x]==1:
                nb_S=nb_S+1
            elif world[y][x]==2:
                nb_E=nb_E+1
            elif world[y][x]==3:
                nb_I=nb_I+1
            elif world[y][x]==4:
                nb_R=nb_R+1
    
    tab_nb_deplacement[0].append(nb_S)
    tab_nb_deplacement[1].append(nb_E)
    tab_nb_deplacement[2].append(nb_I)
    tab_nb_deplacement[3].append(nb_R)
    
    return tab_nb_deplacement    




def delete_grille(fenetre):
    """
    Détruit les éléments d'une fenêtre
    """

    for widget in fenetre.winfo_children():
        if isinstance(widget,Tk.Toplevel):
            widget.destroy()
        else:
            widget.grid_forget()
            widget.destroy()
            
    

# On cree notre fenetre Tkinter

def setup_tkinter(first_time:int,fenetre):
    """
    Setup et affiche notre écran d'accueil, qui demande le nombre d'individus du monde
    et le type du monde.
    """
    
    if (first_time==1):
        
        if (fenetre!=False):
            fenetre.destroy()

        fenetre = Tk.Tk()
        
        fenetre.bind('<Escape>',lambda e: fenetre.destroy())
        
        fenetre.title("Paramètres évolution d'épidémie")
        fenetre.config(bg = "#87CEEB") 
        
        #fenetre.geometry("1000x400+500+300")
        fenetre.geometry("1000x600")
        center_window(fenetre)
        
        
        
        for i in range(8):
            fenetre.columnconfigure(i, weight=1)
    
        
        for j in range(9):
            fenetre.rowconfigure(j, weight=1)
        
    
        nb_S_moyen=Tk.IntVar()
        nb_E_moyen=Tk.IntVar()
        nb_I_moyen=Tk.IntVar()
        nb_R_moyen=Tk.IntVar()
        
        nb_S_grand=Tk.IntVar()
        nb_E_grand=Tk.IntVar()
        nb_I_grand=Tk.IntVar()
        nb_R_grand=Tk.IntVar()
        
        
        Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus \n sains",font=("Arial",18,"bold")).grid(row=0, column=2,sticky='nesw',columnspan=4)
        Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus infectés \n non infectieux",font=("Arial",18,"bold")).grid(row=1, column=2,sticky='nesw',columnspan=4)
        Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus infectés \n infectieux",font=("Arial",18,"bold")).grid(row=2, column=2,sticky='nesw',columnspan=4)
        Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus retirés \n (guéris ou morts)",font=("Arial",18,"bold")).grid(row=3, column=2,sticky='nesw',columnspan=4)
        
        
        Tk.Scale(fenetre,variable=nb_S_moyen,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=0, column=0,columnspan=2)
        Tk.Scale(fenetre,variable=nb_E_moyen,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=1, column=0,columnspan=2)
        Tk.Scale(fenetre,variable=nb_I_moyen,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=2, column=0,columnspan=2)
        Tk.Scale(fenetre,variable=nb_R_moyen,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=3, column=0,columnspan=2)
        
        Tk.Scale(fenetre,variable=nb_S_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=325).grid(row=0, column=6,columnspan=2)
        Tk.Scale(fenetre,variable=nb_E_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=325).grid(row=1, column=6,columnspan=2)
        Tk.Scale(fenetre,variable=nb_I_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=325).grid(row=2, column=6,columnspan=2)
        Tk.Scale(fenetre,variable=nb_R_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=325).grid(row=3, column=6,columnspan=2)        

        
        Tk.Button(fenetre, text = "Générer un monde moyen\n selon paramètres",font=("Arial",20),command=lambda:generer_world(fenetre,False,int(nb_S_moyen.get()),int(nb_E_moyen.get()),int(nb_I_moyen.get()),int(nb_R_moyen.get()),somme=int(nb_S_moyen.get())+int(nb_E_moyen.get())+int(nb_I_moyen.get())+int(nb_R_moyen.get()),maxi=100)).grid(row=5, column=0,columnspan=2,rowspan=2)
        Tk.Button(fenetre, text = "Générer un monde moyen\n aléatoire",font=("Arial",20),command=lambda:generer_world(fenetre,True,0,0,0,0,somme=int(nb_S_moyen.get())+int(nb_E_moyen.get())+int(nb_I_moyen.get())+int(nb_R_moyen.get()),maxi=100)).grid(row=7, column=0,columnspan=2,rowspan=2) 
        
        Tk.Button(fenetre, text = "Générer un grand monde \n selon paramètres",font=("Arial",20),command=lambda:generer_world(fenetre,False,int(nb_S_grand.get()),int(nb_E_grand.get()),int(nb_I_grand.get()),int(nb_R_grand.get()),somme=int(nb_S_grand.get())+int(nb_E_grand.get())+int(nb_I_grand.get())+int(nb_R_grand.get()),maxi=900)).grid(row=5, column=7,columnspan=2,rowspan=2)
        Tk.Button(fenetre, text = "Générer un grand monde \n aléatoire",font=("Arial",20),command=lambda:generer_world(fenetre,True,0,0,0,0,somme=int(nb_S_grand.get())+int(nb_E_grand.get())+int(nb_I_grand.get())+int(nb_R_grand.get()),maxi=900)).grid(row=7, column=7,columnspan=2,rowspan=2) 
        

        
        fenetre.mainloop()
        
    elif (first_time==2):
        Tk.Label(fenetre,bg="#87CEEB",text="Sélectionnez une somme\n d'individus ne dépassant\n pas 100 pour le monde\n moyen",font=("Arial",18,"bold"),fg="Red").grid(row=4, column=2,sticky='nesw',columnspan=4,rowspan=5)

    elif (first_time==3):
        Tk.Label(fenetre,bg="#87CEEB",text="Sélectionnez une somme\n d'individus ne dépassant\n pas 900 pour le grand\n monde",font=("Arial",18,"bold"),fg="Red").grid(row=4, column=2,sticky='nesw',columnspan=4,rowspan=5)



def generer_world(fenetre,aleatoire:bool,nb_S, nb_E, nb_I, nb_R,somme,maxi):
    """
    Permet de setup la représentation du monde
    """

    tab_nb=[[],[],[],[]]
    tab_nb_deplacement=[[],[],[],[]]
    matrice_infos_deplacement=[[],[],[]]
    
    if (aleatoire==True):
        delete_grille(fenetre)
        
        if(maxi==100):
            world=generate_random_world_SEIR()
        else:
            world=generate2_random_world_SEIR()
        
        tab_nb=number_types(world,tab_nb)
        tab_nb_deplacement=number_types_en_deplacement(world,tab_nb_deplacement,matrice_infos_deplacement)
        
        matrice_infection=np.zeros((len(world),len(world)))
        
        # On part du principe qu'un individu non sain a été infecté à l'emplacement 
        # où il a été défini, on l'indique dans matrice_infection
        for y in range(len(matrice_infection)):
            for x in range(len(matrice_infection[0])):
                if ((world[y][x]==2) or (world[y][x]==3) or (world[y][x]==4)):
                    matrice_infection[y][x]=1

        original_world=copy.deepcopy(world)

        afficher_monde_tkinter(fenetre,original_world,world,0,0,0,0,0,0,tab_nb,matrice_infos_deplacement,"Pas de confinement",matrice_infection,tab_nb_deplacement)
        
    elif (aleatoire==False and somme <=maxi):
        delete_grille(fenetre)
        
        if(maxi==100):
            world=generate_world_SEIR(nb_S, nb_E, nb_I, nb_R)
        else:
            world=generate2_world_SEIR(nb_S, nb_E, nb_I, nb_R)

        tab_nb=number_types(world,tab_nb)
        tab_nb_deplacement=number_types_en_deplacement(world,tab_nb_deplacement,matrice_infos_deplacement)
        
        matrice_infection=np.zeros((len(world),len(world)))
        
        # On part du principe qu'un individu non sain a été infecté à l'emplacement 
        # où il a été défini, on l'indique dans matrice_infection
        for y in range(len(matrice_infection)):
            for x in range(len(matrice_infection[0])):
                if ((world[y][x]==2) or (world[y][x]==3) or (world[y][x]==4)):
                    matrice_infection[y][x]=1

        original_world=copy.deepcopy(world)
    
        afficher_monde_tkinter(fenetre,original_world,world,0,0,0,0,0,0,tab_nb,matrice_infos_deplacement,"Pas de confinement",matrice_infection,tab_nb_deplacement)
    
    elif (aleatoire==False and somme >maxi): 
        if (maxi==100):
            setup_tkinter(2,fenetre)
        else :
            setup_tkinter(3,fenetre)














def iterer_tkinter(fenetre,original_world,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement):
    '''
    Fonction intermédiaure appelée par l'itération tkinter, affiche le nouveau 
    monde après itération
    '''
    world,matrice_infos_deplacement=evolution_world_SEIR(world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,matrice_infos_deplacement,confinement,matrice_infection)
    tab_nb=number_types(world,tab_nb)
    tab_nb_deplacement=number_types_en_deplacement(world,tab_nb_deplacement,matrice_infos_deplacement)
    
    afficher_monde_tkinter(fenetre,original_world,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours+1,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement)



def multi_iterer_tkinter(nb_tours_itere,fenetre,original_world,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement):
    '''
    Fonction intermédiaure appelée par l'itération tkinter, affiche le nouveau 
    monde après plusieurs itérations
    '''
    if (nb_tours_itere<0 or nb_tours_itere>200):
        nb_tours_itere=0
    
    
    for i in range(nb_tours_itere):
        world,matrice_infos_deplacement=evolution_world_SEIR(world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,matrice_infos_deplacement,confinement,matrice_infection)
        tab_nb=number_types(world,tab_nb)
        tab_nb_deplacement=number_types_en_deplacement(world,tab_nb_deplacement,matrice_infos_deplacement)
        
    afficher_monde_tkinter(fenetre,original_world,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,(nb_tours+nb_tours_itere),tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement)


def simulation_generale(nb_simus,nb_tours_itere,fenetre2,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement):
    '''
    Permet de récupérer la moyenne de "nb_simus" simulations sur "nb_tours_itere" tours
    à partir d'un monde de départ "world". Affiche ensuite le résultat avec
    la fonction affiche_simus_generales sur l'écran de simulation
    '''
    
    world_simu=[]
    matrice_infos_deplacement_simu=[]
    tab_nb_simu=[]
    tab_nb_deplacement_simu=[]
    matrice_infection_simu=[]
    
    for i in range(nb_simus):
        world_simu=copy.deepcopy(world)
        matrice_infos_deplacement_simu=copy.deepcopy(matrice_infos_deplacement)
        tab_nb_simu=copy.deepcopy(tab_nb)
        tab_nb_deplacement_simu=copy.deepcopy(tab_nb_deplacement)
        matrice_infection_simu_tour=copy.deepcopy(matrice_infection)
        
        for j in range(nb_tours_itere):
            world_simu,matrice_infos_deplacement_simu=evolution_world_SEIR(world_simu,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,matrice_infos_deplacement_simu,confinement,matrice_infection_simu_tour)
            tab_nb_simu=number_types(world_simu,tab_nb_simu)
            tab_nb_deplacement_simu=number_types_en_deplacement(world_simu,tab_nb_deplacement_simu,matrice_infos_deplacement_simu)
        
        
        if (i==0):
            tab_nb_resultat=np.array(tab_nb_simu)
            tab_nb_deplacement_resultat=np.array(tab_nb_deplacement_simu)
            
            matrice_infection_simu=np.array(matrice_infection_simu_tour)
        else:
            tab_nb_resultat=tab_nb_resultat+np.array(tab_nb_simu)
            tab_nb_deplacement_resultat=tab_nb_deplacement_resultat+np.array(tab_nb_deplacement_simu)
            
            matrice_infection_simu=matrice_infection_simu+matrice_infection_simu_tour
        
    
    # On passe tab_nb_resultat et matrice_infection_simu en array avant de les remettre
    # en listes pour faciliter les opérations dans la fonction
    
    tab_nb_resultat=tab_nb_resultat/nb_simus
    tab_nb_resultat=tab_nb_resultat.tolist()
    
    tab_nb_deplacement_resultat=tab_nb_deplacement_resultat/nb_simus
    tab_nb_deplacement_resultat.tolist()
    
    matrice_infection_simu=matrice_infection_simu/nb_simus
    matrice_infection_simu=matrice_infection_simu.tolist()
    
    affiche_simus_generales(fenetre2,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours+nb_tours_itere,tab_nb_resultat,matrice_infos_deplacement_simu,False,confinement,matrice_infection_simu,tab_nb_deplacement_resultat)
        














def show_world(fenetre,world,nb_fenetre:int):
    '''
    Affiche un monde et certaines infos sur lui (les légendes par exemple) sur la fenetre.
    La fenetre en question est déterminée par 'nb_fenetre'.
    'nb_fenetre' = 0 -> fenetre principale
    'nb_fenetre' = 1 -> fenetre de simulation
    '''
    
    
    echelle=1
    echelle_ligne=1
    echelle_pad_grille=1
    
    if(len(world)==30):
        echelle=3
        echelle_ligne=2
        echelle_pad_grille=0.1
    
    
    if (nb_fenetre==1):
        
        
        Tk.Label(fenetre,bg="#87CEEB",text="Légende :",font=("Arial",20,"bold")).grid(row=16*echelle_ligne+2, column=0*echelle,sticky='nesw',columnspan=10*echelle,rowspan=1*echelle_ligne)
        
        Tk.Label(fenetre,bg="#87CEEB",text="S",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=0*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="blue").grid(row=17*echelle_ligne+2, column=1*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
    
        Tk.Label(fenetre,bg="#87CEEB",text="E",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=2*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="green").grid(row=17*echelle_ligne+2, column=3*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
    
        Tk.Label(fenetre,bg="#87CEEB",text="I",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=4*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="orange").grid(row=17*echelle_ligne+2, column=5*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
        
        Tk.Label(fenetre,bg="#87CEEB",text="R",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=6*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="red").grid(row=17*echelle_ligne+2, column=7*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
     
        Tk.Label(fenetre,bg="#87CEEB",text="",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=8*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="#87CEEB").grid(row=17*echelle_ligne+2, column=9*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
     
        # Cache la deuxième ligne de la légende
        Tk.Label(fenetre,bg="#87CEEB").grid(row=18*echelle_ligne+2, column=0*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=(1*echelle_ligne)*15)
    else:
        
        Tk.Label(fenetre,bg="#87CEEB",text="Notre monde avant simulation",font=("Arial",18,"bold")).grid(row=0, column=0,sticky='nesw',columnspan=10,rowspan=2)
        Tk.Label(fenetre,bg="#87CEEB").grid(row=13, column=0,sticky='nesw',rowspan=3,columnspan=10)

    world_color=number_to_color(world)
    
    # Sert à attribuer les couleurs aux cases de la grille du monde selon les types
    
    for y in range(len(world)):
        for x in range(len(world[y])):
            if (nb_fenetre==1):
                Tk.Label(fenetre,bg=world_color[y][x]).grid(row=y, column=x,sticky='nesw',padx=5*echelle_pad_grille, pady=5*echelle_pad_grille)
            else:
                Tk.Label(fenetre,bg=world_color[y][x]).grid(row=y+2, column=x,sticky='nesw',padx=5*echelle_pad_grille, pady=5*echelle_pad_grille)
    
    
def show_infection(fenetre,matrice_infection,nb_fenetre:int):
    '''
    Affiche la matrice du nombre d'infections et certaines infos sur elle (les légendes par 
    exemple) sur la fenetre.
    La fenetre en question est déterminée par 'nb_fenetre'.
    'nb_fenetre' = 0 -> fenetre principale
    'nb_fenetre' = 1 -> fenetre de simulation
    '''
    
    
    echelle=1
    echelle_ligne=1
    echelle_pad_grille=1
    
    
    if (nb_fenetre==1):
    
        if(len(matrice_infection)==10):
        
            Tk.Label(fenetre,bg="#87CEEB",text="Légende, nombre d'infections :",font=("Arial",20,"bold")).grid(row=16*echelle_ligne+2, column=0*echelle,sticky='nesw',columnspan=10*echelle,rowspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="0",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=0*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[0]).grid(row=17*echelle_ligne+2, column=1*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="1",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=2*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[1]).grid(row=17*echelle_ligne+2, column=3*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="2",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=4*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[2]).grid(row=17*echelle_ligne+2, column=5*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="3",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=6*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[3]).grid(row=17*echelle_ligne+2, column=7*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="4",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=8*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[4]).grid(row=17*echelle_ligne+2, column=9*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="5",font=("Arial",16,"bold")).grid(row=18*echelle_ligne+2, column=3*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[5]).grid(row=18*echelle_ligne+2, column=4*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
        
            Tk.Label(fenetre,bg="#87CEEB",text="6+      ",font=("Arial",16,"bold")).grid(row=18*echelle_ligne+2, column=5*echelle,columnspan=2*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[6]).grid(row=18*echelle_ligne+2, column=6*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
        
        if(len(matrice_infection)==30):
            
            echelle=3
            echelle_ligne=2
            echelle_pad_grille=0.1
    
            Tk.Label(fenetre,bg="#87CEEB",text="Légende, nombre d'infections :",font=("Arial",20,"bold")).grid(row=16*echelle_ligne+2, column=0*echelle,sticky='nesw',columnspan=10*echelle,rowspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="0",font=("Arial",14,"bold")).grid(row=17*echelle_ligne+2, column=0*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[0]).grid(row=17*echelle_ligne+2, column=1*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="1",font=("Arial",14,"bold")).grid(row=17*echelle_ligne+2, column=2*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[1]).grid(row=17*echelle_ligne+2, column=3*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="2",font=("Arial",14,"bold")).grid(row=17*echelle_ligne+2, column=4*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[2]).grid(row=17*echelle_ligne+2, column=5*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="3",font=("Arial",14,"bold")).grid(row=17*echelle_ligne+2, column=6*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[3]).grid(row=17*echelle_ligne+2, column=7*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="4",font=("Arial",14,"bold")).grid(row=17*echelle_ligne+2, column=8*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[4]).grid(row=17*echelle_ligne+2, column=9*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="5",font=("Arial",14,"bold")).grid(row=18*echelle_ligne+2, column=0*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[5]).grid(row=18*echelle_ligne+2, column=1*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
        
            Tk.Label(fenetre,bg="#87CEEB",text="6",font=("Arial",14,"bold")).grid(row=18*echelle_ligne+2, column=2*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[6]).grid(row=18*echelle_ligne+2, column=3*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="7",font=("Arial",14,"bold")).grid(row=18*echelle_ligne+2, column=4*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[7]).grid(row=18*echelle_ligne+2, column=5*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
        
            Tk.Label(fenetre,bg="#87CEEB",text="8",font=("Arial",14,"bold")).grid(row=18*echelle_ligne+2, column=6*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[8]).grid(row=18*echelle_ligne+2, column=7*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            Tk.Label(fenetre,bg="#87CEEB",text="9+",font=("Arial",14,"bold")).grid(row=18*echelle_ligne+2, column=8*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[9]).grid(row=18*echelle_ligne+2, column=9*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
    
        world_infections_color=number_to_color2(matrice_infection,1)
        
    else:
        
        Tk.Label(fenetre,bg="#87CEEB",text="Notre matrice d'infections",font=("Arial",18,"bold")).grid(row=0, column=0,sticky='nesw',columnspan=10,rowspan=2)
        world_infections_color=number_to_color2(matrice_infection,2)
        
        
        Tk.Label(fenetre,bg=code_couleur[1]).grid(row=14, column=2,sticky='nesw',rowspan=1,columnspan=1)
        Tk.Label(fenetre,bg=code_couleur[2]).grid(row=14, column=3,sticky='nesw',rowspan=1,columnspan=1)
        Tk.Label(fenetre,bg=code_couleur[3]).grid(row=14, column=4,sticky='nesw',rowspan=1,columnspan=1)
        Tk.Label(fenetre,bg=code_couleur[4]).grid(row=14, column=5,sticky='nesw',rowspan=1,columnspan=1)
        Tk.Label(fenetre,bg=code_couleur[5]).grid(row=14, column=6,sticky='nesw',rowspan=1,columnspan=1)
        Tk.Label(fenetre,bg=code_couleur[6]).grid(row=14, column=7,sticky='nesw',rowspan=1,columnspan=1)
        
        Tk.Label(fenetre,bg="#87CEEB",text="0",font=("Arial",16,"bold")).grid(row=15, column=1,columnspan=2,rowspan=1)
        Tk.Label(fenetre,bg="#87CEEB",text="0.25",font=("Arial",16,"bold")).grid(row=13, column=2,columnspan=2,rowspan=1)
        Tk.Label(fenetre,bg="#87CEEB",text="0.50",font=("Arial",16,"bold")).grid(row=15, column=3,columnspan=2,rowspan=1)
        Tk.Label(fenetre,bg="#87CEEB",text="0.75",font=("Arial",16,"bold")).grid(row=13, column=4,columnspan=2,rowspan=1)
        Tk.Label(fenetre,bg="#87CEEB",text="1",font=("Arial",16,"bold")).grid(row=15, column=5,columnspan=2,rowspan=1)
        Tk.Label(fenetre,bg="#87CEEB",text="1.25",font=("Arial",16,"bold")).grid(row=13, column=6,columnspan=2,rowspan=1)


    # Sert à attribuer les couleurs aux cases de la grille des infections selon le nombre
    
    for y in range(len(matrice_infection)):
        for x in range(len(matrice_infection[y])):
            if (nb_fenetre==1):
                Tk.Label(fenetre,bg=world_infections_color[y][x]).grid(row=y, column=x,sticky='nesw',padx=5*echelle_pad_grille, pady=5*echelle_pad_grille)
            else:
                Tk.Label(fenetre,bg=world_infections_color[y][x]).grid(row=y+2, column=x,sticky='nesw',padx=5*echelle_pad_grille, pady=5*echelle_pad_grille)



def reset(fenetre,original_world):
    '''
    Appelle la fonction affichant la fenetre principale, 'afficher_monde_tkinter',
    mais en faisant un reset des informations et des tours, en ne gardant que le monde
    d'origine pour repartir de zéro.
    '''
    
    
    matrice_infos_deplacement=[[],[],[]]
    
    tab_nb=[[],[],[],[]]
    tab_nb=number_types(original_world,tab_nb)
    tab_nb_deplacement=[[],[],[],[]]
    tab_nb_deplacement=number_types_en_deplacement(original_world,tab_nb_deplacement,matrice_infos_deplacement)
  
    
    matrice_infection=np.zeros((len(original_world),len(original_world))) # On part du principe qu'un individu non sain a été infecté à l'emplacement où il a été défini
    for y in range(len(matrice_infection)):
        for x in range(len(matrice_infection[0])):
            if ((original_world[y][x]==2) or (original_world[y][x]==3) or (original_world[y][x]==4)):
                matrice_infection[y][x]=1

    world=copy.deepcopy(original_world)

    afficher_monde_tkinter(fenetre,original_world,world,0,0,0,0,0,0,tab_nb,matrice_infos_deplacement,"Pas de confinement",matrice_infection,tab_nb_deplacement)













def afficher_monde_tkinter(fenetre,original_world,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement):
    '''
    Affichage de la fenêtre principale, permettant d'itérer le monde
    '''

    
    delete_grille(fenetre)
    
    fenetre.geometry("1400x800+200+150")
    fenetre.title("Modélisation évolution d'épidémie")
    
    fenetre.attributes('-fullscreen', True)
    fenetre.bind('<Escape>',lambda e: fenetre.destroy())
    
    
    echelle=1
    echelle_ligne=1
    if(len(world)==30):
        echelle=3
        echelle_ligne=2
    
    # Setup la fenêtre en grille
    
    for i in range(22*echelle):
        fenetre.columnconfigure(i, weight=1)
    for j in range(20*echelle_ligne):
        fenetre.rowconfigure(j, weight=1)
    
    
    show_world(fenetre,world,1)
    if(len(world)==10):
        show_infection(fenetre,matrice_infection,1)
        show_world(fenetre,world,1)
    
    

    # Partie affichée des paramètres à droite du monde
    
    text_nb_tours=str(nb_tours)
    Tk.Label(fenetre,bg="#87CEEB",text="Tours : "+text_nb_tours,font=("Arial",30,"bold")).grid(row=0*echelle_ligne, column=10*echelle,sticky='nesw',columnspan=2*echelle,rowspan=2*echelle_ligne)
    
    incubation = Tk.IntVar()
    transmission = Tk.IntVar()
    guerison = Tk.IntVar()
    mortalite = Tk.IntVar()
    deplacement = Tk.IntVar()
    
    
    incubation.set(old_incubation)
    transmission.set(old_transmission)
    guerison.set(old_guerison)
    mortalite.set(old_mortalite)
    deplacement.set(old_deplacement)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage \nd'incubation :",font=("Arial",18,"bold")).grid(row=2*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne)
    Tk.Scale(fenetre,variable=incubation,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=2*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage de \ntransmission :",font=("Arial",18,"bold")).grid(row=4*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne)
    Tk.Scale(fenetre,variable=transmission,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=4*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage de \nguérison :",font=("Arial",18,"bold")).grid(row=6*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne)
    Tk.Scale(fenetre,variable=guerison,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=6*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage de \nmortalité :",font=("Arial",18,"bold")).grid(row=8*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne)
    Tk.Scale(fenetre,variable=mortalite,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=8*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage de \ndéplacement :",font=("Arial",18,"bold")).grid(row=10*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne)
    Tk.Scale(fenetre,variable=deplacement,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=10*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne)
    
    
    
    Tk.Button(fenetre, text = "Itérer 1 fois le monde",font=("Arial",18),command=lambda:iterer_tkinter(fenetre,original_world,world,int(incubation.get()),int(transmission.get()),int(guerison.get()),int(mortalite.get()),int(deplacement.get()),nb_tours,tab_nb,matrice_infos_deplacement,str(combobox.get()),matrice_infection,tab_nb_deplacement)).grid(row=12*echelle_ligne, column=10*echelle,columnspan=1*echelle,rowspan=2*echelle_ligne)
    
    
    nb_tours_itere=Tk.IntVar()
    Tk.Spinbox(fenetre, from_= 0, to = 1000,textvariable=nb_tours_itere,font=("Arial",16)).grid(row=14*echelle_ligne, column=11*echelle,columnspan=1*echelle,rowspan=2*echelle_ligne)
    Tk.Button(fenetre, text = "Itérer n fois le monde",font=("Arial",18),command=lambda:multi_iterer_tkinter(int(nb_tours_itere.get()),fenetre,original_world,world,int(incubation.get()),int(transmission.get()),int(guerison.get()),int(mortalite.get()),int(deplacement.get()),nb_tours,tab_nb,matrice_infos_deplacement,str(combobox.get()),matrice_infection,tab_nb_deplacement)).grid(row=12*echelle_ligne, column=11*echelle,columnspan=1*echelle,rowspan=2*echelle_ligne)
    
    
    Tk.Label(fenetre,bg="#87CEEB",text="Confinement :",font=("Arial",18,"bold")).grid(row=16*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne,columnspan=1*echelle)
    combobox=Tk.ttk.Combobox(fenetre, textvariable="Test", values = ["Pas de confinement", "Confinement normal", "Confinement strict"],font=("Arial",18,"bold"))
    combobox.set(confinement)
    combobox.grid(row=16*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne,columnspan=1*echelle)
    
    
    Tk.Button(fenetre, text = "Reset les itérations",font=("Arial",18),command=lambda:reset(fenetre,original_world)).grid(row=18*echelle_ligne, column=10*echelle,columnspan=2*echelle,rowspan=2*echelle_ligne)
    
    if (len(world)==10):
        Tk.Button(fenetre, text = "Simulation générale à partir du monde",font=("Arial",20),command=lambda:setup_affiche_simus_generales(fenetre,world,int(incubation.get()),int(transmission.get()),int(guerison.get()),int(mortalite.get()),int(deplacement.get()),nb_tours,tab_nb,matrice_infos_deplacement,str(combobox.get()),matrice_infection,tab_nb_deplacement)).grid(row=21*echelle_ligne, column=10*echelle,columnspan=2*echelle,pady=10,rowspan=1*echelle_ligne) 
    
    
    # Partie affichée sous le monde
    
    
    Tk.Button(fenetre, text = "Afficher monde",font=("Arial",18),command=lambda:show_world(fenetre,world,1)).grid(row=15*echelle_ligne+2, column=0*echelle,columnspan=5*echelle,rowspan=1*echelle_ligne) 
    Tk.Button(fenetre, text = "Afficher infections",font=("Arial",18),command=lambda:show_infection(fenetre,matrice_infection,1)).grid(row=15*echelle_ligne+2, column=5*echelle,columnspan=5*echelle,rowspan=1*echelle_ligne) 
    
    Tk.Button(fenetre, text = "Générer un nouveau monde",font=("Arial",20),command=lambda:setup_tkinter(1,fenetre)).grid(row=19*echelle_ligne+2, column=0*echelle,columnspan=10*echelle,pady=10,rowspan=1*echelle_ligne) 
    
    Tk.Label(fenetre,bg="#87CEEB",text="Appuyez sur échap pour quitter",font=("Arial",20,"bold")).grid(row=20*echelle_ligne+2, column=0*echelle,sticky='nesw',rowspan=2*echelle_ligne,columnspan=10*echelle)
    
    
    # Partie du plot à droite
    
        
    fig = Figure(figsize=(3, 2), dpi=100)
    t = np.arange(0, nb_tours+1, 1)
    ax = fig.add_subplot()
        
    ax.plot(t, tab_nb[0] , color = 'blue')
    ax.plot(t, tab_nb[1] , color = 'green')
    ax.plot(t, tab_nb[2] , color = 'orange')
    ax.plot(t, tab_nb[3] , color = 'red')
    
    ax.set_ylabel("Nombre d'individus",labelpad=-4,fontsize=18)
    ax.set_xlabel("Nombre de tours",labelpad=2.5,fontsize=18)
    
    canvas = FigureCanvasTkAgg(fig, master=fenetre)  
    canvas.draw()
    canvas.get_tk_widget().grid(row=0*echelle_ligne, column=12*echelle,sticky='nesw',columnspan=10*echelle,rowspan=10*echelle_ligne,padx=5,pady=0)

    

    if (len(world)==10):
        Tk.Label(fenetre,bg="#87CEEB",text="Données sur les individus en déplacement",font=("Arial",18,"bold")).grid(row=11, column=12,sticky='nesw',rowspan=2,columnspan=10)
    elif (len(world)==30):
        Tk.Label(fenetre,bg="#87CEEB",text="Données sur les individus\n en déplacement",font=("Arial",18,"bold")).grid(row=22, column=40,sticky='nesw',rowspan=4,columnspan=20)
        #pass
    fig_deplacement = Figure(figsize=(3, 2), dpi=100)
    ax_deplacement = fig_deplacement.add_subplot()
        
    ax_deplacement.plot(t, tab_nb_deplacement[0] , color = 'blue')
    ax_deplacement.plot(t, tab_nb_deplacement[1] , color = 'green')
    ax_deplacement.plot(t, tab_nb_deplacement[2] , color = 'orange')
    ax_deplacement.plot(t, tab_nb_deplacement[3] , color = 'red')
    
    canvas_deplacement = FigureCanvasTkAgg(fig_deplacement, master=fenetre)  
    canvas_deplacement.draw()
    canvas_deplacement.get_tk_widget().grid(row=13*echelle_ligne, column=13*echelle,sticky='nesw',columnspan=8*echelle,rowspan=8*echelle_ligne)






def setup_affiche_simus_generales(fenetre,world,incubation,transmission,guerison,mortalite,deplacement,nb_tours,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement):
    '''
    Setup l'affichage de simulation, on regarde si il y a pas déjà une fenêtre de simulation ouverte
    Si c'est le cas on la détruit avant d'afficher l'affichage de simulation
    '''
    
    for widget in fenetre.winfo_children():
        if isinstance(widget,Tk.Toplevel):
            widget.destroy()
            
    fenetre2 = Tk.Toplevel(fenetre)
        
    fenetre2.title("Simulation générale")
    fenetre2.config(bg = "#87CEEB") 
    fenetre2.bind('<Escape>',lambda e: fenetre2.destroy())
        
    #fenetre.geometry("1000x400+500+300")
    fenetre2.geometry("1400x800")
    fenetre2.attributes('-topmost', 1)
    center_window(fenetre2)
    
    affiche_simus_generales(fenetre2,world,incubation,transmission,guerison,mortalite,deplacement,nb_tours,tab_nb,matrice_infos_deplacement,True,confinement,matrice_infection,tab_nb_deplacement)

    fenetre2.mainloop()   
    
    
def affiche_simus_generales(fenetre2,world,incubation,transmission,guerison,mortalite,deplacement,nb_tours,tab_nb,matrice_infos_deplacement,first_time,confinement,matrice_infection,tab_nb_deplacement):
    '''
    Affiche la fenêtre de simulation
    ''' 
    
    for i in range(30):
        fenetre2.columnconfigure(i, weight=1)
    for j in range(26):
        fenetre2.rowconfigure(j, weight=1)
    
    delete_grille(fenetre2)
    
    
    # Affichage de gauche de la fenêtre
    
    
    show_world(fenetre2,world,2)
    show_infection(fenetre2,world,2)
    show_world(fenetre2,world,2)
    
    Tk.Button(fenetre2, text = "Afficher monde",font=("Arial",18),command=lambda:show_world(fenetre2,world,2)).grid(row=12, column=0,columnspan=5,rowspan=1) 
    Tk.Button(fenetre2, text = "Afficher infections",font=("Arial",18),command=lambda:show_infection(fenetre2,matrice_infection,2)).grid(row=12, column=5,columnspan=5,rowspan=1) 
    
    
    
    # Affichage du milieu de la fenêtre
    
    text_nb_tours=str(nb_tours)
    Tk.Label(fenetre2,bg="#87CEEB",text="Tours : "+text_nb_tours,font=("Arial",30,"bold")).grid(row=0, column=10,sticky='nesw',columnspan=10,rowspan=2)
    
    
    incubation2 = Tk.IntVar()
    transmission2 = Tk.IntVar()
    guerison2 = Tk.IntVar()
    mortalite2 = Tk.IntVar()
    deplacement2 = Tk.IntVar()
    
    incubation2.set(incubation)
    transmission2.set(transmission)
    guerison2.set(guerison)
    mortalite2.set(mortalite)
    deplacement2.set(deplacement)
    
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Pourcentage \nd'incubation :",font=("Arial",14,"bold")).grid(row=2, column=10,sticky='nesw',rowspan=2,columnspan=5)
    Tk.Scale(fenetre2,variable=incubation2,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=2, column=15,rowspan=2,columnspan=5)
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Pourcentage de \ntransmission :",font=("Arial",14,"bold")).grid(row=4, column=10,sticky='nesw',rowspan=2,columnspan=5)
    Tk.Scale(fenetre2,variable=transmission2,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=4, column=15,rowspan=2,columnspan=5)
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Pourcentage de \nguérison :",font=("Arial",14,"bold")).grid(row=6, column=10,sticky='nesw',rowspan=2,columnspan=5)
    Tk.Scale(fenetre2,variable=guerison2,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=6, column=15,rowspan=2,columnspan=5)
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Pourcentage de \nmortalité :",font=("Arial",14,"bold")).grid(row=8, column=10,sticky='nesw',rowspan=2,columnspan=5)
    Tk.Scale(fenetre2,variable=mortalite2,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=8, column=15,rowspan=2,columnspan=5)
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Pourcentage de \ndéplacement :",font=("Arial",14,"bold")).grid(row=10, column=10,sticky='nesw',rowspan=2)
    Tk.Scale(fenetre2,variable=deplacement2,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=10, column=15,rowspan=2,columnspan=5)
    
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Confinement :",font=("Arial",18,"bold")).grid(row=12, column=10,sticky='nesw',rowspan=2,columnspan=5)
    combobox=Tk.ttk.Combobox(fenetre2, textvariable="Test", values = ["Pas de confinement", "Confinement normal", "Confinement strict"],font=("Arial",18,"bold"))
    combobox.set(confinement)
    combobox.grid(row=12, column=15,rowspan=2,columnspan=5)
    
    
    if (first_time==True):
        Tk.Button(fenetre2, text = "Simuler (100 tours)",font=("Arial",20),command=lambda:simulation_generale(20,100,fenetre2,world,int(incubation2.get()),int(transmission2.get()),int(guerison2.get()),int(mortalite2.get()),int(deplacement2.get()),nb_tours,tab_nb,matrice_infos_deplacement,str(combobox.get()),matrice_infection,tab_nb_deplacement)).grid(row=14, column=10,columnspan=10,pady=10,rowspan=2)
        
        

    
    # Affichage de droite de la fenêtre
    
    if (first_time==True):
        Tk.Label(fenetre2,bg="#87CEEB",text="Notre graphe avant simulation",font=("Arial",18,"bold")).grid(row=0, column=20,sticky='nesw',columnspan=10,rowspan=2)
    else:
        Tk.Label(fenetre2,bg="#87CEEB",text="Notre graphe après simulation",font=("Arial",18,"bold")).grid(row=0, column=20,sticky='nesw',columnspan=10,rowspan=2)
    
    fig2 = Figure(figsize=(3, 2), dpi=100)
    t = np.arange(0, nb_tours+1, 1)
    ax2 = fig2.add_subplot()
        
    ax2.plot(t, tab_nb[0] , color = 'blue')
    ax2.plot(t, tab_nb[1] , color = 'green')
    ax2.plot(t, tab_nb[2] , color = 'orange')
    ax2.plot(t, tab_nb[3] , color = 'red')
    
    ax2.set_ylabel("Nombre d'individus",labelpad=-4,fontsize=18)
    ax2.set_xlabel("Nombre de tours",labelpad=2.5,fontsize=18)
    
    canvas2 = FigureCanvasTkAgg(fig2, master=fenetre2)  
    canvas2.draw()
    canvas2.get_tk_widget().grid(row=2, column=20,sticky='nesw',columnspan=10,rowspan=10,padx=5,pady=0)
    
    
    
    if (first_time==True):
        Tk.Label(fenetre2,bg="#87CEEB",text="Données sur les individus en\n déplacement avant simulation",font=("Arial",18,"bold")).grid(row=14, column=20,sticky='nesw',rowspan=2,columnspan=10)
    else:
        Tk.Label(fenetre2,bg="#87CEEB",text="Données sur les individus en\n déplacement après simulation",font=("Arial",18,"bold")).grid(row=14, column=20,sticky='nesw',rowspan=2,columnspan=10)

    fig2_deplacement = Figure(figsize=(3, 2), dpi=100)
    ax2_deplacement = fig2_deplacement.add_subplot()
        
    ax2_deplacement.plot(t, tab_nb_deplacement[0] , color = 'blue')
    ax2_deplacement.plot(t, tab_nb_deplacement[1] , color = 'green')
    ax2_deplacement.plot(t, tab_nb_deplacement[2] , color = 'orange')
    ax2_deplacement.plot(t, tab_nb_deplacement[3] , color = 'red')
    
    canvas2_deplacement = FigureCanvasTkAgg(fig2_deplacement, master=fenetre2)  
    canvas2_deplacement.draw()
    canvas2_deplacement.get_tk_widget().grid(row=16, column=20,sticky='nesw',columnspan=10,rowspan=10,padx=5,pady=0)



''' Lance l'interface ''' 

setup_tkinter(1,False)

