class Constant:
    '''Mass and radius of major Solar System bodies'''
    def __init__(self):

        # units
        self.au = 149597870700.0
        self.pc = 3.085677581491367e+16

        # sun and moon
        self.r_sun = 695700000.0
        self.m_sun = 1.988409870698051e+30

        self.r_moon = 1737500
        self.m_moon = 7.348e+22

        # planets
        self.r_mercury = 2439700
        self.m_mercury = 3.301e+23

        self.r_venus = 6051800
        self.m_venus = 4.867e+24

        self.r_earth = 6378100.0
        self.m_earth = 5.972167867791379e+24

        self.r_mars = 3389500
        self.m_mars = 6.416999999999999e+23

        self.r_jupiter = 71492000.0
        self.m_jupiter = 1.8981245973360505e+27

        self.r_saturn = 58232000
        self.m_saturn = 5.685e+26

        self.r_uranus = 25362000
        self.m_uranus = 8.682000000000001e+25

        self.r_neptune = 24622000
        self.m_neptune = 1.0240000000000001e+26

        self.r_pluto = 1188300
        self.m_pluto = 1.30900e+22
