from manim_imports_ext import *
from .utils import *

class Particle(Scene):

    def construct(self):
        origin, R = LEFT*2, 2
        particle = circ(origin, R)
        self.play(ShowCreation(particle))

        for theta in np.linspace(PI/2, PI, 20):
            def add_rays(obj, theta1, particle, p=3):
                point1 = particle.get_point_from_function(theta1)
                point0 = np.array([-10, point1[1], point1[2]])

                ray1 = Arrow(point0, point1,buff=0)
                obj.play(ShowCreation(ray1, run_time=0.1))

                theta_i = PI - theta1
                theta_r = calc_theta_r(theta_i, 1, 1.33)

                add_all_rays(obj, point1, theta_i, theta_r, theta1, particle, pn=p,
                             show_in_rays=False, show_out_rays=True,
                             color_out=GREEN)

            add_rays(self, theta, particle, 3)
