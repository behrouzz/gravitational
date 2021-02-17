from datetime import datetime, timedelta
from urllib.request import urlopen

def _get_horizons_url(body, t, b_type, center):
    '''Returns the url of the Horizons API'''
    if isinstance(t, datetime):
        t2 = t + timedelta(seconds=1)
        t1 = t.isoformat().replace('T', ' ')
    else:
        t1 = datetime.strptime(t, '%Y-%m-%d %H:%M:%S')
        t2 = t1 + timedelta(seconds=1)
        t1 = t
    t2 = t2.isoformat().replace('T', ' ')

    b_t = 'DES=' if b_type != 'major' else ''
    
    base = 'https://ssd.jpl.nasa.gov/horizons_batch.cgi?batch=1&'
    params = f"""COMMAND='{b_t}{body}'&CENTER='{center}'&MAKE_EPHEM='YES'
    TABLE_TYPE='VECTORS'&START_TIME='{t1}'&STOP_TIME='{t2}'&STEP_SIZE= '1'
    OUT_UNITS='KM-S'&REF_PLANE='FRAME'&REF_SYSTEM='J2000'&VECT_CORR='NONE'
    VEC_LABELS='NO'&VEC_DELTA_T='NO'&CSV_FORMAT='YES'&OBJ_DATA='NO'
    VEC_TABLE='3'"""
    params = params.replace('\n', '&').replace(' ', '%20')
    url = base + params.replace(' ', '%20%')
    return url


def initial_state(body, t, b_type='major', center='500@0'):
    '''Returns the initial state of a Solar System body'''
    dc = {'sun':'10', 'mercury':'199', 'venus':'299', 'earth':'399',
          'mars':'499', 'jupiter':'599', 'saturn':'699', 'uranus':'799',
          'neptune':'899', 'pluto':'999'}
    if body.lower() in dc.keys():
        body = dc[body.lower()]
    
    url = _get_horizons_url(body, t, b_type, center)
    with urlopen(url) as r:
        text = r.read().decode('utf-8')
    mark1 = text.find('$$SOE')
    text = text[mark1+6:]
    mark2 = text.find(',\n')
    text = text[:mark2]
    ls = text.split(',')[2:8]
    ls = [i.strip() for i in ls]
    ls = [float(i)*1000 for i in ls]
    p0 = tuple(ls[:3])
    v0 = tuple(ls[3:])
    return [p0, v0]


class Constant:
    '''Mass and radius of major Solar System bodies'''
    def __init__(self):

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
