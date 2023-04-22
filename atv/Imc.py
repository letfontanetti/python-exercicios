p = float(input("Informe o peso: "))
a = float(input("Informe a altura: "))

result = p / (a*a)

print ("Seu IMC é: ")

if result < 18.5:
    print("magro")
elif result >= 18.5 and result <= 24.9:
    print("normal")
elif result >= 25 and result <= 29.9:
    print("sobrepeso")
elif result >= 30 and result <= 34.9:
    print("obesidade grau 1")
elif result >= 35 and result <= 39.9:
    print("obesidade grau 2")
else:
    print("obesidade grau 3")
