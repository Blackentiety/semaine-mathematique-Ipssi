# semaine-mathematique-Ipssi

# Rapport d'Analyse : Modélisation Linéaire et Évaluation par la MSE

## 1. Introduction
Ce document présente l'analyse d'un modèle de prédiction linéaire appliqué au **Quatuor d'Anscombe**. L'objectif est de démontrer comment une fonction paramétrée estime des données et comment l'Erreur Quadratique Moyenne (MSE) permet d'en évaluer la précision.

---

## 2. La Fonction de Prédiction Paramétrée

### Rôle et Définition
La fonction de prédiction est l'outil mathématique qui permet de passer d'une donnée d'entrée (la surface $x$) à une estimation de sortie (le prix $y$). Dans ce projet, nous utilisons une régression linéaire simple :

$$f(x) = ax + b$$

* **Paramètre $a$ (Pente) :** Il représente le coefficient directeur. Dans notre contexte, il indique l'augmentation du prix pour chaque unité de surface supplémentaire.
* **Paramètre $b$ (Ordonnée à l'origine) :** Il représente la valeur de $y$ lorsque $x = 0$. C'est le point de départ de la droite.

### Application au Code
Le script calcule ces paramètres via la fonction `calcul_parametres(x, y)`. Une fois $a$ et $b$ déterminés, le modèle devient capable de prédire des valeurs inconnues, comme le prix pour une surface de $100m^2$ :
`prediction = a * 100 + b`

---

## 3. La Fonction de Coût : Mean Squared Error (MSE)

### Calcul Mathématique
La MSE mesure l'écart moyen entre les prédictions du modèle et les valeurs réelles. Elle est définie par la formule :

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$



### Interprétation de l'Erreur
* **Le Carré :** L'utilisation du carré (`** 2` dans le code) a deux fonctions : elle rend toutes les erreurs positives (une erreur de -2 ne doit pas annuler une erreur de +2) et elle pénalise plus lourdement les grands écarts.
* **Le Score :** Plus la MSE est proche de **0**, plus le modèle est précis. Une MSE élevée indique que la droite de régression est loin des points réels.

---

## 4. Analyse du Quatuor d'Anscombe

L'analyse de la capture d'écran ci-dessous est cruciale. Elle montre quatre datasets différents qui possèdent pourtant des statistiques presque identiques (pente, ordonnée à l'origine et MSE).

### Visualisation des Résultats
![Capture d'écran de l'analyse](Lien_Vers_Ta_Capture.png)
*(Note : Remplacez ce lien par le chemin de votre image)*

### Interprétation des 4 cas :
1.  **Dataset 1 (MSE = 1.25) :** Modèle linéaire classique. La droite suit bien la tendance générale malgré un bruit naturel.
2.  **Dataset 2 (MSE = 1.47) :** La relation est clairement courbe. La fonction de prédiction linéaire ($ax + b$) est ici **inadaptée**, même si la MSE semble correcte.
3.  **Dataset 3 (MSE = 1.21) :** La relation est parfaite, sauf pour un **point aberrant (outlier)** qui fausse la pente de la droite.
4.  **Dataset 4 (MSE = 1.31) :** Les données sont verticales. La régression n'a aucun sens mathématique ici, illustrant qu'un chiffre (la MSE) ne suffit pas sans graphique.

---

## 5. Conclusion
Le projet démontre que la **fonction de prédiction** est le moteur du modèle, tandis que la **MSE** en est le juge. Cependant, l'analyse du Quatuor d'Anscombe nous rappelle qu'une MSE faible ne garantit pas la pertinence d'un modèle : la visualisation graphique reste indispensable pour valider l'interprétation des données.
