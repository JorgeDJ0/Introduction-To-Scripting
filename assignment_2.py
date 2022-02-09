"""
Author: Jorge Juarez
Date: 2/8/22
"""

"""
Question 1
This program will print out a right triangle using asterisks and then print it again but reflected
"""

for i in range (1,7):
    for j in range (1,i):
        print ("*", end = " ")
    print()

for i in range (1,7):
    for j in range (1,7-i):
        print (" ", end = " ")
    for k in range (1,i):
        print ("*", end = " ")
    print()

"""
Question 2
This program will take two integers from the user and then put them into two equations
"""

n = int(input("Enter an integer: "))
r = int(input("Enter an integer: "))
print(n / r*(n - r))
print(n / (n - r))

"""
Question 3
This program will be given a list and then sort the list using a loop
"""

list = [20, 68, 41, 88, 16, 40, 65, 97, 85]
print("Before")
for temp in range(0,len(list)):
    print(list[temp], end = " ")

for i in range(0, len(list)):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            num = list[i]
            list[i] = list[j]
            list[j] = num
    
print()
print("After")
for temp in range(0,len(list)):
    print(list[temp], end = " ")

"""
Question 4
This program will be given a list, then find the sum of all the elements in the list, create two new 
lists wil only even and odd numbers, and then find the sum of the lists of odd and even numbers
"""

numbers = [20, 68, 41, 88, 16, 40, 65, 97, 85]
numSum = 0
evenSum = 0
oddSum = 0
evenNums = []
oddNums = []

for temp in range(0,len(numbers)):
    numSum += numbers[temp]
    if numbers[temp] % 2 == 0:
        evenNums.append(numbers[temp])
    elif numbers[temp] % 2 == 1:
        oddNums.append(numbers[temp])

for temp in range(0,len(evenNums)):
    evenSum += evenNums[temp]
for temp in range (0, len(oddNums)):
    oddSum += oddNums[temp]
print("Sum of all the numbers in the list:", numSum)
print("Sum of all the even numbers in the list:", evenSum)
print("Sum of all the odd numbers in the list:", oddSum)

"""
Question 5
This program will find all the prime numbers between 2 and 50 and print them out
"""

prime = [2,3]
numList =[]
num = 2
while num <= 50:    #sets the list of 2-50
    numList.append(num)
    num += 1
for i in range (0, len(numList)):
    if (numList[i] % 2) != 0 and (numList[i] % 3 != 0):
        prime.append(numList[i])
for i in range(0,len(prime)):
    print(prime[i])

"""
Question 6
This program will put the code from questions 1 - 3 into seperate functions and then call upon those functions
"""

def q1():
    for i in range (1,7):
        for j in range (1,i):
            print ("*", end = " ")
        print()

    for i in range (1,7):
        for j in range (1,7-i):
            print (" ", end = " ")
        for k in range (1,i):
            print ("*", end = " ")
        print()
def q2(n, r):
    print(n / r*(n - r))
    print(n / (n - r))
def q3(list):
    print("Before")
    for temp in range(0,len(list)):
        print(list[temp], end = " ")

    for i in range(0, len(list)):
        for j in range(i+1,len(list)):
            if list[i] > list[j]:
                num = list[i]
                list[i] = list[j]
                list[j] = num
    print()
    print("After")
    for temp in range(0,len(list)):
        print(list[temp], end = " ")
#Function calls
q1()
q2(n, r)
q3(list)

"""
Question 7
This program will determine if a number entered by the user is an Armstrong number
"""

num = int(input("Enter a number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp = temp // 10
print(sum)


"""
Question 9
This program will correct the code given to make the loop only print out even numbers
"""

loop_counter = 1
while loop_counter <= 10:
 if loop_counter%2 == 0:
    print(loop_counter)
 loop_counter += 1 
 