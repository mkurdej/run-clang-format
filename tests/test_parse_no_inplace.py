# pylint: disable=C0103,C0111,C0330

import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import run_clang_format  # pylint: disable=C0413


class ParseClangFormatbinary(unittest.TestCase):
    def test_basic(self):
        args = run_clang_format.parse_args([
            sys.argv[0],
            '--no-inplace',
            '-d', 'parse_no_inplace'])
        files = run_clang_format.glob_files(args)

        a_cpp_path = os.path.join('parse_no_inplace', 'a.cpp')

        self.assertEqual(1, len(files))
        self.assertEqual([a_cpp_path], files)

        formatted_files = run_clang_format.format_all(args, files)

        self.assertEqual(1, len(formatted_files))
        self.assertIn(a_cpp_path, formatted_files)

        self.assertEqual(b'void no_inplace() {}',
                         formatted_files[a_cpp_path])


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(  # pylint: disable=E1102
        output='test-reports'))()
