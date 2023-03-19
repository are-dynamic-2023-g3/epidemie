# -*- coding: utf-8 -*-

import numpy as np
import tkinter as Tk
from matplotlib import pyplot as plt


'''
α = alpha (taux d'incubation)
β = beta (taux de transmission)
γ = gamma (taux de guérison)
μ = mu (taux de mortailté)

S = personnes saines (taux entre 0 et 1)
E = personnes infectées non infectieuses (taux entre 0 et 1)
I = personnes infectées infectieusess (taux entre 0 et 1)
R = personnes retirées guéries ou mortes (taux entre 0 et 1)


'''

nb_temps=20

alpha=0.8
beta=0.5
gamma=0.1
mu=0.05

S=0.65
E=0.1
I=0.25
R=0
population=1

#S+E+I+R=1

def dS(beta,S,I,mu):
    '''
    Equation derivée parametre S modele SEIR
    '''
    return -beta*S*I

def dE(beta,S,I,alpha,E,mu):
    '''
    Equation derivée parametre E modele SEIR
    '''
    return beta*S*I-alpha*E

def dI(I,alpha,E,gamma,mu):
    '''
    Equation derivée parametre I modele SEIR
    '''
    return alpha*E-gamma*I

def dR(I,gamma,mu,R):
    '''
    Equation derivée parametre R modele SEIR
    '''
    return gamma*I


def setup_tab_param(S:float, E:float, I:float, R:float,alpha,beta,gamma,mu,nb_temps,population):
    '''
    Hypothese:
    Parametres en taux entre 0 et 1
    
    Renvoie les donnees du modele SEIR sous forme de tableaux, 
    avec un modele appliqué "nb_temps" fois
    
    '''
    
    
    tab_S=[S]
    tab_E=[E]
    tab_I=[I]
    tab_R=[R]
    tab_population=[population]
    tab_temps=[0]
    population_debut=population
    
    for i in range(nb_temps):
        
        S_nouveau=S+dS(beta,S,I,mu)
        tab_S.append(S_nouveau)
        
        E_nouveau=E+dE(beta,S,I,alpha,E,mu)
        tab_E.append(E_nouveau)
        
        I_nouveau=I+dI(I,alpha,E,gamma,mu)
        tab_I.append(I_nouveau)
        
        R_nouveau=R+dR(I,gamma,mu,R)
        tab_R.append(R_nouveau)
        
        
        S=S_nouveau
        E=E_nouveau
        I=I_nouveau
        R=R_nouveau
        
        population=population_debut-mu*R
        tab_population.append(population)

        tab_temps.append(i+1)
    
    return tab_S,tab_E,tab_I,tab_R,tab_population,tab_temps


def show_plot_SEIR(S:float, E:float, I:float, R:float,alpha,beta,gamma,mu,nb_temps,population):
    '''
    Hypothese:
    Parametres en taux entre 0 et 1
    
    Appelle setup_tab_param pour afficher les donnees obtenues en graphiques
    '''
    
    params=setup_tab_param(S,E,I,R,alpha,beta,gamma,mu,nb_temps,population)
    
    
    # S E I R affichés en pourcents entre 0 et 100
    plt.plot(params[5], np.array(params[0])*100, color = 'blue') #S
    plt.plot(params[5], np.array(params[1])*100, color = 'green') #E
    plt.plot(params[5], np.array(params[2])*100, color = 'orange') #I
    plt.plot(params[5], np.array(params[3])*100, color = 'red') #R
    plt.plot(params[5], np.array(params[4])*100, color = 'purple') #Population
    
    plt.show()
        
        
#show_plot_SEIR(S,E,I,R,alpha,beta,gamma,mu,nb_temps,population)   
        
        

def generate_world_SEIR(nb_S:int, nb_E:int, nb_I:int, nb_R:int):
    '''
    Hypotheses:
        
    Les parametres sont le nombre d'individus de chaque groupe
    nb_S+nb_E+nb_I+nb_R <= 100
    
    SI nb_S+nb_E+nb_I+nb_R = 100 -> 0 espace vide
    
    
    
    Crée et renvoit un monde 2D 10*10 avec "nb_S" individus S, "nb_E" individus E,
    "nb_I" individus I, "nb_R" individus R
    
    Dans monde 2D :

    Espace innocupé = 0
    Personne saine = 1 := S
    Personne infectée non infectieuse = 2 := E
    Personne infectée infectieuse = 3 := I
    Personne retirée = 4 := R
    
    '''
    world=np.zeros((10,10))
    
    
    probas_individus=[nb_S,nb_E,nb_I,nb_R] #Ce tableau change pas
    nombre_individus=[nb_S,nb_E,nb_I,nb_R] #Ce tableau change
    
    boucler=True
    
    while (boucler==True) :
        
        
        for y in range(10):
            for x in range(10):
                
                
                nb_S=nombre_individus[0]
                nb_E=nombre_individus[1]
                nb_I=nombre_individus[2]
                nb_R=nombre_individus[3]
                
                if (world[y][x]==0):
                
                    if (nb_S!=0 or nb_E!=0 or nb_I!=0 or nb_R!=0):
                        
                        type_individu=np.random.randint(1,5) # 5 exclu
                        
                        while (nombre_individus[type_individu-1]==0):
                                type_individu=np.random.randint(1,5) # 5 exclu
                        
                        proba = np.random.randint(0,101) # 101 exclu
                        
                        if (proba<=probas_individus[type_individu-1]):
                            world[y][x]=type_individu
                            nombre_individus[type_individu-1]=nombre_individus[type_individu-1]-1
        
        
                    if (nb_S==0 and nb_E==0 and nb_I==0 and nb_R==0):
                        boucler=False
                    
    
    return world


def generate_random_world_SEIR():
    '''
    Appelle generate_world_SEIR avec des parametres aléatoires et le renvoit
    
    On garde toujours un nombre de personnes retirées = 0
    à la création du monde aléatoire
    
    '''
    
    nb_espaces_vide=np.random.randint(0,69)
    
    nb_S=np.random.randint(30,100-nb_espaces_vide)
    nb_E=np.random.randint(0,100-(nb_S+nb_espaces_vide))
    nb_I=100-(nb_espaces_vide+nb_S+nb_E)
    
    
    return generate_world_SEIR(nb_S,nb_E,nb_I,0)

#print(generate_world_SEIR(40,10,0,0))

#print(generate_random_world_SEIR())


'''
def deplacement_world_SEIR()
'''


def distance(world,x,y):
    '''
    
    Renvoit la liste des coordonnes des points voisins du
    point (x,y) dans le monde "world", en excluant les emplacements vides

    '''
    liste_coordonnees=[]
    
    for j in range(10):
        for i in range(10):
            
            if(np.maximum(np.abs(i-x),np.abs(j-y)) == 1 and (i,j) != (x,y) and world[j][i]!=0):
                liste_coordonnees.append((i,j))
    
    return liste_coordonnees




def evolution_world_SEIR(world,proba_incubation,proba_transmission,proba_retire):
    '''
    Hypothese: les probabilites sont sous formes de pourcentages
    
    Effectue un tour du monde et met à jour l'etat de chaque individu
    Renvoit ensuite le nouveau monde
    '''
    
    
    
    for y in range(10):
        for x in range(10):    
            
            liste_coordonnees = distance(world,x,y)
            
            if(len(liste_coordonnees)>0 and world[y][x]!=0):
                
                if (world[y][x]==1): # On regarde un individu sain (S)
                    
                    for coord in liste_coordonnees:
                        
                        
                        
                        x_coord = coord[0]
                        y_coord = coord[1]
                        
                        if(world[y_coord][x_coord]==3): # Si un des ses voisins est infectieux (I)
                            
                            proba=np.random.randint(0,101)
                            
                            if (proba<=proba_transmission):
                                world[y][x]=2 # L'individu est contaminé non infectieux (E)
                
                else:
                    
                    if (world[y][x]==2): # On regarde un individu contaminé non infectieux (E)
                        
                    
                        proba=np.random.randint(0,101)
                                
                        if (proba<=proba_incubation):
                            world[y][x]=3 # L'individu devient infectieux (I)
                            
                        
                    else :
                        
                        if (world[y][x]==3): # On regarde un individu infectieux (I)
                            
                        
                            proba=np.random.randint(0,101)
                                    
                            if (proba<=proba_retire):
                                world[y][x]=4 # L'individu est guérri ou mort (R)
    
    return world
                    
                
        
def affiche_monde(world:list):
    
    '''
    Affiche un tableau python de type list de facon plus propre et lisible
    '''
    
    print(np.array(world))         
        
        
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


'''
proba_incubation_test=50
proba_transmission_test=30
proba_retire_test=30


for i in range(10):
    monde_test=evolution_world_SEIR(monde_test,proba_incubation_test,proba_transmission_test,proba_retire_test)
    affiche_monde(monde_test)
    
'''