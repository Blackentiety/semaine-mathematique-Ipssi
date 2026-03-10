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
