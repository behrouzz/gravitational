import numpy as np
from .utils import magnitude, distance, unit_vector

def L1(Mp, Pp, Ms, Ps):
    '''
    Returns position of lagrangian point L1 for Planet with respect to Star

    Mp : mass of Planet
    Pp : position of  Planet
    Ms : mass of Star
    Ps : position of Star
    '''
    Ps, Pp = np.array(Ps), np.array(Pp)
    # distance from Star to Planet
    Rsp = distance(Ps, Pp)
    L = np.linspace(Rsp/1000000, Rsp/2, 1000000)
    expr = Ms/Rsp**3 + (Mp/(L**2 * (Rsp-L))) - (Ms/(Rsp-L)**3)
    # Distance between L1 and Planet
    L = L[np.argmin(np.abs(expr))]
    # Vector from Planet to Star
    Vps = Ps - Pp
    # Vector from Planet to L1
    Vpl = (L/distance(Ps, Pp)) * Vps
    PL1 = Vpl + Pp 
    return tuple(PL1)


def L2(Mp, Pp, Ms, Ps):
    '''
    Returns position of lagrangian point L2 for Planet with respect to Star

    Mp : mass of Planet
    Pp : position of  Planet
    Ms : mass of Star
    Ps : position of Star
    '''
    Ps, Pp = np.array(Ps), np.array(Pp)
    # distance from Star to Planet
    Rsp = distance(Ps, Pp)
    L = np.linspace(Rsp/1000000, Rsp/2, 1000000)
    expr = Ms/Rsp**3 - (Mp/(L**2 * (Rsp+L))) - (Ms/(Rsp+L)**3)
    # Distance between L2 and Planet
    L = L[np.argmin(np.abs(expr))]
    # Vector from Planet to Star
    Vps = Ps - Pp
    # Vector from Planet to L2
    Vpl = -(L/distance(Ps, Pp)) * Vps
    PL2 = Vpl + Pp 
    return tuple(PL2)


def L3(Mp, Pp, Ms, Ps):
    '''
    Returns position of lagrangian point L3 for Planet with respect to Star

    Mp : mass of Planet
    Pp : position of  Planet
    Ms : mass of Star
    Ps : position of Star
    '''
    Ps, Pp = np.array(Ps), np.array(Pp)
    # distance from Star to Planet
    Rsp = distance(Ps, Pp)
    L = np.linspace(-Rsp/2, Rsp/2, 1_000_000)
    expr = Ms/Rsp**3 - (Mp/((2*Rsp+L)**2 * (Rsp+L))) - (Ms/(Rsp+L)**3)
    # Distance between L3 and Planet's orbit
    L = L[np.argmin(np.abs(expr))]
    # Distance between L3 and Planet
    L = 2*Rsp + L
    # Vector from Planet to Star
    Vps = Ps - Pp
    # Vector from Planet to L3
    Vpl = (L/distance(Ps, Pp)) * Vps
    PL3 = Vpl + Pp 
    return tuple(PL3)

def L4(Pp, Vp, Ps):
    '''
    Returns position of L4
    
    Pp  : position of Planet
    Vp  : velocity of Planet
    Ps  : position of Star
    '''
    # Convert to vectors
    Ps, Pp, Vp = np.array(Ps), np.array(Pp), np.array(Vp)
    r = magnitude(Ps - Pp)
    # A & B are components of the vector pointing from planet to L4
    A = unit_vector(Vp) * np.sqrt(r**2 - (r/2)**2)
    B = 0.5 * (Ps - Pp)
    pL4 = A + B +  Pp
    return tuple(pL4)

def L5(Pp, Vp, Ps):
    '''
    Returns position of L5
    
    Pp  : position of Planet
    Vp  : velocity of Planet
    Ps  : position of Star
    '''
    # Convert to vectors
    Ps, Pp, Vp = np.array(Ps), np.array(Pp), np.array(Vp)
    r = magnitude(Ps - Pp)
    # A & B are components of the vector pointing from planet to L5
    A = unit_vector(Vp) * np.sqrt(r**2 - (r/2)**2) * -1
    B = 0.5 * (Ps - Pp)
    pL5 = A + B +  Pp
    return tuple(pL5)
