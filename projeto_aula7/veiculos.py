#veiculos.py

#classe mãe ou superclasse (classe genérica)
class Veiculo:
    def __init__(self, marca, modelo, placa, ano):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    def ligar(self):
        print('Veículo ligado')

    def abastecer(self):
        print('Veículo abastecendo')

    #função builtin
    def __str__(self):
        return f'{self.marca} {self.modelo}'

#classe filha ou subclasse (classe especializada)
class Carro(Veiculo):
    def ligar(self):
        print('Carro ligado')
    def abastecer(self):
        print('Carro abastecendo')

class Motocicleta(Veiculo):

    def __init__(self, marca, modelo, placa, ano, cilindrada):
        #chama a super classe
        super().__init__(marca, modelo, placa, ano)
        self.cilindrada = cilindrada

class Aviao(Veiculo):

    def ligar(self):

        print('Avião ligado')
    def abastecer(self):
        print('Avião abastecendo')
    def decolar(self):
        print('Avião decolando')
    def pousar(self):
        print('Avião pousando')


