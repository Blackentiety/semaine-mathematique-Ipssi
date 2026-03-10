v1 = [4,6]
v2 = [1,2]
v3 = [5,9]
m1 = [[1,2],[2,4]]

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


