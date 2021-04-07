from manimlib import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()

        # Stretched 4 times in the vertical direction
        self.play(circle.animate.stretch(4, dim=0))
        # Rotate the ellipse 90°
        self.play(Rotate(circle, TAU / 4))
        # Move 2 units to the right and shrink to 1/4 of the original
        self.play(circle.animate.shift(2 * RIGHT), circle.animate.scale(0.25))
        # Insert 10 curves into circle for non-linear transformation (no animation will play)
        circle.insert_n_curves(10)
        # Apply a complex transformation of f(z)=z^2 to all points on the circle
        self.play(circle.animate.apply_complex_function(lambda z: z**2))
        # Close the window and exit the program
        exit()

class InteractiveDevlopment(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()

        # This opens an iPython termnial where you can keep writing
        # lines as if they were part of this construct method.
        # In particular, 'square', 'circle' and 'self' will all be
        # part of the local namespace in that terminal.
        self.embed()

        # Try copying and pasting some of the lines below into
        # the interactive shell
        # self.play(ReplacementTransform(square, circle))
        # self.wait()
        # self.play(circle.animate.stretch(4, 0))
        # self.play(Rotate(circle, 90 * DEGREES))
        # self.play(circle.animate.shift(2 * RIGHT).scale(0.25))

        # text = Text("""
        #     In general, using the interactive shell
        #     is very helpful when developing new scenes
        # """)
        # self.play(Write(text))

        # # In the interactive shell, you can just type
        # # play, add, remove, clear, wait, save_state and restore,
        # # instead of self.play, self.add, self.remove, etc.

        # # To interact with the window, type touch().  You can then
        # # scroll in the window, or zoom by holding down 'z' while scrolling,
        # # and change camera perspective by holding down 'd' while moving
        # # the mouse.  Press 'r' to reset to the standard camera position.
        # # Press 'q' to stop interacting with the window and go back to
        # # typing new commands into the shell.

        # # In principle you can customize a scene to be responsive to
        # # mouse and keyboard interactions
        # always(circle.move_to, self.mouse_point)

class AnimatingMethods(Scene):
    def construct(self):
        grid = Tex(r"\pi").get_grid(10, 10, height=4)
        self.add(grid)

        # You can animate the application of mobject methods with the
        # ".animate" syntax:
        self.play(grid.animate.shift(LEFT))

        # Alternatively, you can use the older syntax by passing the
        # method and then the arguments to the scene's "play" function:
        self.play(grid.shift, LEFT)

        # Both of those will interpolate between the mobject's initial
        # state and whatever happens when you apply that method.
        # For this example, calling grid.shift(LEFT) would shift the
        # grid one unit to the left, but both of the previous calls to
        # "self.play" animate that motion.

        # The same applies for any method, including those setting colors.
        self.play(grid.animate.set_color(YELLOW))
        self.wait()
        self.play(grid.animate.set_submobject_colors_by_gradient(BLUE, GREEN))
        self.wait()
        self.play(grid.animate.set_height(TAU - MED_SMALL_BUFF))
        self.wait()

        # The method Mobject.apply_complex_function lets you apply arbitrary
        # complex functions, treating the points defining the mobject as
        # complex numbers.
        self.play(grid.animate.apply_complex_function(np.exp), run_time=5)
        self.wait()

        # Even more generally, you could apply Mobject.apply_function,
        # which takes in functions form R^3 to R^3
        self.play(
            grid.animate.apply_function(
                lambda p: [
                    p[0] + 0.5 * math.sin(p[1]),
                    p[1] + 0.5 * math.sin(p[0]),
                    p[2]
                ]
            ),
            run_time=5,
        )
        self.wait()