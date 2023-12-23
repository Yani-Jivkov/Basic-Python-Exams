budget = float(input())
fuel_liters = float(input())
day = input()

if day == 'Saturday':
    total = fuel_liters * 2.1
    total += 100
    total *= 0.9
else:
    total = fuel_liters * 2.1
    total += 100
    total *= 0.8

if total <= budget:
    print(f'Safari time! Money left: {budget - total:.2f} lv. ')
else:
    print(f'Not enough money! Money needed: {total - budget:.2f} lv.')