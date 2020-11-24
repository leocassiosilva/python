ant = 0
prox =1
soma=0
for i in range(0, 10, 1):
    print("%d numero : [%d]" %(i, ant))
   
    soma=ant+prox
    ant=prox
    prox=soma