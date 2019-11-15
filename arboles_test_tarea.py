from arboles_binarios import NodoArbol

def main():
    root = NodoArbol('10', NodoArbol('20', NodoArbol('30',None,NodoArbol('40',NodoArbol('50'),NodoArbol('60',None,NodoArbol('70',NodoArbol('80')))))))

    print(root.left.left.right.right.right.left.data)                         
                             

main()
