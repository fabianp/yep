
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
    description='The Yep Extension Profiler',
    version='0.0',
    author='Fabian Pedregosa',
    author_email='fabian.pedregosa@inria.fr',
    url='http://fseoane.net/software/yep',
	py_modules=['yep'],
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],

)
