import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from matplotlib.animation import FuncAnimation

# === 1. PRÉPARATION DES DONNÉES (Dataset 1) ===
X = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
Y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
n = len(X)

# === 2. DESCENTE DE GRADIENT FROM SCRATCH ===
# Paramètres initiaux
w = 0.0  # pente
b = 0.0  # biais
lr = 0.005  # Learning Rate (ajusté pour éviter la divergence)
iterations = 500

# Historique pour l'analyse et l'animation
loss_history = []
w_history = []
b_history = []

for i in range(iterations):
    # Prédiction actuelle
    Y_pred = w * X + b
    
    # Calcul de l'erreur (MSE)
    loss = np.mean((Y - Y_pred)**2)
    loss_history.append(loss)
    
    # Calcul des gradients (dérivées partielles)
    dw = (-2/n) * np.sum(X * (Y - Y_pred))
    db = (-2/n) * np.sum(Y - Y_pred)
    
    # Mise à jour des paramètres
    w = w - lr * dw
    b = b - lr * db
    
    # Stockage pour l'animation
    w_history.append(w)
    b_history.append(b)

print("--- Résultats Descente de Gradient ---")
print(f"w (pente) = {w:.4f}")
print(f"b (biais) = {b:.4f}")

# === 3. COURBE DE LOSS ===
plt.figure(figsize=(10, 4))
plt.plot(loss_history, color='orange')
plt.xlabel("Itérations")
plt.ylabel("MSE Loss")
plt.title("Convergence de la Loss (Erreur)")
plt.grid(True, alpha=0.3)
plt.show()

# === 4. COMPARAISON AVEC SCIKIT-LEARN ===
model = LinearRegression()
model.fit(X.reshape(-1, 1), Y)

print("\n--- Résultats Scikit-Learn ---")
print(f"Coeff (w) = {model.coef_[0]:.4f}")
print(f"Intercept (b) = {model.intercept_:.4f}")

# === 5. ANIMATION DE LA TRAJECTOIRE ===
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(X, Y, color="blue", label="Données réelles")
line, = ax.plot([], [], 'r-', label="Droite GD")

def init():
    ax.set_xlim(min(X)-1, max(X)+1)
    ax.set_ylim(min(Y)-1, max(Y)+1)
    return line,

def update(i):
    # On affiche l'évolution toutes les 5 itérations pour que ce soit plus rapide
    idx = i * 5 
    if idx < len(w_history):
        y_vals = w_history[idx] * X + b_history[idx]
        line.set_data(X, y_vals)
    return line,

# Animation (on réduit le nombre de frames pour la fluidité)
ani = FuncAnimation(fig, update, frames=len(w_history)//5, init_func=init, blit=True, interval=50)

plt.title("Évolution de la droite pendant la Descente de Gradient")
plt.legend()
plt.show()
