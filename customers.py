# Costumer.py
# Author: Saydie 
# Module 11 Lab: Costumer Dictionary And Lookup

print("--Excercise 1 ---")
costumer = {
    "name": "Alice",
    "Name": "Not-Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(costumer["name"])
print(costumer["email"])
print(costumer["tier"])
print(costumer["ytd_spend"])

print("---Excercie 2---")
costumer['phone']= '555-5555' # Adding Key Value to Dictionary
print(costumer)
costumer['tier'] = 'platinum'
print(costumer)
del costumer['Name']
print(costumer)

print(costumer.get('ytd_spend', 0))

print("---Excercise 3---")
print(costumer.get("email","no email on file"))

try:
    print(costumer['email'])
except KeyError as error:
    print('KeyError caught', error)

print("---Excercise 4---")

for key, value in costumer.items():
        print(f"{key}: {value})")
for key in costumer:
        print(key)

print("---Exercise 5 ---")

tier_discounts = {"bronze": 0,
       "silver": 0.05,
       "gold": 0.1,
       "platinum": 0.15
       }

purchase = 200
discount_rate = tier_discounts.get(costumer["tier"], 0)
final_price = purchase * (1- discount_rate)
print(f"Tier: {costumer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print("Final Price: ${final_price:.2f}")

print("---Exercise 6---")

costumers = [
      {"name": "bob", "tier": "ytd_spend": 3200}
      {"name":"Carol", "tier": "gold", "ytd_spend": 8750}
      {"name": "David", "tier": "bronze", "ytd_spend": 450}
]

for record in costumers:
      rate = tier_discounts.get["tier", 0]
      discount = 300 * rate
      print(f"{record['name']} ([record[tier]]): Discount = ${discount:.2f}" off a $300 purchase)

print("--- Exercise 7 --")
catolog = {
      "Widget A": {"price": 9.99, "stock": 150},
      "Gadget C": {"price": 49.99, "stock": 8},
}

for name, details in catolog.items():
      if details["stock"] < 20:
            print(f"LOW STOCK: {name} - only{details['stock']} left")

print("---Exercise 8---")

transactions = [
      {"region": "South", "amount": 300},
      {"region": "North","amount": 150},
      {"region": "South", "amount": 200}
]

sales_by_region = {}
for sale in transactions:
      region = sale["region"]
      amount = sale["amount"]
      sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
      print(f"{region}: ${sales_by_region[region]:.2f}")


# Reflection 1: When I would use .get() and when I would use bracket notation: Use the .get() method when you are unsure if a key exists in a dictionary to safely return a default value and avoid a KeyError. Use bracket notation when you know the key is present or want an explicit error if a key is missing.

# Reflection 2: What the Exercise 8 summary reminds me of in Excel, and why Python is more useful for large datasets: The summary reminds me of an Excel PivotTable, which groups and summarizes data across categories. Python is much more useful for large datasets because Excel suffers from performance bottlenecks and row limits, whereas Python processes massive amounts of data efficiently.
