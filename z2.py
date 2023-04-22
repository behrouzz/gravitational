from gravitational.simulation import Simulation
from gravitational.solar_system import initial_state
from gravitational.constants import Constant

# Define the time as a datetime object or a string (default now)
t1 = '2029-01-01 00:00:00'
t2 = '2030-01-01 00:00:00'

sim = Simulation(t1)
c = Constant()
"""
# Get initial states from Horizons API
p0_sun, v0_sun = initial_state('sun', t)
p0_venus, v0_venus = initial_state('venus', t)
p0_earth, v0_earth = initial_state('earth', t)

# Add bodies
s = sim.add_body(name='Sun', color='y', size=25, mass=c.m_sun,
                 position=p0_sun, velocity=v0_sun)

v = sim.add_body(name='Venus', color='k', size=8, mass=c.m_venus,
                 position=p0_venus, velocity=v0_venus)

e = sim.add_body(name='Earth', color='b', size=10, mass=c.m_earth,
                 position=p0_earth, velocity=v0_earth)

# Run and play the simulation
sim.play(path=True)
"""

from hypatie import Vector
import pickle

N = 1000
sun = Vector('sun', t1, t2, step=N)
_ = input('Press Enter...')
earth = Vector(399, t1, t2, step=N)
_ = input('Press Enter...')
jupiter = Vector(599, t1, t2, step=N)
_ = input('Press Enter...')
saturn = Vector(699, t1, t2, step=N)

obj = [sun.time, sun.pos, earth.pos, jupiter.pos, saturn.pos]

with open('z2.pickle', 'wb') as f:
    pickle.dump(obj, f)
