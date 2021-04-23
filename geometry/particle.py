from manim_imports_ext import *
from .utils import *

class Demo2(Scene):

    def construct(self):

        # axis = Axes(
        #     [-8, 8],
        #     [-8, 8]
        # )
        axes = Axes(
            x_range=(-5, 5),
            y_range=(-5, 5),
            height=7,
            width=7,
            axis_config={
                # "include_tip": False,
                "numbers_to_exclude": [],
            }
        )
        # axes.set_x(0)
        axes.add_coordinate_labels()
        origin, R = LEFT*2, 3


        # particle = Circle(
        #     arc_center=origin,
        #     radius=R,
        #     stroke_width=5,
        #     stroke_color=BLACK,
        #     # fill_color=BLACK,
        #     # fill_opacity=0.1,
        # )
        particle=circ(origin, R)


        self.play(
            ShowCreation(axes),
            ShowCreation(particle),
            # FadeIn(particle, RIGHT),
        )

        line1 = Line(np.array([-2, 1, 0]), np.array([2, -1, 0]))
        self.add(line1)

        for i in np.linspace(-R+origin[0], R+origin[0], 10):

            (circx, circy) = getCircPos(R, origin, x=i, unit=1)

            self.play(ShowCreation(createRay([circx, 6], [circx, circy])), run_time=0.2)

        ray_2 = TangentLine(particle,
                            alpha=0.15,
                            length=5,
                            color=BLACK)
        # ray_2.set_color(BLACK)

        self.play(ShowCreation(ray_2))
        ray_3 = TangentLine(particle,
                            alpha=0.75,
                            length=5,
                            color=BLACK)
        # ray_3.set_color(BLACK)
        self.play(ShowCreation(ray_3))