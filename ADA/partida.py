from vida import SoporteVida


class Juego:

    def __init__( self, rows, cols ):
        self.__tablero = SoporteVida( rows, cols )
        self.__contador = 1

    def configure( self, inicial, generaciones ):
        self.__tablero.configure( inicial, generaciones )

    def to_string( self ):
        self.__tablero.to_string()
    
    def get_gens( self ):
        return self.__tablero.get_gens()


    def reglas( self, row, col ):
        vecinos = self.__tablero.get_alive_neighbors( row, col )
        if( self.__tablero.is_alive_cell( row, col )):
            if( vecinos == 2 or vecinos == 3):
                return True
            else:
                return False
        else:
            if( vecinos == 3):
                return True
            else:
                return False
    def checarReglas( self ):
        nuevaConfig = []
        for i in range( self.__tablero.get_num_rows() ):
            for j in range( self.__tablero.get_num_cols() ):
                if(self.reglas( i, j )):
                    tupla = [i, j]
                    nuevaConfig.append(tupla)
        return nuevaConfig

    def iterarGeneracion( self ):
        if( self.__tablero.get_gens() > 1):
            self.__contador += 1
            arregloNuevaGen = self.checarReglas()
            self.__tablero.set_gens( self.__tablero.get_gens() -1 )
            self.__tablero.configure( arregloNuevaGen,  self.__tablero.get_gens())
            print(f"-------- {self.__contador}° Generación --------")
            self.to_string()
            self.iterarGeneracion()

if __name__ == "__main__":
    randomtemp= []
    while(True):
        tamaño= int(input("Un tamaño mínimo de 4.\nTamaño del tablero: "))
        if(tamaño>=4):
            break
    part1 = Juego( tamaño, tamaño )
    generacinones= int(input("¿Cuantas generaciones?"))
    part1.configure( [[1,2],[2,1],[2,2],[2,3]], generacinones )
    print("-------- 1° Generación --------")
    part1.to_string()
    part1.iterarGeneracion()
    pass