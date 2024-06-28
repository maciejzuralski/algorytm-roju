import random
from typing import List, Any

VELOCITY_SCALE = 10


class Particle:
    def __init__(self, function, borders):
        self.function = function
        self.position = [random.random() * (borders[0][1] - borders[0][0]) + borders[0][0],
                         random.random() * (borders[1][1] - borders[1][0]) + borders[1][0]]
        self.velocity = [random.random() / VELOCITY_SCALE, random.random() / VELOCITY_SCALE]
        self.bestLocally = self.position
        self.bestLocallyValue = function(self.position[0], self.position[1])

    def getX(self):
        return self.position[0]

    def getZ(self):
        return self.position[1]

    def getY(self):
        return self.function(self.position[0], self.position[1])

    def getPosition(self):
        return self.position

    def getVelocity(self):
        return self.velocity

    def particleOptimization(self, bestGlobally):
        def addV(a, b):
            return [a[i] + b[i] for i in range(len(a))]

        def subV(a, b):
            return [a[i] + b[i] for i in range(len(a))]

        def mulV(a, v):
            return [v[i] * a for i in range(len(v))]

        newPosition = addV(mulV(0.5, self.velocity), addV(mulV(0.5 * random.random(), subV(self.bestLocally, self.position)), mulV(0.5 * random.random(), subV(bestGlobally, self.position))))

        self.velocity = [newPosition[0] - self.position[0], newPosition[1] - self.position[1]]
        self.position = newPosition

        if self.bestLocallyValue > self.getY():
            self.bestLocally = self.position
            self.bestLocallyValue = self.getY()
