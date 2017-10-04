# pylint: disable=C0103,C0111,C0330

import os
import sys
import unittest
sys.path.append(os.path.abspath('..'))
import run_clang_format  # pylint: disable=C0413


class GlobAllExtensions(unittest.TestCase):
    def test_basic(self):
        args = run_clang_format.parse_args(
            [sys.argv[0], '-d', 'glob_all_extensions'])
        files = run_clang_format.glob_files(args)
        self.assertEqual(10, len(files))
        self.assertEqual([
            os.path.join('glob_all_extensions', 'a.c'),
            os.path.join('glob_all_extensions', 'a.cc'),
            os.path.join('glob_all_extensions', 'a.cpp'),
            os.path.join('glob_all_extensions', 'a.cxx'),
            os.path.join('glob_all_extensions', 'a.c++'),
            os.path.join('glob_all_extensions', 'a.h'),
            os.path.join('glob_all_extensions', 'a.hh'),
            os.path.join('glob_all_extensions', 'a.hpp'),
            os.path.join('glob_all_extensions', 'a.hxx'),
            os.path.join('glob_all_extensions', 'a.h++')],
            files)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(  # pylint: disable=E1102
        output='test-reports'))()
