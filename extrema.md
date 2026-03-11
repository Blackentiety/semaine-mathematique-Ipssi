# Analyse des Points Critiques : Fonction Cubique

Dans cet exercice, nous étudions la fonction $f(x) = x^3 - 3x$ pour identifier ses sommets (points où la pente est nulle).

## 1. Calcul de la dérivée
Pour trouver la pente de la fonction, on calcule sa dérivée $f'(x)$ en utilisant la règle des puissances :

$$f'(x) = 3x^2 - 3$$



## 2. Recherche des points critiques
Les points critiques apparaissent lorsque la dérivée est égale à zéro ($f'(x) = 0$). Cela correspond aux endroits où la courbe arrête de monter ou de descendre pour changer de direction.

$$3x^2 - 3 = 0$$
$$3x^2 = 3$$
$$x^2 = 1$$

Nous obtenons deux solutions pour $x$ :
- $x = 1$
- $x = -1$

## 3. Coordonnées des points critiques
Pour obtenir les points exacts sur le graphique, on calcule $f(x)$ pour chaque valeur trouvée :

### Point A (Minimum local)
Pour $x = 1$ :
$$f(1) = (1)^3 - 3(1) = 1 - 3 = -2$$
**Coordonnées : (1, -2)**

### Point B (Maximum local)
Pour $x = -1$ :
$$f(-1) = (-1)^3 - 3(-1) = -1 + 3 = 2$$
**Coordonnées : (-1, 2)**



## 4. Conclusion
Contrairement à une fonction quadratique (en $x^2$) qui n'a qu'un seul point critique, une fonction cubique peut présenter :
1. Un **Maximum local** : Le "sommet" d'une bosse.
2. Un **Minimum local** : Le "fond" d'un creux.

C'est une notion fondamentale en optimisation : selon l'endroit où l'on commence notre recherche (par exemple en descente de gradient), on peut tomber dans un creux qui n'est pas forcément le point le plus bas de toute la fonction.
