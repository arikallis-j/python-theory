import unittest
import calc
 
class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(1, 2), 3)
        self.assertEqual(calc.add("1", "2"), "12")
        #self.assertEqual(calc.add("1", 2), "12")
        #self.assertEqual(calc.add(1, "2"), 3)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, 1), calc.add(1, -1))
        
    def test_sub(self):
        self.assertEqual(calc.sub(4, 2), 2)
        
    def test_mul(self):
        self.assertEqual(calc.mul(2, 5), 10)
        
    def test_div(self):
        self.assertEqual(calc.div(8, 4), 2)
        
if __name__ == '__main__':
    unittest.main()