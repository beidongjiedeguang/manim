from manim_imports_ext import *

class Text1(Scene):
    def construct(self):
        text1 = TexText("根据通用近似定理可知：")
        eq1 = TexText("$E = mc^2$")
        self.play(Write(text1.move_to(UL)))
        self.play(Write(eq1.scale(2).move_to(ORIGIN)))

        self.play(Transform(eq1, eq1.copy().shift(RIGHT*3)), run_time=1)


class ColorExample(Scene):
    def construct(self):
        text1 = Text(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        text2 = Text("nice gradient", gradient=(BLUE, GREEN))
        text3 = Text(
            'nice <gradient from="RED" to="YELLOW">intermediate</gradient> gradient',
            gradient=(BLUE, GREEN),
        )

        group = VGroup(text1, text2, text3).arrange(DOWN)
        self.add(group)

class TextExample(Scene):

    def construct(self):
        # title = TexText("This is some \\LaTeX")
        # title = TexText("Differential\\\\equations", font_size=60)
        a = 101010
        title = TexText(f"But what\\\\is $e^{{M}}$? 并且可以输入在中文哦！" +
                        f"\\\\ var a is {a}")
        basel = Tex(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, UP),
        )
        self.wait()

if __name__ == "__main__":
    # os.system("manimgl start.py Text1")

    os.system("manimgl start.py ColorExample -f")

