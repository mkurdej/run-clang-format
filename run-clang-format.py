#!/usr/bin/env python

# pylint: disable=C0103,C0111

"""
Runs clang format over all cpp files
"""

from __future__ import print_function
import argparse
import fnmatch
import os
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(
        description='Runs clang-format over all files in a current directory.'
        ' Requires clang-format in PATH.')
    parser.add_argument('-clang-format-binary', metavar='PATH',
                        default='clang-format',
                        help='path to clang-format binary')

    parser.add_argument('-p', dest='build_path',
                        help='Path used to glob source files.',
                        default=os.getcwd())

    args = parser.parse_args()

    ignore = [
    ]

    extensions = "c cc cpp cxx h hh hpp hxx".split()
    files = []

    for root, _, filenames in os.walk(args.build_path):
        for ext in extensions:
            for filename in fnmatch.filter(filenames, '*.' + ext):
                # for filename in glob.glob(args.build_path + "/**/*." + ext):
                files.append(os.path.join(root, filename))

    invocation = [args.clang_format_binary, '-i', '-style=file']
    for filename in files:
        for txt in ignore:
            if txt in filename or filename in txt:
                break
        else:
            full_invocation = invocation
            full_invocation.append('"' + filename + '"')
            try:
                print('Processing', filename)
                print(str(full_invocation))
                subprocess.check_output(full_invocation)
            except subprocess.CalledProcessError as ex:
                print("Unable to run clang-format.", file=sys.stderr)
                print("Command    : " + ' '.join(ex.cmd) + ").", file=sys.stderr)
                print("Return code: " + str(ex.returncode), file=sys.stderr)
                sys.exit(1)


if __name__ == '__main__':
    main()
