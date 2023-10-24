import unittest

from fraction import fraction

class TestFractionMethods(unittest.TestCase):

  def test_create(self):
    f1 = fraction(1,1)
    self.assertEqual(f1.num, 1)
    self.assertEqual(f1.den, 1)

  def test_reduce(self):
    f1 = fraction(6,8)
    self.assertEqual(f1.num, 3)
    self.assertEqual(f1.den, 4)

  def test_zero(self):
    f1 = fraction(0,0)
    self.assertEqual(f1.num, 0)
    self.assertEqual(f1.den, 1)
    
  def test_negative(self):
    f1 = fraction(-6,8)
    self.assertEqual(f1.num, -3)
    self.assertEqual(f1.den, 4)
    f2 = fraction(6,-8)
    self.assertEqual(f2.num, -3)
    self.assertEqual(f2.den, 4)



  def test_add(self):
    f1 = fraction(1,1)
    f2 = fraction(1,1)
    f3 = f1 + f2
    self.assertEqual(f3.num, 2)
    self.assertEqual(f3.den, 1)
    

      
if __name__ == '__main__':
    unittest.main()