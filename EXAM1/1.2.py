tereza_daily = float(input())
daily_income = float(input())
full_outcome = float(input())
present = float(input())

total = 0
total += tereza_daily * 5
total1 = daily_income * 5
sum = total + total1
sum -= full_outcome

if sum >= present:
    print(f'Profit: {sum:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {present - sum:.2f} BGN.')