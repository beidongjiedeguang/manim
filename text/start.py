from manim_imports_ext import *

class TextExample(Scene):

    def construct(self):
        title = TexText("This is some \\LaTeX")
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
    os.system("manimgl start.py -f")

