# Costumer.py
# Author: Saydie 
# Module 11 Lab: Costumer Dictionary And Lookup

print("--Excercise 1 ---")
costumer = {
    "name": "Alice",
    "Name": "Not-Alice",
    "email":"alice@example.com"
    "tier":"gold",
    "ytd_spend": 12400
}

print(costumer["name"])
print(costumer["email"])
print(costumer["tier"])
print(costumer["ytd_spend"])

print("---Excercie 2---")
costumer['phone']= '555-5555'
print(costumer)
costumer['tier'] = 'platinum'
print(costumer)
del costumer['Name']
print(costumer)
