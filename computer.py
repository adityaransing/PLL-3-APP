import json

with open("products.json", "r") as file:
    products = json.load(file)

total = 0

for product in products:
    value = product["quantity"] * product["price"]
    total += value

print("Total value of all products:", total)