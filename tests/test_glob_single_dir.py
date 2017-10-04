# pylint: disable=C0103,C0111,C0330

import os
import sys
import unittest
sys.path.append(os.path.abspath('..'))
import run_clang_format  # pylint: disable=C0413


class GlobSingleDir(unittest.TestCase):
    def test_basic(self):
        args = run_clang_format.parse_args([
            sys.argv[0],
            '-d', 'glob_single_dir'])
        files = run_clang_format.glob_files(args)
        self.assertEqual(2, len(files))
        self.assertEqual([
            os.path.join('glob_single_dir', 'a.cpp'),
            os.path.join('glob_single_dir', 'a.hpp')],
            files)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(  # pylint: disable=E1102
        output='test-reports'))()
