#adivinhação
#atualizado no git

import random

def jogar():
    print('#################')
    print('Bem vindo ao jogo de adivinhação')
    print('#################')


    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

        
    numero_secreto = random.randrange(1,101)


    for tentativas in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'.format(tentativas, total_de_tentativas))
        
        chute = int(input('Digite um número entre 1 e 100: '))

        if (chute <1 or chute >100):
            print('Digite um número entre 1 e 100')
            continue

        if (chute == numero_secreto):
            print('Acertou!')
            break
        else:
            #abs => retorna o valor sem o sinal (sempre positivo)
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            if (chute > numero_secreto):
                print('Errou! Seu chute foi maior que o número secreto')
            else:
                print('Errou! Seu chute foi menor que o número secreto')
    print('##Fim do jogo##')
    print('O número secreto era {}'.format(numero_secreto))
    print('Você fez {} pontos'.format(pontos))

#permite executar automaticamente via linha de comando
if (__name__ -- '__main__'):
    jogar()
            
        



