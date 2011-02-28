#!/usr/bin/env python
"""Yep Extension Profiler

Yep is a tool to profile compiled code (C/C++/Fortran) from the Python
interpreter. It uses the google-perftools CPU profiler and depends on
pprof for visualization.

See http://fseoane.net/software/yep for more info.
"""

_CMD_USAGE = """usage: python -m yap scriptfile [arg] ...

This will create a file scriptfile.prof that can be analyzed with
pprof (google-pprof on Debian-based systems).
"""


#       .. find google-perftools ..
import ctypes.util
google_profiler = ctypes.util.find_library('profiler')
if google_profiler:
    libprofiler = ctypes.CDLL(google_profiler)
else:
    raise ImportError(
        'Unable to find libprofiler, please make sure google-perftools '
        'is installed on your system'
        )


def start(file_name=None):
    """
    Start the CPU profiler.

    Parameters
    ----------
    fname : string, optional
       Name of file to store profile count. If not given, 'out.prof'
       will be used
    """
    if file_name is None:
        file_name = 'out.prof'
    status = libprofiler.ProfilerStart(file_name)
    if status < 0:
        raise ValueError('Profiler did not start')


def stop():
    """Stop the CPU profiler"""
    libprofiler.ProfilerStop()


def main():
    import sys, os, __main__
    from optparse import OptionParser
    parser = OptionParser(usage=_CMD_USAGE)
    parser.add_option('-o', '--outfile', dest='outfile',
        help='Save stats to <outfile>', default=None)
    parser.add_option('-v', '--visualize', action='store_true',
        dest='visualize', help='Visualize result at exit',
        default=False)

    if not sys.argv[1:] or sys.argv[1] in ("--help", "-h"):
        parser.print_help()
        sys.exit(2)

    (options, args) = parser.parse_args()

#       .. get file name ..
    main_file = os.path.abspath(args[0])
    if options.outfile is None:
        options.outfile = os.path.basename(main_file) + '.prof'
    if not os.path.exists(main_file):
        print('Error:', main_file, 'does not exist')
        sys.exit(1)

#       .. execute file ..
    sys.path.insert(0, os.path.dirname(main_file))
    start(options.outfile)
    exec(compile(open(main_file).read(), main_file, 'exec'),
         __main__.__dict__)
    stop()

    if options.visualize:
        from subprocess import call
        try:
            res = call('google-pprof --help > /dev/null', shell=True)
        except OSError:
            res = 1
        pprof_exec = ('google-pprof', 'pprof')[res != 0]

#       .. strip memory address, 32 bit-compatile ..
        sed_filter = '/[[:xdigit:]]\{8\}$/d'
        call("%s --cum --text %s %s | sed '%s' | less" % \
             (pprof_exec, sys.executable, options.outfile, sed_filter), shell=True)
    
if __name__ == '__main__':
    main()
