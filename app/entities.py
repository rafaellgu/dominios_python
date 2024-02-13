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
            
class Cupo():
    
    def __init__(self, letra):
        self.letra = letra
        
class Pago():
    
    def __init__(self, fecha_inicio, hora_inicio, fecha_fin, hora_fin, valor,carro,cupo):
        self.fecha_inicio = fecha_inicio
        self.hora_inicio = hora_inicio
        self.fecha_fin = fecha_fin
        self.hora_fin = hora_fin
        self.valor = valor
        self.carro = carro
        self.cupo = cupo
        