import unittest
from src.PREN_flawas import DataVerify


class testDataVerify(unittest.TestCase):
    def testcheckAvailability(self):
        DataVerify.checkAvailability("http://18.192.48.168:5000/cubes/")

if __name__ == '__main__':
    unittest.main()