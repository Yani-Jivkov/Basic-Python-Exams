from math import ceil

avg_speed = float(input())
gas_for_100km = float(input())

total_1 = 384400 * 2

total = ceil(total_1 / avg_speed)
total += 3

fuel = (gas_for_100km * total_1) / 100

print(total)
print(f'{fuel:.0f}')
