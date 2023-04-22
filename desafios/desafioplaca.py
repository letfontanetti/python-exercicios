y = int(input("Informe a altura : "))
x = int(input("Informe a largura : "))
m = int(input("Informe a quantidade de peças : "))
i = 1

while i <= m:
    yi=int(input("\nQual a altura da peça do cliente: "))
    xi=int(input("\nQual a largura da peça do cliente: "))
    if xi > x or xi >y or yi > x or yi > y:
        print("\n Não temos espaço na placa")
    else:
        print("\n Temos espaço na placa")
    i = i + 1