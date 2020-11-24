#Desenvolva um programa que imprima os 100 primeiros números da sequência de Fibonacci na tela. [0,1,1,2,3,5,8,13,21,34...]

ant = 0
prox =1
soma=0
for i in range(0, 10, 1):
    print("%d numero : [%d]" %(i, ant))
   
    soma=ant+prox
    ant=prox
    prox=soma
