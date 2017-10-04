# pylint: disable=C0103,C0111

import os
import sys
import unittest
sys.path.append(os.path.abspath('..'))
import run_clang_format  # pylint: disable=C0413


class GlobAllExtensions(unittest.TestCase):
    def test_basic(self):
        args = run_clang_format.parse_args([
            sys.argv[0],
            '-d', 'glob_alternative_extensions',
            '-e', 'c1,c2'])
        files = run_clang_format.glob_files(args)
        self.assertEqual(3, len(files))
        files.sort()
        self.assertEqual([
            os.path.join('glob_alternative_extensions', 'a.c1'),
            os.path.join('glob_alternative_extensions', 'a.c2'),
            os.path.join('glob_alternative_extensions', 'b.c1')],
            files)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(  # pylint: disable=E1102
        output='test-reports'))()
