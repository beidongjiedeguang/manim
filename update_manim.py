from guang import rm
import os
os.system('pip uninstall manimlib -y && python setup_manimlib.py install')

rm(['eggs', 'dist', 'build'])
