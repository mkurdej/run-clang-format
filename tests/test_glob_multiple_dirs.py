# pylint: disable=C0103,C0111,C0330

import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import run_clang_format  # pylint: disable=C0413


class GlobChildrenDirs(unittest.TestCase):
    def test_basic(self):
        args = run_clang_format.parse_args([
            sys.argv[0],
            os.path.join('glob_multiple_dirs', 'a'),
            os.path.join('glob_multiple_dirs', 'b'),
            os.path.join('glob_multiple_dirs', 'c')])
        files = run_clang_format.glob_files(args)
        self.assertEqual(6, len(files))
        self.assertEqual([
            os.path.join('glob_multiple_dirs', 'a', 'a.cpp'),
            os.path.join('glob_multiple_dirs', 'a', 'a.hpp'),
            os.path.join('glob_multiple_dirs', 'b', 'b.cpp'),
            os.path.join('glob_multiple_dirs', 'b', 'b.hpp'),
            os.path.join('glob_multiple_dirs', 'c', 'c.cpp'),
            os.path.join('glob_multiple_dirs', 'c', 'c.hpp')],
            files)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(  # pylint: disable=E1102
        output='test-reports'))()
