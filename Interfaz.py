from api import api
from Sudoku import Sudoku 

class Interfaz():

    def ingresar_dimension(self):
        self.tamaño = 0

        #Para ingresear la dimension del tablero
        while self.tamaño !="9" and self.tamaño != "4":
            self.tamaño = input("Ingrese el tamaño del tablero (4/9)\n")
            if self.tamaño !="9" and self.tamaño != "4":
                print ("Ingrese el tamaño del tablero nuevamente\n")

        self.tamaño = int(self.tamaño)      
        self.tablero= api (int(self.tamaño))
        self.game = Sudoku(self.tablero)

    def ingresar_coordenadas(self,fila,columna,valor):  #verifica que si ingresa el valor de la fila, columna y valor  

        if (fila > 0 and fila <= self.tamaño and columna > 0 and columna <= self.tamaño 
        and valor > 0 and valor <= self.tamaño):
            return True
        else:
            return False
        
    def ingresa_valor(self,numero,x,y): 
        try:
            if int(x) > self.tamaño:
                return False
            elif int(y) > self.tamaño:
                return False
            elif numero != "x":
                if int(numero) > 0 and int(numero) < self.tamaño+1:
                    return True
            return True
        except Exception as w: 
            print(w)
            return False
            

    def pedir_valores(self):   #Ingresa los valores el jugador 
        self.numero = input("Ingrese un numero\n")
        self.fila = input("Ingrese Fila\n")
        self.columna = input("Ingrese Columna\n")

        print ("")
          
        
    def jugar(self):    #FUNCION PARA JUGAR 
        print("\n\n         BIENVENIDO AL SUDOKU        \n\n")
        self.ingresar_dimension()    
        print("")   
        print(self.game.imprimir_tablero())

        while not self.game.gano():
            self.pedir_valores()
            if self.ingresa_valor(self.fila,self.columna,self.numero):
                self.game.ingresar_numero(int(self.fila)-1, int(self.columna)-1,self.numero)
                print(self.game.imprimir_tablero())
            else:
                print("INGRESE UN VALOR CORRECTO")



if __name__ == '__main__':    
    game = Interfaz()
    game.jugar()