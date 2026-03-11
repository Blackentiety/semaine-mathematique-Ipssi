import numpy as np
import matplotlib.pyplot as plt

# === Dataset 1 d'hier ===
X = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
Y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])

# --- CALCUL MATRICIEL ---
# On crée la matrice X avec une colonne de 1 pour le biais (intercept)
# X_matrix ressemble à : [[1, 10], [1, 8], ...]
X_matrix = np.column_stack((np.ones(len(X)), X))

# Application de l'équation normale : theta = (X^T * X)^-1 * X^T * Y
theta = np.linalg.inv(X_matrix.T @ X_matrix) @ X_matrix.T @ Y

b = theta[0] # L'ordonnée à l'origine
a = theta[1] # La pente

print(f"Pente (a) : {a:.3f}")
print(f"Biais (b) : {b:.3f}")

# --- VISUALISATION ---
plt.figure(figsize=(8, 5))
plt.scatter(X, Y, color="blue", label="Données réelles")

# Génération de la droite de régression
x_line = np.array([min(X), max(X)])
y_line = a * x_line + b

plt.plot(x_line, y_line, color="red", linewidth=2, label=f"Régression : y = {a:.2f}x + {b:.2f}")

plt.title("Régression Linéaire (Méthode Matricielle) - Dataset 1")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
