# -*- coding: utf-8 -*-

import numpy as np
import tkinter as Tk
from matplotlib import pyplot as plt



'''
POUR L'INTERFACE GRAPHIQUE IL FAUT EXECUTER tkinter_projet.py
'''


'''
α = alpha (taux d'incubation)
β = beta (taux de transmission)
γ = gamma (taux de guérison + mortalité)
μ = mu (taux de mortalité) #(pas utilisé ici)
S = personnes saines (taux entre 0 et 1)
E = personnes infectées non infectieuses (taux entre 0 et 1)
I = personnes infectées infectieusess (taux entre 0 et 1)
R = personnes retirées guéries ou mortes (taux entre 0 et 1)
'''



''' PARTIE EQUATIONS SEIR ET GRAPHES SEIR'''



nb_temps=60

alpha=0.3
beta=0.8
gamma=0.5
mu=0.05 #(pas utilisé ici)

S=0.75
E=0.1
I=0.15
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
    #plt.plot(params[5], np.array(params[4])*100, color = 'purple') #Population
    
    plt.ylabel('Pourcentage de population')
    plt.xlabel('Temps (unité arbitraire)')
    
    plt.show()
        
        
#show_plot_SEIR(S,E,I,R,alpha,beta,gamma,mu,nb_temps,population)   
        





def affiche_monde(world:list):
    
    '''
    Affiche un tableau python de type list de facon plus propre et lisible
    '''
    
    print(np.array(world))         






''' PARTIE MONDE SEIR SPATIAL '''




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
    
    nb_espaces_vide=np.random.randint(0,59)
    
    nb_S=np.random.randint(40,100-nb_espaces_vide)
    nb_E=np.random.randint(0,100-(nb_S+nb_espaces_vide))
    nb_I=100-(nb_espaces_vide+nb_S+nb_E)
    
    
    return generate_world_SEIR(nb_S,nb_E,nb_I,0)


#print(generate_world_SEIR(40,10,0,0))
#print(generate_random_world_SEIR())



def generate2_world_SEIR(nb_S:int, nb_E:int, nb_I:int, nb_R:int):
    '''
    Version 2 de generate_world_SEIR qui renvoit un monde 30*30 (900 individus)
    '''
    world=np.zeros((30,30))
    
    # On met les probas sur une échelle de 0 à 100
    probas_individus=[(nb_S/900)*100,(nb_E/900)*100,(nb_I/900)*100,(nb_R/900)*100] #Ce tableau change pas
    nombre_individus=[nb_S,nb_E,nb_I,nb_R] #Ce tableau change
    
    boucler=True
    while (boucler==True) :
        
        
        for y in range(30):
            for x in range(30):
                
                
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


def generate2_random_world_SEIR():
    '''
    Version 2 de generate_random_world_SEIR qui renvoit un monde aléatoire 30*30 (900 individus)
    
    '''
    
    nb_espaces_vide=np.random.randint(0,559)
    
    nb_S=np.random.randint(340,900-nb_espaces_vide)
    nb_E=np.random.randint(0,900-(nb_S+nb_espaces_vide))
    nb_I=900-(nb_espaces_vide+nb_S+nb_E)
    
    
    return generate2_world_SEIR(nb_S,nb_E,nb_I,0)










def distance(world,x,y):
    '''
    
    Renvoit la liste des coordonnes des points voisins du
    point (x,y) dans le monde "world", en excluant les emplacements vides
    '''
    liste_coordonnees=[]
    
    for j in range(len(world)):
        for i in range(len(world[j])):
            
            if(np.maximum(np.abs(i-x),np.abs(j-y)) == 1 and (i,j) != (x,y) and world[j][i]!=0):
                liste_coordonnees.append((i,j))
    
    return liste_coordonnees


def zero_voisin(world,x,y):
    '''
    
    Verifie s'il existe un espace vide autour d'un individu 
    point (x,y) dans le monde "world", en excluant les emplacements vides
    '''
    
    for j in range(len(world)):
        for i in range(len(world[j])):
            
            if(np.maximum(np.abs(i-x),np.abs(j-y)) == 1 and (i,j) != (x,y) and world[j][i]==0):
                return True
    return False


    
def coordonnees_zero(world,coordonnees_origine):
    '''
    
    Renvoie la liste des coordonnees des espaces vides du monde 'world'
    
    '''
    
    liste_coordonnees = []
    
    for j in range(len(world)):
        for i in range(len(world[j])):
            
            if (world[j][i]==0 and (i,j) not in coordonnees_origine):
                liste_coordonnees.append((i,j))
    
    return liste_coordonnees





def deplacement_world_SEIR(world,x,y,coordonnees_origine):
    '''
    Hypothese : verifiée à l'appel, l'individu est au bord d'un rassemblement et il
    y a au minimum une place dispo pour se déplacer
    
    Renvoit le monde actualisé après déplacement d'un individu de coordonnees d'origine 
    (x,y), en plus de renvoyer les nouvelles coordonnées (i,j)
    
    '''
    
    places_pour_se_deplacer = coordonnees_zero(world,coordonnees_origine)
    
    # Choisit les nouvelles coordonnes au hasard
    indice_coordonnees = np.random.randint(0,len(places_pour_se_deplacer))
    new_coordonnees=places_pour_se_deplacer[indice_coordonnees]
        
    i = new_coordonnees[0]
    j = new_coordonnees[1]
        
    tmp=world[y][x]
    world[j][i]=tmp
    world[y][x]=0

    return world,i,j

        
matrice_infection = np.zeros((10,10))
matrice_infos_deplacement=[[],[],[]]
def evolution_world_SEIR(world,proba_incubation,proba_transmission,proba_guerison,proba_mort,proba_deplacement,matrice_infos_deplacement, confinement, matrice_infection):
    '''
    Hypothese: les probabilites sont sous formes de pourcentages
    
    Effectue un tour du monde et met à jour l'etat de chaque individu
    Renvoit ensuite le nouveau monde, en plus de la matrice_infos_deplacement
    
    
    
    
    Lors du tour, un individu soit se déplace, soit est susceptible de changer d'état
    Il peut soit être dans un des 2 cas, soit dans aucun cas, mais jamais dans les 2
    pendant le même tour
    
    A noter qu'on dispose d'une matrice_infos_deplacement, elle contient 3 tableaux :
        - un contenant des tuples de coordonnées d'origines d'individus avant déplacement
        - un contenant des tuples de coordonnées de destination d'individus après déplacement
        - un contenant le nombre de tours restant du déplacement de l'individu
        
    Chaque individu qui se déplace part à des coordonnées dispos pendant max 10 tours,
    avant de revenir à son point de départ (il peut changer d'état entre temps)
                                            
    La valeur du parametre confinement ne doit prendre que soit 0, soit 1 soit 2:
        - si confinement = "Pas de confinement": il n'y a pas de confinement
        - si confinement = "Confinement normal": il y a un confinement mais il reste des chances pour les individus de se deplacer
        - si confinement = "Confinement strict": il n'y a aucune chance que les individus se deplacent
    
    '''
  
    
    #matrice_infos_deplacement de la forme [[coordonnees_origine],[coordonnees_cible],[nb_tours_restants]]
    
    coordonnees_origine=matrice_infos_deplacement[0]
    coordonnees_cible=matrice_infos_deplacement[1]
    nb_tours_restants=matrice_infos_deplacement[2]
    # Les 3 tableaux sont de même longueur de sorte que lorsque on fait
    # coordonnees_origine[i], coordonnees_cible[i] ou nb_tours_restants[i]
    # on récupère les informations d'un individu en déplacement
    

    
    if (confinement == "Confinement normal"): 
        
        proba_deplacement = proba_deplacement / 10
    
    if (confinement == "Confinement strict"):
        
        proba_deplacement = 0
    
    
    for y in range(len(world)):
        for x in range(len(world[y])):    
            
    
            if (world[y][x]!=0):
            
                places_pour_se_deplacer = coordonnees_zero(world,coordonnees_origine)
    
                proba=np.random.randint(1,101)
                
                
                # Cas où l'individu se déplace pendant le tour
                if(proba<=proba_deplacement and (x,y) not in coordonnees_cible and len(places_pour_se_deplacer)>0 and zero_voisin(world, x, y)==True):
                    
                    world,x_nouv,y_nouv=deplacement_world_SEIR(world,x,y,coordonnees_origine)
                    
                    coordonnees_origine.append((x,y))
                    coordonnees_cible.append((x_nouv,y_nouv))
                    
                    nb_tours=np.random.randint(1,10)
                    nb_tours_restants.append(nb_tours)
                
                # Sinon on regarde si l'individu change d'état
                else:
                
                    liste_coordonnees = distance(world,x,y)
                    
                    if(len(liste_coordonnees)>0):
                        
                        if (world[y][x]==1): # On regarde un individu sain (S)
                            
                            for coord in liste_coordonnees:
                                
                                
                                
                                x_coord = coord[0]
                                y_coord = coord[1]
                                
                                if(world[y_coord][x_coord]==3): # Si un des ses voisins est infectieux (I)
                                    
                                    proba=np.random.randint(1,101)
                                    
                                    if (proba<=proba_transmission):
                                        world[y][x]=2 # L'individu est contaminé non infectieux (E)
                                        matrice_infection[y_coord][x_coord]= matrice_infection[y_coord][x_coord] + 1
                                        
                        
                        else:
                            
                            if (world[y][x]==2): # On regarde un individu contaminé non infectieux (E)
                                
                            
                                proba=np.random.randint(1,101)
                                        
                                if (proba<=proba_incubation):
                                    world[y][x]=3 # L'individu devient infectieux (I)
                                    
                                
                            else :
                                
                                if (world[y][x]==3): # On regarde un individu infectieux (I)
                                    
                                
                                    proba=np.random.randint(1,101)
                                            
                                    if (proba<=((proba_guerison+proba_mort)/2)): # Pour R, moyenne guérison et mort pour l'instant
                                        world[y][x]=4 # L'individu est guérri ou mort (R)
      
    
    
    
    print("Voici la matrice_infection")
    print(matrice_infection)
    
    # On regarde si des individus ont un nombre de tours restants en déplacement=0
    # Si c'est le cas on les remets à leus coordonnees d'origine
    if (len(nb_tours_restants)>0):
    
        l=len(nb_tours_restants)
        i=0
        while (i<l) :
            if (nb_tours_restants[i]==0):
                (x_origine,y_origine)=coordonnees_origine.pop(i)
                (x_cible,y_cible)=coordonnees_cible.pop(i)
                nb_tours_restants.pop(i)
                
                tmp=world[y_cible][x_cible]
                world[y_cible][x_cible]=0
                world[y_origine][x_origine]=tmp
                
                l=len(nb_tours_restants)
            else :
                i=i+1
    
    
    # On réduit de 1 le nombre de tours restants
    if (len(nb_tours_restants)>0):
        for i in range(len(nb_tours_restants)):
            nb_tours_restants[i]=nb_tours_restants[i]-1
        
        
    #print(coordonnees_origine,"\n")    
    #print(coordonnees_cible,"\n")    
    #print(nb_tours_restants,"\n")
    return world,matrice_infos_deplacement
                
                
def multi_evolution_world_SEIR(nb_tours,world,proba_incubation,proba_transmission,proba_guerison,proba_mort,proba_deplacement,matrice_infos_deplacement, confinement, matrice_infection):
    '''
    Renvoit un monde après plusieurs itérations SEIR
    '''
    print("\nTour : 0\n")
    affiche_monde(world)

    for i in range(nb_tours):
        
        world,matrice_infos_deplacement=evolution_world_SEIR(world,proba_incubation,proba_transmission,proba_guerison,proba_mort,proba_deplacement,matrice_infos_deplacement, confinement, matrice_infection)
        print("\nTour :",i+1,"\n")
        affiche_monde(world)
        affiche_monde(matrice_infection)
        
    return world

'''
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
proba_incubation=50
proba_transmission=30
proba_guerison=30
proba_mort=20
proba_deplacement=5
multi_evolution_world_SEIR(10,monde_test,proba_incubation,proba_transmission,proba_guerison,proba_mort,proba_deplacement,matrice_infos_deplacement)


multi_evolution_world_SEIR(100,monde_test,26,46,50,10,40,matrice_infos_deplacement,"Pas de confinement",matrice_infection)

'''