from manimlib import *
import time

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
        self.embed()

    def quit(self):
        self.quit_interaction =True
        self.window.is_closing = True
        self.quit()
        self.window.destroy()
        self.unlock_mobject_data()

class JupyterModeScene(EagerModeScene):
    def __init__(self):
        super().__init__()

    def hold_on(self):
        pass

    def embed(self):
        pass

    def quit(self):
        exit()
