import numpy as np

def magnitude(x):
    """Returns magnitude of a vector"""
    return np.linalg.norm(np.array(x))

def distance(p1, p2):
    """Returns distance between two positions p1 and p2"""
    return magnitude(np.array(p2) - np.array(p1))

def unit_vector(x):
    """Returns unit_vector of a vector"""
    return np.array(x)/magnitude(x)

def random_sphere(center, radius, size, seed=123):
    """Create a list of random points in a sphere.

    Keyword arguments:
    center -- center of sphere
    radius -- radius of sphere
    size   -- number of points to create
    seed   -- random state (default 123)
    """
    np.random.seed(seed)
    x0, y0, z0 = center
    phi = np.random.uniform(0, 2*np.pi, size)
    costheta = np.random.uniform(-1, 1, size)
    u = np.random.uniform(0, 1, size)
    theta = np.arccos( costheta )
    r = radius * (u**(1/3))
    xs = (r * np.sin(theta) * np.cos(phi)) + x0
    ys = (r * np.sin(theta) * np.sin(phi)) + y0
    zs = (r * np.cos(theta)) + z0
    return list(zip(xs,ys,zs))

def random_ec_sphere(center, r1, r2, size, seed=123):
    """Create a list of random points between two concentric spheres.

    Keyword arguments:
    center -- center of spheres
    r1 -- radius of the smaller sphere
    r2 -- radius of the bigger sphere
    size   -- number of points to create
    seed   -- random state (default 123)
    """
    np.random.seed(seed)
    inc_size = int(2*size / (1 - (r1/r2)**3))
    x0, y0, z0 = center
    ls = random_sphere(center, r2, inc_size, seed)
    x = np.array([i[0] for i in ls])
    y = np.array([i[1] for i in ls])
    z = np.array([i[2] for i in ls])
    cnd = x**2 + y**2 + z**2 > r1**2
    xs = x[cnd]
    ys = y[cnd]
    zs = z[cnd]
    return list(zip(xs,ys,zs))[:size]
