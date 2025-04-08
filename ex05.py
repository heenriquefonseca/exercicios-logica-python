hour = input('Que horas são? ')

if hour.isdigit():
    hour = int(hour)

    if hour == 0 and hour <= 11:
        print('Bom dia!')
        ...
    elif hour >= 12 and hour <= 17:
        print('Boa tarde!')
        ...
    elif hour >= 18 and hour <=23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora.')
else:
    print('Digite um número inteiro.')