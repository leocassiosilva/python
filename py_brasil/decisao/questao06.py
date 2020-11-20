#Exemplo de Elif

categoria = int(input("Entre com a categoria"))

preco = 0

if categoria == 1:
    preco = 10
elif categoria == 2:
     preco = 18
elif categoria == 3:
     preco = 23
elif categoria == 4:
     preco = 26
elif categoria == 5:
    preco = 31

print("O valor do produto é %3.2f" %preco)
