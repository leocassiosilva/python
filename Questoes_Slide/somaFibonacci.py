#Desenvolva um programa que imprima o 25º número da sequência de Fibonacci na tela
ant = 0
prox =1
soma=0
n = 6
for i in range(0, n, 1):
   
    soma=ant+prox
    ant=prox
    prox=soma

 
 
print("Soma: %d " %soma)