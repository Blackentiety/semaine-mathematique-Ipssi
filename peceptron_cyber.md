# Réponses au Questionnaire : Perceptron & Cybersécurité (SenCyber)

## 1. Structure du Perceptron (Niveau Débutant)
**Question :** Citez les 5 features analysées par SenCyber et leur interprétation.

| Feature | Description | Signal si valeur élevée |
| :--- | :--- | :--- |
| **x1 : nb_paquets** | Nombre de paquets envoyés | **Attaque** (DDoS / Scan) |
| **x2 : taille_moy** | Taille moyenne des paquets | **Légitime** (les attaques utilisent souvent de petits paquets) |
| **x3 : duree** | Durée de la connexion | **Légitime** (une attaque est souvent très brève) |
| **x4 : nb_erreurs** | Erreurs TCP détectées | **Attaque** (tentatives de connexion forcées) |
| **x5 : frequence** | Requêtes par seconde | **Attaque** (automatisation / bot) |

---

## 2. Calcul du score $z$ (Niveau Débutant)
**Données :** $x = [0.92, 0.10, 0.03, 0.91, 0.98]$  
**Poids :** $w = [0.83, -0.72, -0.68, 0.79, 0.81]$ | **Biais :** $b = -0.85$

**Calcul :**
$z = (x1·w1) + (x2·w2) + (x3·w3) + (x4·w4) + (x5·w5) + b$
$z = (0.92 \times 0.83) + (0.10 \times -0.72) + (0.03 \times -0.68) + (0.91 \times 0.79) + (0.98 \times 0.81) - 0.85$
$z = 0.7636 - 0.072 - 0.0204 + 0.7189 + 0.7938 - 0.85$
**$z = 1.3339$**

**Décision :** Comme $z \geq 0$, la sortie $\hat{y} = 1$. La connexion est classée comme **ATTAQUE**.

---

## 3. Règle de mise à jour (Niveau Débutant)
**Question :** Si une attaque ($y=1$) n'est pas détectée ($\hat{y}=0$), comment sont modifiés les poids ?

L'erreur est $err = y - \hat{y} = 1 - 0 = 1$.
La mise à jour est : $w_i = w_i + \alpha \cdot 1 \cdot x_i$.
Les poids associés aux features présentes ($x_i > 0$) vont **augmenter**, rendant le neurone plus sensible à ces signaux lors de la prochaine itération.

---

## 4. FN vs FP en Sécurité (Niveau Intermédiaire)
**Question :** Comparaison Modèle A (3 FN) vs Modèle B (8 FP). Lequel choisir ?

* **Faux Négatif (FN) :** Une attaque réelle qui passe inaperçue (très dangereux).
* **Faux Positif (FP) :** Une alerte pour une connexion normale (coûteux en temps).

**Choix : Modèle B.** En cybersécurité, on privilégie le **Rappel (Recall)**. Il vaut mieux vérifier 8 fausses alertes (Modèle B) que de laisser passer 3 pirates dans le réseau (Modèle A).

---

## 5. Convergence et Poids appris (Niveau Intermédiaire)
**Question :** Pourquoi les poids $w2$ (taille) et $w3$ (durée) sont-ils négatifs ?

Le perceptron a appris que plus la taille des paquets et la durée de connexion augmentent, moins il y a de chances que ce soit une attaque. Un poids négatif agit comme un **frein** sur le score $z$. Si $x2$ ou $x3$ sont élevés, ils tirent $z$ vers le négatif (zone légitime).

---

## 6. Analyse de l'évolution des poids (Niveau Intermédiaire)
Après 100 itérations, si le poids $w4$ (erreurs) passe de $0.1$ à $0.85$, cela signifie que le modèle a découvert que le nombre d'erreurs TCP est un **indicateur très fiable** pour identifier les attaques dans ce dataset spécifique.

---

## 8. Implémentation "From Scratch" (Niveau Avancé)
Voici la fonction d'entraînement simplifiée (sans bibliothèques) :

```python
def entrainer(X, y, alpha=0.01, epochs=50):
    poids = [0.0] * 5
    biais = 0.0
    for _ in range(epochs):
        for i in range(len(X)):
            # Somme pondérée
            z = sum(X[i][j] * poids[j] for j in range(5)) + biais
            y_hat = 1 if z >= 0 else 0
            # Erreur
            erreur = y[i] - y_hat
            # Mise à jour
            if erreur != 0:
                for j in range(5):
                    poids[j] += alpha * erreur * X[i][j]
                biais += alpha * erreur
    return poids, biais 
```


## 9. Limites et cas réels (Niveau : Avancé)
**Problématique :** Un attaquant sophistiqué lance une **APT** (Advanced Persistent Threat) en envoyant des connexions très lentes (1 paquet/min), avec de grands paquets et peu d'erreurs, imitant le trafic légitime.

**Pourquoi le perceptron simple échouera-t-il ?**
1. **Absence de séparabilité linéaire :** Le perceptron simple ne peut séparer les données que par une ligne droite (un hyperplan). Si l'attaque imite parfaitement les caractéristiques du trafic normal, les points "Attaque" et "Légitime" se confondent dans l'espace des données. Il n'existe aucune frontière linéaire permettant de les distinguer.
2. **Manque de contexte temporel :** Le perceptron analyse chaque connexion de manière isolée. Il n'a pas de "mémoire". Une attaque étalée sur plusieurs heures ne peut être détectée que si l'on analyse la séquence et la répétition des événements, ce que le perceptron simple ne fait pas.



**Solutions architecturales proposées :**
* **Modèles Récurrents (LSTM/RNN) :** Ces réseaux possèdent une mémoire interne capable de détecter des anomalies dans des séquences temporelles (attaques lentes).
* **Détection d'anomalies (Auto-encodeurs) :** Au lieu de classer (0 ou 1), on apprend au modèle ce qu'est un comportement "normal". Tout écart, même minime ou très lent, est alors signalé comme suspect.

---

## 10. Analyse critique du Dataset (Niveau : Avancé)
**Contexte :** Le dataset contient 16 exemples (8 légitimes, 8 attaques) et le modèle affiche 100% d'accuracy. 

**Problèmes identifiés avant un déploiement en production :**

1.  **Surapprentissage (Overfitting) :** Avec seulement 16 exemples, le modèle a probablement "appris par cœur" le bruit du dataset plutôt que les vraies caractéristiques des attaques. Il échouera sur toute nouvelle variante d'attaque.
2.  **Manque de représentativité :** 16 connexions ne représentent pas la diversité infinie du trafic réseau réel d'une banque ou d'un opérateur télécom.
3.  **Déséquilibre des classes en réalité :** En production, le trafic légitime représente 99,9% des données. Un modèle entraîné sur un dataset 50/50 générera énormément de fausses alertes (Faux Positifs) en conditions réelles.
4.  **Absence de split Train/Test :** L'accuracy de 100% est calculée sur les données d'entraînement. Pour valider un modèle, il faut impérativement le tester sur des données qu'il n'a jamais vues.

**Protocole de validation recommandé :**
* **Augmentation du Dataset :** Collecter des milliers de logs réels.
* **Split Train/Test/Validation :** Entraîner sur 70% des données et tester sur les 30% restants.
* **Validation Croisée (K-Fold) :** Pour s'assurer que la performance est stable peu importe l'échantillon choisi.
* **Analyse de la Matrice de Confusion :** Ne pas regarder uniquement l'Accuracy, mais viser un **Rappel (Recall)** de 100% pour ne manquer aucune attaque.
