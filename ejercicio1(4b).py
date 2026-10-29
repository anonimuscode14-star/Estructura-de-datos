class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.apuntador = None
        
class lista_enlazadas:

    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo = nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo
            return 
        actual = self.cabeza

        while actual.apuntador is not None:
             actual = actual.apuntador
        actual.apuntador = nuevo

    def imprimir(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.dato)
            actual = actual.apuntador
        print("Fin del nodo")

#Se imprimira el programa principal

mi_lista = lista_enlazadas()

# Creamos la lista vacia

mi_lista.insertar(10)
mi_lista.insertar(20)
mi_lista.insertar(30)
mi_lista.imprimir()
        