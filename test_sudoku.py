import unittest
from Sudoku import Sudoku

class TestSudoku(unittest.TestCase):


    def test_Sudoku_Fila_1(self):
        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])
        self.assertFalse(sudoku.ingresar_numero(0,2,5))
    
    def test_Sudoku_Fila_2(self):
        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])
        self.assertFalse(sudoku.ingresar_numero(6,4,6))
    
    def test_Sudoku_Columna_1(self):
        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])
        self.assertFalse(sudoku.ingresar_numero(8,0,5))
    
    def test_Sudoku_Columna_2(self):
        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])
        self.assertFalse(sudoku.ingresar_numero(0,8,9))

    def test_Sudoku_Zona(self):
        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])
        self.assertFalse(sudoku.ingresar_numero(2,2,5))

    def test_Sudoku_Valores_Fijos(self):
        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])
        self.assertFalse(sudoku.ingresar_numero(0,0,1))

    def test_Sudoku_Perdio(self):
        sudoku = Sudoku([["5", "3", "x", "x", "7", "x", "x", "x", "x"],
                         ["6", "x", "x", "1", "9", "5", "x", "x", "x"],
                         ["x", "9", "8", "x", "x", "x", "x", "6", "x"],
                         ["8", "x", "x", "x", "6", "x", "x", "x", "3"],
                         ["4", "x", "x", "8", "x", "3", "x", "x", "1"],
                         ["7", "x", "x", "x", "2", "x", "x", "x", "6"],
                         ["x", "6", "x", "x", "x", "x", "2", "8", "x"],
                         ["x", "3", "x", "4", "1", "9", "x", "x", "5"],
                         ["x", "x", "x", "x", "8", "x", "x", "7", "9"]])
        self.assertFalse(sudoku.gano())   
    
    def test_Sudoku_Gano(self):
        sudoku = Sudoku([["4", "1", "3", "8", "2", "5", "6", "7", "9"],
                         ["5", "6", "7", "1", "4", "9", "8", "3", "2"],
                         ["2", "8", "9", "7", "3", "6", "1", "4", "5"],
                         ["1", "9", "5", "4", "6", "2", "7", "8", "3"],
                         ["7", "2", "6", "9", "8", "3", "5", "1", "4"],
                         ["3", "4", "8", "5", "1", "7", "2", "9", "6"],
                         ["8", "5", "1", "6", "9", "4", "3", "2", "7"],
                         ["9", "7", "2", "3", "5", "8", "4", "6", "1"],
                         ["6", "3", "4", "2", "7", "1", "9", "5", "8"]])
        self.assertTrue(sudoku.gano())    

    def test_Sudoku_Fila_3(self):
        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])
        self.assertFalse(sudoku.ingresar_numero(0,3,4))
    
    def test_Sudoku_Fila_4(self):
        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])
        self.assertFalse(sudoku.ingresar_numero(0,3,1))

    def test_Sudoku_Columna_3(self):
        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])
        self.assertFalse(sudoku.ingresar_numero(1,0,4))
    
    def test_Sudoku_columna_4(self):
        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])
        self.assertFalse(sudoku.ingresar_numero(0,3,3))
    
    def test_Sudoku_Zona_ch(self):
        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])
        self.assertFalse(sudoku.ingresar_numero(0,1,1))

    def test_Sudoku_Valor_Fijo_ch(self):
        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])
        self.assertFalse(sudoku.ingresar_numero(1,0,1))
    
    def test_Sudoku_Perdio_ch(self):
        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])
        self.assertFalse(sudoku.gano())

    def test_Sudoku_Gano_ch(self):
        sudoku = Sudoku([["4", "3", "2", "1"],
                         ["2", "1", "3", "4"],
                         ["3", "4", "1", "2"],
                         ["1", "2", "4", "3"]])
        self.assertTrue(sudoku.gano())
    def test_Sudoku_Zona_c(self):
        sudoku = Sudoku([["4", "x", "x", "1"],
                         ["x", "1", "3", "x"],
                         ["x", "4", "1", "x"],
                         ["1", "x", "x", "3"]])
        self.assertTrue(sudoku.ingresar_numero(0,1,3))

if __name__ == '__main__':    
    unittest.main()