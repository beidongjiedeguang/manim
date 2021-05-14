from manimlib import Scene
import time
import sys
import os

__all__ = ["EagerModeScene", "JupyterModeScene"]

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
        """We don't need it in jupyter lab/notebook."""
        pass

    def embed(self):
        """We don't need it in jupyter lab/notebook."""
        pass

    def quit(self) :
        """Please use exit() or quit() in jupyter cell."""
        pass











