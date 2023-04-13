#000000
# Modèle SEIR
## Introduction / Première semaine 6/02 --> 12/02
Pendant la prémière séance, nous avons discuté sur plusieurs sujets qui nous intéressaient et nous avons décidé de nous baser sur l'épidémiologie, qui est à la fois un sujet intéressant et dont la modélisation pourrait aussi être intéressante. On a alors décidé de se concentrer sur le modèle SEIR, dérivé du modèle SIR. Voici une simple représentation du modèle:
![](https://www.linkpicture.com/q/graphe_seir_premiere_semaine.png)
Nous avons 4 sous- poupulations : S pour les individus sains, E pour ceux infectés et non infectieux, I pour les infectés infectieux, et R pour les retirés (guérris ou morts), avec différents paramètres faisant le lien entre ces sous-populations.

## Deuxième semaine 13/02 --> 19/02
Pendant la deuxième séance, nous étions à la B.U recherchant des documentations, et plus précisement des recherches faites sur le sujet d'épidémiologie.
On a alors trouvé différentes manières d'appliquer certains formules dans le cadre de notre projet, notamment des équations différentiels telles que: 

![](https://www.mmnp-journal.org/articles/mmnp/full_html/2020/01/mmnp200124/mmnp200124-eq2.png)

α = Taux d'incubation, β = Taux de transmission, γ = Taux de guérisson + mortalité (On ne différencie pas pour l'instant la mortalité de la guérison),
N = 1(Population totale)

D'ailleurs, concernant la forme de notre modèle SEIR. Voici une simple représentation de notre modèle actuel:

![](https://www.linkpicture.com/q/image_2023-04-02_183544767.png)



 
## Troisième semaine 20/02 --> 26/02
Pendant la troisième séance nous nous sommes notamment concentrés sur notre carnet de bord, où se trouvent les sources des recherches que l'on a faites, pour le terminer.

## Quatrième semaine 27/02 --> 05/03
Pendant la semaine des vacances nous avons discuté sur le modèle que l'on allait appliquer dans notre code. Le modèle de ségragation de Schelling a parru être le meilleur choix, vu que la propagation d'épidémies se base certainement aussi sur le voisinage et les déplacements. Voici une représentation d'une simulation d'un modèle de Schelling trouvée sur internet:

![](https://demonstrations.wolfram.com/SchellingsModelOfResidentialSegregation/img/popup_1.png)



## Cinquième semaine 06/03 --> 12/03
C'est pendant la 5ème semaine que l'on a commencé notre code python. On a ainsi appliqué les premières formules du modèle SEIR, permettant de générer nos premiers graphiques SEIR, et qui pourront être comparés bien plus tard à nos graphiques obtenus par notre modèle de Schelling.

Voici un première graphique avec des populations de départ S=80% E=10% I=10% R=0%:

Paramètres α = 0.4, β = 0.4, γ = 0.1

![](https://www.linkpicture.com/q/image_2023-04-02_173357243.png)
 
Un deuxième graphique avec des populations de départ S=50% E=10% I=40% R=0%:

Paramètres α = 0.9, β = 0.4, γ = 0.3

![](https://www.linkpicture.com/q/image_2023-04-02_175833294.png)

Un troisième graphique avec des populations de départ S=75% E=10% I=15% R=0%:

Paramètres α = 0.3, β = 0.8, γ = 0.5

![](https://www.linkpicture.com/q/image_2023-04-02_175439863.png)

## Sixième semaine 13/03 --> 19/03
La 6ème semaine fut la semaine où l'on a vraiment avancé sur le code python. Voici un extrait du code main.py sur la fonction d'évolution spatiale:

![](https://www.linkpicture.com/q/image_2023-04-03_011747937.png)

Voici les résultats des tests:

Paramètres des probabilités α = 50%, β =30%, γ = 30%

![](https://www.linkpicture.com/q/image_2023-04-03_012158657.png)

## Septième semaine 20/03 --> 26/03
Pendant la septième semaine, nous avons commencé a implémenter l'interface graphique avec le module tkinter de python. Grace à tkinter, on arrive à faire des simulations de l'épidémie de manière itérative. On trouve désormais à notre disposition un écran d'accueil permettant de choisir les tailles des populations de notre monde.

Voici l'interface de l'accueil de notre simulateur:

![](https://www.linkpicture.com/q/image_2023-04-03_023431405.png)

De plus, nous disposons aussi d'un écran d'itération, permettant d'afficher notre monde sous la forme d'une grille, de choisir les différents paramètres et d'itérer selon ces mêmes paramètres.
Voici les instants d'un même monde durant 2 itérations:

![](https://www.linkpicture.com/q/image_2023-04-03_023721496.png)

![](https://www.linkpicture.com/q/image_2023-04-03_023834588.png)

![](https://www.linkpicture.com/q/image_2023-04-03_024012020.png)

## Huitième semaine 27/03 --> 02/04
Pendant la huitième semaine, 3 grands changements ont été faits: 
-Tout d'abord, l'écran d'accueil a été modifié. Il est maintenant possible de créer un monde avec 900 individus, voici un extrait:

![](https://www.linkpicture.com/q/image_2023-04-12_195307266.png)

-Nous avons implémenté le déplacement des individus. Selon le pourcentage choisi, si l'individu se déplace celui-ci quitte son emplacement d'origine entre 1 et 6 tours inclus. Durant ce temps son emplacement d'origine ne peut être occupé par un autre individu. Nous avons aussi fait l'hypothèse que seuls les individus en bordure d'un regroupement sont aptes à potentiellement se déplacer.
Voici des extraits montrant les changements:

![](https://www.linkpicture.com/q/image_2023-04-12_201750438.png)

![](https://www.linkpicture.com/q/image_2023-04-12_214140529.png)

![](https://www.linkpicture.com/q/image_2023-04-12_214256373.png)

![](https://www.linkpicture.com/q/image_2023-04-12_214355100.png)

-D'ailleurs, il est maintenant aussi possible de tout itérer d'un coup, ce qui nous aide a gagner du temps et à automatiser les itérations. Voici les deux étapes de l'itération d'un coup:

![](https://www.linkpicture.com/q/image_2023-04-12_200542053.png)

![](https://www.linkpicture.com/q/image_2023-04-12_201141739.png)

## Neuvième semaine 03/04 --> 09/04
Pendant la neuvième semaine, les plus grandes modifications ont été faites:

-Tout d'abord, on a départagé les guérris et les morts. La sous-population totale R qu'on avait a été divisé en 2. Maintenant, on a R1 qui représente les guérris et R2 qui représente les morts.

-Un bouton qui réinitialise les itérations et le monde, permettant de revenir au monde d'origine vierge avant toutes itérations a été ajouté. 

-Une matrice d'infections qui montre le nombre d'infections par case a été également ajoutée, avec un bouton qui change le type de monde montré (normal/infections).

-Même si le graphe SEIR reste comme il est, un graphique avancé a été ajouté. Cet nouveau graphe montre maintenant l'évolution des S, E, I, R différenciés (Pour R1 et R2), et l'évolution de la population totale. On a aussi pour ça ajouté un bouton permettant de switcher entre les 2 graphiques.

-Un deuxième nouveau graphique sur les données des déplacements des individus a été ajouté. Pour les sous populations S E I R1 on a l'évolution du nombre d'individus de chaque sous-population en déplacement pendant le tour, et en plus en gris on a l'évolution du nombre d'individus contaminés pendant un déplacement depuis le début. 

-Maintenant passons aux exemples: 

Partons de ce monde au début:

![](https://www.linkpicture.com/q/image_2023-04-12_214843676.png)

Itérons ce monde 100 fois. Voici les nouveaux résultats avec notre nouveau monde obtenu, les données sur les déplacements et le graphiques normal.

![](https://www.linkpicture.com/q/image_2023-04-12_215211116.png)

Voici les nouveaux résultats avec la matrice d'infections et le graphique avancé de cette semaine.

![](https://www.linkpicture.com/q/image_2023-04-12_215351611.png)

Maintenant, passons à l'écran de p


