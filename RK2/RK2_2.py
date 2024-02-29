import unittest
from RK2_1 import *

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.PCs, self.OSs, self.PC_OSs = getData()

    def test_t1(self):
        want = [('ASUS', 'Windows 7'), ('Colorful', 'FreeDOS'), ('Dell', 'Linux'), ('Lenovo', 'Windows 7')]
        actual = t1(self.PCs, self.OSs, self.PC_OSs)

        self.assertCountEqual(want, actual)

    def test_t2(self):
        want =[('Linux', 1024.0), ('Windows 10', 1536.0), ('Windows 7', 1536.0), ('FreeDOS', 3072.0), ('Windows 11', 4096.0)]
        actual = t2(self.PCs, self.OSs, self.PC_OSs)

        self.assertCountEqual(want, actual)

    def test_t3(self):
        want = {'Windows 10': ['Lenovo', 'ASUS'], 'Windows 11': ['Dell', 'hp', 'ASUS', 'Colorful'], 'Windows 7': ['Dell']}
        actual = t3(self.PCs, self.OSs, self.PC_OSs)

        self.assertCountEqual(want, actual)

unittest.main()

