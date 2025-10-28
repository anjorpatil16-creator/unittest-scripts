"""
Author: Anjor Patil
Date: 23-10-2025
Time: 20:30
"""


import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(50, 5), 55)
        self.assertEqual(calc.add(20, 90), 110)
        
        
    def test_subt(self):
        self.assertEqual(calc.subtract(200, 50), 150) 
        self.assertEqual(calc.subtract(60, 50), 10)  
        self.assertEqual(calc.subtract(40, 10), 30)  
         
        
    def test_mult(self):
        self.assertEqual(calc.multiply(30, 2), 60)  
        self.assertEqual(calc.multiply(20, 5), 100)    
        self.assertEqual(calc.multiply(4, 20), 80)    
          
      
    def test_divd(self):
        self.assertEqual(calc.divide(30, 5), 6)  
        self.assertEqual(calc.divide(60, 2), 30)    
        self.assertEqual(calc.divide(80, 5), 16)    
          

if __name__ == '__main__':
    unittest.main()