from manim_imports_ext import *
from geometry.utils import *

class Particle(Scene):

    def construct(self):
        origin, R = ORIGIN, 2
        particle = circ(origin, R)
        self.play(ShowCreation(particle))

        for theta in np.linspace(PI/2, PI-1e-3, 60):
            self.add_rays(theta, particle, 3)

    def add_rays(self, theta1, particle, p=3):
        point1 = particle.get_point_from_function(theta1)
        point0 = np.array([-10, point1[1], point1[2]])

        ray1 = Arrow(point0, point1,buff=0, thickness=0.01)
        ray1.set_opacity(0.1)
        self.play(ShowCreation(ray1, run_time=0.1))

        theta_i = PI - theta1
        theta_r = calc_theta_r(theta_i, 1, 1.33)

        self.add_in_out_rays(point1, theta_i, theta_r, theta1, particle, pn=p,
                     show_in_rays=True, show_out_rays=True,
                     color_out=GREEN)

    def add_in_out_rays(self, point1, theta_i, theta_r, theta0, particle, pn,
                     show_in_rays=True, show_out_rays=True,
                     color_in=None, color_out=None):
        for p in range(pn):
            theta_def = get_theta_def(theta_i, theta_r, p)

            if show_out_rays:
                add_out_rays(self, theta_def, point1, color=color_out, run_time=0.02)

            theta = theta0 - (PI - 2 * theta_r)
            point2 = particle.get_point_from_function(theta)

            if show_in_rays:
                add_in_rays(self, point1, point2, color=color_in, run_time=0.02)

            point1 = point2
            theta0 = theta