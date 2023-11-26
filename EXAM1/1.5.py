sea_eks = int(input())
mountain_eks = int(input())
total_income = 0

while True:
    place = input()

    if place == 'Stop':
        break

    if place == 'sea' and sea_eks == 0:
        total_income += 0
    elif place == 'sea':
        total_income += 680
        sea_eks -= 1

    if place == 'mountain' and mountain_eks == 0:
        total_income += 0
    elif place == 'mountain':
        total_income += 499
        mountain_eks -= 1

    if sea_eks == 0 and mountain_eks == 0:
        break

if sea_eks == 0 and mountain_eks == 0:
    print(f'Good job! Everything is sold.')
    print(f'Profit: {total_income} leva.')
else:
    print(f'Profit: {total_income} leva.')