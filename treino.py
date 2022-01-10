#A: 3 produtos;
#1-qual tem menor preço?;
#2-qual tem maior preço?;
#3-qual o valor dos produtos?;
#4-qual o preço médio dos produtos?

a = 1
b = 2
c = 3

if (a < b and a < c):
    print('produto a é menor')
elif (b < c):
    print('produto b é menor')
else:
    print('produto c é menor')

if (a > b and a > c):
    print('produto a é maior')
elif(b > c):
    print('produto b é maior')
else:
    print('produto c é maior')

total = a + b + c
print('Total= ', total)

media = total/3
print('Média = ', media)




    

    
    

