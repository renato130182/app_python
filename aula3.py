a = int(input("Primeiro valor: \n"))
b = int(input("Segundo valor: \n"))

if(a>b and b<a):
    print("Primeiro valor é maior: {maior}".format(maior=a))
elif(b>a or a!=b):
    print("Segundo valor é maior {maior}" .format(maior=b))
else:
    print("São iguais {} e {}".format(a,b))

if not a > 5:
    print('A é menor ou igual a 5')