# -*- coding: utf-8 -*-

import tkinter as Tk
from matplotlib import pyplot as plt


'''
α = alpha (incubation)
β = beta (taux de transmission)
γ = gamma (guérison)
μ = mu (taux de mortailté)

S = personnes saines (taux entre 0 et 1)
E = personnes infectées non infectieuses (taux entre 0 et 1)
I = personnes infectées infectieusess (taux entre 0 et 1)
R = personnes retirées guéries ou mortes (taux entre 0 et 1)


'''

nb_temps=20

alpha=0.75
beta=0.8
gamma=0.05
mu=0.01

S=0.5
E=0
I=0.5
R=0
population=1

#S+E+I+R=1

def dS(beta,S,I,mu):
    return -beta*S*I-mu*S

def dE(beta,S,I,alpha,E,mu):
    return beta*S*I-alpha*E-mu*E

def dI(I,alpha,E,gamma,mu):
    return alpha*E*-gamma*I-mu*I

def dR(I,gamma,mu,R):
    return gamma*I-mu*R


def setup_tab_param(S,E,I,R,alpha,beta,gamma,mu,nb_temps,population):
    
    tab_S=[S]
    tab_E=[E]
    tab_I=[I]
    tab_R=[R]
    tab_population=[population]
    tab_temps=[0]
    
    for i in range(nb_temps):
        
        S=S+dS(beta,S,I,mu)
        tab_S.append(S)
        
        E=E+dE(beta,S,I,alpha,E,mu)
        tab_E.append(E)
        
        I=I+dI(I,alpha,E,gamma,mu)
        tab_I.append(I)
        
        R=R+dR(I,gamma,mu,R)
        tab_R.append(R)
        
        population=1-R
        tab_population.append(population)
        
        tab_temps.append(i+1)
    
    return tab_S,tab_E,tab_I,tab_R,tab_population,tab_temps


params=setup_tab_param(S,E,I,R,alpha,beta,gamma,mu,nb_temps,population)


plt.plot(params[5], params[0], color = 'blue')
plt.plot(params[5], params[1], color = 'green')
plt.plot(params[5], params[2], color = 'orange')
plt.plot(params[5], params[3], color = 'red')
plt.plot(params[5], params[4], color = 'purple')

plt.show()
        
        
        
        
        
    
    



