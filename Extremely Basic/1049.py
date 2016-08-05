filo = input()
classe = input()
ordem = input()

if filo == 'vertebrado':
    if classe == 'ave':
        if ordem == 'carnivoro':
            print("aguia")
        else:
            print("pomba")
    else:
        if ordem == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if classe == "inseto":
        if ordem == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if ordem == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
