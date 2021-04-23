from manim_imports_ext import *

def createRay(start, end):

    """
    start: 2d point coordinate
    end: 2d point coordinate
    """
    ray = Arrow(
        np.array([start[0], start[1], 0]),
        np.array([end[0], end[1], 0]),
        buff = 0
    )
    ray.set_stroke(color=BLACK, width=1, opacity=1)
    return ray

def getCircPos(R, Origin, x=None, y=None, unit=1):
    if x is not None:
        root = abs(R**2 - (x-Origin[0])**2)**0.5
        y = unit* root+ Origin[1] # unit=1,上侧的根
        return x, y
    elif y is not None:
        root = abs(R**2 - (y-Origin[1])**2)**0.5

        x = unit*root+ Origin[0] # unit=1,右侧的根
        return x, y

    else:
        return ValueError


def sphere(origin, r):
    sphere0 = ParametricSurface(
        lambda u, v: np.array([
            r * np.cos(u) * np.cos(v) - origin[0],
            r * np.cos(u) * np.sin(v) - origin[1],
            r * np.sin(u) - origin[2]
        ]),
        v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
        # checkerboard_colors=[RED_D, RED_E],
        # resolution=(15, 32)
    )
    return sphere0

def circ(origin, r):

    circle = ParametricCurve(
        lambda theta: np.array([
            r * np.cos(theta) + origin[0],
            r * np.sin(theta) + origin[1],
            origin[2]
        ]),
        [0, 2*TAU],
        color=RED
    )
    return circle