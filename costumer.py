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
    print(costumer["email"])
except KeyError as error:
    print()