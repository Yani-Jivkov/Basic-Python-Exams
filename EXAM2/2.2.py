from math import ceil

football_player = input()
budget = float(input())
beers = int(input())
chips = int(input())

total_beers = beers * 1.2
one_chips = total_beers * 0.45
total_chips = chips * one_chips
total_chips = ceil(total_chips)

total = total_beers + total_chips

if budget >= total:
    print(f'{football_player} bought a snack and has {budget - total:.2f} leva left.')
else:
    print(f"{football_player} needs {total - budget:.2f} more leva!")


