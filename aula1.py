Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Olá, Mundo!')
Olá, Mundo!
>>> print('Soma=', 1+2)
Soma= 3
>>> print('Subtração=', 4-3)
Subtração= 1
>>> print('=', 4-3)
= 1
>>> print('Multiplicação=', 3*4)
Multiplicação= 12
>>> print('Divisão=',4/3)
Divisão= 1.3333333333333333
>>> print('Divisão inteira=',4//3)
Divisão inteira= 1
>>> print('Divisão inteira=',4//3)
Divisão inteira= 1
>>> print('Resto=',9%2)
Resto= 1
>>> print('Resto=',8%2)
Resto= 0
>>> print('Resto=',7%2)
Resto= 1
>>> print('Resto=',6%2)
Resto= 0
>>> print('Resto=',5%2)
Resto= 1
>>> print('Resto=',4%2)
Resto= 0
>>> print('Resto=',3%2)
Resto= 1
>>> print('Resto=',2%2)
Resto= 0
>>> print('Resto=',1%2)
Resto= 1
>>> print('Resto=',0%2)
Resto= 0
>>> print('Resto=',11%3)
Resto= 2
>>> print('Potência=',2**3)
Potência= 8
>>> import math
>>> print('Potência:'math.pow(2,3))
SyntaxError: invalid syntax
>>> print('Potência:', math.pow(2,3))
Potência: 8.0
>>> print('Raiz:', math.sqrt(9))
Raiz: 3.0
>>> print('PI:', math.pi)
PI: 3.141592653589793
>>> #operadores relacionais
>>> print ('Menor=', 4<5)
Menor= True
>>> print ('Maior=', 5>4)
Maior= True
>>> print ('Menor ou igual=', 6<=6)
Menor ou igual= True
>>> print ('Menor ou igual=', 4<=6)
Menor ou igual= True
>>> print ('Maior ou igual=', 7>=5)
Maior ou igual= True
>>> a+1
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a+1
NameError: name 'a' is not defined
>>> a=1
>>> a=1
>>> a
1
>>> a=5
>>> a
5
>>> print('Igualdade=','uva'=='uva')
Igualdade= True
>>> print('Igualdade=','uva'=='Uva')
Igualdade= False
>>> a=1
>>> b=1
>>> print(a==b)
True
#Formatação de strings
%s=significa string = 'texto 123' ou "texto 123"
%d=número inteiro (sem parte decimal) = 123
%f=número flutuante (com parte decimal)=123.0
%.2 f=flutuante com 2 casas decimais=123.00

preco=1.990
#Preço do produto: R$ 1.99
#Texto formatado
print('\n%s=%.2f\n%s=%d kg'% ('Preço do produto', preco,'Quantidade',3))
      
