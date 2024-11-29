import unittest

maxValue = 2147483647
minValue = -2147483647

def can_drive(age):
    if age <= 0:
        raise ValueError("Age must be a positive integer.")
    driving_age = 16
    return age >= driving_age


class TestCDF(unittest.TestCase):
    def test_year1(self):
        self.assertFalse(can_drive(15))

    def test_year2(self):
        self.assertTrue(can_drive(16))

    def test_year3(self):
        self.assertTrue(can_drive(17))

    def test_year4(self):
        self.assertTrue(can_drive(maxValue))

    def test_year5(self):
        self.assertTrue(can_drive(maxValue - 1))

    def test_year6(self):
        with self.assertRaises(ValueError):
            can_drive(0)

    def test_year7(self):
        with self.assertRaises(ValueError):
            can_drive(-1)

    def test_year8(self):
        self.assertFalse(can_drive(1))

    def test_year9(self):
        with self.assertRaises(ValueError):
            can_drive(minValue)

    def test_year10(self):
        with self.assertRaises(ValueError):
            can_drive(minValue + 1)

if __name__ == "__main__":
    unittest.main()

