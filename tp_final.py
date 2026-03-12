# TP final – Neurone multivarié avec MSE et Gradient Descent
import numpy as np

# ==========================================
# Données
# ==========================================
# Entrées : x1 et x2
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
    [2, 1]
])

# Sortie y basée sur la règle : y = 3*x1 - 2*x2 + 1
y = np.array([1, -1, 4, 2, 6])

# ==========================================
# Exercice 1 – Prédiction du neurone
# ==========================================
def predict(x, w, b):
    """
    x : vecteur des entrées [x1, x2]
    w : vecteur des poids [w1, w2]
    b : biais
    """
    # Calcul : (w1*x1 + w2*x2) + b
    y_pred = np.dot(x, w) + b  
    return y_pred

# ==========================================
# Exercice 2 – Calcul de la MSE
# ==========================================
def mse(y_true, y_pred):
    # Moyenne des carrés des différences : 1/n * somme((y - y_hat)^2)
    error = np.mean((y_true - y_pred)**2)  
    return error

# ==========================================
# Exercice 3 – Gradient Descent
# ==========================================
def train(X, y, lr=0.01, epochs=200):
    w = np.array([0.0, 0.0])  # Initialisation des poids w1, w2
    b = 0.0                   # Initialisation du biais
    n = len(X)
    
    for i in range(epochs):
        # Calcul des prédictions pour tous les points de X
        y_pred = np.array([predict(x, w, b) for x in X])
        
        # Calcul du gradient pour les poids (dw) et le biais (db)
        # Formule : (-2/n) * somme(X * (y_true - y_pred))
        dw = (-2/n) * np.dot(X.T, (y - y_pred))
        db = (-2/n) * np.sum(y - y_pred)
        
        # Mise à jour des paramètres : on soustrait le gradient multiplié par le learning rate
        w = w - lr * dw   
        b = b - lr * db   
        
    return w, b

# ==========================================
# Exercice 4 – Test du modèle
# ==========================================

# Lancement de l'apprentissage
w, b = train(X, y, lr=0.05, epochs=1000)

print("Poids appris :", w)  # Devrait être proche de [3, -2]
print("Biais appris :", b)  # Devrait être proche de 1

# Tester sur une nouvelle donnée : x1=3, x2=2
# Théoriquement : 3*(3) - 2*(2) + 1 = 6
x_test = np.array([3, 2])
prediction = predict(x_test, w, b)

print(f"Prediction pour x_test [3, 2] = {prediction:.4f}")
