from particle import Particle


class Group:
    particle: list[Particle]

    def __init__(self, function, particles):
        self.function = function
        self.particles = particles
        self.bestGlobal = self.findBestParticle()

    def findBestParticle(self):
        bestValue = 999999999
        bestParticle = self.particles[0]

        for particle in self.particles:
            y = particle.getY()
            if y < bestValue:
                bestValue = y
                bestParticle = particle
        return bestParticle

    def getParticles(self):
        return self.particles

    def groupOptimization(self):
        for particle in self.particles:
            particle.particleOptimization(self.bestGlobal.getPosition())
        self.bestGlobal = self.findBestParticle()