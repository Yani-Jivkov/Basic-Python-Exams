price_for_baggage = float(input())
kg_baggage = float(input())
days_travelling = int(input())
baggage_count = int(input())

if kg_baggage < 10:
    total = price_for_baggage * 0.2
elif kg_baggage <= 20:
    total = price_for_baggage * 0.5
else:
    total = price_for_baggage

if days_travelling > 30:
    total = total + (total * 0.1)
elif days_travelling >= 7:
    total = total + (total * 0.15)
else:
    total = total + (total * 0.4)

total *= baggage_count

print(f'The total price of bags is: {total:.2f} lv. ')