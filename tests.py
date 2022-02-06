
import unittest

''' Just test something for CodeCov tool '''
class Testing(unittest.TestCase):
    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()