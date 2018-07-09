from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='picol',
    version='0.2',
    description=('picol (pronounced "pickle") will fetch the ten most used '
                 'colors in an image and present the hex colors.'),
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL-v3.0',
    author='armandg',
    author_email='armandg@gmail.com',
    entry_points={
        'console_scripts': [
            'picol = picol.picol:main'
        ]
    },
    packages=find_packages(),
    install_requires=[
        'colorgram.py',
        'pillow'
    ],
    package_data={
        'picol': [
            'fonts/OpenSans-Bold.ttf',
            'fonts/OpenSans-ExtraBoldItalic.ttf',
            'fonts/OpenSans-ExtraBold.ttf',
            'fonts/OpenSans-Italic.ttf',
            'fonts/OpenSans-LightItalic.ttf',
            'fonts/OpenSans-Light.ttf',
            'fonts/OpenSans-Regular.ttf',
            'fonts/OpenSans-SemiboldItalic.ttf',
            'fonts/OpenSans-Semibold.ttf',
            'README.md'
        ]
    },
)
