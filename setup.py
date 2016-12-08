from distutils.core import setup
import py2exe

Mydata_files = [('', ['spacetrees.png']),
				('', ['freesansbold.ttf'])]

setup(
    console=['oil_water.py'],
    data_files = Mydata_files
)