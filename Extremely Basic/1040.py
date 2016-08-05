n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10.0

if media >= 7.0:
    print("Media: %.1f\nAluno aprovado." %media)
elif media < 5.0:
    print("Media: %.1f\nAluno reprovado." %media)
else:
    print("Media: %.1f\nAluno em exame." %media)
    #recuperacao = float(input("Nota do exame: "))
    recuperacao = float(input())
    print("Nota do exame: %.1f" %recuperacao)

    media = (media + recuperacao) / 2.0
    if media >= 5.0:
        print("Aluno aprovado.\nMedia final: %.1f" %media)
    else:
        print("Aluno reprovado.\nMedia final: %.1f" %media)
