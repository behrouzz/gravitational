import numpy as np

def magnitude(x):
    return np.linalg.norm(np.array(x))

def distance(p1, p2):
        '''Returns distance between two positions'''
        return magnitude(np.array(p2) - np.array(p1))

def unit_vector(x):
    return np.array(x)/magnitude(x)

def random_normal_sphere(center, radius, size, std=1, seed=123):
    '''creates xyz coordiantes in a sphere'''
    np.random.seed(seed)
    x0, y0, z0 = center
    x = np.random.normal(loc=x0, scale=std, size=size)
    y = np.random.normal(loc=y0, scale=std, size=size)
    z = np.random.normal(loc=z0, scale=std, size=size)
    mag = np.sqrt((x-x0)**2 + (y-y0)**2 + (z-z0)**2)
    xs = x[np.where(mag<=radius)]
    ys = y[np.where(mag<=radius)]
    zs = z[np.where(mag<=radius)]
    return list(zip(xs,ys,zs))

def random_uniform_sphere(center, radius, size, seed=123):
    '''creates xyz coordiantes in a sphere'''
    np.random.seed(seed)
    x0, y0, z0 = center
    x = np.random.uniform(low=x0, high=x0+radius, size=size)
    y = np.random.uniform(low=x0, high=x0+radius, size=size)
    z = np.random.uniform(low=x0, high=x0+radius, size=size)
    mag = np.sqrt((x-x0)**2 + (y-y0)**2 + (z-z0)**2)
    xs = x[np.where(mag<=radius)]
    ys = y[np.where(mag<=radius)]
    zs = z[np.where(mag<=radius)]
    return list(zip(xs,ys,zs))
