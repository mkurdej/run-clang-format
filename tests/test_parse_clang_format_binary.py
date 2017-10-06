# pylint: disable=C0103,C0111,C0330

import os
import sys
import unittest
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import run_clang_format  # pylint: disable=C0413


class ParseClangFormatBinary(unittest.TestCase):
    def test_basic(self):
        args = run_clang_format.parse_args([
            sys.argv[0],
            '--clang-format-binary', 'unexisting-clang-format',
            '-d', 'parse_clang_format_binary'])
        files = run_clang_format.glob_files(args)

        self.assertEqual(1, len(files))

        self.assertRaises(OSError, run_clang_format.format_all, args, files)


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(  # pylint: disable=E1102
        output='test-reports'))()
