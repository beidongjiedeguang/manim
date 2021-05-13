from manimlib import Scene
import time
import sys
import os

class EagerModeScene(Scene):

    def __init__(self):
        super().__init__()
        self.virtual_animation_start_time = 0
        self.real_animation_start_time = time.time()
        self.file_writer.begin()

        self.setup()

    def hold_on(self):
        self.tear_down()

    def embed(self):
        super().embed()



class JupyterModeScene(EagerModeScene):
    def __init__(self):
        super().__init__()

    def hold_on(self):
        pass

    def embed(self):
        pass

    def quit(self) :
        self.quit_interaction = True
        self.unlock_mobject_data()
        self.window.destroy()








__all__ = ["EagerModeScene", "JupyterModeScene"]
