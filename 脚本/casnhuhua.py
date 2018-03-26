import unittest
from nose_parameterized import parameterized
a=1
abc=[
        ("TC_INT_1",1, 1, 2),
        ("TC_INT_2",3, 2, 5),
        ("TC_INT_3",1, 3, 6),
    ]

class interfaceTest(unittest.TestCase):


    @parameterized.expand(abc)
    def test_cae(self, name, a, b, c):
        self.assertEqual(a + b, c)


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(interfaceTest('TC_INT'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main(verbosity=2)