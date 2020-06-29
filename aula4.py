# for x in range (100): # de 0 a 99
#     print(x)
#
# for x in range(1,100): # de 1 a 99
#     print(x)
div=0
a = int(input('Digite um numero para validar se é primo'))
for x in range(1,a+1):
    resto = a%x
    if(resto==0):
        div += 1
if(div==2):
    print('Numero {} é primo' .format(a))
else:
    print('Numero {} não é primo'.format(a))

#quantos são primos dentro do  range
for num in range(1,101):
    div=0
    for x in range(1,num+1):
        resto = num%x
        if(resto==0):
            div += 1
    if(div==2):
        print('Numero {} é primo' .format(num))

lop=0
while  lop <=10:
    print('loop')
    lop+=1


