import unittest
from BMIcalculator import heightcal, bmical

class TestBMIcalculator(unittest.TestCase):
    def test_heightcal(self):
        self.assertEqual(heightcal(5, 8), 68)
        self.assertEqual(heightcal(6, 0), 72)
        
    def test_bmical(self):
        self.assertAlmostEqual(bmical(68, 1.75**2), 22.2, delta=0.1)
        self.assertAlmostEqual(bmical(130, 1.65**2), 47.7, delta=0.1)
        
if __name__ == '__main__':
    unittest.main()
