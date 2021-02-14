# gravitational
*A package for gravitational simulations*


## Installation

You can install gravitational from [PyPI](https://pypi.org/project/gravitational/):

    pip install gravitational

The only requirements are *numpy* and *matplotlib*. You can install them:

    pip install numpy
    pip install matplotlib


## How to use

An example of simulating the inner planets:

    >>> from gravitational.simulation import Simulation
    >>> from gravitational.utils import SolarSystem
    >>> ss = SolarSystem()
    >>> sim = Simulation(ss.t)
    >>> bodies = [ss.sun(), ss.mercury(), ss.venus(), ss.earth(), ss.mars()]
    >>> names = ['sun', 'mercury', 'venus', 'earth', 'mars']
    >>> colors = ['y','k','g','b','r']
    >>> sizes = [25,8,9,10,9]
    >>> for i,b in enumerate(bodies):
           sim.add_body(name=names[i], color=colors[i], radius=b.r, size=sizes[i], 
           mass=b.m, position=b.p0, velocity=b.v0)
    >>> sim.play(path=True)

