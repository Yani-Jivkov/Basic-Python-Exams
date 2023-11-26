food_buyed = int(input())
food_buyed = food_buyed * 1000
total = 0

while True:
    food_today = input()

    if food_today == 'Adopted':
        break

    food_today = int(food_today)

    total += food_today

if food_buyed >= total:
    print(f'Food is enough! Leftovers: {food_buyed - total} grams.')
else:
    print(f'Food is not enough. You need {total - food_buyed} grams more.')