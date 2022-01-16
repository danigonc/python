from veiculos import Veiculo, Carro, Motocicleta, Aviao


veiculo = Veiculo('Ford', 'Fiesta', 'ABC-1234', 2015)
carro = Carro('VW', 'Polo', 'DEF-4567', 2018)
moto = Motocicleta('Honda', 'CG', 'MMM-4567', 2021, 600)
aviao = Aviao('A', 'B', 'C', 2020)

veiculo.ligar()
veiculo.abastecer()

carro.ligar()
carro.abastecer()

moto.ligar()
moto.abastecer()

aviao.ligar()
aviao.abastecer()
aviao.decolar()
aviao.pousar()

print(carro)

lista = [veiculo, carro, moto, aviao, 123, 5.0]

for item in lista:
    if(isinstance(item, Carro)):
       print('É um carro')

    elif (isinstance(item, Motocicleta)):
        print('É uma moto')

    elif (isinstance(item, Aviao)):
        print('É um avião')

    elif (isinstance(item, Veiculo)):
        print('É um veículo')

    elif (isinstance(item, int)):
        print('É um int')

    else:
       print('Tipo desconhecido')



