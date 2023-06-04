from VNuevos import Nuevo
from VUsados import Usado
from Lista import Lista
from Nodos import Nodo

import unittest
class TestLista(unittest.TestCase):
    __lista: Lista

    def setUp(self) -> None:
        
        v = Nuevo('Nuevo','Toyota','Corolla',4,'blanco',20000000,'full')
        nodo = Nodo(v)
        self.__lista = Lista()
    def test_AgregarVehiculoOK(self):
        vehiculo = Usado('Usado', 'Ford', 'Focus', 4, 'Azul', 800000, 'AB-123-CD', 2017, 50000)
        self.__lista.agregarVehiculo(vehiculo)
        # Verificar que el vehículo se agregó correctamente
        self.assertEqual(self.__lista.getTope(), 1)  # Verificar el tamaño de la lista
        self.assertEqual(self.__lista.getComienzo().getvehiculo(), vehiculo)  # Verificar el primer vehículo de la lista
        self.assertNotEqual(self.__lista.getComienzo(),None) #Verificar si la lista no esta vacia
        #self.assertIsNotNone(self.__lista) #Verifica que la lista es no vacia. Conviene en caso que sea una lista del tipo: []
    def test_InsertarVehiculoPrincipioOK(self):
        vehiculo = Usado('Usado','Fiat','Argos',4,'Rojo',1000000,'AE-321-CD',2019,100000)
        v = Nuevo('Nuevo','Toyota','Corolla',4,'blanco',20000000,'full')
        self.__lista.agregarVehiculo(v)
        #self.assertEqual(self.__lista.getComienzo(),None) #Verifica que la lista esta vacia
        self.__lista.insertarVehiculo(vehiculo,0)
        self.assertNotEqual(self.__lista.getComienzo(),None) #Verificar si la lista no esta vacia
    def test_InsertarVehiculoIntermedioOK(self):
        vehiculo = Usado('Usado','Fiat','Argos',4,'Rojo',1000000,'AE-321-CD',2019,100000)
        v = Nuevo('Nuevo','Toyota','Corolla',4,'blanco',20000000,'full')
        v1 = Usado('Usado', 'Ford', 'Focus', 4, 'Azul', 800000, 'AB-123-CD', 2017, 50000)
        self.__lista.agregarVehiculo(v)
        self.__lista.agregarVehiculo(vehiculo)
        self.__lista.insertarVehiculo(v1,1) #Inserta al vehiculo en la posicion 1
        nodo = self.__lista.buscarnodo(1) #Busca el nodo que se encuentra en la posicion 1
        self.assertEqual(v1,nodo.getvehiculo()) # Verifica que el nodo esta en la posicion donde se lo inserto
        self.assertNotEqual(self.__lista.getComienzo(),None) #Verificar si la lista no esta vacia
    def test_InsertarVehiculoFinalOK(self):
        vehiculo = Usado('Usado','Fiat','Argos',4,'Rojo',1000000,'AE-321-CD',2019,100000)
        v = Nuevo('Nuevo','Toyota','Corolla',4,'blanco',20000000,'full')
        v1 = Usado('Usado', 'Ford', 'Focus', 4, 'Azul', 800000, 'AB-123-CD', 2017, 50000)
        v2 = Nuevo('Nuevo','Fiat','Cronos',4,'Azul',90000000,'base')
        self.__lista.agregarVehiculo(v)
        self.__lista.agregarVehiculo(vehiculo)
        self.__lista.agregarVehiculo(v1)
        tope = self.__lista.getTope()
        self.__lista.insertarVehiculo(v2,tope)
        self.assertNotEqual(self.__lista.getComienzo(),None) #Verificar si la lista no esta vacia
    def test_Patente(self):
        vehiculo = Usado('Usado','Fiat','Argos',4,'Rojo',1000000,'AE-321-CD',2019,100000)
        v1 = Usado('Usado', 'Ford', 'Focus', 4, 'Azul', 800000, 'AB-123-CD', 2017, 50000)
        self.__lista.agregarVehiculo(vehiculo)
        self.__lista.agregarVehiculo(v1)
        self.__lista.buscarXpatente()


if __name__ == '__main__':
    unittest.main()
