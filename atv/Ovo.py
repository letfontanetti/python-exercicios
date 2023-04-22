result = 0

tamanho = input("Informe o tamanho do ovo\nP - pequeno\nM - médio\nG - grande\nR: ")

if tamanho == "P" or tamanho == "M" or tamanho == "G":
    if tamanho == "P":
        vTamanho = 7.80
    elif tamanho == "M":
        vTamanho = 12.90
    elif tamanho == "G":
        vTamanho = 23.95

    sabor = int(input("Informe o sabor do ovo\n1-Chocolate preto\n2-Chocolate branco\n3-Chocolate ao leite\nR: "))

    if sabor == 1 or sabor == 2 or sabor == 3:
        if sabor == 1:
            vSabor = 9.67
        elif sabor == 2:
            vSabor = 4.50
        elif sabor == 3:
            vSabor = 9.32

        recheio = int(input("Informe o recheio do ovo\n1-Chocolate preto\n2-Chocolate branco\nR: "))

        if recheio == 1 or recheio == 2:
            if sabor == 1:
                vRecheio = 4.83
            elif sabor == 2:
                vRecheio = 2.25

            rDividido = int(input("Informe se o recheio vai ser dividido em dois:\n1-Sim\n2-Não\nR: "))

            if rDividido == 1:
                result = result + (vRecheio / 2)

            adicionais = int(input("Informe se vai querer adicionais:\n1-Sim\n2-Não\nR: "))

            if adicionais == 1:
                adicionais = int(input("Informe qual dos adicionais será escolhido:\n1-KitKat\n2-MM'S\nR: "))

            if adicionais == 1 or adicionais == 2:
                if adicionais == 1:
                    vAdicionais = 4.67
                elif adicionais == 2:
                    vAdicionais = 5.43

            presente = int(input("Informe se for presente:\n1-Sim\n2-Não\nR: "))

            if presente == 1:
                vPresente = 2.50

    else:
        print("Erro no sistema")

vTotal = result + (vTamanho + vSabor + rDividido + vRecheio + adicionais + vPresente)

print(vTotal)



