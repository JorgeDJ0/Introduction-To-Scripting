"""
Author: Jorge Juarez
Date: 2/22/22
"""
"""
Question 1
This program will display a menu that lets the user look for an employee, add a new
one, change elements of an exisiting employee, delete an employee, and quit the 
program.
"""

class employee():
    def _init_(self, depart, job):
        self.department = depart
        self.jobTitle = job

    

if __name__ == "__main__":
    names = {
        '47899' : 'Susan Meyers',
        '39119' : 'Mark Jones',
        '81774' : 'Joy Rogers'
    }

    E1 = employee(names['47899'], 'Accounting', 'Vice President')
    E2 = employee(names['39119'], 'IT', 'Programmer')
    E3 = employee(names['81774'], 'Manufacturing', 'Engineer')

"""
Question 2
This program will get a series of 20 numbers from the user, store them in a list, and 
then display the lowest number, highest number, total of the numbers, and the 
average of the numbers is the list.
"""
"""
numbers = []
for i in range (0, 20):
    temp = int(input("Enter any number: "))
    numbers.append(temp)

lowest = numbers[0]
for i in range (0,20):
    if numbers[i] < lowest:
        lowest = numbers[i]

print("The lowest number in the list is:", lowest)

highest = numbers[0]
for i in range (0,20):
    if numbers[i] > highest:
        highest = numbers[i]

print("The highest number in the list is:", highest)

total = 0
for i in range (0,20):
    total += numbers[i]

print("The total of the nummbers is:", total)

average = total / 20
print("The average of the numbers is:", average)
"""
"""
Question 3
This program will get a number entered by the user and display that number and its 
value squared
"""
"""
num = int(input("Enter any number: "))
number = {
    1 : 1
}

for i in range (2, num + 1):
    number[i] = i * i
print(number)
"""
"""
Question 4
This program will use a random list of 100 values, find the second largest element
in the list, and remove any repeating elements in the list
"""
"""
import random
randlist = []
for i in range (0, 100):
    randlist.append(random.randint(0,20))

print(randlist)

largest = randlist[0]
for i in range (1, 100):
    if randlist[i] > largest:
        secLargest = largest
        largest = randlist[i]
print(secLargest)

temp = 0
for i in range (0,20):
    for j in range (0,len(randlist)):
        if randlist[j] == i:
            temp += 1
    for j in range (0, temp - 1):
        randlist.remove(i)
    temp = 0            
print(randlist)
"""