from distutils.core import setup
from distutils.command.install import install as _install
import getpass


def _post_install(dir):
    from subprocess import call
    call([sys.executable, 'fc-cache -f'])


class install(_install):
    def run(self):
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install task")


_username = getpass.getuser()
font_dir = '/home/{}/.fonts/'.format(_username)

setup(
    name='picol',
    version='0.1',
    author='armandg',
    author_email='armandg@gmail.com',
    description = ('picol (pronounced "pickle") will fetch the ten most used '
                   'colors in an image and present the hex colors.'),
    packages=['picol'],
    data_files=[
        (font_dir, [
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
    long_description=open('README.md').read(),
    cmdclass={'install': install},
)
