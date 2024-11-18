import unittest
from tema2.solucionario.sol_examen_ud2 import *

class TestingTest2(unittest.TestCase):
    def testNumLunas(self):
        self.assertEqual(numLunas("Tierra"), 1)
        self.assertEqual(numLunas("Marte"), 2)
        self.assertEqual(numLunas("Pluton"), 5)
        self.assertEqual(numLunas("Alderaan"), None)

    def testNumLunasPlanetas(self):
        planets = ["MERCURIO", "VENUS", "TIERRA", "ALDERAAN", "JUPITER", "MARTE", "SATURNO", "NEPTUNO", "PLUTON"]
        self.assertEqual(numLunasPlanetas(planets), "Mercurio: 0 Lunas, Venus: 0 Lunas, Tierra: 1 Lunas, Alderaan: no existe en el Sistema Solar, Jupiter: 79 Lunas, Marte: 2 Lunas, Saturno: 82 Lunas, Neptuno: 14 Lunas, Pluton: 5 Lunas")    
        self.assertEqual(numLunasPlanetas(["JUPITER", "MARTE", "SATURNO", "NEPTUNO"]), "Jupiter: 79 Lunas, Marte: 2 Lunas, Saturno: 82 Lunas, Neptuno: 14 Lunas")   

    def testArbolNavidad(self):
        self.assertEqual(arbolNavidad(6), "     *\n    ***\n   *****\n  *******\n *********\n***********\n    ***")
        self.assertEqual(arbolNavidad(3), "  *\n ***\n*****\n ***")
        self.assertEqual(arbolNavidad(1), None)
        self.assertEqual(arbolNavidad(0), None)

    def testCualificacion(self):
        self.assertEqual(cualificacion(10), "Matrícula de Honor")
        self.assertEqual(cualificacion(9.8), "Sobresaliente") 
        self.assertEqual(cualificacion(7), "Notable")   
        self.assertEqual(cualificacion(6.2), "Aprobado")  
        self.assertEqual(cualificacion(5), "Aprobado")    
        self.assertEqual(cualificacion(4.3), "Suspenso")  
        self.assertEqual(cualificacion(13), None)  
        self.assertEqual(cualificacion(-2), None)   

    def testCualificacionMaterias(self):
        materias = ["Matemáticas", "Física", "Química", "Inglés"]
        notas = [9.5, 7.2, 11, 8.9]
        notas2 = [9.5, 7.2, 8.9]
        self.assertEqual(cualificacionMaterias(materias, notas), ["Matemáticas: Sobresaliente", "Física: Notable", "Química: Nota incorrecta", "Inglés: Notable"])  
        self.assertEqual(cualificacionMaterias(materias, notas2), ["Error: Las listas no tienen la misma longitud"])
        self.assertEqual(cualificacionMaterias([], []), [])
        self.assertEqual(cualificacionMaterias(["1"], [1]), ["1: Suspenso"])
        self.assertEqual(cualificacionMaterias([], [1]), ["Error: Las listas no tienen la misma longitud"])

    def testSumaLista(self):
        self.assertEqual(sumaLista([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sumaLista([1, 2, 3, 4, 5, 6]), 21)
        self.assertEqual(sumaLista([1, 2, 3, 4, 5, 6, 7]), 28)
        self.assertEqual(sumaLista([1]), 1)
        self.assertEqual(sumaLista([]), 0)
        self.assertNotEqual(sumaLista([1, 2, 3, 4, 5]), 10)

    def testBuscarElemento(self):
        self.assertEqual(buscarElemento([1, 2, 3, 4, 5], 3), True)
        self.assertEqual(buscarElemento([1, 2, 3, 4, 5], 6), False)
        self.assertEqual(buscarElemento([1, 2, 3, 4, 5], 1), True)
        self.assertEqual(buscarElemento([1, 2, 3, 4, 5], 5), True)
        self.assertNotEqual(buscarElemento([1, 2, 3, 4, 5], 6), True)
        self.assertNotEqual(buscarElemento([1, 2, 3, 4, 5], 1), False)
        self.assertNotEqual(buscarElemento([1, 2, 3, 4, 5], 5), False)


if __name__ == '__main__':
    unittest.main()
