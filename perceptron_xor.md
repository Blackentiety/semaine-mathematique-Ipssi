# Analyse TP : Les limites du Perceptron (Le cas XOR)

## 1. Table de vérité du XOR (OU Exclusif)
| x1 | x2 | y (Cible) |
|:--:|:--:|:---------:|
| 0  | 0  |     0     |
| 0  | 1  |     1     |
| 1  | 0  |     1     |
| 1  | 1  |     0     |

## 2. Observations de l'entraînement
Lors de l'exécution du script, on remarque que :
* Le nombre d'erreurs ne tombe jamais à **0**, même en augmentant les itérations (epochs).
* Le perceptron "saute" d'une solution à une autre sans jamais stabiliser une frontière qui sépare les quatre points correctement.
* Au mieux, il parvient à classer 75% des points (3 sur 4), mais échoue systématiquement sur le quatrième.

## 3. Pourquoi le perceptron simple échoue-t-il ?
Le perceptron simple est un **classifieur linéaire**. Mathématiquement, il ne peut créer qu'une **droite de séparation** (un hyperplan). 



Dans le cas du XOR :
* Les points de la classe `0` sont positionnés en (0,0) et (1,1).
* Les points de la classe `1` sont positionnés en (0,1) et (1,0).

Ces points sont disposés de manière croisée. Il est géométriquement impossible de tracer une seule ligne droite qui laisse les deux `1` d'un côté et les deux `0` de l'autre. On dit que le problème XOR n'est pas **linéairement séparable**.



## 4. Réponses aux questions de conclusion

### Que se passe-t-il si on change le taux d'apprentissage ou les itérations ?
* **Taux d'apprentissage ($\eta$) :** S'il est trop grand, les poids changent violemment ; s'il est petit, ils changent lentement. Mais peu importe la valeur, cela ne créera jamais une séparation non-linéaire.
* **Itérations :** Le perceptron continuera de boucler indéfiniment sur ses erreurs car la solution qu'il cherche (une droite parfaite) n'existe pas.

### Comment une couche cachée permet-elle de résoudre XOR ?
Pour résoudre le XOR, il faut un **Perceptron Multicouche (MLP)**.
1. La **couche cachée** effectue une transformation de l'espace. Elle crée deux droites différentes (par exemple une porte AND et une porte OR).
2. La **couche de sortie** combine ces résultats pour isoler la zone spécifique au XOR.
En résumé, la couche cachée permet de "plier" ou de "tordre" l'espace pour que les points deviennent enfin séparables par une droite.
