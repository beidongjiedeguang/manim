from manimlib import *


class TextExample(Scene):
    def construct(self):
        text = Text("Here is a text", font="Consolas", font_size=90)
        difference = Text(
            """
            The most important difference between Text and TexText is that\n
            you can change the font more easily, but can't use the LaTeX grammar.
            
            """,
            font="Arial", font_size=24,
            t2c={"Text": BLUE, "TexText": BLUE, "LaTeX": ORANGE}
        )
        VGroup(text, difference).arrange(DOWN, buff=1)
        self.play(Write(text))
        self.play(FadeIn(difference, UP))
        self.wait(3)

        fonts = Text(
            " And you can also set the font according to different words",
            font="Arial",
            t2f={"font": "Consolas", "words": "Consolas"},
            t2c={"font": BLUE, "words": GREEN}
        )
        slant = Text(
            "And the same as slant and weight",
            font="Consolas",
            t2s={"slant": ITALIC},
            t2w={"weight": BOLD},
            t2c={"slant": ORANGE, "weight": RED}
        )
        VGroup(fonts, slant).arrange(DOWN, buff=0.8)
        self.play(FadeOut(text), FadeOut(difference, shift=DOWN))
        self.play(Write(fonts))
        self.wait()
        self.play(Write(slant))
        self.wait()

class Chinese(Scene):
    def construct(self):
        text = Text("这里是中a文。 askdjf ", font_size=90)
        self.play(Write(text))


class TexTransformExample(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            # Surrounding substrings with double braces
            # will ensure that those parts are separated
            # out in the Tex.  For example, here the
            # Tex will have 5 submobjects, corresponding
            # to the strings [A^2, +, B^2, =, C^2]
            Tex("{{A^2}} + {{B^2}} = {{C^2}}"),
            Tex("{{A^2}} = {{C^2}} - {{B^2}}"),
            # Alternatively, you can pass in the keyword argument
            # "isolate" with a list of strings that should be out as
            # their own submobject.  So both lines below are equivalent
            # to what you'd get by wrapping every instance of "B", "C"
            # "=", "(" and ")" with double braces
            Tex("{{A^2}} = (C + B)(C - B)", isolate=to_isolate),
            Tex("A = \\sqrt{(C + B)(C - B)}", isolate=to_isolate)
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": TEAL,
                "C": GREEN,
            })

        play_kw = {"run_time": 2}
        self.add(lines[0])
        # The animation TransformMatchingTex will line up parts
        # of the source and target which have matching tex strings.
        # Here, giving it a little path_arc makes each part sort of
        # rotate into their final positions, which feels appropriate
        # for the idea of rearranging an equation
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()

        # Now, we could try this again on the next line...
        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()
        # ...and this looks nice enough, but since there's no tex
        # in lines[2] which matches "C^2" or "B^2", those terms fade
        # out to nothing while the C and B terms fade in from nothing.
        # If, however, we want the C^2 to go to C, and B^2 to go to B,
        # we can specify that with a key map.
        self.play(FadeOut(lines[2]))
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                }
            ),
            **play_kw
        )
        self.wait()

        # And to finish off, a simple TransformMatchingShapes would work
        # just fine.  But perhaps we want that exponent on A^2 to transform into
        # the square root symbol.  At the moment, lines[2] treats the expression
        # A^2 as a unit, so we might create a new version of the same line which
        # separates out just the A.  This way, when TransformMatchingTex lines up
        # all matching parts, the only mismatch will be between the "^2" from
        # new_line2 and the "\sqrt" from the final line.  By passing in,
        # transform_mismatches=True, it will transform this "^2" part into
        # the "\sqrt" part.
        new_line2 = Tex("{{A}}^2 = (C + B)(C - B)", isolate=to_isolate)
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2, lines[3],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(3)
        self.play(FadeOut(lines, RIGHT))

        # Alternatively, if you don't want to think about breaking up
        # the tex strings deliberately, you can TransformMatchingShapes,
        # which will try to line up all pieces of a source mobject with
        # those of a target, regardless of the submobject hierarchy in
        # each one, according to whether those pieces have the same
        # shape (as best it can).
        source = Text("the morse code", height=1)
        target = Text("here come dots", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()
