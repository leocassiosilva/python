#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
sexo = input("Entre com o sexo (F - Feminino ou M - Masculino)")

if sexo == "F" or sexo == "f":
    print("Feminino")
else:
    if sexo == "M" or sexo == "m":
        print("Masculino")
    else: 
        print("Digito não condiz com as opções de sexos!")
