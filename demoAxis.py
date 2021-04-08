from manimlib import *

class Demo1(Scene):
    def construct(self):
        axis = NumberLine(
            x_min=-2, x_max=2,
            include_ticks=True, #添加刻度
            include_tip=True, # 添加箭头
            # include_numbers=True,
            unit_size=1.5, # 表示数轴上单位长度为manim中多少个单位
            tick_frequency=0.5,
            label_direction=UP,

        ).shift(LEFT*4)
        self.play(FadeIn(axis))
