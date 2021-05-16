import os
from guang.Utils.toolsFunc import rm

rm(['eggs', 'dist', 'build', 'manim_kunyuan.egg-info'])
os.system('python setup_manimlib.py sdist bdist_wheel')
os.system('twine upload dist/*')