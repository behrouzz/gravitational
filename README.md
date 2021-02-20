# gravitational
*A package for gravitational simulations*


## Installation

You can install the latest version of *gravitational* from [PyPI](https://pypi.org/project/gravitational/):

    pip install gravitational

The only requirements are *numpy* and *matplotlib*.


## How to use

An example of simulating the inner planets:

    from gravitational.simulation import Simulation
    from gravitational.solar_system import initial_state
    from gravitational.constants import Constant

    t = '2021-02-17 04:26:00'

    sim = Simulation(t)
    c = Constant()

    p0_sun, v0_sun = initial_state('sun', t)
    p0_venus, v0_venus = initial_state('venus', t)
    p0_earth, v0_earth = initial_state('earth', t)

    s = sim.add_body(name='Sun', color='y', size=25, mass=c.m_sun,
                     position=p0_sun, velocity=v0_sun)

    v = sim.add_body(name='Venus', color='k', size=8, mass=c.m_venus,
                     position=p0_venus, velocity=v0_venus)

    e = sim.add_body(name='Earth', color='b', size=10, mass=c.m_earth,
                     position=p0_earth, velocity=v0_earth)

    sim.play(path=True)

