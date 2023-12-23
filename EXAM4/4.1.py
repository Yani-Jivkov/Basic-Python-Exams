strawberry_price_sec = float(input())
bananas_kg = float(input())
orange_kg = float(input())
raspberry_kg = float(input())
strawberry_kg = float(input())


raspberry_price_sec = strawberry_price_sec / 2
raspberry_price = (raspberry_kg * strawberry_price_sec) / 2
orange_price = orange_kg * (raspberry_price_sec * 0.6)
bananas_price = bananas_kg * (raspberry_price_sec * 0.2)
strawberry_price = strawberry_price_sec * strawberry_kg

total = strawberry_price + raspberry_price + orange_price + bananas_price

print(f'{total:.2f}')