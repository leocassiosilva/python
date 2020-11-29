def exibirMenu():
    print("****MENU****\n")
    print("0 - SAIR\n")
    print("1 - SOMAR\n")
    opcao = int(input("Entre com um numero: "))
    return opcao

def somar(num1, num2):
    resultado = num1+num2
    return resultado

i=0
opcao=1
num1 =0
num2 =0

resultado=0

while opcao!= 0:
    opcao = exibirMenu()
    if opcao <=0:
        break
    num1 = float(input("Informe o primeiro numero: "))
    num2 = float(input("Informe o segundo numero: "))
    if opcao == 1:
        resultado = somar(num1, num2)
    print("Resultado: %f\n\n " %resultado)