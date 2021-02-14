import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D, proj3d


def _set_ax(bodies, dim):
    '''Sets ax and limits'''

    if dim=='2d':
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
    elif dim=='3d':
        fig = plt.figure(figsize=plt.figaspect(0.5)*1.2)
        ax = fig.add_subplot(111, projection='3d')
    
    ds = [b.radius*2 for b in bodies]  # diameters (data scale)
    edges = sum(ds)
    
    minx = min([b.xs.min() for b in bodies])
    maxx = max([b.xs.max() for b in bodies])
    miny = min([b.ys.min() for b in bodies])
    maxy = max([b.ys.max() for b in bodies])
    minz = min([b.zs.min() for b in bodies])
    maxz = max([b.zs.max() for b in bodies])
    limits = [minx,maxx,miny,maxy,minz,maxz]

    mn = min([minx-edges, miny-edges])
    mx = max([maxx+edges, maxy+edges])
    mn = mn*1.1 if mn<0 else mn*0.9
    mx = mx*0.9 if mx<0 else mx*1.1
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    
    if dim=='3d':
        ax.set_zlabel('Z')
        ax.tick_params(axis='x', labelsize=8)
        ax.tick_params(axis='y', labelsize=8)
        ax.tick_params(axis='z', labelsize=8)
    else:
        ax.set_xlim([mn, mx])
        ax.set_ylim([mn, mx])
    
    return fig, ax, limits, mn, mx

def _set_size(ax, radiusS, limits, dim):
    '''Sets the marker size of each body'''

    M = ax.transData.get_matrix()
    xscale = M[0,0]
    yscale = M[1,1]
    xy_scale = (xscale+yscale)/2
    
    # Size in display scale
    s = np.array([i*xy_scale for i in radiusS*2])

    minx,maxx,miny,maxy,_,_ = limits

    if dim=='3d':
        d_display = xy_scale
    else:
        ll = ax.transData.transform((minx, miny)) # LowerLeft (disp scale)
        ur = ax.transData.transform((maxx, maxy)) # UpperRight (disp scale)
        d_display = np.mean(ur-ll)

    coef = d_display / s.mean() # A Coefficient to increase the size
    cov = s.std()/s.mean() # Coefficient of variation
    
    sizes = (coef*s)**(1/(cov**2))

    return sizes

def _play3d(legend, bodies, dates, path=False, interval=20):
    '''Animation 3d'''
    
    fig, ax, limits, _, _ = _set_ax(bodies=bodies, dim='3d')
    minx,maxx,miny,maxy,minz,maxz = limits

    radiusS = np.array([b.radius for b in bodies])

    
    if bodies[0].size is None:
        if bodies[0].radius > 0:
            sizes = _set_size(ax, radiusS, limits, dim='3d')
        else:
            sizes = len(bodies) * [5]
    else:
        sizes = [b.size for b in bodies]
    
    
    txt = ax.text(minx, maxy, maxz, '')

    lines = []

    alpha = 0.2 if path else 0
    
    for i in range(len(bodies)):
        ax.plot(bodies[i].xs, bodies[i].ys, bodies[i].zs, bodies[i].color, alpha=alpha)
        lines.append(ax.plot(bodies[i].xs[0:2], bodies[i].ys[0:2], bodies[i].zs[0:2],
                             color=bodies[i].color, marker='o', markersize=sizes[i],
                             label=bodies[i].name)[0])

    def init():
        for line in lines:
            line.set_xdata(np.array([]))
            line.set_ydata(np.array([]))
            line.set_3d_properties(np.array([]))
        return lines

    def animate(i):
        for j,line in enumerate(lines):
            if i<=bodies[j].age:
                line.set_xdata(bodies[j].xs[i])
                line.set_ydata(bodies[j].ys[i])
                line.set_3d_properties(bodies[j].zs[i])
            else:
                line.set_xdata(maxx*1000) #disappear
                line.set_ydata(maxy*1000)
                line.set_3d_properties(maxz*1000)
        txt.set_text(dates[i].isoformat().replace('T', ' '))
        return lines + [txt]

    plt.locator_params(axis='x', nbins=7)
    plt.locator_params(axis='y', nbins=7)
    plt.locator_params(axis='z', nbins=7)
    
    if legend:
        plt.legend()
    plt.grid(True)

    _ = FuncAnimation(fig, animate, init_func=init,
                      frames=len(dates),
                      interval=interval, blit=True, repeat=True)
    plt.show()

def _play2d(legend, bodies, dates, path=False, interval=20):
    '''Animation 2d'''
    
    fig, ax, limits, mn, mx = _set_ax(bodies=bodies, dim='2d')
    minx,maxx,miny,maxy,_,_ = limits
    
    radiusS = np.array([b.radius for b in bodies])
    
    if bodies[0].size is None:
        if bodies[0].radius > 0:
            sizes = _set_size(ax, radiusS, limits, dim='2d')
        else:
            sizes = len(bodies) * [5]
    else:
        sizes = [b.size for b in bodies]
    
    txt = ax.text(minx, maxy, '')

    alpha = 0.2 if path else 0
    lines = []
    for i in range(len(bodies)):
        ax.plot(bodies[i].xs, bodies[i].ys, bodies[i].color+'-',
                linewidth=1, markersize=sizes[i], alpha=alpha)
        lines.append(ax.plot(bodies[i].xs, bodies[i].ys,
                             color=bodies[i].color, marker='o', label=bodies[i].name,
                             markersize=sizes[i])[0])
    
    def animate(i):
        for j,line in enumerate(lines):
            if i<=bodies[j].age:
                line.set_data(bodies[j].xs[i], bodies[j].ys[i])
            else:
                line.set_data(maxx*1000, maxy*1000) #disappear
        txt.set_text(dates[i].isoformat().replace('T', ' '))
        return lines + [txt]

    _ = FuncAnimation(fig, animate, frames=len(dates),
                      interval=interval, blit=True, repeat=False)

    if legend:
        plt.legend()
    plt.grid(True)
    plt.show()
