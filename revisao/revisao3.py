while True:
    var = input("Você gosta de Python?\n")
    var = var.upper()
    if var == "SIM":
        print("Resposta correta!")
        break
    else:
        print("Essa não é a resposta correta, tente novamente")