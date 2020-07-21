import unittest
from my_lambdata.ds_utilities import enlarge

class TestDsUtilities(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(3), 300)

if __name__ == '__main__':
    unittest.main()
