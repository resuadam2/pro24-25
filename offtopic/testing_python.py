# Cómo hacer test unitarios en python:

# 1. Importar unittest
import unittest

# 2. Crear una clase que herede de unittest.TestCase
class TestingPython(unittest.TestCase):

    # 3. Crear un método que empiece con test_
    def test_suma(self):
        # 4. Hacer las operaciones que se deseen
        resultado = 2 + 2
        # 5. Asegurarse de que el resultado sea el esperado
        self.assertEqual(resultado, 4)

    def test_resta(self):
        resultado = 2 - 2
        self.assertEqual(resultado, 0)

    def test_multiplicacion(self):
        resultado = 2 * 2
        self.assertEqual(resultado, 4)

    def test_division(self):
        resultado = 2 / 2
        self.assertEqual(resultado, 1)

# 6. Ejecutar los test

if __name__ == '__main__':
    unittest.main()

# Para ejecutar el test, se debe correr el archivo con el siguiente comando:
# python testing_python.py

# Si se desea correr un test específico, se puede hacer de la siguiente manera:
# python testing_python.py TestingPython.test_suma

# Si se desea correr todos los test que empiecen con test, se puede hacer de la siguiente manera:
# python testing_python.py -v

# Para más información, se puede consultar la documentación oficial de python:
# https://docs.python.org/3/library/unittest.html

# Para crear test que testeen funciones definidas en otro archivo, se puede hacer de la siguiente manera:   
# from archivo import funcion
# class TestingPython(unittest.TestCase):
#     def test_funcion(self):
#         resultado = funcion()
#         self.assertEqual(resultado, 4)

# Los distintos métodos que se pueden utilizar para comparar los resultados son:
# self.assertEqual(a, b) -> a == b
# self.assertNotEqual(a, b) -> a != b
# self.assertTrue(x) -> bool(x) is True
# self.assertFalse(x) -> bool(x) is False
# self.assertIs(a, b) -> a is b
# self.assertIsNot(a, b) -> a is not b
# self.assertIsNone(x) -> x is None
# self.assertIsNotNone(x) -> x is not None
# self.assertIn(a, b) -> a in b
# self.assertNotIn(a, b) -> a not in b
# self.assertIsInstance(a, b) -> isinstance(a, b)
# self.assertNotIsInstance(a, b) -> not isinstance(a, b)
# self.assertAlmostEqual(a, b) -> round(a-b, 7) == 0
# self.assertNotAlmostEqual(a, b) -> round(a-b, 7) != 0
# self.assertGreater(a, b) -> a > b
# self.assertGreaterEqual(a, b) -> a >= b
# self.assertLess(a, b) -> a < b
# self.assertLessEqual(a, b) -> a <= b
# self.assertRegex(s, r) -> r.search(s)
# self.assertNotRegex(s, r) -> not r.search(s)
# self.assertCountEqual(a, b) -> a y b tienen las mismas keys y los mismos valores
# self.assertMultiLineEqual(a, b) -> a y b son strings y son iguales
# self.assertSequenceEqual(a, b) -> a y b son secuencias
# self.assertListEqual(a, b) -> a y b son listas y son iguales
# self.assertTupleEqual(a, b) -> a y b son tuplas y son iguales
# self.assertSetEqual(a, b) -> a y b son sets y son iguales
# self.assertDictEqual(a, b) -> a y b son diccionarios y son iguales
# self.assertItemsEqual(a, b) -> a y b tienen los mismos elementos
# self.assertDictContainsSubset(a, b) -> a es un subconjunto de b
# self.assertWarns(a, b) -> a genera una advertencia
# self.assertWarnsRegex(a, b, c) -> a genera una advertencia que coincide con b
# self.assertLogs(a, b) -> a genera logs
# self.assertRaises(a, b) -> a genera una excepción de tipo b
# self.assertRaisesRegex(a, b, c) -> a genera una excepción de tipo b que coincide con c

# Para más información, se puede consultar la documentación oficial de python:
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertEqual