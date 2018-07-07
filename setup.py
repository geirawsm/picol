from distutils.core import setup
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(BASE_DIR, 'fonts')


def read_full_documentation(filename):
    with open(os.path.join(BASE_DIR, filename)) as fin:
        return fin.read()


requirements = [
    'colorgram.py',
]


setup(
    name='picol',
    version='0.2',
    author='armandg',
    author_email='armandg@gmail.com',
    description=('picol (pronounced "pickle") will fetch the ten most used '
                 'colors in an image and present the hex colors.'),
    packages=['picol'],
    package_data={
        'picol': [
            'fonts/OpenSans-BoldItalic.ttf',
            'fonts/OpenSans-Bold.ttf',
            'fonts/OpenSans-ExtraBoldItalic.ttf',
            'fonts/OpenSans-ExtraBold.ttf',
            'fonts/OpenSans-Italic.ttf',
            'fonts/OpenSans-LightItalic.ttf',
            'fonts/OpenSans-Light.ttf',
            'fonts/OpenSans-Regular.ttf',
            'fonts/OpenSans-SemiboldItalic.ttf',
            'fonts/OpenSans-Semibold.ttf'
        ]
    },
    install_requires=requirements,
    include_package_data=True,
    license='GPL-v3.0',
    long_description=read_full_documentation('README.rst'),
    entry_points={
        'console_scripts': [
            'picol = picol.picol:main'
        ]
    },
)
