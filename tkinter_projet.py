# -*- coding: utf-8 -*-

import numpy as np
import tkinter as Tk
from matplotlib import pyplot as plt
from main import *
import copy


from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


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
        
        Tk.Scale(fenetre,variable=nb_S_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=200).grid(row=0, column=6,columnspan=2)
        Tk.Scale(fenetre,variable=nb_E_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=200).grid(row=1, column=6,columnspan=2)
        Tk.Scale(fenetre,variable=nb_I_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=200).grid(row=2, column=6,columnspan=2)
        Tk.Scale(fenetre,variable=nb_R_grand,font=("Arial",20),bg="#87CEEB",from_=0,to=900,resolution=1,orient="horizontal",length=200).grid(row=3, column=6,columnspan=2)        

        
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
    
    if (aleatoire==True):
        delete_grille(fenetre)
        
        if(maxi==100):
            world=generate_random_world_SEIR()
        else:
            world=generate2_random_world_SEIR()
        matrice_infos_deplacement=[[],[],[]]
        tab_nb=number_types(world,tab_nb)
        afficher_monde_tkinter(fenetre,world,0,0,0,0,0,0,tab_nb,matrice_infos_deplacement)
        
    elif (aleatoire==False and somme <=maxi):
        delete_grille(fenetre)
        
        if(maxi==100):
            world=generate_world_SEIR(nb_S, nb_E, nb_I, nb_R)
        else:
            world=generate2_world_SEIR(nb_S, nb_E, nb_I, nb_R)
        matrice_infos_deplacement=[[],[],[]]
        tab_nb=number_types(world,tab_nb)
        afficher_monde_tkinter(fenetre,world,0,0,0,0,0,0,tab_nb,matrice_infos_deplacement)
    
    elif (aleatoire==False and somme >maxi): 
        if (maxi==100):
            setup_tkinter(2,fenetre)
        else :
            setup_tkinter(3,fenetre)




def iterer_tkinter(fenetre,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement):
    '''
    Fonction intermédiaure appelée par l'itération tkinter, affiche le nouveau 
    monde après itération
    '''
    world,matrice_infos_deplacement=evolution_world_SEIR(world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,matrice_infos_deplacement)
    tab_nb=number_types(world,tab_nb)
    afficher_monde_tkinter(fenetre,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours+1,tab_nb,matrice_infos_deplacement)



def multi_iterer_tkinter(nb_tours_itere,fenetre,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement):
    '''
    Fonction intermédiaure appelée par l'itération tkinter, affiche le nouveau 
    monde après plusieurs itérations
    '''
    if (nb_tours_itere<0 or nb_tours_itere>200):
        nb_tours_itere=0
    
    
    for i in range(nb_tours_itere):
        world,matrice_infos_deplacement=evolution_world_SEIR(world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,matrice_infos_deplacement)
        tab_nb=number_types(world,tab_nb)
        
    afficher_monde_tkinter(fenetre,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,(nb_tours+nb_tours_itere),tab_nb,matrice_infos_deplacement)


def simulation_generale(nb_simus,nb_tours_itere,fenetre2,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement):
    '''
    Permet de récupérer la moyenne de "nb_simus" simulations sur "nb_tours_itere" tours
    à partir d'un monde de départ "world". Affiche ensuite le résultat avec
    la fonction affiche_simus_generales sur l'écran de simulation
    '''
    
    world_simu=[]
    matrice_infos_deplacement_simu=[]
    tab_nb_simu=[]
    
    for i in range(nb_simus):
        world_simu=copy.deepcopy(world)
        matrice_infos_deplacement_simu=copy.deepcopy(matrice_infos_deplacement)
        tab_nb_simu=copy.deepcopy(tab_nb)
        
        
        for j in range(nb_tours_itere):
            world_simu,matrice_infos_deplacement_simu=evolution_world_SEIR(world_simu,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,matrice_infos_deplacement_simu)
            tab_nb_simu=number_types(world_simu,tab_nb_simu)
        
        # tab_nb_resultat : np.array
        if (i==0):
            tab_nb_resultat=np.array(tab_nb_simu)
        else:
            tab_nb_resultat=tab_nb_resultat+np.array(tab_nb_simu)
    
    tab_nb_resultat=tab_nb_resultat/nb_simus
    tab_nb_resultat=tab_nb_resultat.tolist()
    
    affiche_simus_generales(fenetre2,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours+nb_tours_itere,tab_nb_resultat,matrice_infos_deplacement_simu,False)
        

def afficher_monde_tkinter(fenetre,world,old_incubation,old_transmission,old_guerison,old_mortalite,old_deplacement,nb_tours,tab_nb,matrice_infos_deplacement):
    '''
    Affichage permettant d'itérer le monde
    '''
    
    delete_grille(fenetre)
    
    fenetre.geometry("1400x800+200+150")
    fenetre.title("Modélisation évolution d'épidémie")
    
    fenetre.attributes('-fullscreen', True)
    fenetre.bind('<Escape>',lambda e: fenetre.destroy())
    
    
    echelle=1
    echelle_ligne=1
    echelle_pad_grille=1
    if(len(world)==30):
        echelle=3
        echelle_ligne=2
        echelle_pad_grille=0.1
    
    # Setup la fenêtre en grille
    
    for i in range(22*echelle):
        fenetre.columnconfigure(i, weight=1)
    for j in range(20*echelle_ligne):
        fenetre.rowconfigure(j, weight=1)
    
    
    world_color=number_to_color(world)
    
    # Sert à attribuer les couleurs aux cases de la grille selon les types
    
    for y in range(len(world)):
        for x in range(len(world[y])):
            Tk.Label(fenetre,bg=world_color[y][x]).grid(row=y, column=x,sticky='nesw',padx=5*echelle_pad_grille, pady=5*echelle_pad_grille)
    
    
    
    
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
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage \nd'incubation :",font=("Arial",14,"bold")).grid(row=2*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne)
    Tk.Scale(fenetre,variable=incubation,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=2*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage de \ntransmission :",font=("Arial",14,"bold")).grid(row=4*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne)
    Tk.Scale(fenetre,variable=transmission,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=4*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage de \nguérison :",font=("Arial",14,"bold")).grid(row=6*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne)
    Tk.Scale(fenetre,variable=guerison,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=6*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage de \nmortalité :",font=("Arial",14,"bold")).grid(row=8*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne)
    Tk.Scale(fenetre,variable=mortalite,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=8*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne)
    
    Tk.Label(fenetre,bg="#87CEEB",text="Pourcentage de \ndéplacement :",font=("Arial",14,"bold")).grid(row=10*echelle_ligne, column=10*echelle,sticky='nesw',rowspan=2*echelle_ligne)
    Tk.Scale(fenetre,variable=deplacement,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=10*echelle_ligne, column=11*echelle,rowspan=2*echelle_ligne)
    
    
    
    Tk.Button(fenetre, text = "Itérer 1 fois le monde",font=("Arial",18),command=lambda:iterer_tkinter(fenetre,world,int(incubation.get()),int(transmission.get()),int(guerison.get()),int(mortalite.get()),int(deplacement.get()),nb_tours,tab_nb,matrice_infos_deplacement)).grid(row=12*echelle_ligne, column=10*echelle,columnspan=1*echelle,rowspan=2*echelle_ligne)
    
    
    nb_tours_itere=Tk.IntVar()
    Tk.Spinbox(fenetre, from_= 0, to = 1000,textvariable=nb_tours_itere,font=("Arial",16)).grid(row=13*echelle_ligne, column=11*echelle,columnspan=1*echelle,rowspan=2*echelle_ligne)
    Tk.Button(fenetre, text = "Itérer n fois le monde",font=("Arial",18),command=lambda:multi_iterer_tkinter(int(nb_tours_itere.get()),fenetre,world,int(incubation.get()),int(transmission.get()),int(guerison.get()),int(mortalite.get()),int(deplacement.get()),nb_tours,tab_nb,matrice_infos_deplacement)).grid(row=12*echelle_ligne, column=11*echelle,columnspan=1*echelle,rowspan=2*echelle_ligne)
    
    
    # Partie affichée sous le monde
    
    Tk.Label(fenetre,bg="#87CEEB",text="Légende :",font=("Arial",20,"bold")).grid(row=14*echelle_ligne, column=0*echelle,sticky='nesw',columnspan=10*echelle,rowspan=1*echelle_ligne)
    
    Tk.Label(fenetre,bg="#87CEEB",text="S",font=("Arial",16,"bold")).grid(row=16*echelle_ligne, column=0*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
    Tk.Label(fenetre,bg="blue").grid(row=16*echelle_ligne, column=1*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)

    Tk.Label(fenetre,bg="#87CEEB",text="E",font=("Arial",16,"bold")).grid(row=16*echelle_ligne, column=2*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
    Tk.Label(fenetre,bg="green").grid(row=16*echelle_ligne, column=3*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)

    Tk.Label(fenetre,bg="#87CEEB",text="I",font=("Arial",16,"bold")).grid(row=16*echelle_ligne, column=4*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
    Tk.Label(fenetre,bg="orange").grid(row=16*echelle_ligne, column=5*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
    
    Tk.Label(fenetre,bg="#87CEEB",text="R",font=("Arial",16,"bold")).grid(row=16*echelle_ligne, column=6*echelle,sticky='nesw',columnspan=1*echelle,rowspan=1*echelle_ligne)
    Tk.Label(fenetre,bg="red").grid(row=16*echelle_ligne, column=7*echelle,sticky='nesw',padx=5, pady=5,rowspan=1*echelle_ligne,columnspan=1*echelle_ligne)
    
    Tk.Button(fenetre, text = "Générer un nouveau monde",font=("Arial",20),command=lambda:setup_tkinter(1,fenetre)).grid(row=17*echelle_ligne, column=0*echelle,columnspan=10*echelle,pady=10,rowspan=1*echelle_ligne) 
    
    Tk.Label(fenetre,bg="#87CEEB",text="Appuyez sur échap pour quitter",font=("Arial",20,"bold")).grid(row=18*echelle_ligne, column=0*echelle,sticky='nesw',rowspan=2*echelle_ligne,columnspan=10*echelle)
    
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
    canvas.get_tk_widget().grid(row=0*echelle, column=12*echelle,sticky='nesw',columnspan=10*echelle,rowspan=10*echelle_ligne,padx=5,pady=0)

    if (len(world)==10):
        Tk.Button(fenetre, text = "Simulation générale à partir du monde",font=("Arial",20),command=lambda:setup_affiche_simus_generales(fenetre,world,int(incubation.get()),int(transmission.get()),int(guerison.get()),int(mortalite.get()),int(deplacement.get()),nb_tours,tab_nb,matrice_infos_deplacement)).grid(row=17*echelle_ligne, column=12*echelle,columnspan=10*echelle,pady=10,rowspan=1*echelle_ligne) 





def setup_affiche_simus_generales(fenetre,world,incubation,transmission,guerison,mortalite,deplacement,nb_tours,tab_nb,matrice_infos_deplacement):
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
    fenetre2.geometry("1400x600")
    fenetre2.attributes('-topmost', 1)
    center_window(fenetre2)
    
    affiche_simus_generales(fenetre2,world,incubation,transmission,guerison,mortalite,deplacement,nb_tours,tab_nb,matrice_infos_deplacement,True)

    fenetre2.mainloop()   
    
    
def affiche_simus_generales(fenetre2,world,incubation,transmission,guerison,mortalite,deplacement,nb_tours,tab_nb,matrice_infos_deplacement,first_time):
    '''
    Affiche la fenêtre de simulation
    ''' 
    
    for i in range(22):
        fenetre2.columnconfigure(i, weight=1)
    for j in range(20):
        fenetre2.rowconfigure(j, weight=1)
    
    delete_grille(fenetre2)
    
    # Affichage de gauche de la fenêtre
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Notre monde avant simulation",font=("Arial",18,"bold")).grid(row=0, column=0,sticky='nesw',columnspan=10,rowspan=2)
    
    world_color=number_to_color(world)
    
    for y in range(len(world)):
        for x in range(len(world[y])):
            Tk.Label(fenetre2,bg=world_color[y][x]).grid(row=2+y, column=x,sticky='nesw',padx=5, pady=5)
    
    
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
    
    
    # Affichage du milieu de la fenêtre
    
    text_nb_tours=str(nb_tours)
    Tk.Label(fenetre2,bg="#87CEEB",text="Tours : "+text_nb_tours,font=("Arial",30,"bold")).grid(row=0, column=10,sticky='nesw',columnspan=2,rowspan=2)
    
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Pourcentage \nd'incubation :",font=("Arial",14,"bold")).grid(row=2, column=10,sticky='nesw',rowspan=2)
    Tk.Scale(fenetre2,variable=incubation2,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=2, column=11,rowspan=2)
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Pourcentage de \ntransmission :",font=("Arial",14,"bold")).grid(row=4, column=10,sticky='nesw',rowspan=2)
    Tk.Scale(fenetre2,variable=transmission2,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=4, column=11,rowspan=2)
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Pourcentage de \nguérison :",font=("Arial",14,"bold")).grid(row=6, column=10,sticky='nesw',rowspan=2)
    Tk.Scale(fenetre2,variable=guerison2,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=6, column=11,rowspan=2)
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Pourcentage de \nmortalité :",font=("Arial",14,"bold")).grid(row=8, column=10,sticky='nesw',rowspan=2)
    Tk.Scale(fenetre2,variable=mortalite2,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=8, column=11,rowspan=2)
    
    Tk.Label(fenetre2,bg="#87CEEB",text="Pourcentage de \ndéplacement :",font=("Arial",14,"bold")).grid(row=10, column=10,sticky='nesw',rowspan=2)
    Tk.Scale(fenetre2,variable=deplacement2,font=("Arial",14),bg="#87CEEB",from_=0,to=100,resolution=1,orient="horizontal",length=200).grid(row=10, column=11,rowspan=2)
    
    
    if (first_time==True):
        Tk.Button(fenetre2, text = "Simuler (100 tours)",font=("Arial",20),command=lambda:simulation_generale(30,100,fenetre2,world,int(incubation2.get()),int(transmission2.get()),int(guerison2.get()),int(mortalite2.get()),int(deplacement2.get()),nb_tours,tab_nb,matrice_infos_deplacement)).grid(row=12, column=10,columnspan=2,pady=10,rowspan=2)
        
        

    
    # Affichage de droite de la fenêtre
    
    if (first_time==True):
        Tk.Label(fenetre2,bg="#87CEEB",text="Notre graphe avant simulation",font=("Arial",18,"bold")).grid(row=0, column=12,sticky='nesw',columnspan=10,rowspan=2)
    else:
        Tk.Label(fenetre2,bg="#87CEEB",text="Notre graphe après simulation",font=("Arial",18,"bold")).grid(row=0, column=12,sticky='nesw',columnspan=10,rowspan=2)
    
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
    canvas2.get_tk_widget().grid(row=2, column=12,sticky='nesw',columnspan=10,rowspan=10,padx=5,pady=0)
    
    
    
''' Lance l'interface ''' 

setup_tkinter(1,False)

