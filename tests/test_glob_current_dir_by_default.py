# pylint: disable=C0103,C0111,C0330

import os
import sys
import unittest
sys.path.append(os.path.abspath('..'))
import run_clang_format  # pylint: disable=C0413


class GlobCurrentDirByDefault(unittest.TestCase):
    def setUp(self):
        os.chdir('glob_current_dir_by_default')

    def tearDown(self):
        os.chdir('..')

    def test_basic(self):
        old_sys_argv = sys.argv
        sys.argv = [old_sys_argv[0]]
        args = run_clang_format.parse_args()
        sys.argv = old_sys_argv

        files = run_clang_format.glob_files(args)
        self.assertEqual(2, len(files))
        self.assertEqual([
            os.path.join(os.getcwd(), 'a.cpp'),
            os.path.join(os.getcwd(), 'a.hpp')],
            files)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(  # pylint: disable=E1102
        output='test-reports'))()
