from manim_imports_ext import *

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
    os.system("pwd")
    os.system("manimgl start.py")

