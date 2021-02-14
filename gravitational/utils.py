import numpy as np
from datetime import datetime

def magnitude(x):
    return np.linalg.norm(np.array(x))

def unit_vector(x):
    return tuple(np.array(x)/magnitude(x))

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


class SolarSystem:
    def __init__(self):
        self.t = datetime.strptime('2000-01-01 12:00:00', '%Y-%m-%d %H:%M:%S')
        self.list = ['sun','mercury','venus','earth','moon','mars','jupiter','saturn','uranus','neptune']
    class sun:
        def __init__(self):
            self.r = 695700000.0
            self.m = 1.988409870698051e+30
            self.p0 = (-1067599234.8091303,-395987673.56883085,-138072335.97758806)
            self.v0 = (9.312473177909851,-11.701360702514648,-5.251247406005859)
    class mercury:
        def __init__(self):
            self.r = 2439700
            self.m = 3.301e+23
            self.p0 = (-20529051444.52753,-60323851183.28949,-30130746884.78446)
            self.v0 = (37004.22379684448,-8541.396339416504,-8398.373783111572)
    class venus:
        def __init__(self):
            self.r = 6051800
            self.m = 4.867e+24
            self.p0 = (-108524016816.98979,-7318842365.395707,3548158539.174672)
            self.v0 = (1391.3459167480469,-32029.177081108093,-14496.897749900818)
    class earth:
        def __init__(self):
            self.r = 6378100.0
            self.m = 5.972167867791379e+24
            self.p0 = (-27566628950.998325,132361429959.96907,57418644625.43733)
            self.v0 = (-29784.946437835693,-5029.756530761719,-2180.645538330078)
    class moon:
        def __init__(self):
            self.r = 1737500
            self.m = 7.348e+22
            self.p0 = (-27858220058.78771,132094699909.01393,57342542505.01981)
            self.v0 = (-29141.3419342041,-5695.838516235352,-2481.9834365844727)
    class mars:
        def __init__(self):
            self.r = 3389500
            self.m = 6.416999999999999e+23
            self.p0 = (206978937430.56082,-180887205.70743364,-5663893358.034903)
            self.v0 = (1171.7222290039062,23906.443120896816,10933.825539588928)
    class jupiter:
        def __init__(self):
            self.r = 71492000.0
            self.m = 1.8981245973360505e+27
            self.p0 = (597557268706.4581,408919262581.324,160745461034.0766)
            self.v0 = (-7897.13720703125,10171.327087402344,4552.181945800781)
    class saturn:
        def __init__(self):
            self.r = 58232000
            self.m = 5.685e+26
            self.p0 = (957047262546.2631,923410574099.111,340115125208.9392)
            self.v0 = (-7428.0562744140625,6098.05078125,2838.2779541015625)
    class uranus:
        def __init__(self):
            self.r = 25362000
            self.m = 8.682000000000001e+25
            self.p0 = (2157937800760.6216,-1871405909825.5876,-850176467726.5356)
            self.v0 = (4644.798095703125,4249.363037109375,1795.3834228515625)
    class neptune:
        def __init__(self):
            self.r = 24622000
            self.m = 1.0240000000000001e+26
            self.p0 = (2513975552737.6646,-3438157439451.012,-1469848899194.046)
            self.v0 = (4476.26953125,2876.8955078125,1065.881591796875)
