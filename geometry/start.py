from manim_imports_ext import *

class Demo1(Scene):
    def construct(self):

        # https://www.bilibili.com/video/BV1kA411b7kq/?spm_id_from=333.788.recommend_more_video.-1

        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait(0.3)

        circle.move_to(np.array((0, 1, 0)))

        self.play(ReplacementTransform(square, circle))

        self.play(FadeOut(circle), run_time=2)

        arc = Arc(start_angle=0,
                  arc_center=3*LEFT,
                  angle=90*DEGREES,
                  color=RED,
                  )
        # arc.move_to(3*LEFT)
        self.play(ShowCreation(arc))


        curveArrow = CurvedArrow(
            start_point=np.array((0, 2, 0)),
            end_point=np.array((1, -2, 0)),
            angle=180*DEGREES
        )
        self.play(ShowCreation(curveArrow))


class Demo2(Scene):
    def construct(self):
        origin, R = ORIGIN, 2
        particle = Circle(
            arc_center=origin,
            radius=R,
            stroke_width=5,
            stroke_color=WHITE,
            fill_color=BLACK,
            fill_opacity=0.1,
        )
        self.play(ShowCreation(particle))

        height1 = R * 3/4
        ray_1 = Arrow(
            np.array([-1, height1, 0]),
            np.array([1, height1, 0])
        )

        self.play(ShowCreation(ray_1))

        ray_2 = TangentLine(particle,
                            alpha=0.25,
                            length=5)

        self.play(ShowCreation(ray_2))
        ray_3 = TangentLine(particle,
                            alpha=0.75,
                            length=5)
        self.play(ShowCreation(ray_3))



