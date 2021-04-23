from manim_imports_ext import *
from .scatter import Particle, Ray

class ScatteringModel(Scene):
    def construct(self):
        p1 = Particle()
        self.play(ShowCreation(p1.get_axes()))
        R = 3

        p1.create_particle(LEFT*2, R, GREEN)
        p1.create_particle(RIGHT*2, 3, WHITE)
        p1.create_lights(LEFT*2, R, orient='x', unit=-1)

        for i in p1.get_particles():
            self.play(ShowCreation(i),  run_time=0.1)
            # self.add(i)

        for i in p1.get_lights():
            self.play(ShowCreation(i),  run_time=0.1)
        
        arrow  = Arrow(
            np.array([1, 1, 0]),
            np.array([2, 1, 0]),
            buff = 0,
        )
        arrow.set_color(GREEN)
        self.play(ShowCreation(arrow))


        

