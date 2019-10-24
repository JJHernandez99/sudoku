import unittest
from Interfaz import Interfaz

class TestInterface(unittest.TestCase):

    def test_Interface_(self): 

        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor("a", 1 , "*"))   
    
    def test_Interface_1(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor("w", 6 , "!"))
    
    def test_Interface_2(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor(".", "?" , "!"))
    
    def test_Interface_3(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor(0, 4 , "!"))

    def test_Interface_4(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor(7, 4 , "a"))

    def test_Interface_5(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor(6, 4 , "+"))
    
    def test_Interface_6(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor(7, "%", "$"))

    def test_Interface_7(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertTrue(usuario.ingresa_valor(7, 4 , 5))
    
if __name__ == '__main__':    
    unittest.main()