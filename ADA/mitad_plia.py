def mitad_pila(lista, index=0):
    mitad = len(lista)//2
    if index<len(lista):
        if index != mitad:
            index+=1
            h = mitad_pila(lista,index)
            return h
        else:
            lista.remove(lista[index])
            return lista
def borrar(lista, borrar):
    
    pass

if __name__ == "__main__":
    print("[2,4,8,10,12,14]")
    print(mitad_pila([1,1,1,1,1]))
    pass