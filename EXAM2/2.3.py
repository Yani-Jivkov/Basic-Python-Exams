team = input()
type = input()
count = int(input())

if team == "Argentina":
    if type == 'flags':
        total = 3.25 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'caps':
        total = 7.2 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'posters':
        total = 5.1 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'stickers':
        total = 1.25 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    else:
        print('Invalid stock!')
elif team == "Brazil":
    if type == 'flags':
        total = 4.2 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'caps':
        total = 8.5 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'posters':
        total = 5.35 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'stickers':
        total = 1.2 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    else:
        print('Invalid stock!')
elif team == "Croatia":
    if type == 'flags':
        total = 2.75 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'caps':
        total = 6.9 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'posters':
        total = 4.95 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'stickers':
        total = 1.1 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    else:
        print('Invalid stock!')
elif team == "Denmark":
    if type == 'flags':
        total = 3.1 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'caps':
        total = 6.5 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'posters':
        total = 4.8 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    elif type == 'stickers':
        total = 0.9 * count
        print(f'Pepi bought {count} {type} of {team} for {total:.2f} lv.')
    else:
        print('Invalid stock!')
else:
    print('Invalid country!')
