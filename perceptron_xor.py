import numpy as np
import matplotlib.pyplot as plt

# 1. Configuration du Perceptron
def step(s):
    return 1 if s >= 0 else 0

def train_perceptron(X, y, eta=0.1, epochs=100):
    w = np.zeros(X.shape[1])
    b = 0.0
    errors_log = []
    
    for epoch in range(epochs):
        total_errors = 0
        for xi, yi in zip(X, y):
            s = np.dot(w, xi) + b
            y_hat = step(s)
            error = yi - y_hat
            if error != 0:
                w += eta * error * xi
                b += eta * error
                total_errors += 1
        errors_log.append(total_errors)
    return w, b, errors_log

# 2. Données du XOR
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y_xor = np.array([0, 1, 1, 0])

# 3. Entraînement
w, b, history = train_perceptron(X, y_xor)

# 4. Visualisation de la frontière de décision
def plot_xor(X, y, w, b):
    xx, yy = np.meshgrid(np.linspace(-0.5, 1.5, 100), np.linspace(-0.5, 1.5, 100))
    Z = np.array([step(w[0]*x + w[1]*y_ + b) for x, y_ in zip(xx.ravel(), yy.ravel())])
    Z = Z.reshape(xx.shape)
    
    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='RdBu')
    plt.scatter(X[:,0], X[:,1], c=y, s=200, edgecolors='k', cmap='RdBu')
    
    # Annotations des points
    for i, txt in enumerate(['(0,0)','(0,1)','(1,0)','(1,1)']):
        plt.annotate(txt, (X[i,0], X[i,1]), textcoords="offset points", xytext=(0,10), ha='center')
        
    plt.title("Échec du Perceptron Simple sur le XOR")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

print(f"Poids finaux : {w}, Biais final : {b}")
plot_xor(X, y_xor, w, b)
