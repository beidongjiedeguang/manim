from manim_imports_ext import *

class Ray:
    # config = {
    # }
    def __init__(self, 
        coord=np.array([-4, 0, 0]),
        wavelength = 632,
        rm = 1,
        orientation=RIGHT
        ):
        self.c = 2.9979
        self.rm = rm # refractive index real part
        self.im = 0 # refractive index image part (unused)
        self.wavelength = wavelength # wavelength
        self.v = self.c # light speed
        self.frequency = self.v/self.wavelength
        
        self.orientation = orientation
        self.current_coord = coord

        self.need_update_v = False
        self.need_update_orientation = False

    def set_m(self, rm, im):
        self.rm = rm
        self.im = im

    def get_v(self):
        return self.v
    
    def update_v(self):
        self.v = self.c/self.rm
        self.need_update_v = False

    def update_orientation(self):
        # update from refrective index
        self.need_update_orientation = False
    
    def update_status(self):
        if self.need_update_v:
            self.update_v()

        if self.need_update_orientation:
            self.update_oritation()

    



class Particle:
    def __init__(self, ) -> None:

        self.axes = Axes(
            x_range=[-6, 6], y_range=[-6, 6],
            height=8, width=8,
            axis_config={
                # "include_tip": False,
                "numbers_to_exclude": [],
            }
        )
        for axis in self.axes:
            axis.add_numbers(range(-4, 6, 2), color=GREY_B)
            # axis.numbers[4].set_opacity(0)


        self.particles = []
        self.lights = []
        

    def get_axes(self):
        return self.axes

    def get_particles(self):
        return self.particles
    
    def get_lights(self):
        return self.lights

    def create_particle(self, origin, r, color=RED):
        self.particles.append(self.circ(origin, r, color))
        
    def create_lights(self, origin, r, n=10, orient='x', unit=1):
        if orient == 'y':
            for i in np.linspace(-r + origin[0], r + origin[0], n):
                (circx, circy) = getCircPos(r, origin, x=i, unit=unit)
                self.lights.append(self._ray([circx, 6], [circx, circy]))

        if orient == 'x':
            for i in np.linspace(-r + origin[1], r + origin[1], n):
                (circx, circy) = getCircPos(r, origin, y=i, unit=unit)
                self.lights.append(self._ray([-10, circy], [circx, circy]))

    def _ray(self, start, end):

        """
        start: 2d point coordinate
        end: 2d point coordinate
        """
        ray = Arrow(
            self.axes.c2p(*np.array([start[0], start[1], 0])),
            self.axes.c2p(*np.array([end[0], end[1], 0])),
            buff = 0,
            thickness=0.02

        )
        # ray.set_stroke(width=0.1, opacity=1)
        ray.set_color(GREEN)

        return ray 

    def circ(self, origin, r, color=RED):
        circle = ParametricCurve(
            lambda theta: self.axes.c2p(*np.array([
                r * np.cos(theta) + origin[0],
                r * np.sin(theta) + origin[1],
                origin[2]
            ])),
            [0, 2*TAU],
            color=color
        )
        return circle 


    
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


# def sphere(origin, r):
#     sphere0 = ParametricSurface(
#         lambda u, v: np.array([
#             r * np.cos(u) * np.cos(v) - origin[0],
#             r * np.cos(u) * np.sin(v) - origin[1],
#             r * np.sin(u) - origin[2]
#         ]),
#         v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2,
#         # checkerboard_colors=[RED_D, RED_E],
#         # resolution=(15, 32)
#     )
#     return sphere0

