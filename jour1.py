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

def v_multi(v1, v2):
    temp = 0
    res = 0
    for i in range(len(v1)):
        temp = v1[i]*v2[i]
        res+=temp
    return res

print(v_multi(v1,v2))

def mv_produit(matrice,vecteur):
    resultat = []
    for ligne in range(len(matrice)):
        somme_ligne = 0
        for i in range(len(vecteur)):
            somme_ligne += ligne * vecteur[i]
    resultat.append(somme_ligne)
    return resultat 

print(mv_produit(m1,v1))

def moyenne(liste):
    resultat = 0
    for valeur in liste:
        resultat+= valeur
    return resultat/len(liste)

moyenne_surface = moyenne(surface)
moyenne_prix = moyenne(prix)

def numerateur(liste):
    m = moyenne(liste)
    resultat = []
    for valeur in liste:
        resultat.append((valeur-m))
    return resultat

num_a = numerateur(surface)
num_b = numerateur(prix)

def calcul_final_a(vecteur1, vecteur2):
    num_a = numerateur(vecteur1)
    print(num_a)
    num_b = numerateur(vecteur2)
    print(num_b)
    denominateur = v_multi(num_a,num_a)
    print(denominateur)
    print(v_multi(num_a,num_b))
    resultat = v_multi(num_a,num_b)/denominateur
    return resultat

print(calcul_final_a(surface,prix))

def calcul_final_b(vecteur1, vecteur2):
    a = calcul_final_a(vecteur1, vecteur2)
    moy_x = moyenne(surface)
    moy_y = moyenne(prix)
    b = moy_y - (a * moy_x)
    return b 

print(calcul_final_b(prix, surface))

