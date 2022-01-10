#Programa que permita a entrada de valores numéricos
#pergunta quantos valores quer
#entrada.numericos.py

quant = int(input('Quantos valores? '))
valores = []

for i in range(quant):
    msg = 'Digite um valor {}: '.format(i + 1)
    valor = float(input(msg))
    valores.append(valor)

print(valores)
    
#mostrar o maior valor:

maior = valores[0]
for valor in valores:
    if (valor > maior):
        maior = valor

print('O maior valor é: ', maior)

#mostrar o menor valor da lista

menor = valores[0]
for valor in valores:
    if (valor < menor):
        menor = valor

print('O menor valor é: ', menor)

#mostrar a média

total = 0
for valor in valores:
    total = total + valor

print('Media = ', total / len(valores))
