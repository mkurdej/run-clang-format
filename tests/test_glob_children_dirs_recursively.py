# pylint: disable=C0103,C0111

import os
import sys
import unittest
sys.path.append(os.path.abspath('..'))
import run_clang_format  # pylint: disable=C0413


class GlobChildrenDirsRecursively(unittest.TestCase):
    def test_basic(self):
        args = run_clang_format.parse_args(
            [sys.argv[0], '-d', 'glob_children_dirs_recursively'])
        files = run_clang_format.glob_files(args)
        self.assertEqual(8, len(files))
        self.assertEqual([
            os.path.join('glob_children_dirs_recursively', 'root.cpp'),
            os.path.join('glob_children_dirs_recursively', 'root.hpp'),
            os.path.join('glob_children_dirs_recursively', 'a', 'a.cpp'),
            os.path.join('glob_children_dirs_recursively', 'a', 'a.hpp'),
            os.path.join('glob_children_dirs_recursively', 'a', 'b', 'b.cpp'),
            os.path.join('glob_children_dirs_recursively', 'a', 'b', 'b.hpp'),
            os.path.join('glob_children_dirs_recursively',
                         'a', 'b', 'c', 'c.cpp'),
            os.path.join('glob_children_dirs_recursively', 'a', 'b', 'c', 'c.hpp')],
            files)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(  # pylint: disable=E1102
        output='test-reports'))()
