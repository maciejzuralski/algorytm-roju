def funkcja(x, z):
    return (-(1/200) * (x - 5)**6 + (1/10) * (x - 5)**4 - (x - 5) + (1/60) * (x - 5)**2 + 2) * (-(1/200) * (z - 5)**6 + (1/10) * (z - 5)**4 - (z - 5) + (1/60) * (z - 5)**2 + 2)


def rastrigin(x, y):
    return 20 + x**2 + y**2 - 10 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))