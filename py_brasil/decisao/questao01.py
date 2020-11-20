#Faça um Programa que peça dois números e imprima o maior deles.
num1 = int(input("Entre com um numero"))

num2 = int(input("Entre com um outro numero"))

if num1 > num2:
    print("O numero %d maior que o numero %d" %(num1, num2))
else :
    print("O numero %d maior que o numero %d" %(num2, num1))