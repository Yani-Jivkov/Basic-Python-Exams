n = int(input())
hearthstone_p = 0
fornite_p = 0
overwatch_p = 0
others_p = 0

for i in range(n):
    game_name = input()

    if game_name == 'Hearthstone':
        hearthstone_p += 1
    elif game_name == 'Fornite':
        fornite_p += 1
    elif game_name == 'Overwatch':
        overwatch_p += 1
    else:
        others_p += 1

hearthstone_p = (hearthstone_p / n) * 100
fornite_p = (fornite_p / n) * 100
overwatch_p = (overwatch_p / n) * 100
others_p = (others_p / n) * 100
print(f'Hearthstone - {hearthstone_p:.2f}%')
print(f'Fornite - {fornite_p:.2f}%')
print(f'Overwatch - {overwatch_p:.2f}%')
print(f'Others - {others_p:.2f}%')