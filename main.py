import numpy as np
import matplotlib.pyplot as plt

from functions import funkcja, rastrigin


def showEverything():
    x = np.linspace(-5.12, 5.12, 400)
    y = np.linspace(-5.12, 5.12, 400)
    X, Z = np.meshgrid(x, y)

    Y = rastrigin(X, Z)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Z, Y, cmap='viridis')
    fig.colorbar(surf)
    ax.set_title('Wizualizacja funkcji')
    ax.set_xlabel('X')
    ax.set_ylabel('Z')
    ax.set_zlabel('Wartość funkcji')
    plt.show()