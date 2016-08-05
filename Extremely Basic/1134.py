alcohol = 0
gasoline = 0
diesel = 0
readNext = True

while readNext:
    fuel = input()
    if fuel == '4':
        readNext = False
    elif fuel == '1':
        alcohol = alcohol + 1
    elif fuel == '2':
        gasoline = gasoline + 1
    elif fuel == '3':
        diesel = diesel + 1

print('MUITO OBRIGADO')
print('Alcool: %i' %alcohol)
print('Gasolina: %i' %gasoline)
print('Diesel: %i' %diesel)
