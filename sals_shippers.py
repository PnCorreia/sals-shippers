#Greating

print("Welcome to Sal's Shippers")
print("What's the weight of your package?")

#Variables

weight = 2
ground_price = 0
premium_price = 125.00
drone_price = 0
best_price = 0
way = ""

#Ground shipping price 

if weight <= 2:
  ground_price = (weight * 1.50) + 20.00
elif weight > 2 and weight <= 6:
  ground_price = (weight * 3.00) + 20.00
elif weight > 6 and weight <= 10:
  ground_price = (weight * 4.00) + 20.00
else:
  ground_price = (weight * 4.75) + 20.00

#Drone shipping price

if weight <= 2:
  drone_price = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_price = weight * 9.00
elif weight > 6 and weight <= 10:
  drone_price = weight * 12.00
else:
  drone_price = weight * 14.25

#Which is cheaper:

if ground_price < premium_price and ground_price < drone_price:
  best_price = ground_price
elif ground_price >= premium_price and premium_price < drone_price:
  best_price = premium_price
elif ground_price <= premium_price and ground_price > drone_price:
  best_price = drone_price

# Defining way ground vs by drone

if best_price == ground_price:
  way = "ground shipping service"
elif best_price == premium_price:
  way = "ground shipping premium service"
else:
  way = "drone shipping service"

# Output

print("The best way to ship your package is with our", way, "it will cost only", best_price, "$")





