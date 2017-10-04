# pylint: disable=C0103,C0111

import os
import sys
import unittest
sys.path.append(os.path.abspath('..'))
import run_clang_format  # pylint: disable=C0413


class GlobChildrenDirs(unittest.TestCase):
    def test_basic(self):
        args = run_clang_format.parse_args(
            [sys.argv[0], '-d', 'glob_children_dirs'])
        files = run_clang_format.glob_files(args)
        self.assertEqual(8, len(files))
        self.assertEqual([os.path.join('glob_children_dirs', 'root.cpp'),
                          os.path.join('glob_children_dirs', 'root.hpp'),
                          os.path.join('glob_children_dirs', 'a', 'a.cpp'),
                          os.path.join('glob_children_dirs', 'a', 'a.hpp'),
                          os.path.join('glob_children_dirs', 'b', 'b.cpp'),
                          os.path.join('glob_children_dirs', 'b', 'b.hpp'),
                          os.path.join('glob_children_dirs', 'c', 'c.cpp'),
                          os.path.join('glob_children_dirs', 'c', 'c.hpp')],
                         files)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(  # pylint: disable=E1102
        output='test-reports'))()
