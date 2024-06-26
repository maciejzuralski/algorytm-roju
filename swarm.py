from functions import funkcja, rastrigin
from particle import Particle
from group import Group
import random

class Swarm:
    def __init__(self, groupSize, numberOfGroups, borders):
        self.borders = borders
        self.groups = []
        for _ in range(numberOfGroups):
            particles = []
            for _ in range(numberOfGroups):
                particles.append(Particle(borders))
            self.groups.append(Group(rastrigin, particles))