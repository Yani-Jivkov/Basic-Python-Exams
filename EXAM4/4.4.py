budget = float(input())
items_bought = 0
total_price = 0

while budget >= 0:
    name = input()

    if name == 'Stop':
        break

    price = float(input())
    items_bought += 1

    if items_bought % 3 == 0:
        price /= 2

    total_price += price
    budget -= price

if budget <= 0:
    print(f'You don\'t have enough money!')
    print(f'You need {abs(budget):.2f} leva!')
else:
    print(f'You bought {items_bought} products for {total_price:.2f} leva.')
