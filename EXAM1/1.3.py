num_dancers = int(input())
points = float(input())
season = input()
location = input()


earnings = num_dancers * points

if location == "Abroad":
    earnings += 0.5 * earnings

if season == "summer":
    expenses = 0.1 if location == "Abroad" else 0.05
else:
    expenses = 0.15 if location == "Abroad" else 0.08

earnings_after_expenses = earnings - (expenses * earnings)
charity = 0.75 * earnings_after_expenses
remaining_money = earnings_after_expenses - charity
money_per_dancer = remaining_money / num_dancers


print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")