#000000
# Modèle SEIR
## Première semaine 6/02 --> 12/02
Pendant la prémière séance, nous avons discuté sur plusieurs sujets qui nous baser sur l'épidémiologie, un phénomène intéressant à rechercher. On a décidé alors de se concentrer sur le modèle SEIR, dérivé du modèle SIR. Voici une simple représentation du modèle:
![](https://www.linkpicture.com/q/graphe_seir_premiere_semaine.png)

## Deuxième semaine 13/02 --> 19/02
Pendant la deuxième séance, nous étions à la B.U recherchant des documentations, plus précisement des recherches faites sur le sujet, des livres écritent.
On a alors trouvé des différentes manières de développer et d'appliquer certains formules, notamment des équations différentiels tels que: 

![](https://www.mmnp-journal.org/articles/mmnp/full_html/2020/01/mmnp200124/mmnp200124-eq2.png)

D'ailleurs, on a notamment parlé sur la forme de notre modèle SEIR. Voici une simple représentation de notre modèle finale:

![](https://www.linkpicture.com/q/image_2023-04-02_183544767.png)

α = Taux d'incubation, β = Taux de transmission, γ = Taux de guérisson + mortalité(On différencie pas pour l'instant la mortalité de la guérison)
N = 1(Population totale)

 
## Troisième semaine 20/02 --> 26/02
Pendant la troisième séance, nous étions à fond pour terminer notre carnet de bord où se trouve les sources des recherches qu'on a fait. 

## Quatrième semaine 27/02 --> 05/03
Pendant la semaine des vacances, nous avons discuté sur le modèle qu'on allait impliqué sur notre code. Le modèle de ségragation de Schelling a parru être le meilleur choix, vu que l'épidéomologie se base aussi sur le voisinage et les déplacements. Voici une représentation d'une simulation du modèle de Schelling:

![](https://demonstrations.wolfram.com/SchellingsModelOfResidentialSegregation/img/popup_1.png)



## Cinquième semaine 06/03 --> 12/03
C'est pendant la 5e semaine qu'on a commencé notre code python. On a ainsi impliquer les premières formules sur l'ordinateur en générant plusieurs graphiques.

Voici une première graphique avec populations de départ S=80% E=10% I=10% R=0%:

Paramètres α = 0.4, β = 0.4, γ = 0.1

![](https://www.linkpicture.com/q/image_2023-04-02_173357243.png)
 
Une deuxième graphique avec populations de départ S=50% E=10% I=40% R=0%:

Paramètres α = 0.9, β = 0.4, γ = 0.3

![](https://www.linkpicture.com/q/image_2023-04-02_175833294.png)

Une troisième graphique avec populations de départ S=75% E=10% I=15% R=0%:

Paramètres α = 0.3, β = 0.8, γ = 0.5

![](https://www.linkpicture.com/q/image_2023-04-02_175439863.png)

## Sixième semaine 13/03 --> 19/03
La 6e semaine fut la semaine où on a vraiment avancé sur le code python. Voici un extrait du code main.py sur la fonction d'évolution spatiale:

![](https://www.linkpicture.com/q/image_2023-04-03_011747937.png)

Voici les résultats des tests:

Paramètres des probabilités α = 50%, β =30%, γ = 30%

![](https://www.linkpicture.com/q/image_2023-04-03_012158657.png)

## Septième semaine 20/03 --> 26/03
Pendant la septième semaine, on a commencé a implémenté l'interface graphique avec le module tkinter de python. Grace à tkinter, on arrive à faire des simulations de l'épidémie d'une manière itérative. On trouve en disposition les échelles, c'est à dire la grandeur de la population, le taux de mortalité par la maladie et le taux de propagation.

Voici l'interface de l'accueil de notre simulateur:

![](https://www.linkpicture.com/q/image_2023-04-03_023431405.png)

De plus, voici 3 instants du simulation avec plusieurs itérations:

![](https://www.linkpicture.com/q/image_2023-04-03_023721496.png)

![](https://www.linkpicture.com/q/image_2023-04-03_023834588.png)

![](https://www.linkpicture.com/q/image_2023-04-03_024012020.png)

## Huitième semaine 27/03 --> 02/04
Pendant la huitième semaine, 3 grands changements ont été fait: 
-Tout d'abord, l'écran d'accueil a été modifié. Il est maintenant possible de créer un monde avec 900 individus, voici un extrait:

![](https://www.linkpicture.com/q/image_2023-04-12_195307266.png)

-Des majeures changements ont été fait sur le déplacement des individus. Voici 2 extraits résumant les changements:

![](https://www.linkpicture.com/q/image_2023-04-12_201750438.png)

![]()

![]()

![]()

-D'ailleurs, il est maintenant possible de tout itérer d'un coup, ce qui nous aide a gagner du temps et automatiser les coups. Voici les deux étapes de l'itérisation d'un coup:

![](https://www.linkpicture.com/q/image_2023-04-12_200542053.png)

![](https://www.linkpicture.com/q/image_2023-04-12_201141739.png)

## Neuvième semaine 03/04 --> 09/04
Pendant la neuvième semaine, les plus grands modifications ont été faits: 
-Tout d'abord, on a départagé les guérris et les morts. La sous-population total R qu'on avait a été divisé en 2. Maintenant, on a R1 qui représente les guéris et R2 qui représente les morts.

-Un bouton qui réinitialise les itérations et le monde d'origine vierge avant tous les itérations a été ajouté. 

-


