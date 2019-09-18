from Array2d import Array2D
##
#Del tipo Zero-Player
#Creado por John H Conway (1970) 
#Ejemplifica, el ascenso, caida y alternancia de los seres vivos
#Reglas:
# 1. Si una celula esta viva y tiene 2 o 3 vecinos vivos, la celula sobrevive a la sig generación. Los vecinos
# son las 8 celulas que la rodean inmediatamente, tanto en vertical, horizontal y diagonal.
# 2. Una celula que no tiene vecinos vivos o que tiene un solo vecino vivo, morire por soledad para la sig generación.
# 3. Una celula viva que tiene 4 o mas vecinos vivos muere por sobre población para la sig generacion.
# 4. Una celula muerta con exactamente 3 vecinos vivos resulta en un nacimiento cuya vida empezará la sig generación.
# todas las celulas muertas restantes se mantienen muertas la siguiente generación  
# #
class SoporteVida :
    def __init__(self, rows, cols):
        self.__rows=rows
        self.__cols = cols
        self.__grid = Array2D(rows,cols)
        self.__grid.clearing(0)
        
        pass
    def get_num_rows(self):
        return self.__rows
    def get_num_cols(self):
        return self.__cols
    def to_String(self):
        self.__grid.to_string()
        pass
    def configure(self,inicial, generacion):
        self.__gens = generacion
        
        for celula in inicial:
            self.__grid.set_item(celula[0], celula[1], 1)
            pass
        pass
    pass
    def clear_cell(self, row, col):
        self.__grid.set_item(row,col,0)
        pass
    def set_cell(self, row,col):
        self.__grid.set_item(row,col,1)
        pass
    def is_alive_cell(self, row, col):
        return self.__grid.get_item(row,col) ==1
    def get_alive_neighbors(self, row, col):
        limites= self.__calcula_vecinos(row,col)
        vivos=0
        for r in range(limites[2], limites[3]+1,1):
            for c in range(limites[0], limites[1],1):
                if self.__grid.get_item(r,c) ==1:
                    vivos+= 1
                    
                    pass
                pass
            pass
        return vivos
    def __calcula_vecinos(self, ren, col):
        
        x_ini = col-1
        x_fin = col+1 
        y_ini = ren-1
        y_fin = ren+1
        if col==0:
            x_ini = 0
        if col ==self.__cols-1:
            x_fin = self.__cols-1
        if ren==0:
            y_ini=0
            pass
        if ren==self.__rows - 1:
            y_fin =self.__rows-1
            pass
        return [x_ini,x_fin,y_ini,y_fin]
if __name__ == "__main__":
    juego = SoporteVida(5,5)
    juego.to_String()
    juego.configure([[1,2],[2,1],[2,2],[2,3]],5)
    juego.to_String()
    print(juego.get_alive_neighbors(2,2))