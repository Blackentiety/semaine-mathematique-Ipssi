import matplotlib.pyplot as plt

v1 = [4,6]
v2 = [1,2]
v3 = [5,9]
m1 = [[1,2],[2,4]]

surface = [50,70,90]
prix = [100, 140, 180]

def v_add(v1,v2):
    res = [v1[i] + v2[i] for i in range(len(v1))]
    return res 

print(v_add(v1,v2))

def mv_produit(matrice, vecteur):
    resultat = []
    for ligne in matrice:
        somme_ligne = 0
        for i in range(len(vecteur)):
            somme_ligne += ligne[i] * vecteur[i]
        
        resultat.append(somme_ligne)
    
    return resultat

# Test avec tes données de l'image
A = [[1, 2], [3, 4]]
x = [5, 6]

print(mv_produit(A, x)) # Affiche [17, 39]
# données
surface = [50, 70, 90]
prix = [100, 140, 180]

# --- Fonctions utilitaires ---
def moyenne(liste):
    return sum(liste) / len(liste)

def v_multi(v1, v2): # Produit scalaire
    return sum(v1[i] * v2[i] for i in range(len(v1)))

# --- Calcul de la régression ---
def calcul_parametres(x, y):
    mx = moyenne(x)
    my = moyenne(y)
    
    # Numérateur : somme de (xi - mx) * (yi - my)
    ecart_x = [(val - mx) for val in x]
    ecart_y = [(val - my) for val in y]
    numerateur = v_multi(ecart_x, ecart_y)
    
    # Dénominateur : somme de (xi - mx)²
    denominateur = v_multi(ecart_x, ecart_x)
    
    a = numerateur / denominateur
    b = my - (a * mx)
    
    return a, b

a, b = calcul_parametres(surface, prix)
print(f"Le prix prédit est : y = {a} * surface + {b}")

# Test de prédiction pour une maison de 100m2
prediction = a * 100 + b
print(f"Pour 100m2, le prix estimé est de {prediction} k€")


# -- Calcul Erreur Quadratique moyenne -- 
def calcul_mse(y_reel, y_predit):
    n = len(y_reel)
    somme_carres = 0
    
    for i in range(n):
        # (Y_i - Y_chapeau_i) au carré
        erreur = y_reel[i] - y_predit[i]
        somme_carres += erreur ** 2
        
    return somme_carres / n

# Data set 1
x1 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

# Data set 2
x2 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 7.26, 7.26, 4.74]

# Data set 3
x3 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y3 = [7.46, 6.77, 12.74, 7.11, 8.81, 8.84, 6.08, 5.39, 8.15, 6.40, 5.73]

# Data set 4
x4 = [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0]
y4 = [6.58, 5.76, 5.76, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

datasets = [
    {"nom": "Dataset 1", "x": x1, "y": y1},
    {"nom": "Dataset 2", "x": x2, "y": y2},
    {"nom": "Dataset 3", "x": x3, "y": y3},
    {"nom": "Dataset 4", "x": x4, "y": y4}
]

# --- PRÉPARATION DES GRAPHIQUES  ---
# fig: la fenêtre, axes: la grille 2x2 de graphiques
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
axes_flat = axes.flatten() # Pour passer plus facilement d'un graphique à l'autre
fig.suptitle("Quatuor d'Anscombe : Mêmes Statistiques, Graphiques Différents", fontsize=16)

# --- BOUCLE PRINCIPALE  ---
print(f"{'Dataset':<12} | {'Pente (a)':<10} | {'Ordonnée (b)':<12} | {'MSE':<8}")
print("-" * 55)

for i, data in enumerate(datasets):
    x = data["x"]
    y = data["y"]
    nom = data["nom"]

    # --- a. Tes calculs (inchangés) ---
    a, b = calcul_parametres(x, y)
    y_pred = [(a * val + b) for val in x]
    erreur = calcul_mse(y, y_pred)
    print(f"{nom:<12} | {a:<10.2f} | {b:<12.2f} | {erreur:<8.2f}")

    # --- b. Les graphiques pour ce dataset ---
    ax = axes_flat[i] # Sélectionne le bon sous-graphique

    # 1. Dessiner les points de données réelles
    ax.scatter(x, y, color='blue', marker='o', label='Données Réelles')

    # 2. Dessiner la droite de régression (y = ax+b)
    # On crée une belle droite sur tout l'axe des X
    x_line = [min(x), max(x)]
    y_line_pred = [a * val + b for val in x_line]
    ax.plot(x_line, y_line_pred, color='red', linestyle='--', linewidth=2, label=f'Régression: y={a:.2f}x + {b:.2f}')

    # 3. Personnaliser le graphique
    ax.set_title(f"{nom} (MSE = {erreur:.2f})")
    ax.set_xlabel("X (Surface m²)")
    ax.set_ylabel("Y (Prix k€)")
    ax.grid(True, linestyle=':', alpha=0.5) # Ajoute une grille discrète

# --- FINALISER ET AFFICHER ---
plt.tight_layout() # Empêche les titres de se chevaucher
plt.subplots_adjust(top=0.90) # Fait de la place pour le grand titre
plt.show() # Affiche la fenêtre avec les 4 graphiques
