===============================
YEP: the Yep Extension Profiler
===============================

Yep is a tool to profile compiled code (C/C++/Fortran) from the Python
interpreter. It uses the google-perftools CPU profiler and depends on
pprof (google-pprof on Debian) for visualization.


Install
-------

This package depends on google-perftools (package google-perftools in
Debian). Once you have fulfilled these depencies you can install the
package with the usual command::

    $ python setup.py install

However, since the package one-file distribution, you can also just
put yep.py somewhere in your $PYTHONPATH.


Usage
-----

There are various ways to use the profiler. The simplest is add this
module as argument to the Python interpreter when running your
script and add flag -v to visualize the result::

    $ python -m yep -v my_script.py

This will create a file my_script.py.prof that can be analyzed with
pprof. Execute ``python -m yep`` to get the full list of options.

It is also possible to manually start/stop the profiler from inside
Python code::

    >>> import yep
    >>> yep.start('file_name.prof')
    >>> # do your computations
    >>> yep.stop()

This will create a file_name.prof to be analized with pperf.


Development
-----------

Git repository can be found here::

    https://github.com/fabianp/yep


Bugs
----

Visualize the result with -v will only work on UNIX. An option --prof=
would also be nice.


Misc
----

Author: Fabian Pedregosa <fabian.pedregosa@inria.fr>


License
-------

Simplified BSD License, (C) 2011 Fabian Pedregosa.
