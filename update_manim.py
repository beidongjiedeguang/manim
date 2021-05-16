import os
from guang.Utils.toolsFunc import rm

rm(['eggs', 'dist', 'build', 'manim_kunyuan.egg-info'])
os.system('pip uninstall manim_kunyuan -y && python setup_manimlib.py install')

rm(['eggs', 'dist', 'build', 'manim_kunyuan.egg-info'])
