from math import ceil

h = int(input())
w = int(input())
p_not = int(input())

painting = h * w * 4
painting -= painting * (p_not / 100)
painting = ceil(painting)

while True:
    inp = input()

    if inp == 'Tired!':
        break

    painted = int(inp)

    painting -= painted

    if painting <= 0:
        break

if painting < 0:
    print(f'All walls are painted and you have {abs(painting)} l paint left!')
elif painting == 0:
    print(f'All walls are painted! Great job, Pesho!')
else:
    print(f" {painting} quadratic m left.")
