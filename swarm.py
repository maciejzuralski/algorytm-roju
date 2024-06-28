import matplotlib.pyplot as plt
import numpy as np

from group import Group
from particle import Particle


class Swarm:
    def __init__(self, groupSize, numberOfGroups, borders, function):
        self.borders = borders
        self.groups = []
        self.function = function
        for _ in range(numberOfGroups):
            particles = []
            for _ in range(groupSize):
                particles.append(Particle(function, borders))
            self.groups.append(Group(function, particles))

    def showSwarm(self):
        x = np.linspace(self.borders[0][0], self.borders[0][1], 400)
        y = np.linspace(self.borders[1][0], self.borders[1][1], 400)
        X, Z = np.meshgrid(x, y)

        Y = self.function(X, Z)

        # Tworzenie wykresu
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # Wykres powierzchni
        surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.5)
        # Dodawanie losowych punktów
        colors = ['r', 'b', 'y']
        for i, group in enumerate(self.groups):
            x = []
            y = []
            z = []
            for particle in group.getParticles():
                x.append(particle.getX())
                y.append(particle.getY())
                z.append(particle.getZ())
            ax.scatter(x, y, z, color=colors[i], s=50)  # s kontroluje rozmiar punktów
        #fig.colorbar(surf)
        ax.view_init(elev=0, azim=90)
        ax.set_title('Algorytm Roju')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

    def particleSwarmOptimization(self):
        for group in self.groups:
            group.groupOptimization()