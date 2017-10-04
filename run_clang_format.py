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

    args = parser.parse_args(argv[1:])

    if not args.directories:
        args.directories = [os.getcwd()]

    return args


def format_all(args, files):
    invocation = [args.clang_format_binary, '-i', '-style=' + args.style]
    for filename in files:
        full_invocation = invocation
        full_invocation.append(filename)
        try:
            print('Processing', filename)
            subprocess.check_output(full_invocation)
        except subprocess.CalledProcessError as ex:
            print("Unable to run clang-format.", file=sys.stderr)
            print("Command    : " + ' '.join(ex.cmd) + ").",
                  file=sys.stderr)
            print("Return code: " + str(ex.returncode), file=sys.stderr)
            sys.exit(1)


def main():
    args = parse_args()

    files = glob_files(args)

    format_all(args, files)


if __name__ == '__main__':
    main()
