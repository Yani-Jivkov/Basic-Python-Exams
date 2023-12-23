quantity = int(input())
type = input()
delivery = input()

if type == '90X130':
    if quantity > 60:
        total = quantity * 110
        total *= 0.92
    elif quantity > 30:
        total = quantity * 110
        total *= 0.95
    else:
        total = quantity * 110
elif type == '100X150':
    if quantity > 80:
        total = quantity * 140
        total *= 0.94
    elif quantity > 40:
        total = quantity * 140
        total *= 0.90
    else:
        total = quantity * 140
elif type == '130X180':
    if quantity > 50:
        total = quantity * 190
        total *= 0.88
    elif quantity > 20:
        total = quantity * 190
        total *= 0.93
    else:
        total = quantity * 190
else:
    if quantity > 50:
        total = quantity * 250
        total *= 0.86
    elif quantity > 25:
        total = quantity * 250
        total *= 0.91
    else:
        total = quantity * 250

if delivery == 'With delivery':
    total += 60


if quantity > 99:
    total = total + (total * 0.04)


if quantity < 10:
    print('Invalid')
else:
    print(f'{total:.2f} BGN')