import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Perceptron

# ==========================================
# 1. FONCTIONS DE BASE (FROM SCRATCH)
# ==========================================

def step(s):
    return 1 if s >= 0 else 0

def perceptron_train(X, y, eta=0.1, epochs=10):
    w = np.zeros(X.shape[1])
    b = 0.0
    for _ in range(epochs):
        for xi, yi in zip(X, y):
            s = np.dot(w, xi) + b
            y_pred = step(s)
            error = yi - y_pred
            if error != 0:
                w += eta * error * xi
                b += eta * error
    return w, b

def plot_decision_boundary(X, y, model_type, w=None, b=None, clf=None, title=""):
    """
    Visualise la frontière de décision. 
    Supporte le mode 'scratch' (w, b) ou 'sklearn' (clf).
    """
    xx, yy = np.meshgrid(np.linspace(-0.5, 1.5, 100), np.linspace(-0.5, 1.5, 100))
    
    if model_type == 'scratch':
        Z = np.array([step(w[0]*x + w[1]*y_ + b) for x, y_ in zip(xx.ravel(), yy.ravel())])
    else: # sklearn
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
        
    Z = Z.reshape(xx.shape)
    
    plt.figure(figsize=(6, 5))
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
    plt.scatter(X[:,0], X[:,1], c=y, s=150, edgecolors='k', cmap='coolwarm')
    plt.title(title)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# ==========================================
# 2. DATASETS (AND, OR, XOR)
# ==========================================
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y_and = np.array([0, 0, 0, 1])
y_or  = np.array([0, 1, 1, 1])
y_xor = np.array([0, 1, 1, 0])

# ==========================================
# 3. ANALYSE XOR (L'ÉCHEC DU LINÉAIRE)
# ==========================================
print("Apprentissage XOR (From Scratch)...")
w_xor, b_xor = perceptron_train(X, y_xor, epochs=20)
plot_decision_boundary(X, y_xor, 'scratch', w_xor, b_xor, title="XOR - From Scratch (Échec)")

# ==========================================
# 4. COMPARAISON AVEC SCIKIT-LEARN
# ==========================================
tasks = [("AND", y_and), ("OR", y_or), ("XOR", y_xor)]

for name, y in tasks:
    print(f"\nEntraînement Scikit-Learn pour : {name}")
    clf = Perceptron(max_iter=100, eta0=0.1, random_state=42)
    clf.fit(X, y)
    
    print(f"Poids {name}: {clf.coef_} | Biais {name}: {clf.intercept_}")
    plot_decision_boundary(X, y, 'sklearn', clf=clf, title=f"Sklearn Perceptron - {name}")
