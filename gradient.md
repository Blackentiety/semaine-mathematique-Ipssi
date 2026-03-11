# Optimisation par Descente de Gradient (From Scratch)

Après avoir utilisé l'Équation Normale (approche directe), nous implémentons ici la **Descente de Gradient**, l'algorithme d'optimisation fondamental du Deep Learning.

##  Principe de l'algorithme

La Descente de Gradient ne cherche pas la solution d'un seul coup. Elle part de paramètres aléatoires ($w=0, b=0$) et les ajuste par petits pas pour minimiser la fonction de coût (**MSE**).

### La fonction de coût (Loss)
Nous utilisons l'Erreur Quadratique Moyenne :
$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - (w x_i + b))^2$$



### Mise à jour des paramètres
À chaque itération, on calcule la pente de l'erreur (le gradient) et on descend dans la direction opposée :
- $w = w - \eta \cdot \frac{\partial MSE}{\partial w}$
- $b = b - \eta \cdot \frac{\partial MSE}{\partial b}$

*Où $\eta$ (eta) est le **Learning Rate**.*

## Analyse de la Convergence
Courbe de Loss
La courbe de perte permet de vérifier la santé de l'entraînement :

- Descente régulière : Le Learning Rate est bien choisi.
- Oscillations / Explosion : Le Learning Rate est trop élevé (divergence).
- Stagnation haute : Le Learning Rate est trop faible.

## Pourquoi le Dataset 1 

Sur le Dataset 1, la descente de gradient converge vers $w \approx 0.50$ et $b \approx 3.00$, ce qui correspond exactement aux résultats de Scikit-Learn. Cela prouve que notre implémentation "from scratch" est mathématiquement correcte.

