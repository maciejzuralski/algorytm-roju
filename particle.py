import random
VELOCITY_SCALE = 4

class Particle:
    def __init__(self, borders):
        self.position = [random.random() * (borders[0][1] - borders[0][0]) + borders[0][0],
                         random.random() * (borders[1][1] - borders[1][0]) + borders[1][0]]
        self.velocity = [(random.random() * (borders[0][1] - borders[0][0]) + borders[0][0])
                         * (random.random() / VELOCITY_SCALE),
                         (random.random() * (borders[1][1] - borders[1][0]) + borders[1][0])
                         * (random.random() / VELOCITY_SCALE)]
