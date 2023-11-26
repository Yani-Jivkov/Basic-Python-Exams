percent_fat = int(input())
percent_protein = int(input())
percent_carbs = int(input())
total_calories = int(input())
percent_water = int(input())

fat_calories = (percent_fat / 100) * total_calories
protein_calories = (percent_protein / 100) * total_calories
carbs_calories = (percent_carbs / 100) * total_calories

total_food_weight = (fat_calories / 9) + (protein_calories / 4) + (carbs_calories / 4)
food_calories = total_calories / total_food_weight

water_calories = (percent_water / 100) * food_calories
final_calories = food_calories - water_calories

print(f"{final_calories:.4f}")