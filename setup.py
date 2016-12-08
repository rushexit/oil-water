from distutils.core import setup
import py2exe

Mydata_files = [('', ['spacetrees.png']),
				('', ['freesansbold.ttf']),
				('data/states/act_i_scene_i', ['test_script.txt'])]

setup(
    console=['oil_water.py'],
    data_files = Mydata_files
)