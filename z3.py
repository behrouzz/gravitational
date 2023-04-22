from gravitational.simulation2 import Simulation
from gravitational.solar_system import initial_state
from gravitational.constants import Constant
import numpy as np

# Define the time as a datetime object or a string (default now)
t1 = '2029-01-01 00:00:00'
t2 = '2030-01-01 00:00:00'


sim = Simulation(t1)
c = Constant()
"""

# Add bodies
s = sim.add_body(name='Sun', color='y', size=25, mass=c.m_sun,
                 position=p0_sun, velocity=v0_sun)

v = sim.add_body(name='Venus', color='k', size=8, mass=c.m_venus,
                 position=p0_venus, velocity=v0_venus)

e = sim.add_body(name='Earth', color='b', size=10, mass=c.m_earth,
                 position=p0_earth, velocity=v0_earth)

"""

import pickle

with open('z2.pickle', 'rb') as f:
    t, sun_pos, ear_pos, jup_pos, sat_pos = pickle.load(f)

dt = t[1]-t[0]

apophis_mass = 6.1e10 #kg

#p0_apo, v0_apo = initial_state('99942', t1)
p0_apo = (-81357878549.74826, 128849900408.5687, 45816335136.7952)
v0_apo = (-24168.29279417816, -10019.439142957619, -4330.721941105357)

#p0_sun, v0_sun = initial_state('10', t1)
p0_sun = (184485533.5130677, -191495465.7659891, -77920589.2727616)
v0_sun = (-0.7079052283639198, 8.344022061446594, 3.600166726475592)

#p0_ear, v0_ear = initial_state('399', t1)
p0_ear = (-26489415126.319347, 132536338249.56601, 57456355678.21983)
v0_ear = (-29767.81411418322, -5046.6732506591325, -2186.1596493009856)

#p0_jup, v0_jup = initial_state('599', t1)
p0_jup = (-789580900992.451, -194681292672.8613, -64216108837.48608)
v0_jup = (3115.661758763625, -11041.84107524847, -4808.611912175529)

#p0_sat, v0_sat = initial_state('699', t1)
p0_sat = (1059423454039.0231, 828035578415.0048, 296386098160.4824)
v0_sat = (-6685.277706938829, 6753.883892840782, 3077.3962505168047)


sim.dates = t

sun = sim.add_body(name='Sun', mass=c.m_sun, position=p0_sun, velocity=v0_sun)
ear = sim.add_body(name='Earth', mass=c.m_earth, position=p0_ear, velocity=v0_ear)
