class nodo:
    dato: str
    siguiente: 'nodo'
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
    ##user
class nodoarbol:
    dato: str
    izq: 'nodoarbol'
    der: 'nodoarbol'
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None
    
    
    
#
#
# Implementacion de los metodos raiz de las estructuras
#
#

###################################################                HISTORIAL DE BUSQUEDAS
class Pila:# clase pila funcionando correctamente
    tope: 'nodo'
    
    def __init__(self):
        self.tope = None
    def insertarPila(self, elemento):
        actual = nodo(elemento)
        if not self.tope:
            self.tope = actual
        else:
            actual.siguiente = self.tope
            self.tope = actual
    def sacarPila(self):
        eliminado = self.tope
        self.tope = eliminado.siguiente
        del(eliminado)
    def mostrarPila(self):
        actual = self.tope
        while actual:
            print(actual.dato)
            actual = actual.siguiente

#######################################                            PARA USUARIOS
class ArbolBinarioBusqueda():
    raiz : 'nodoarbol'
    def __init__(self):
        raiz = None
    def insertar(self, elemento):
        actual = nodoarbol(elemento)



pila = Pila()
while 1:
    print("1. Insertar")
    print("2. Eliminar")
    print("3. mostrar")
    x = int(input("Ingresando el caso"))
    
    match x:
        case 1:
            n = input("dato:")
            pila.insertarPila(n)
        case 2:
            pila.sacarPila()
        case 3:
            pila.mostrarPila()
    
            
        