class Carro():
        
    #metodo costructor
    def __init__(self, placa , tipo_vehiculo):
        self.placa = placa
        self.tipo_vehiculo = tipo_vehiculo

        
class Cliente():
    
    #metodo costructor
    def __init__(self,nombre , documento , licencia_conduccion , celular , lista_carros):
        self.nombre = nombre
        self.documento = documento
        self.licencia_conduccion = licencia_conduccion
        self.celular = celular
        self.lista_carros = lista_carros
        
    def addCar(self, car):
        self.lista_carros.append(car)
        
    def lisCar(self):
        for i in self.lista_carros:
            print("carro con placas:" + i.placa)