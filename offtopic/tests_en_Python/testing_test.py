# Test para testear las funciones de prueba2.py

import unittest
from file_to_test import factorial, numPerfecto, numPrimo

class TestingPrueba2(unittest.TestCase):
        
        def test_factorial(self):
            resultado = factorial(5)
            self.assertEqual(resultado, 120)
            
        def test_numPerfecto(self):
            resultado = numPerfecto(6)
            self.assertTrue(resultado)
            
        def test_numPrimo(self):
            resultado = numPrimo(7)
            self.assertTrue(resultado)

        def test_numPrimoFalse(self):
            resultado = numPrimo(8)
            self.assertFalse(resultado)            

if __name__ == '__main__':
    unittest.main()