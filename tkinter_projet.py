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


'''
PROGRAMME D'INTERFACE GRAPHIQUE
'''








# Utilisé pour les dégradés de couleurs des infections d'individus
code_couleur=["white","#F7FF86","#FFDC00","#FFAA00","#FF7B00","#FF4800",
              "#D90025","#B4004A","#8F006F","#63009B"]




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
       [1, 4, 0, 2, 2, 2],
       [2, 3, 3, 2, 2, 5]]

    str_world=[['white', 'orange', 'blue', 'blue', 'green', 'green'],
     ['green', 'orange', 'white', 'green', 'orange', 'white'],
     ['pink', 'white', 'blue', 'orange', 'white', 'blue'],
     ['green', 'green', 'orange', 'blue', 'green', 'orange'],
     ['blue', 'pink', 'white', 'green', 'green', 'green'],
     ['green', 'orange', 'orange', 'green', 'green', 'purple']]
     
    Utilisée dans 'show_world' et 'show_infection'
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
                str_world[y].append("pink")        
            elif world[y][x]==5:
                str_world[y].append("#A51616")    

    
    return str_world


def number_to_color2(matrice_infection:list,nb_fenetre)->list:
    """
    Même principe que pour number_to_color, la seule différence est le code couleur
    Fonction appelée pour attribuer les couleurs à la matrice d'infections
    
    Utilisée dans 'show_infection'
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
    tab_nb[3] -> historique des R1
    tab_nb[4] -> historique des R2
    tab_nb[5] -> historique du nombre total de population (en enlevant les morts)
    
    Utilisée dans 'generer_world', 'iterer_tkinter', 'multi_iterer_tkinter', 
    'simulation_generale', et 'reset'
    '''
    
    nb_S=0
    nb_E=0
    nb_I=0
    nb_R1=0
    nb_R2=0
    nb_Total=0
    for y in range(len(world)):
        for x in range(len(world[y])):
            
            if world[y][x]==1:
                nb_S=nb_S+1
                nb_Total=nb_Total+1
            
            elif world[y][x]==2:
                nb_E=nb_E+1
                nb_Total=nb_Total+1
            
            elif world[y][x]==3:
                nb_I=nb_I+1
                nb_Total=nb_Total+1
            
            elif world[y][x]==4:
                nb_R1=nb_R1+1
                nb_Total=nb_Total+1
            
            elif world[y][x]==5:
                nb_R2=nb_R2+1
    
    tab_nb[0].append(nb_S)
    tab_nb[1].append(nb_E)
    tab_nb[2].append(nb_I)
    tab_nb[3].append(nb_R1)
    tab_nb[4].append(nb_R2)
    tab_nb[5].append(nb_Total)
    
    
    return tab_nb


def number_types_en_deplacement(world,tab_nb_deplacement,matrice_infos_deplacement):
    '''
    Renvoit un tableau mis à jour qui contient l'historique du nombre d'individus 
    en déplacement au fil des tours
    tab_nb_deplacement[0] -> nombre de S en déplacement
    tab_nb_deplacement[1] -> nombre de E en déplacement
    tab_nb_deplacement[2] -> nombre de I en déplacement
    tab_nb_deplacement[3] -> nombre de R1 en déplacement
    
    Utilisée dans 'generer_world', 'iterer_tkinter', 'multi_iterer_tkinter', 
    'simulation_generale', et 'reset'
    '''
    
    coordonnees_cible=matrice_infos_deplacement[1]
    
    # Rappel : coordonnees_cible est un tableau de couples (x,y)
    # Ces (x,y) représentent les coordonnées dun indivdus actuellement 
    # en déplacement à ces ccordonnées
    
    nb_S=0
    nb_E=0
    nb_I=0
    nb_R1=0
    
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
                nb_R1=nb_R1+1
    
    tab_nb_deplacement[0].append(nb_S)
    tab_nb_deplacement[1].append(nb_E)
    tab_nb_deplacement[2].append(nb_I)
    tab_nb_deplacement[3].append(nb_R1)
    
    return tab_nb_deplacement    



def center_window(fenetre):
    '''
    Fonction qui en étant appellée est censée centrer la fenêtre passée en paramètre.
    '''
    
    eval_ = fenetre.nametowidget('.').eval
    eval_('tk::PlaceWindow %s center' % fenetre)



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
            
            
            
            
            
    
''' Fonctions de setup / génération du monde '''
    

def setup_tkinter(first_time:int,fenetre):
    """
    Setup et affiche notre écran d'accueil, qui demande le nombre d'individus du monde
    et le type du monde.
    
    Si first time != 1, ça veut dire qu'on affiche un nombre d'erreur concernant le
    nombre d'individus choisis selon le monde.
    """
    
    if (first_time==1):
        
        if (fenetre!=False):
            fenetre.destroy()

        fenetre = Tk.Tk()
        
        fenetre.bind('<Escape>',lambda e: fenetre.destroy())
        
        fenetre.title("Paramètres évolution d'épidémie")
        fenetre.config(bg = "#87CEEB") 
        
        #fenetre.geometry("1000x600+500+300")
        fenetre.geometry("1000x600")
        center_window(fenetre)
        
        
        
        for i in range(8):
            fenetre.columnconfigure(i, weight=1)
        for j in range(9):
            fenetre.rowconfigure(j, weight=1)
        
    
        nb_S_moyen=Tk.IntVar()
        nb_E_moyen=Tk.IntVar()
        nb_I_moyen=Tk.IntVar()
        nb_R1_moyen=Tk.IntVar()
        nb_R2_moyen=Tk.IntVar()
        
        nb_S_grand=Tk.IntVar()
        nb_E_grand=Tk.IntVar()
        nb_I_grand=Tk.IntVar()
        nb_R1_grand=Tk.IntVar()
        nb_R2_grand=Tk.IntVar()
        
        
        Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus \n sains",font=("Arial",18,"bold")).grid(row=0, column=2,sticky='nesw',columnspan=4)
        Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus infectés \n non infectieux",font=("Arial",18,"bold")).grid(row=1, column=2,sticky='nesw',columnspan=4)
        Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus infectés \n infectieux",font=("Arial",18,"bold")).grid(row=2, column=2,sticky='nesw',columnspan=4)
        Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus \nguérris",font=("Arial",18,"bold")).grid(row=3, column=2,sticky='nesw',columnspan=4)
        Tk.Label(fenetre,bg="#87CEEB",text="Nombre d'individus \nmorts",font=("Arial",18,"bold")).grid(row=4, column=2,sticky='nesw',columnspan=4)
        
        
        Tk.Scale(fenetre,variable=nb_S_moyen,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=0, column=0,columnspan=2)
        Tk.Scale(fenetre,variable=nb_E_moyen,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=1, column=0,columnspan=2)
        Tk.Scale(fenetre,variable=nb_I_moyen,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=2, column=0,columnspan=2)
        Tk.Scale(fenetre,variable=nb_R1_moyen,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=3, column=0,columnspan=2)
        Tk.Scale(fenetre,variable=nb_R2_moyen,font=("Arial",20),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=4, column=0,columnspan=2)
        
        Tk.Scale(fenetre,variable=nb_S_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=325).grid(row=0, column=6,columnspan=2)
        Tk.Scale(fenetre,variable=nb_E_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=325).grid(row=1, column=6,columnspan=2)
        Tk.Scale(fenetre,variable=nb_I_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=325).grid(row=2, column=6,columnspan=2)
        Tk.Scale(fenetre,variable=nb_R1_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=325).grid(row=3, column=6,columnspan=2)        
        Tk.Scale(fenetre,variable=nb_R2_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=325).grid(row=4, column=6,columnspan=2)
        
        
        Tk.Button(fenetre, text = "Générer un monde moyen\n selon paramètres",font=("Arial",20),command=lambda:generer_world(fenetre,False,int(nb_S_moyen.get()),int(nb_E_moyen.get()),int(nb_I_moyen.get()),int(nb_R1_moyen.get()),int(nb_R2_moyen.get()),somme=int(nb_S_moyen.get())+int(nb_E_moyen.get())+int(nb_I_moyen.get())+int(nb_R1_moyen.get())+int(nb_R2_moyen.get()),maxi=100)).grid(row=6, column=0,columnspan=2,rowspan=2)
        Tk.Button(fenetre, text = "Générer un monde moyen\n aléatoire",font=("Arial",20),command=lambda:generer_world(fenetre,True,0,0,0,0,0,somme=int(nb_S_moyen.get())+int(nb_E_moyen.get())+int(nb_I_moyen.get())+int(nb_R1_moyen.get()),maxi=100)).grid(row=8, column=0,columnspan=2,rowspan=2) 
        
        Tk.Button(fenetre, text = "Générer un grand monde \n selon paramètres",font=("Arial",20),command=lambda:generer_world(fenetre,False,int(nb_S_grand.get()),int(nb_E_grand.get()),int(nb_I_grand.get()),int(nb_R1_grand.get()),int(nb_R2_grand.get()),somme=int(nb_S_grand.get())+int(nb_E_grand.get())+int(nb_I_grand.get())+int(nb_R1_grand.get())+int(nb_R2_grand.get()),maxi=900)).grid(row=6, column=7,columnspan=2,rowspan=2)
        Tk.Button(fenetre, text = "Générer un grand monde \n aléatoire",font=("Arial",20),command=lambda:generer_world(fenetre,True,0,0,0,0,0,somme=int(nb_S_grand.get())+int(nb_E_grand.get())+int(nb_I_grand.get())+int(nb_R1_grand.get()),maxi=900)).grid(row=8, column=7,columnspan=2,rowspan=2) 
        

        fenetre.mainloop()
        
    elif (first_time==2):
        Tk.Label(fenetre,bg="#87CEEB",text="Sélectionnez une somme\n d'individus ne dépassant\n pas 100 pour le monde\n moyen",font=("Arial",18,"bold"),fg="Red").grid(row=5, column=2,sticky='nesw',columnspan=4,rowspan=5)

    elif (first_time==3):
        Tk.Label(fenetre,bg="#87CEEB",text="Sélectionnez une somme\n d'individus ne dépassant\n pas 900 pour le grand\n monde",font=("Arial",18,"bold"),fg="Red").grid(row=5, column=2,sticky='nesw',columnspan=4,rowspan=5)



def generer_world(fenetre,aleatoire:bool,nb_S, nb_E, nb_I, nb_R1,nb_R2,somme,maxi):
    """
    Permet de setup la représentation du monde. 
    Pour information "somme" c'est juste la somme des nb S E I R1 R2.
    
    Dans le cas où la somme dépasse le nombre maximal de cases du monde, la 
    fonction redirige vers l'écran d'accueil
    
    Utilisée dans 'setup_tkinter' (boutons)
    """

    tab_nb=[[],[],[],[],[],[]]
    tab_nb_deplacement=[[],[],[],[]]
    matrice_infos_deplacement=[[],[],[]]
    tab_infectes_pendant_deplacement=[0]
    
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
                if ((world[y][x]==2) or (world[y][x]==3) or (world[y][x]==4) or (world[y][x]==5)):
                    matrice_infection[y][x]=1

        original_world=copy.deepcopy(world)

        afficher_monde_tkinter(fenetre,original_world,world,0,0,0,0,0,0,tab_nb,matrice_infos_deplacement,"Pas de confinement",matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement)
        
    elif (aleatoire==False and somme <=maxi):
        delete_grille(fenetre)
        
        if(maxi==100):
            world=generate_world_SEIR(nb_S, nb_E, nb_I, nb_R1 , nb_R2)
        else:
            world=generate2_world_SEIR(nb_S, nb_E, nb_I, nb_R1 , nb_R2)

        tab_nb=number_types(world,tab_nb)
        tab_nb_deplacement=number_types_en_deplacement(world,tab_nb_deplacement,matrice_infos_deplacement)
        
        matrice_infection=np.zeros((len(world),len(world)))
        
        # On part du principe qu'un individu non sain a été infecté à l'emplacement 
        # où il a été défini, on l'indique dans matrice_infection
        for y in range(len(matrice_infection)):
            for x in range(len(matrice_infection[0])):
                if ((world[y][x]==2) or (world[y][x]==3) or (world[y][x]==4) or (world[y][x]==5)):
                    matrice_infection[y][x]=1

        original_world=copy.deepcopy(world)
    
        afficher_monde_tkinter(fenetre,original_world,world,0,0,0,0,0,0,tab_nb,matrice_infos_deplacement,"Pas de confinement",matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement)
    
    
    # Dans le cas où il y a un problème de somme
    elif (aleatoire==False and somme >maxi): 
        if (maxi==100):
            setup_tkinter(2,fenetre)
        else :
            setup_tkinter(3,fenetre)










''' Fonctions d'itérations / simulations '''



def iterer_tkinter(fenetre,original_world,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement):
    '''
    Fonction intermédiaure appelée par l'itération tkinter, affiche le nouveau 
    monde après itération
    
    Utilisée dans 'afficher_monde_tkinter' (bouton)
    '''
    world=evolution_world_SEIR(world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,matrice_infos_deplacement,confinement,matrice_infection,tab_infectes_pendant_deplacement)
    tab_nb=number_types(world,tab_nb)
    tab_nb_deplacement=number_types_en_deplacement(world,tab_nb_deplacement,matrice_infos_deplacement)
    
    afficher_monde_tkinter(fenetre,original_world,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours+1,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement)



def multi_iterer_tkinter(nb_tours_itere,fenetre,original_world,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement):
    '''
    Fonction intermédiaure appelée par l'itération tkinter, affiche le nouveau 
    monde après plusieurs itérations
    
    Utilisée dans 'afficher_monde_tkinter'(bouton)
    '''
    
    # On évite de faire plus de 200 itérations d'un seul coup
    if (nb_tours_itere<0 or nb_tours_itere>200):
        nb_tours_itere=0
    
    
    for i in range(nb_tours_itere):
        world=evolution_world_SEIR(world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,matrice_infos_deplacement,confinement,matrice_infection,tab_infectes_pendant_deplacement)
        tab_nb=number_types(world,tab_nb)
        tab_nb_deplacement=number_types_en_deplacement(world,tab_nb_deplacement,matrice_infos_deplacement)
        
    afficher_monde_tkinter(fenetre,original_world,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,(nb_tours+nb_tours_itere),tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement)


def simulation_generale(nb_simus,nb_tours_itere,fenetre2,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement,donnees_reset_simu):
    '''
    Permet de récupérer la moyenne de "nb_simus" simulations sur "nb_tours_itere" tours
    à partir d'un monde de départ "world". Affiche ensuite le résultat avec
    la fonction affiche_simus_generales sur l'écran de simulation
    
    Utilisée dans 'affiche_simus_generales'
    '''

    for i in range(nb_simus):
        
        # On fait des copies par simulation de chaques tableaux et matrices utilisés
        world_simu=copy.deepcopy(world)
        matrice_infos_deplacement_simu=copy.deepcopy(matrice_infos_deplacement)
        tab_nb_simu=copy.deepcopy(tab_nb)
        tab_nb_deplacement_simu=copy.deepcopy(tab_nb_deplacement)
        matrice_infection_simu=copy.deepcopy(matrice_infection)
        tab_infectes_pendant_deplacement_simu=copy.deepcopy(tab_infectes_pendant_deplacement)
        
        for j in range(nb_tours_itere):
            world_simu=evolution_world_SEIR(world_simu,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,matrice_infos_deplacement_simu,confinement,matrice_infection_simu,tab_infectes_pendant_deplacement_simu)
            tab_nb_simu=number_types(world_simu,tab_nb_simu)
            tab_nb_deplacement_simu=number_types_en_deplacement(world_simu,tab_nb_deplacement_simu,matrice_infos_deplacement_simu)
        
        
        if (i==0):
            tab_nb_resultat=np.array(tab_nb_simu)
            tab_nb_deplacement_resultat=np.array(tab_nb_deplacement_simu)
            tab_infectes_pendant_deplacement_resultat=np.array(tab_infectes_pendant_deplacement_simu)
            
            matrice_infection_resultat=np.array(matrice_infection_simu)
        else:
            tab_nb_resultat=tab_nb_resultat+np.array(tab_nb_simu)
            tab_nb_deplacement_resultat=tab_nb_deplacement_resultat+np.array(tab_nb_deplacement_simu)
            tab_infectes_pendant_deplacement_resultat=tab_infectes_pendant_deplacement_resultat+np.array(tab_infectes_pendant_deplacement_simu)
            
            matrice_infection_resultat=matrice_infection_resultat+matrice_infection_simu
        
    
    # On passe des tableaux et matrices en array avant de les remettre
    # en listes pour faciliter les opérations dessus
    
    tab_nb_resultat=tab_nb_resultat/nb_simus
    tab_nb_resultat=tab_nb_resultat.tolist()
    
    tab_nb_deplacement_resultat=tab_nb_deplacement_resultat/nb_simus
    tab_nb_deplacement_resultat.tolist()
    
    tab_infectes_pendant_deplacement_resultat=tab_infectes_pendant_deplacement_resultat/nb_simus
    tab_infectes_pendant_deplacement_resultat.tolist()
    
    matrice_infection_resultat=matrice_infection_resultat/nb_simus
    matrice_infection_resultat=matrice_infection_resultat.tolist()
    
    affiche_simus_generales(fenetre2,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours+nb_tours_itere,tab_nb_resultat,matrice_infos_deplacement_simu,False,confinement,matrice_infection_resultat,tab_nb_deplacement_resultat,tab_infectes_pendant_deplacement_resultat,donnees_reset_simu)
        



def reset(fenetre,original_world):
    '''
    Appelle la fonction affichant la fenetre principale, 'afficher_monde_tkinter',
    mais en faisant un reset des informations et des tours, en ne gardant que le monde
    d'origine pour repartir de zéro.
    
    Utilisée dans 'afficher_monde_tkinter' (bouton)
    '''
    
    
    matrice_infos_deplacement=[[],[],[]]
    
    tab_nb=[[],[],[],[],[],[]]
    tab_nb=number_types(original_world,tab_nb)
    tab_nb_deplacement=[[],[],[],[]]
    tab_nb_deplacement=number_types_en_deplacement(original_world,tab_nb_deplacement,matrice_infos_deplacement)
    tab_infectes_pendant_deplacement=[0]
    
    
    matrice_infection=np.zeros((len(original_world),len(original_world))) # On part du principe qu'un individu non sain a été infecté à l'emplacement où il a été défini
    for y in range(len(matrice_infection)):
        for x in range(len(matrice_infection[0])):
            if ((original_world[y][x]==2) or (original_world[y][x]==3) or (original_world[y][x]==4)):
                matrice_infection[y][x]=1

    world=copy.deepcopy(original_world)

    afficher_monde_tkinter(fenetre,original_world,world,0,0,0,0,0,0,tab_nb,matrice_infos_deplacement,"Pas de confinement",matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement)








''' Fonctions d'affichage des matrices du monde / des graphiques '''



def show_world(fenetre,world,nb_fenetre:int):
    '''
    Affiche un monde et certaines infos sur lui (les légendes par exemple) sur la fenetre.
    La fenetre en question est déterminée par 'nb_fenetre'.
    'nb_fenetre' = 0 -> fenetre principale
    'nb_fenetre' = 1 -> fenetre de simulation
    
    Utilisée dans 'afficher_monde_tkinter' et 'affiche_simus_generales' (boutons)
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
        
        
        # Cache les éléments ne faisant pas partie de la légendu du monde
        Tk.Label(fenetre,bg="#87CEEB").grid(row=18*echelle_ligne+2, column=0*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=10*int((echelle_ligne*1.5)))
        
        
        # Chaines de caractères de la légende
        Tk.Label(fenetre,bg="#87CEEB",text="S",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=0*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="#87CEEB",text="E",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=2*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="#87CEEB",text="I",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=4*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="#87CEEB",text="R1",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=5*echelle,sticky='nesw',columnspan=3*echelle,rowspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="#87CEEB",text="R2",font=("Arial",16,"bold")).grid(row=17*echelle_ligne+2, column=7*echelle,sticky='nesw',columnspan=3*echelle,rowspan=1*echelle_ligne)
        
        Tk.Label(fenetre,bg="#87CEEB",text="guérris",font=("Arial",16,"bold")).grid(sticky='nesw',row=18*echelle_ligne+2, column=6*echelle,columnspan=2*echelle,rowspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="#87CEEB",text="morts",font=("Arial",16,"bold")).grid(sticky='nesw',row=18*echelle_ligne+2, column=8*echelle,columnspan=2*echelle,rowspan=1*echelle_ligne)
        

        # Couleurs de la légende
        Tk.Label(fenetre,bg="blue").grid(row=17*echelle_ligne+2, column=1*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="green").grid(row=17*echelle_ligne+2, column=3*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="orange").grid(row=17*echelle_ligne+2, column=5*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="pink").grid(row=17*echelle_ligne+2, column=7*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
        Tk.Label(fenetre,bg="#A51616").grid(row=17*echelle_ligne+2, column=9*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
     
        

    
    else:
        echelle_pad_grille=0.5
        
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
    
    Utilisée dans 'afficher_monde_tkinter' et 'affiche_simus_generales' (boutons)
    '''
    
    
    echelle=1
    echelle_ligne=1
    echelle_pad_grille=1
    
    
    if (nb_fenetre==1):
    
        if(len(matrice_infection)==10):
        
            Tk.Label(fenetre,bg="#87CEEB",text="Légende, nombre d'infections :",font=("Arial",20,"bold")).grid(row=16*echelle_ligne+2, column=0*echelle,sticky='nesw',columnspan=10*echelle,rowspan=1*echelle_ligne)
            
            
            # Cache les éléments ne faisant pas partie de la légendu du monde
            Tk.Label(fenetre,bg="#87CEEB").grid(row=18*echelle_ligne+2, column=0*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=10*int((echelle_ligne*1.5)))
            
            
            # Chaines de caractères de la légende
            Tk.Label(fenetre,bg="#87CEEB",text="0",font=("Arial",16,"bold")).grid(sticky='nesw',row=17*echelle_ligne+2, column=0*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="1",font=("Arial",16,"bold")).grid(sticky='nesw',row=17*echelle_ligne+2, column=2*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="2",font=("Arial",16,"bold")).grid(sticky='nesw',row=17*echelle_ligne+2, column=4*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="3",font=("Arial",16,"bold")).grid(sticky='nesw',row=17*echelle_ligne+2, column=6*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="4",font=("Arial",16,"bold")).grid(sticky='nesw',row=17*echelle_ligne+2, column=8*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="5",font=("Arial",16,"bold")).grid(sticky='nesw',row=18*echelle_ligne+2, column=3*echelle,columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="6+      ",font=("Arial",16,"bold")).grid(sticky='nesw',row=18*echelle_ligne+2, column=5*echelle,columnspan=2*echelle,rowspan=1*echelle_ligne)
            
            
            # Couleurs de la légende
            Tk.Label(fenetre,bg=code_couleur[0]).grid(row=17*echelle_ligne+2, column=1*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[1]).grid(row=17*echelle_ligne+2, column=3*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[2]).grid(row=17*echelle_ligne+2, column=5*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[3]).grid(row=17*echelle_ligne+2, column=7*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[4]).grid(row=17*echelle_ligne+2, column=9*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[5]).grid(row=18*echelle_ligne+2, column=4*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[6]).grid(row=18*echelle_ligne+2, column=6*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
        
        
        if(len(matrice_infection)==30):
            
            echelle=3
            echelle_ligne=2
            echelle_pad_grille=0.1
    
    
            Tk.Label(fenetre,bg="#87CEEB",text="Légende, nombre d'infections :",font=("Arial",20,"bold")).grid(row=16*echelle_ligne+2, column=0*echelle,sticky='nesw',columnspan=10*echelle,rowspan=1*echelle_ligne)
            
            
            # Cache les éléments ne faisant pas partie de la légendu du monde
            Tk.Label(fenetre,bg="#87CEEB").grid(row=18*echelle_ligne+2, column=0*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=10*int((echelle_ligne*1.5)))
            
            
            # Chaines de caractères de la légende
            Tk.Label(fenetre,bg="#87CEEB",text="0",font=("Arial",14,"bold")).grid(row=17*echelle_ligne+2, column=0*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="1",font=("Arial",14,"bold")).grid(row=17*echelle_ligne+2, column=2*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="2",font=("Arial",14,"bold")).grid(row=17*echelle_ligne+2, column=4*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="3",font=("Arial",14,"bold")).grid(row=17*echelle_ligne+2, column=6*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="4",font=("Arial",14,"bold")).grid(row=17*echelle_ligne+2, column=8*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="5",font=("Arial",14,"bold")).grid(row=18*echelle_ligne+2, column=0*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="6",font=("Arial",14,"bold")).grid(row=18*echelle_ligne+2, column=2*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="7",font=("Arial",14,"bold")).grid(row=18*echelle_ligne+2, column=4*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="8",font=("Arial",14,"bold")).grid(row=18*echelle_ligne+2, column=6*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="#87CEEB",text="9+",font=("Arial",14,"bold")).grid(row=18*echelle_ligne+2, column=8*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
            
            
            # Couleurs de la légende
            Tk.Label(fenetre,bg=code_couleur[0]).grid(row=17*echelle_ligne+2, column=1*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[1]).grid(row=17*echelle_ligne+2, column=3*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[2]).grid(row=17*echelle_ligne+2, column=5*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[3]).grid(row=17*echelle_ligne+2, column=7*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[4]).grid(row=17*echelle_ligne+2, column=9*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[5]).grid(row=18*echelle_ligne+2, column=1*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[6]).grid(row=18*echelle_ligne+2, column=3*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[7]).grid(row=18*echelle_ligne+2, column=5*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[8]).grid(row=18*echelle_ligne+2, column=7*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            Tk.Label(fenetre,bg=code_couleur[9]).grid(row=18*echelle_ligne+2, column=9*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            
    
        world_infections_color=number_to_color2(matrice_infection,1)
        
    else:
        echelle_pad_grille=0.5
        
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




def show_type_graphique(fenetre,world,nb_tours,tab_nb,type_graphique:int,nb_fenetre:int):
    '''
    Permet d'afficher un graphique présentant le nombre d'individus au fil des tours
    selon les différentes populations.
    
    type_graphique=1 : graphique SEIR
    type_graphique=2 : graphique avancé (S, E, I, R1 et R2 séparés, nombre population totale affichés)
    
    La fenetre en question est déterminée par 'nb_fenetre'.
    'nb_fenetre' = 0 -> fenetre principale
    'nb_fenetre' = 1 -> fenetre de simulation
    
    Utilisée dans 'afficher_monde_tkinter' et 'affiche_simus_generales' (boutons)
    '''
    
    echelle=1
    echelle_ligne=1
    
    t = np.arange(0, nb_tours+1, 1)
    
    lim_y=(tab_nb[5][0])+5 # Fixe l'échelle en y des graphiques
    
    if(len(world))==10:
        
        if (nb_fenetre==1):
            
            
            fig = Figure(figsize=(3, 2), dpi=100)
            ax = fig.add_subplot()
            
            if (type_graphique==1):
                
                # On nettoie la légende du graphique
                Tk.Label(fenetre,bg="#87CEEB").grid(row=11*echelle_ligne, column=12*echelle,sticky='nesw',columnspan=10*echelle,rowspan=1*echelle_ligne)
            
                # Légende du graphique SEIR
                Tk.Label(fenetre,bg="#87CEEB",text="R1 + R2 = R",font=("Arial",14,"bold")).grid(row=11*echelle_ligne, column=14*echelle,sticky='nesw',columnspan=5*echelle,rowspan=1*echelle_ligne)
                Tk.Label(fenetre,bg="red").grid(row=11*echelle_ligne, column=18*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            
                total_R=np.array(tab_nb[3])+np.array(tab_nb[4])
                total_R.tolist()
                
                ax.set_ylim(0, lim_y)
                ax.plot(t, tab_nb[0] , color = 'blue') #S
                ax.plot(t, tab_nb[1] , color = 'green') #E
                ax.plot(t, tab_nb[2] , color = 'orange') #I
                ax.plot(t, total_R , color = 'red') #R
                
            elif (type_graphique==2):    
                
                # On nettoie la légende du graphique
                Tk.Label(fenetre,bg="#87CEEB").grid(row=11*echelle_ligne, column=12*echelle,sticky='nesw',columnspan=10*echelle,rowspan=1*echelle_ligne)
                
                # Légende du graphique avancé
                Tk.Label(fenetre,bg="#87CEEB",text="Population",font=("Arial",14,"bold")).grid(row=11*echelle_ligne, column=14*echelle,sticky='nesw',columnspan=5*echelle,rowspan=1*echelle_ligne)
                Tk.Label(fenetre,bg="black").grid(row=11*echelle_ligne, column=18*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
                
                
                ax.set_ylim(0, lim_y)
                ax.plot(t, tab_nb[0] , color = 'blue') #S
                ax.plot(t, tab_nb[1] , color = 'green') #E
                ax.plot(t, tab_nb[2] , color = 'orange') #I
                ax.plot(t, tab_nb[3] , color = 'pink') #R1
                ax.plot(t, tab_nb[4] , color = '#A51616') #R2
                ax.plot(t, tab_nb[5] , color = 'black') # La population totale
            
            ax.set_ylabel("Nombre d'individus",labelpad=-4,fontsize=18)
            ax.set_xlabel("Nombre de tours",labelpad=2.5,fontsize=18)
            
            canvas = FigureCanvasTkAgg(fig, master=fenetre)  
            canvas.draw()
            canvas.get_tk_widget().grid(row=0*echelle_ligne, column=12*echelle,sticky='nesw',columnspan=10*echelle,rowspan=10*echelle_ligne,padx=5,pady=0)

        
        elif (nb_fenetre==2):

            
            fig = Figure(figsize=(3, 2), dpi=100)
            ax = fig.add_subplot()
            
            if (type_graphique==1):
            
                total_R=np.array(tab_nb[3])+np.array(tab_nb[4])
                total_R.tolist()
                
                ax.set_ylim(0, lim_y)
                ax.plot(t, tab_nb[0] , color = 'blue') #S
                ax.plot(t, tab_nb[1] , color = 'green') #E
                ax.plot(t, tab_nb[2] , color = 'orange') #I
                ax.plot(t, total_R , color = 'red') #R
                
            elif (type_graphique==2):    
                
                
                ax.set_ylim(0, lim_y)
                ax.plot(t, tab_nb[0] , color = 'blue') #S
                ax.plot(t, tab_nb[1] , color = 'green') #E
                ax.plot(t, tab_nb[2] , color = 'orange') #I
                ax.plot(t, tab_nb[3] , color = 'pink') #R1
                ax.plot(t, tab_nb[4] , color = '#A51616') #R2
                ax.plot(t, tab_nb[5] , color = 'black') # La population totale
            
            ax.set_ylabel("Nombre d'individus",labelpad=-4,fontsize=18)
            ax.set_xlabel("Nombre de tours",labelpad=-3,fontsize=18)
            
            canvas2 = FigureCanvasTkAgg(fig, master=fenetre)  
            canvas2.draw()
            canvas2.get_tk_widget().grid(row=2, column=20,sticky='nesw',columnspan=10,rowspan=10,padx=5,pady=0)
    
    
    elif (len(world))==30:
        
        
        echelle=3
        echelle_ligne=2
        
        lim_y=(tab_nb[5][0])+15

        fig = Figure(figsize=(3, 2), dpi=100)
        ax = fig.add_subplot()
        
        if (type_graphique==1):
            
            # On nettoie la légende du graphique
            Tk.Label(fenetre,bg="#87CEEB").grid(row=11*echelle_ligne, column=12*echelle,sticky='nesw',columnspan=10*echelle,rowspan=1*echelle_ligne)
            
            # Légende du graphique SEIR
            Tk.Label(fenetre,bg="#87CEEB",text="R1 + R2 = R",font=("Arial",14,"bold")).grid(row=11*echelle_ligne, column=14*echelle,sticky='nesw',columnspan=5*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="red").grid(row=11*echelle_ligne, column=18*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
        
            total_R=np.array(tab_nb[3])+np.array(tab_nb[4])
            total_R.tolist()
            
            ax.set_ylim(0, lim_y)
            ax.plot(t, tab_nb[0] , color = 'blue') #S
            ax.plot(t, tab_nb[1] , color = 'green') #E
            ax.plot(t, tab_nb[2] , color = 'orange') #I
            ax.plot(t, total_R , color = 'red') #R
            
        elif (type_graphique==2):    
            
            # On nettoie la légende du graphique
            Tk.Label(fenetre,bg="#87CEEB").grid(row=11*echelle_ligne, column=12*echelle,sticky='nesw',columnspan=10*echelle,rowspan=1*echelle_ligne)
            
            # Légende du graphique avancé
            Tk.Label(fenetre,bg="#87CEEB",text="Population",font=("Arial",14,"bold")).grid(row=11*echelle_ligne, column=14*echelle,sticky='nesw',columnspan=5*echelle,rowspan=1*echelle_ligne)
            Tk.Label(fenetre,bg="black").grid(row=11*echelle_ligne, column=18*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
            
            
            ax.set_ylim(0, lim_y)
            ax.plot(t, tab_nb[0] , color = 'blue') #S
            ax.plot(t, tab_nb[1] , color = 'green') #E
            ax.plot(t, tab_nb[2] , color = 'orange') #I
            ax.plot(t, tab_nb[3] , color = 'pink') #R1
            ax.plot(t, tab_nb[4] , color = 'purple') #R2
        
            
        ax.set_ylabel("Nombre d'individus",labelpad=-4,fontsize=18)
        ax.set_xlabel("Nombre de tours",labelpad=2.5,fontsize=18)
        
        canvas = FigureCanvasTkAgg(fig, master=fenetre)  
        canvas.draw()
        canvas.get_tk_widget().grid(row=0*echelle_ligne, column=12*echelle,sticky='nesw',columnspan=10*echelle,rowspan=10*echelle_ligne,padx=5,pady=0)










''' Fonctions d'affichage des fenêtre d'itérations / de simulations'''



def afficher_monde_tkinter(fenetre,original_world,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement,confinement:str,matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement):
    '''
    Affichage de la fenêtre principale, permettant d'itérer le monde
    
    Utilisée dans 'generer_world', 'iterer_tkinter', 'multi_iterer_tkinter' et 'reset'
    '''

    
    delete_grille(fenetre)
    
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
    
    
    # Affiche le monde
    show_world(fenetre,world,1)
    if(len(world)==10): # Pour éviter des problèmes d'échelle
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
    
    
    
    Tk.Button(fenetre, text = "Itérer 1 fois le monde",font=("Arial",18),command=lambda:iterer_tkinter(fenetre,original_world,world,int(incubation.get()),int(transmission.get()),int(guerison.get()),int(mortalite.get()),int(deplacement.get()),nb_tours,tab_nb,matrice_infos_deplacement,str(combobox.get()),matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement)).grid(row=12*echelle_ligne, column=10*echelle,columnspan=1*echelle,rowspan=2*echelle_ligne)
    
    
    nb_tours_itere=Tk.IntVar()
    Tk.Spinbox(fenetre, from_= 0, to = 1000,textvariable=nb_tours_itere,font=("Arial",16)).grid(row=14*echelle_ligne, column=11*echelle,columnspan=1*echelle,rowspan=2*echelle_ligne)
    Tk.Button(fenetre, text = "Itérer n fois le monde",font=("Arial",18),command=lambda:multi_iterer_tkinter(int(nb_tours_itere.get()),fenetre,original_world,world,int(incubation.get()),int(transmission.get()),int(guerison.get()),int(mortalite.get()),int(deplacement.get()),nb_tours,tab_nb,matrice_infos_deplacement,str(combobox.get()),matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement)).grid(row=12*echelle_ligne, column=11*echelle,columnspan=1*echelle,rowspan=2*echelle_ligne)
    
    
    Tk.Label(fenetre,bg="#87CEEB",text="Confinement :",font=("Arial",18,"bold")).grid(row=16*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne,columnspan=1*echelle)
    combobox=Tk.ttk.Combobox(fenetre, values = ["Pas de confinement", "Confinement normal", "Confinement strict"],font=("Arial",18,"bold"))
    combobox.set(confinement)
    combobox.grid(row=16*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne,columnspan=1*echelle)
    
    
    Tk.Button(fenetre, text = "Reset les itérations",font=("Arial",18),command=lambda:reset(fenetre,original_world)).grid(row=18*echelle_ligne, column=10*echelle,columnspan=2*echelle,rowspan=2*echelle_ligne)
    
    if (len(world)==10):
        Tk.Button(fenetre, text = "Simulation générale à partir du monde",font=("Arial",20),command=lambda:setup_affiche_simus_generales(fenetre,world,int(incubation.get()),int(transmission.get()),int(guerison.get()),int(mortalite.get()),int(deplacement.get()),nb_tours,tab_nb,matrice_infos_deplacement,str(combobox.get()),matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement)).grid(row=21*echelle_ligne, column=10*echelle,columnspan=2*echelle,pady=10,rowspan=1*echelle_ligne) 
    
    
    # Partie affichée sous le monde
    
    
    Tk.Button(fenetre, text = "Afficher monde",font=("Arial",18),command=lambda:show_world(fenetre,world,1)).grid(row=15*echelle_ligne+2, column=0*echelle,columnspan=5*echelle,rowspan=1*echelle_ligne) 
    Tk.Button(fenetre, text = "Afficher infections",font=("Arial",18),command=lambda:show_infection(fenetre,matrice_infection,1)).grid(row=15*echelle_ligne+2, column=5*echelle,columnspan=5*echelle,rowspan=1*echelle_ligne) 
    
    Tk.Button(fenetre, text = "Générer un nouveau monde",font=("Arial",20),command=lambda:setup_tkinter(1,fenetre)).grid(row=19*echelle_ligne+2, column=0*echelle,columnspan=10*echelle,pady=10,rowspan=1*echelle_ligne) 
    
    Tk.Label(fenetre,bg="#87CEEB",text="Appuyez sur échap pour quitter",font=("Arial",20,"bold")).grid(row=20*echelle_ligne+2, column=0*echelle,sticky='nesw',rowspan=2*echelle_ligne,columnspan=10*echelle)
    
    
    # Partie du plot à droite
    
    
    show_type_graphique(fenetre, world, nb_tours, tab_nb, 1, 1)
    
    
    Tk.Button(fenetre, text = "Graphique SEIR",font=("Arial",18),command=lambda:show_type_graphique(fenetre, world, nb_tours, tab_nb, 1, 1)).grid(row=10*echelle_ligne, column=12*echelle,columnspan=5*echelle,rowspan=1*echelle_ligne) 
    Tk.Button(fenetre, text = "Graphique avancé",font=("Arial",18),command=lambda:show_type_graphique(fenetre, world, nb_tours, tab_nb, 2, 1)).grid(row=10*echelle_ligne, column=17*echelle,columnspan=5*echelle,rowspan=1*echelle_ligne) 


    if (len(world)==10):
        Tk.Label(fenetre,bg="#87CEEB",text="Données sur les individus en déplacement",font=("Arial",18,"bold")).grid(row=12, column=12,sticky='nesw',rowspan=1,columnspan=10)
    elif (len(world)==30):
        Tk.Label(fenetre,bg="#87CEEB",text="Données sur les individus\n en déplacement",font=("Arial",18,"bold")).grid(row=24, column=40,sticky='nesw',rowspan=2,columnspan=20)


    fig_deplacement = Figure(figsize=(3, 2), dpi=100)
    t = np.arange(0, nb_tours+1, 1)
    ax_deplacement = fig_deplacement.add_subplot()
        
    ax_deplacement.plot(t, tab_nb_deplacement[0] , color = 'blue')
    ax_deplacement.plot(t, tab_nb_deplacement[1] , color = 'green')
    ax_deplacement.plot(t, tab_nb_deplacement[2] , color = 'orange')
    ax_deplacement.plot(t, tab_nb_deplacement[3] , color = 'pink')
    ax_deplacement.plot(t, tab_infectes_pendant_deplacement , color = 'gray')
    
    canvas_deplacement = FigureCanvasTkAgg(fig_deplacement, master=fenetre)  
    canvas_deplacement.draw()
    canvas_deplacement.get_tk_widget().grid(row=13*echelle_ligne, column=13*echelle,sticky='nesw',columnspan=8*echelle,rowspan=8*echelle_ligne)


    Tk.Label(fenetre,bg="#87CEEB",text="Nb d'individus infectés pendant déplacement",font=("Arial",16,"bold"),fg="gray").grid(row=21*echelle_ligne, column=12*echelle,sticky='nesw',rowspan=1*echelle_ligne,columnspan=10*echelle)



def setup_affiche_simus_generales(fenetre,world,incubation,transmission,guerison,mortalite,deplacement,nb_tours,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement):
    '''
    Setup la fenêtre de simulation, on regarde si il y a pas déjà une fenêtre de simulation ouverte
    Si c'est le cas on la détruit avant d'afficher l'affichage de simulation
    
    Utilisée dans'afficher_monde_tkinter' (bouton)
    '''
    
    for widget in fenetre.winfo_children():
        if isinstance(widget,Tk.Toplevel):
            widget.destroy()
            
    fenetre2 = Tk.Toplevel(fenetre)
        
    fenetre2.title("Simulation générale")
    fenetre2.config(bg = "#87CEEB") 
    fenetre2.bind('<Escape>',lambda e: fenetre2.destroy())
        
    #fenetre.geometry("1300x800+500+300")
    fenetre2.geometry("1300x800")
    fenetre2.wm_transient(fenetre)
    center_window(fenetre2)
    
    affiche_simus_generales(fenetre2,world,incubation,transmission,guerison,mortalite,deplacement,nb_tours,tab_nb,matrice_infos_deplacement,True,confinement,matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement,False)

    fenetre2.mainloop()   
    
    
def affiche_simus_generales(fenetre2,world,incubation,transmission,guerison,mortalite,deplacement,nb_tours,tab_nb,matrice_infos_deplacement,first_time,confinement,matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement,donnees_reset_simu):
    '''
    Affiche la fenêtre de simulation
    
    Concernant le paramètre "donnees_reset_simu", si la fonction est appelée avant simulation,
    alors donnees_reset_simu=False. Ca coincide avec first_time=True.
    Sinon si après une simulation on fait un reset, on ré-affiche l'affichage avec les données
    issues de "donnees_reset_simu".
    
    Utilisée dans'setup_affiche_simus_generales'
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
    
    
    if (first_time==True):
        
        # On crée notre tableau de données d'avant simulation
        donnees_reset_simu=[world,incubation,transmission,guerison,mortalite,deplacement,nb_tours,tab_nb,matrice_infos_deplacement,confinement,matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement]
        
        nb_tours2_itere=Tk.IntVar()
        Tk.Spinbox(fenetre2, from_= 0, to = 1000,textvariable=nb_tours2_itere,font=("Arial",20),width=4).grid(row=16, column=7,columnspan=2,pady=10,rowspan=4)
        
        Tk.Button(fenetre2, text = "Simuler n tours",font=("Arial",20),command=lambda:simulation_generale(20,int(nb_tours2_itere.get()),fenetre2,world,int(incubation2.get()),int(transmission2.get()),int(guerison2.get()),int(mortalite2.get()),int(deplacement2.get()),nb_tours,tab_nb,matrice_infos_deplacement,str(combobox.get()),matrice_infection,tab_nb_deplacement,tab_infectes_pendant_deplacement,donnees_reset_simu)).grid(row=16, column=0,columnspan=8,pady=10,rowspan=4)
    
        
    else:
        # En cas de reset, on utilise le tableau de données d'avant simulation pour afficher l'écran de simulation
        # Par contre on reprend les paramètres rentrés avec la simulation
        Tk.Button(fenetre2, text = "Reset simulation",font=("Arial",20),command=lambda:affiche_simus_generales(fenetre2,donnees_reset_simu[0],int(incubation2.get()),int(transmission2.get()),int(guerison2.get()),int(mortalite2.get()),int(deplacement2.get()),donnees_reset_simu[6],donnees_reset_simu[7],donnees_reset_simu[8],True,donnees_reset_simu[9],donnees_reset_simu[10],donnees_reset_simu[11],donnees_reset_simu[12],False)).grid(row=16, column=0,columnspan=10,pady=10,rowspan=4)
    
    
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
    combobox=Tk.ttk.Combobox(fenetre2, values = ["Pas de confinement", "Confinement normal", "Confinement strict"],font=("Arial",18,"bold"))
    combobox.set(confinement)
    combobox.grid(row=12, column=15,rowspan=2,columnspan=5)
    
    
    
    # Graphe classique SEIR 'classique'
    
    S=tab_nb[0][0]
    E=tab_nb[1][0]
    I=tab_nb[2][0]
    R=tab_nb[3][0]+tab_nb[4][0]
    population=tab_nb[5][0]

    params=setup_tab_param(S/100, E/100, I/100, R/100,incubation/100,transmission/100,guerison/100,mortalite/100,nb_tours,population/100)
    # La fonction prend en paramètres des taux, entre 0 et 1, non des pourcentages
    
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Graphique SEIR 'classique',\n obtenu avec équations",font=("Arial",17,"bold")).grid(row=14, column=10,sticky='nesw',columnspan=10,rowspan=2)
    
    fig2_SEIR_classique = Figure(figsize=(3, 2), dpi=100)
    ax2_SEIR_classique = fig2_SEIR_classique.add_subplot()
    
    # On affiche les valeurs sur une échelle de 0 à 100
    ax2_SEIR_classique.plot(params[5], np.array(params[0])*100 , color = 'blue')
    ax2_SEIR_classique.plot(params[5], np.array(params[1])*100 , color = 'green')
    ax2_SEIR_classique.plot(params[5], np.array(params[2])*100 , color = 'orange')
    ax2_SEIR_classique.plot(params[5], np.array(params[3])*100 , color = 'red')
    ax2_SEIR_classique.plot(params[5], np.array(params[4])*100 , color = 'black')
    
    canvas2_SEIR_classique = FigureCanvasTkAgg(fig2_SEIR_classique, master=fenetre2)  
    canvas2_SEIR_classique.draw()
    canvas2_SEIR_classique.get_tk_widget().grid(row=16, column=10,sticky='nesw',columnspan=10,rowspan=10,padx=5,pady=5)
    




    
    # Affichage de droite de la fenêtre
    
    if (first_time==True):
        Tk.Label(fenetre2,bg="#87CEEB",text="Notre graphe avant simulation",font=("Arial",18,"bold")).grid(row=0, column=20,sticky='nesw',columnspan=10,rowspan=2)
    else:
        Tk.Label(fenetre2,bg="#87CEEB",text="Notre graphe après simulation",font=("Arial",18,"bold")).grid(row=0, column=20,sticky='nesw',columnspan=10,rowspan=2)
    
    
    show_type_graphique(fenetre2, world, nb_tours, tab_nb, 1, 2)
    
    
    Tk.Button(fenetre2, text = "Graphique SEIR",font=("Arial",18),command=lambda:show_type_graphique(fenetre2, world, nb_tours, tab_nb, 1, 2)).grid(row=12, column=20,columnspan=5,rowspan=1) 
    Tk.Button(fenetre2, text = "Graphique avancé",font=("Arial",18),command=lambda:show_type_graphique(fenetre2, world, nb_tours, tab_nb, 2, 2)).grid(row=12, column=25,columnspan=5,rowspan=1) 
    
    
    if (first_time==True):
        Tk.Label(fenetre2,bg="#87CEEB",text="Données sur les individus en\n déplacement avant simulation",font=("Arial",17,"bold")).grid(row=14, column=20,sticky='nesw',rowspan=2,columnspan=10)
    else:
        Tk.Label(fenetre2,bg="#87CEEB",text="Données sur les individus en\n déplacement après simulation",font=("Arial",17,"bold")).grid(row=14, column=20,sticky='nesw',rowspan=2,columnspan=10)

    fig2_deplacement = Figure(figsize=(3, 2), dpi=100)
    t = np.arange(0, nb_tours+1, 1)
    ax2_deplacement = fig2_deplacement.add_subplot()
        
    ax2_deplacement.plot(t, tab_nb_deplacement[0] , color = 'blue')
    ax2_deplacement.plot(t, tab_nb_deplacement[1] , color = 'green')
    ax2_deplacement.plot(t, tab_nb_deplacement[2] , color = 'orange')
    ax2_deplacement.plot(t, tab_nb_deplacement[3] , color = 'pink')
    ax2_deplacement.plot(t, tab_infectes_pendant_deplacement , color = 'gray')
    
    canvas2_deplacement = FigureCanvasTkAgg(fig2_deplacement, master=fenetre2)  
    canvas2_deplacement.draw()
    canvas2_deplacement.get_tk_widget().grid(row=16, column=20,sticky='nesw',columnspan=10,rowspan=10,padx=5,pady=5)



''' Lance l'interface ''' 

setup_tkinter(1,False)

