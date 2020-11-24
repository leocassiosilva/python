total_geral = 0
i=1

while i<=3:
    qtd_acai = int(input("Entre com a quantidade de caçais vendidos: "))
    total = qtd_acai * 3.00
    print("Foram vendidos R$ %.2f de açaí. "%total)
    total_geral=total_geral+total
    i= i+1

    print("Foram vendidos R$ %.2f de açaí nos %d dias." %(total_geral, i-1))