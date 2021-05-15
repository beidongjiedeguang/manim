from express.eager import EagerModeScene, JupyterModeScene
from manimlib import *
scene = EagerModeScene()
circle = Circle()
circle.move_to([1, 1, 0]).set_color(BLUE)

scene.play(ShowCreation(circle))
scene.play(FadeOut(circle))
