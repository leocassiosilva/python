total_geral = 0
for i in range(1, 4):
    qtd_acai = int(input("Entre com a quantidade de açais vendidos %d dia(s) atrás: " %i))
    total = qtd_acai * 3.00
    print("Foram vendidos R$ %.2f de acai. " %total)
total_geral=total_geral+total


print("Foram vendidos R$ %.2f de açai nos %d dias." %(total_geral, i))