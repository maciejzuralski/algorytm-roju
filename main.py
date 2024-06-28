from swarm import Swarm
from functions import dwa, rastrigin, funkcja

if __name__ == '__main__':
    s = Swarm(10, 3, [[-1, 9], [-1, 9]], funkcja)
    while True:
        s.showSwarm()
        s.particleSwarmOptimization()