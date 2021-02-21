import re
import numpy as np
from datetime import timedelta, datetime
from .plays import _play2d, _play3d
from .orbit import set_orbit, L1,L2,L3,L4,L5
from .utils import distance


class Simulation:
    '''The main class'''
    def __init__(self, t0=None):
        if t0 is None:
            self.t0 = datetime.now()
        elif isinstance(t0, datetime):
            self.t0 = t0
        elif isinstance(t0, str) and bool(re.match("\d{4}-\d\d-\d\d \d\d:\d\d:\d\d", t0)):
            self.t0 = datetime.strptime(t0, '%Y-%m-%d %H:%M:%S')
        else:
            raise Exception("t0 should be a datetime object or a string in the format: '%Y-%m-%d %H:%M:%S'")
        self.G = 6.6743e-11
        self.bodies = []
        self.dates = []
        self.d3 = False
        self.runned = False

    class Body:
        def __init__(self, name, color, size, radius, mass, position, velocity):
            self.name = name
            self.color = color
            self.size = size
            self.radius = radius
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

    def add_body(self, name=None, color='b', size=None, radius=0, mass=1.988409870698051e+30, position=(0,0,0), velocity=(0,0,0)):
        """Add body to the system"""
        
        if (len(position)==3 and len(velocity)==3):
            self.d3 = True
        elif (len(position)==2 and len(velocity)==2):
            position = position + (0,)
            velocity = velocity + (0,)
            self.d3 = True #badan tasmim migiram chejoori 3d ya 2d boodano tashkhis bede tooye run
        else:
            raise Exception('Position and velocity should have two or three dimensions')
        
        if name is None:
            name = 'unknown_'+str(len(self.bodies))
        
        body = self.Body(name, color, size, radius, mass, position, velocity)
        
        position_possible = True
        for b in self.bodies:
            if b != body:
                if distance(b.p, body.p) < b.radius + body.radius:
                    position_possible = False

        if position_possible:
            self.bodies.append(body)
            return body
        else:
            print('The position conflicts with another body.\nBody not added. Try again.')


    def set_orbit(self, b1, b2):
        '''Changes the velocity of b1 to be in the orbit of b2'''
        if len(self.bodies)<2:
            raise Exception('You have to add at least two bodies')
        else:
            b1.v = set_orbit(b1.p, b1.v, b2.p, b2.v, b2.m, self.G)

    def set_lagrange(self, L, b1, b2, b3):
        '''Changes the position of b1 to be in lagrangian point of b2 with respect to b3'''
        if L.upper()=='L1':
            b1.p = np.array(L1(b2.m, b2.p, b3.m, b3.p))
        elif L.upper()=='L2':
            b1.p = np.array(L2(b2.m, b2.p, b3.m, b3.p))
        elif L.upper()=='L3':
            b1.p = np.array(L3(b2.m, b2.p, b3.m, b3.p))
        elif L.upper()=='L4':
            b1.p = np.array(L4(b2.p, b2.v, b3.p))
        elif L.upper()=='L5':
            b1.p = np.array(L5(b2.p, b2.v, b3.p))

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

    def run(self, duration=365, dt=1):
        '''Run the simulation'''
        
        if len(self.bodies)==0:
            raise Exception("You should add at least one body using 'add_body'")

        t = np.arange(0, int(duration/dt), 1)
        dt = timedelta(days=dt)
        self.dates = self.t0 + t*dt
        dt = dt.total_seconds()

        for b in self.bodies:
            b.age = len(t)

        for i in range(len(t)):
            for b in self.bodies:
                b.p = b.p + b.v*dt
                if self._collision(b)[0]:
                    body = self._collision(b)[1][0]
                    if b.m <= body.m and b.m != 0 and body.m != 0:
                        print('Collision at i =',i)
                        body.v = (b.m*b.v + body.m*body.v)/(b.m+body.m)
                        body.m = body.m + b.m
                        b.age = i
                        b.m = 0
                        b.v = body.v
                        
                b.pS.append(b.p)
            if len(self.bodies)>1:
                for b in self.bodies:
                    b.f = self._force_nbd(b, self.bodies) if b.m!=0 else 0
                for b in self.bodies:
                    b.v = b.v + (b.f/b.m)*dt if b.m!=0 else b.v
                    b.vS.append(b.v)
            else:
                b.f = 0
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
