capacity = int(input())
total_sum = 0
seats = 0
while True:
    people = input()

    if people == 'Movie time!':
        break

    people = int(people)
    sum = people * 5

    if people % 3 == 0:
        sum -= 5

    seats += people
    total_sum += sum

    if capacity <= seats:
        break

if capacity <= seats:
    print(f'The cinema is full.')
    print(f'Cinema income - {total_sum} lv.')
else:
    print(f'There are {capacity - seats} seats left in the cinema.')
    print(f'Cinema income - {total_sum} lv.')