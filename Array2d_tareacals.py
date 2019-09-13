class Array2D:
    def  __init__ ( self , rows , cols ):
        self.__rows = rows
        self.__cols = cols
        self.__data = []
        for r in range( self.__rows):
            tmp = []
            for c in range( self.__cols):
                tmp.append(None)
            self.__data.append(tmp)

    def get_num_rows( self ):
        return self.__rows

    def get_num_cols( self):
        return self.__cols

    def clearing( self , value):
        for r in range(self.__rows):
            for c in range(self.__cols):
                self.__data[r][c] = value
                
    def set_item( self , r , c , value):
        self.__data[r][c]= value

    def get_item( self , r , c ):
        return self.__data[r][c]
          

    def to_string(self):
        print(self.__data)

def main():

    archivo_calificaciones=open('calificaciones.txt')
    datos=archivo_calificaciones.readlines()
    #print(datos)
    arraycal=[]
    for l in datos:
        arraycal.append(l.split(','))
    #print(arraycal)
        
    a2d=Array2D(4, 3)
    a2d.set_item( 0 , 0 , arraycal[0][1])
    a2d.set_item( 0 , 1 , arraycal[0][2])
    a2d.set_item( 0 , 2 , arraycal[0][3])
    a2d.set_item( 1 , 0 , arraycal[1][1])
    a2d.set_item( 1 , 1 , arraycal[1][2])
    a2d.set_item( 1 , 2 , arraycal[1][3])
    a2d.set_item( 2 , 0 , arraycal[2][1])
    a2d.set_item( 2 , 1 , arraycal[2][2])
    a2d.set_item( 2 , 2 , arraycal[2][3])
    a2d.set_item( 3 , 0 , arraycal[3][1])
    a2d.set_item( 3 , 1 , arraycal[3][2])
    a2d.set_item( 3 , 2 , arraycal[3][3])
    a2d.to_string()
    
    """
    a2d=Array2D( 2, 3)
    a2d.to_string()
    a2d.clearing(0)
    a2d.to_string()
    a2d.set_item( 0 , 0 , 10)
    a2d.set_item( 0 , 1 , 9)
    a2d.set_item( 0 , 2 , 8)
    a2d.set_item( 1 , 0 , 7)
    a2d.set_item( 1 , 1 , 6)
    a2d.set_item( 1 , 2 , 9)
    a2d.to_string()
    print (f"Christian sacó en español { a2d.get_item(1,1)}")
    """
    
main()
