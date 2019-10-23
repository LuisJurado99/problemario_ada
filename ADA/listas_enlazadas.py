"""Listas
Una lista es una estructura de datos que contiene una secuencuia de elementosde cierto tipo 
las listas no son arreglos ya que las listas no tienen un tamaño fijo , un arreglo si; esta 
caracteristica las hace flexibles y muy atractivas de usar para diferentes soluciones de desarrollo
para mantener esta flexibilidad  de crecimiento es nesesario implementar una lista enlazada 
la cual permite crear objetos en memoria no secuencial "y recalco en memoria" de forma  logica
si lo deben ser

Listas enlazada

una lista enlazada  es una coleccion de objetos llamados nodos , en el cual cada
uno de ellos contiene un campo interno que apunta al siguiente elemento  lo cual
permitira un recorrido trsansversal sobre la estructura la imagen de una lista
ligada es la siguiente
existe un elemento head (cabeza) que indica el punto de entrada a la estructura,
el elemnto final de la misma es conocido como cola(tail) 
"""

class Nodo:
    def __init__(self,value, siguiente = None):
        self.data = value
        self.next = siguiente
#ADT Linked List #
class Linked_List:
    def __init__(self):
        self.head =None
        self.size =0

    def is_empty(self):
        return self.head==None

    def get_tamano(self):
        return self.size
    
    def get_tail(self):
        cur_node = self.head
        while cur_node.next != None:
            cur_node=cur_node.next     
        return cur_node
    
    def append(self, value):
        self.size+=1
        if self.is_empty():
            self.head=Nodo(value)        
        else:
            self.get_tail().next=Nodo(value)
    
    def transversal(self):
        cur_node = self.head
        while cur_node.next != None:
            print(cur_node.data,'->', end='')
            cur_node=cur_node.next
        print(cur_node.data)
    
    def pre_append(self, value): 
        self.head = Nodo(value, self.head)
        self.size+=1
    
    def borrar_nodo(self,value_reference):
        cur_node = self.head
        try:
            previo = None
            while cur_node.data != value_reference:
                previo = cur_node
                cur_node = cur_node.next
                pass
            previo.next = cur_node.next  
            
            self.size-=1
            pass
        except:
            print("Valor no valido")
            pass
        pass
    
    def pop(self):
        cur_node = self.head
        prev = None
        while cur_node.next!=None:
            prev = cur_node
            cur_node = cur_node.next
            pass
        prev.next = None 
    def add_before(self, reference_value, value):
        cur_node = self.head
        while cur_node.data != reference_value:
            prev = cur_node
            cur_node = cur_node.next
            pass
        prev.next = Nodo(value)
        prev.next.next = cur_node
        pass
    
    def find(self, value):
        cur_node = self.head
        while cur_node.data != value:
            cur_node=cur_node.next
        return cur_node
            
    def add_after(self, valor_referencia, valor):
        valor_referencia = self.find(valor_referencia)
        temp = valor_referencia.next
        valor_referencia.next = Nodo(valor)
        valor_referencia.next.next = temp
         
    pass
 
