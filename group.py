class Group:
    def __init__(self, function, particles):
        self.function = function
        self.particles = particles
        self.bestLocally = self.findBestParticle

    def findBestParticle(self):
        bestValue = self.function(self.particles[0]) + 1
        bestParticle = self.particles[0]

        for particle in self.particles:
            if self.function(particle) < bestValue:
                bestValue = self.function(particle)
                bestParticle = particle
        return bestParticle
