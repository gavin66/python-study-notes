import unittest


class ProductTestCase(unittest.TestCase):
    def square(self, x, y):
        return x * y

    def testIntegers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = self.square(x, y)
                self.failUnless(p == x * y, 'Integer multiplication failed')

    def testFloats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10.0
                y = y / 10.0
                p = self.square(x, y)
                self.failUnless(p == x * y, 'Float multiplication failed')


if __name__ == '__main__':
    unittest.main()
