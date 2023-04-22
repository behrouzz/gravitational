import re
import numpy as np
from datetime import timedelta, datetime
from .plays import _play2d, _play3d
from .orbit import set_orbit, L1,L2,L3,L4,L5
from .utils import distance


class Simulation:
    def __init__(self, t0):
        if isinstance(t0, datetime):
            self.t0 = t0
        elif isinstance(t0, str) and bool(re.match("\d{4}-\d\d-\d\d \d\d:\d\d:\d\d", t0)):
            self.t0 = datetime.strptime(t0, '%Y-%m-%d %H:%M:%S')
        else:
            raise Exception("t0 should be a datetime object or a str: '%Y-%m-%d %H:%M:%S'")
        self.G = 6.6743e-11
        self.bodies = []
        self.dates = []
        self.runned = False


    class Body:
        def __init__(self, name, mass, position, velocity, modif=False):
            self.name = name
            self.modif = modif
            self.m = mass
            self.p = np.array(position)
            self.pS = []
            self.v = np.array(velocity)
            self.vS = []
            self.f = np.array([])
            self.xs = np.array([])
            self.ys = np.array([])
            self.zs = np.array([])
            self.age = 0

    def add_body(self, name, mass, position, velocity):
        body = self.Body(name, mass, position, velocity)
        self.bodies.append(body)
        return body


    def _force_2bd(self, b1, b2):
        '''Gravitational force acting on b1 from b2'''
        d = distance(b1.p, b2.p)
        mag_f = (self.G * b1.m * b2.m) / (d**2)
        f = mag_f * (b1.p - b2.p) / d
        return f

    def _force_nbd(self, b, bodies):
        '''Gravitational force acting on b from other bodies'''
        fS = []
        for i in bodies:
            if i != b:
                fS.append(self._force_2bd(i, b))
        f = np.array(fS)
        f = np.array([f[:,0].sum(), f[:,1].sum(), f[:,2].sum()])
        return f

    def run(self):#, duration=365, dt=1):

        #t = np.arange(0, int(duration/dt), 1)
        #dt = timedelta(days=dt)
        #self.dates = self.t0 + t*dt
        t = np.arange(len(self.dates))
        dt = (self.dates[1]-self.dates[0]).total_seconds()

        for b in self.bodies:
            b.age = len(t)

        for i in range(len(t)):
            for b in self.bodies:
                if b.modif:
                    b.p = b.p + b.v*dt
                    b.pS.append(b.p)

            for b in self.bodies:
                b.f = self._force_nbd(b, self.bodies) if b.m!=0 else 0
            for b in self.bodies:
                b.v = b.v + (b.f/b.m)*dt if b.m!=0 else b.v
                b.vS.append(b.v)

        
        for b in self.bodies:
            b.pS = np.array(b.pS)
            b.vS = np.array(b.vS)
            #b.pS = b.pS / 1.49597871e+11 # convert m to au
            b.xs, b.ys, b.zs = b.pS[:,0], b.pS[:,1], b.pS[:,2]

        self.runned = True

    def _collision(self, body):
        '''Checks whether body colids with other bodies'''
        collision = False
        col_bodies = []
        for b in self.bodies:
            if (distance(b.p, body.p) <= b.radius + body.radius) and (b!=body):
                collision = True
                col_bodies.append(b)
        return [collision, col_bodies]

    def play(self, dim='3d', legend=False, path=False, interval=20):
        '''Play the animation'''
        
        if not self.runned:
            self.run()

        if self.d3 and dim=='3d':
            _play3d(legend=legend, bodies=self.bodies, dates=self.dates, path=path, interval=interval)
        elif dim=='2d':
            _play2d(legend=legend, bodies=self.bodies, dates=self.dates, path=path, interval=interval)
        else:
            raise Exception("Specify dim as: dim='2d' or dim='3d'")
