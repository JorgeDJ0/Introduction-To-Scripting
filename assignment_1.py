"""
Author: Jorge Juarez
Date: 2/1/22
"""

"""
Question 1
This program will use print to print out the outputs
"""

print("Name: Jorge Juarez")
print("Address: 7037 Islander Way")
print("City: Corpus Christi")
print("State: Texas")
print("ZIP Code: 78412")
print("Phone Number: (361)555-5555")
print("Major: Computer Science")

"""
Question 2
This program will receive a value form the user and calculate the number of acres
in the tract
"""

squareFeet = int(input("Enter the total square feet: "))
acres = squareFeet / 43560
print(acres)

"""
Question 3
This program will calculate the distance a car will travel based on the time and
speed it is traveling
"""

print("A car traveling 70 mph for 6 hours will travel", 70 * 6, "miles")
print("A car traveling 70 mph for 10 hours will travel", 70 * 10, "miles")
print("A car traveling 70 mph for 15 hours will travel", 70 * 15, "miles")

"""
Question 4
This program will get an age from the user and print the classification for that age
(ex: 15 = teenager)
"""

age = int(input("Enter an age: "))

if age <= 1:
    print("This person is an infant")
if age > 1 and age < 13:
    print("This person is a child")
if age >= 13 and age < 20:
    print("This person is a teenager")
if age >= 20:
    print("This person is an adult")

"""
Question 5
This program will get the amount of pennies, nickels, dimes, and quarters from the 
user and determine whether that amount adds up to a dollar
"""

coins = int(input("Enter the amount of pennies: "))
price = 0.01 * coins
coins = int(input("Enter the amount of nickels: "))
price += 0.05 * coins
coins = int(input("Enter the amount of dimes: "))
price += 0.1 * coins
coins = int(input("Enter the amount of quarters: "))
price += 0.25 * coins

if price == 1.0:
    print("Congratulations!")
if price > 1.0:
    print("The amount entered is greater than a dollar")
if price < 1.0:
    print("The amount entered is less than a dollar")

"""
Question 6
This program will ask the user for a year, then it will determine whether February 
has 28 or 29 days for that year
"""

year = int(input("Enter a year: "))
if year % 100 == 0 and year % 400 == 0:
    print("There are 29 days in February in", year)
elif year % 4 == 0:
    print("There are 29 days in February in", year)
else:
    print("There are 28 days in February in", year)