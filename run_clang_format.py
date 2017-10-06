#!/usr/bin/env python

# pylint: disable=C0111

"""
Runs clang format over all cpp files
"""

from __future__ import print_function
import argparse
import fnmatch
import os
import subprocess
import sys


def glob_files(args):
    files = []

    extensions = args.extensions.split(',')

    for directory in args.directories:
        for root, _, filenames in os.walk(directory):
            for ext in extensions:
                for filename in fnmatch.filter(filenames, '*.' + ext):
                    files.append(os.path.join(root, filename))

    return files


def parse_args(argv=None):
    if argv is None:
        argv = sys.argv
    parser = argparse.ArgumentParser(
        description='Runs clang-format over all files in given directories.'
        ' Requires clang-format in PATH.')
    parser.add_argument('--clang-format-binary', metavar='PATH',
                        default='clang-format',
                        help='path to clang-format binary')
    parser.add_argument('-d', '--directory', metavar='DIRPATH', dest='directories', action='append',
                        help='path(s) used to glob source files')
    parser.add_argument('-e', '--extensions', dest='extensions',
                        help='comma-delimited list of extensions used to glob source files',
                        default="c,cc,cpp,cxx,c++,h,hh,hpp,hxx,h++")
    parser.add_argument('-style',
                        help='formatting style',
                        default="file")
    parser.add_argument('--no-inplace', dest='inplace', action='store_false',
                        help='do not format files inplace, but write output to the console'
                        ' (useful for debugging)',
                        default=True)

    args = parser.parse_args(argv[1:])

    if not args.directories:
        args.directories = [os.getcwd()]

    return args


def format_all(args, files):
    invocation = [args.clang_format_binary]
    invocation.append('-style=' + args.style)
    if args.inplace:
        invocation.append('-i')

    formatted_files = {}
    for filename in files:
        full_invocation = invocation
        full_invocation.append(filename)
        try:
            print('Processing {}'.format(filename), file=sys.stderr)
            formatted = subprocess.check_output(full_invocation)
            formatted_files[filename] = formatted
        except OSError as ex:
            print("Cannot find clang-format at '{}'.".format(args.clang_format_binary),
                  file=sys.stderr)

            raise ex
        except subprocess.CalledProcessError as ex:
            print("Running clang-format failed with non-zero status.", file=sys.stderr)
            print("Command    : {}".format(' '.join(ex.cmd)), file=sys.stderr)
            print("Return code: {}".format(str(ex.returncode)), file=sys.stderr)

            raise ex

    return formatted_files


def main():
    args = parse_args()

    files = glob_files(args)

    format_all(args, files)


if __name__ == '__main__':
    main()
