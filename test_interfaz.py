import unittest
from Interfaz import Interfaz
from parameterized import parameterized
from Interfaz import Interfaz


class TestInterface(unittest.TestCase):

    def test_Interface_valores(self): 

        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor("a", 1 , "*"))   
    
    def test_Interface_valores_1(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor("w", 6 , "!"))
    
    def test_Interface_valores_2(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor(".", "?" , "!"))
    
    def test_Interface_3(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor(9, 4 , "!"))

    def test_Interface_valores_4(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor(7, 4 , "a"))

    def test_Interface_valores_ch(self):
        
        usuario = Interfaz()
        usuario.tamaño = 4
        self.assertFalse(usuario.ingresa_valor(3, 4 , "+"))
    
    def test_Interface_valores_ch_1(self):
        
        usuario = Interfaz()
        usuario.tamaño = 4
        self.assertFalse(usuario.ingresa_valor(7, "%", "$"))

    def test_Interface_valores_correctos_9x9(self):
        
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertTrue(usuario.ingresa_valor(7, 4 , 5))
    
    def test_Interface_valores_correctos_4x4(self):
        
        usuario = Interfaz()
        usuario.tamaño = 4
        self.assertTrue(usuario.ingresa_valor(1, 3 , 4))

   
    def test_numero_mayor_9x9(self):
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertFalse(usuario.ingresa_valor(2, 2, 10)) #FILA-2 ; COLUMNA-2 ; Nº 10 error

    def test_numero_mayor_4x4(self):
        usuario = Interfaz()
        usuario.tamaño = 4    
        self.assertFalse(usuario.ingresa_valor(1, 1, 5)) #FILA-1 ; COLUMNA-1 ; Nº 5 error
        

    @parameterized.expand([
        (1,0,1),
        (2,0,1),
        (3,0,1),
        (4,0,1),
        (5,0,1),
        (6,0,1),
        (7,0,1),
        (8,0,1),
        (9,0,1) ])
    def test_ingresa_valor_correcto_9x9(self,numero,x,y): #NUMEROS DE 1 A 9
        usuario = Interfaz()
        usuario.tamaño = 9
        self.assertTrue(usuario.ingresa_valor(numero,x,y))

    @parameterized.expand([
        (1,0,1),
        (2,0,1),
        (3,0,1),
        (4,0,1)])
    def test_ingresa_valor_correcto_4x4(self,numero,x,y): #NUMEROS DE 1 A 4
        usuario = Interfaz()
        usuario.tamaño = 4
        self.assertTrue(usuario.ingresa_valor(numero,x,y))

if __name__ == '__main__':
    unittest.main()