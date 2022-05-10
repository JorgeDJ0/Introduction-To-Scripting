"""
Author: Jorge Juarez
Date: 5/10/22
"""

#Question 1
list =  ['z', 'm', 'n', 'a', 'c', 'i', 'g', 'x', 't']   #Declares the list
listSize = len(list)
for i in range (0, listSize):   #Sorts the list
    for j in range (0, listSize-i-1):
        if list[j] < list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]

print(list) #Displays the list

#Question 2
import random
class Student():    #Holds the student's name and course grades
    def __init__(self, name, c1, c2, c3, c4, c5, c6):
        self._name = name
        self._course1 = c1
        self._course2 = c2
        self._course3 = c3
        self._course4 = c4
        self._course5 = c5
        self._course6 = c6
    def displayStudent(self):
        print(self._name)
        print(self._course1)
        print(self._course2)
        print(self._course3)
        print(self._course4)
        print(self._course5)
        print(self._course6)
    def getCourse1(self):
        return self._course1
    def getCourse2(self):
        return self._course2
    def getCourse3(self):
        return self._course3
    def getCourse4(self):
        return self._course4
    def getCourse5(self):
        return self._course5
    def getCourse6(self):
        return self._course6

def main():
    sum1 = 0    #Initializes the sum tracker for each course
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    studentList = []
    for i in range (0,25):  #Creates each object
        a = random.randint(0,100)
        b = random.randint(0,100)
        c = random.randint(0,100)
        d = random.randint(0,100)
        e = random.randint(0,100)
        f = random.randint(0,100)
        students = Student("Joe", a, b, c, d, e, f)
        studentList.append(students)

    for i in range (0,25):  #Adds all the course grades from all the students
        sum1 += studentList[i].getCourse1()
        sum2 += studentList[i].getCourse2()
        sum3 += studentList[i].getCourse3()
        sum4 += studentList[i].getCourse4()
        sum5 += studentList[i].getCourse5()
        sum6 += studentList[i].getCourse6()
    
    #Displays the averages for each course
    print("The average for course 1 is:", sum1/25)
    print("The average for course 2 is:", sum2/25)
    print("The average for course 3 is:", sum3/25)
    print("The average for course 4 is:", sum4/25)
    print("The average for course 5 is:", sum5/25)
    print("The average for course 6 is:", sum6/25)

main()

#Question 4
class Clothes():    #Holds the item's description, units, and price
    def __init__ (self, d, u, p):
        self._description = d
        self._units = u
        self._price = p
    def getDescription(self):
        return self._description
    def getUnits(self):
        return self._units
    def getPrice(self):
        return self._price

def question4():
    clothes = []
    temp = Clothes("Jacket", "40", "59.95")
    clothes.append(temp)
    temp = Clothes("Designer Jeans", "100", "34.95")
    clothes.append(temp)
    temp = Clothes("Shirt", "200", "24.95")
    clothes.append(temp)
    infile = open('clothes.txt', 'w') #Writes clothes objects data to file
    for i in range (0,3):
        infile.write(clothes[i].getDescription())
        infile.write(clothes[i].getUnits())
        infile.write(clothes[i].getPrice())
    infile.close()

question4()

#Question 5
string_test = """Hello my name is Rajesh, and my number is 123456789. My friend's name is
Timmy, and his phone number is 987654321. Other friend’s name is Rick, and his phone number
is 2222222222. Other friend’s name is Malisa, and her phone number is 1111111111. Other
friend’s name is Steven, and his phone number is 4545454545"""

str1 = "Emma-is-a-data-scientist"
str2 = ""
for i in range (0, len(str1)):
    if str1[i].isalpha():
        str2 += str1[i]
    elif str1[i] == "-":
        str2 += " "
str1 = str2
print(str1)

str3 = "/*Jon is @developer & musician"
str4 = ""
for i in range (0, len(str3)):
    if str3[i].isalpha():
        str4 += str3[i]
    elif str3[i].isspace():
        str4 += str3[i]

str3 = str4
print(str3)

#Question 6
num = int(input("Enter a number: "))
