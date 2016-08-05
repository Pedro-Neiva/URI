readNext = True

while readNext:
    password = input()
    if password == '2002':
        readNext = False
        print('Acesso Permitido')
    else:
        print('Senha Invalida')
