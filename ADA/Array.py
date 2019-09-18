class Array:
    def __init__(self, size):
        self.__size = size
        self.__data = []
        for index in range(size):
            self.__data.append(None)
            pass
        pass
    def length(self):
        return self.__size
    def get_item(self,index):
        return self.__data[index]
    def set_item(self,index,valor):
        if index >=0 and index<self.__size:
            self.__data[index]=valor    
            pass
        else:
            print('Todo mal')
            pass
        
    def clearing(self, valor):
        self.__data=valor
        pass
    def to_String(self):
        print(self.__data)
        pass
class Array2D:
    def __init__(self, rows, cols):
        self.__rows = rows
        self.__cols = cols
        self.__data = []
        for r in range(self.__rows):
            pass
            for c in range(self.__cols):
                pass
        pass
    def get_num_rows(self,asd):
        pass
    pass    
if __name__ == "__main__":
    #adt = Array(10)
    #adt.to_String()
    #print(f"El tamaño del arreglo es {adt.length()}")
    #adt.set_item(4,34)
    #adt.to_String()
    #print(f"El elemento 4 es: {adt.get_item(4)}")
    #adt.clearing(0)
    #adt.to_String()
    #adt.set_item(14,50)
    pass
    
