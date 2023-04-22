p1 = [4,5,7,8,2,9]
p2 = [6,2,4,6,8,10]

media_p1 = sum(p1) / len(p1)
media_p2 = sum(p2) / len(p2)

if media_p1 > media_p2:
    print("A turma teve melhor média na prova 1: %.2f" % media_p1)
elif media_p2 > media_p1:
    print("A turma teve melhor média na prova 2: %.2f" % media_p2)
else:
    print("A turma teve a mesma média nas duas provas: %.2f" % media_p1)