import yep
from distutils.core import setup

CLASSIFIERS = """\
Development Status :: 4 - Beta
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved
Programming Language :: Python
Programming Language :: Python :: 3
Topic :: Software Development
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS

"""

setup(
    name='yep',
    description='A module for profiling compiled extensions',
    long_description=open('README.rst').read(),
    version=yep.__version__,
    author='Fabian Pedregosa',
    author_email='fabian.pedregosa@inria.fr',
    url='http://pypi.python.org/pypi/yep',
	py_modules=['yep'],
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],

)
