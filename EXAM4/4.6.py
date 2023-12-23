days = int(input())
hours_per_day = int(input())

total_amount = 0

for day in range(1, days + 1):
    daily_amount = 0
    for hour in range(1, hours_per_day + 1):
        if (day % 2 == 0) and (hour % 2 != 0):
            daily_amount += 2.50
        elif (day % 2 != 0) and (hour % 2 == 0):
            daily_amount += 1.25
        else:
            daily_amount += 1.00

    total_amount += daily_amount
    print(f"Day: {day} - {daily_amount:.2f} leva")

print(f"Total: {total_amount:.2f} leva")