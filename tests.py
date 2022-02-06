''' Just test something for CodeCov tool '''
import unittest

class Testing(unittest.TestCase):
    ''' Class docstring'''
    def test_boolean(self):
        ''' Tests docstring '''
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
