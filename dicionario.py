#dicionário
#dicionários são indexados pro chaves (keys)
#chave : valor
#key : value
tel = {'joão' : 1234, 'maria' : 4567}
print(tel['joão'])

#altera
tel['joão']=3333
print(tel['joão'])

if 'joão' in tel:
    print('existe telefone do João')

if 'Beatriz' not in tel:
    print('não existe beatriz')

#retorna todas as chaves do dicionário
print('Retornando as chaves: ')
print(list(tel))

#apaga uma chave e seu valor:
del tel['joão']
print (tel)

