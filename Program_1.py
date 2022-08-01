#Importing Decimal
from decimal import Decimal

#Fixed values for taxes
PST = Decimal("0.09975")
GST = Decimal("0.05")
total_tax_rate = PST + GST

#Requesting input values from the user
number_diners = int(input("Please insert the number of diners >"))
price_meal = Decimal(input("Please insert the price of the meal before tax >"))
tip_percentage = (input("Please insert the tip percentage: 1) Exceptional 20% , 2) Good 15%, 3) Basic 10%, 4) Horrible 0% >"))

#Variable to be used as a condition to break the loop
price_meal_tip = 0

#Initiating a while loop to adjust the meal price according to the tip percentage
while price_meal_tip == 0:
    if tip_percentage == "1":
        price_meal_tip = price_meal * Decimal(1.2)
        print(price_meal_tip)
    elif tip_percentage == "2":
        price_meal_tip = price_meal * Decimal(1.15)
    elif tip_percentage == "3":
        price_meal_tip = price_meal * Decimal(1.10)
    elif tip_percentage == "4":
        price_meal_tip = price_meal
    else:
        tip_percentage=input("Please insert the tip percentage: 1) Exceptional 20% , 2) Good 15%, 3) Basic 10%, 4) Horrible 0% >")

#Calculating amount added by the taxes, the final meal price and the amount owed per person
price_PST = int(price_meal_tip) * PST
price_GST = int(price_meal_tip) * GST
price_after_tax = int(price_meal_tip) * (1 + total_tax_rate)
price_per_person= price_after_tax / number_diners

#Printing the values of interest
print(f"The number of diners is {number_diners}.")
print("The price of the meal before tax is {:.2f}$.".format(price_meal_tip))
print("The Federal tax added is {:.2f}$.".format(price_PST))
print("The Provincial tax added is {:.2f}$.".format(price_GST))
print("The grand total price including tax is {:.2f}$.".format(price_after_tax))
print("The amount owed per person is {:.2f}$.".format(price_per_person))


