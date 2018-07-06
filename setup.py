from distutils.core import setup
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(BASE_DIR, 'fonts')


def read_full_documentation(filename):
    return open(os.path.join(BASE_DIR, filename)).read()


requirements = [
    'cologram.py==1.1.0',
    'Pillow==5.2.0',
]


setup(
    name='picol',
    version='0.2',
    author='armandg',
    author_email='armandg@gmail.com',
    description=('picol (pronounced "pickle") will fetch the ten most used '
                 'colors in an image and present the hex colors.'),
    packages=['picol'],
    data_files=[
        (FONT_DIR, [
            'fonts/OpenSans-BoldItalic.ttf',
            'fonts/OpenSans-Bold.ttf',
            'fonts/OpenSans-ExtraBoldItalic.ttf',
            'fonts/OpenSans-ExtraBold.ttf',
            'fonts/OpenSans-Italic.ttf',
            'fonts/OpenSans-LightItalic.ttf',
            'fonts/OpenSans-Light.ttf',
            'fonts/OpenSans-Regular.ttf',
            'fonts/OpenSans-SemiboldItalic.ttf',
            'fonts/OpenSans-Semibold.ttf'])],
    license='GPL-v3.0',
    long_description=read_full_documentation('README.rst'),
    entry_points={
        'console_scripts': [
            'picol = picol.picol:main'
        ]
    }
)
