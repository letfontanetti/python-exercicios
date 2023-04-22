import random
#random=gerar números aleatória

while True:
    num = int(input("Digite um número para treinar a tabuada: "))
    acertos = 0
    erros = 0
    for x in range(1, 11):
        resp = int(input(f"Qual é o resultado de {num} x {x}? "))
        if resp == num * x:
            print("CORRETO")
            acertos += 1
        else:
            print(f"QUE PENA, VOCÊ ERROU, O VALOR CORRETO É {num*x}")
            erros += 1
    print(f"Total de acertos: {acertos}")
    print(f"Total de erros: {erros}")
    opcao = input("Deseja começar de novo? (S/N)").lower()
    if opcao == "n":
        break
