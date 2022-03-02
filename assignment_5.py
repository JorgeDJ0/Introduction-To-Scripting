"""
Author: Jorge Juarez
Date: 3/1/22
"""
"""
Question 1
This program will take a string entered by the user and convert it into morse code
"""

def morse (hold):
    var2 = ""
    for temp in range (0, len(hold)):
        if hold[temp] == " ":
            var2 += " "
        elif hold[temp] == ",":
            var2 += "--..--"
        elif hold[temp] == ".":
            var2 += ".-.-.-"
        elif hold[temp] == "?":
            var2 += "..--.."
        elif hold[temp] == "0":
            var2 += "-----"
        elif hold[temp] == "1":
            var2 += ".----"
        elif hold[temp] == "2":
            var2 += "..---"
        elif hold[temp] == "3":
            var2 += "...--"
        elif hold[temp] == "4":
            var2 += "....-"
        elif hold[temp] == "5":
            var2 += "....."
        elif hold[temp] == "6":
            var2 += "-...."
        elif hold[temp] == "7":
            var2 += "--..."
        elif hold[temp] == "8":
            var2 += "---.."
        elif hold[temp] == "9":
            var2 += "----."
        elif hold[temp] == "A":
            var2 += ".-"
        elif hold[temp] == "B":
            var2 += "-..."
        elif hold[temp] == "C":
            var2 += "-.-."
        elif hold[temp] == "D":
            var2 += "-.."
        elif hold[temp] == "E":
            var2 += "."
        elif hold[temp] == "F":
            var2 += "..-."
        elif hold[temp] == "G":
            var2 += "--."
        elif hold[temp] == "H":
            var2 += "...."
        elif hold[temp] == "I":
            var2 += ".."
        elif hold[temp] == "J":
            var2 += ".---"
        elif hold[temp] == "K":
            var2 += "-.-"
        elif hold[temp] == "L":
            var2 += ".-.."
        elif hold[temp] == "M":
            var2 += "--"
        elif hold[temp] == "N":
            var2 += "-."
        elif hold[temp] == "O":
            var2 += "---"
        elif hold[temp] == "P":
            var2 += ".--."
        elif hold[temp] == "Q":
            var2 += "--.-"
        elif hold[temp] == "R":
            var2 += ".-."
        elif hold[temp] == "S":
            var2 += "..."
        elif hold[temp] == "T":
            var2 += "-"
        elif hold[temp] == "U":
            var2 += "..-"
        elif hold[temp] == "V":
            var2 += "...-"
        elif hold[temp] == "W":
            var2 += ".--"
        elif hold[temp] == "X":
            var2 += "-..-"
        elif hold[temp] == "Y":
            var2 += "-.-"
        elif hold[temp] == "Z":
            var2 += "--.."
    print(var2)

var = input("Enter a string: ")
var = var.upper()
morse(var)

"""
Question 2
This program will get a string from the user and output how many vowels and 
consonants are in the string
"""

def vowels (hold):
    vowels = 0
    for temp in range (0, len(hold)):
        temp2 = hold[temp]
        if temp2.isalpha():
            if temp2.upper() == "A" or temp2.upper() == "E" or  temp2.upper() == "I" or temp2.upper() == "O" or temp2.upper() == "U":
                vowels += 1
    return vowels 

def consonants (hold, vowels):
    consonants = 0
    for temp in range (0, len(hold)):
        temp2 = hold[temp]
        if temp2.isalpha():
            consonants += 1
    consonants -= vowels
    return consonants

var = input("Enter a string: ")
vow = vowels(var)
con = consonants(var, vow)
print("There are", vow, "vowels and", con, "consonants")

"""
Question 3
This program will remove certian aspects from various provided strings
"""

str1 = "P@#yn26at^&i5ve"
str2 = "/*Jon is @developer & musician"
str3 = "Emma-is-a-data-scientist"
str4 = "Hello, have a good day"
letter = 0
digits = 0
symbols = 0

#Q1
for i in range (0, len(str1)):
    if str1[i].isalpha():
        letter += 1
    elif str1[i].isdigit():
        digits += 1

symbols = len(str1) - (letter + digits)
print("There are", letter, "letters,", digits, "digits, and", symbols, "symbols")

#Q2
str2_2 = ""
for i in range (0, len(str2)):
    if str2[i].isalpha():
        str2_2 += str2[i]
    elif str2[i].isspace():
        str2_2 += str2[i]

str2 = str2_2
print(str2)

#Q3
str3_2 = ""
for i in range (0, len(str3)):
    if str3[i].isalpha():
        str3_2 += str3[i]
    elif str3[i] == "-":
        str3_2 += " "
str3 = str3_2
print(str3)

#Q4
str4_2 = ""
for i in range (0, len(str4)):
    if str4[i].isalpha():
        if str4[i].upper() == "A" or str4[i].upper() == "E" or  str4[i].upper() == "I" or str4[i].upper() == "O" or str4[i].upper() == "U":
            str4_2 += str4[i]
    else:
        str4_2 += str4[i]
str4 = str4_2
print(str4)
"""
Question 5
This program will alter the given string
"""
str1 = "this is the string for the class"
temp = "T"
for i in range (1,len(str1)):
    if str1[i].isalpha():
        if str1[i-1].isspace():
            temp += " "
            temp += str1[i].upper()
        else:
            temp += str1[i]
str1 = temp
print(str1)

temp = ""
for i in range (0, len(str1)):
    if str1[i].isalpha():
        temp += str1[i]
str1 = temp
print(str1)

temp = ""
for i in range (0, len(str1)):
    if str1[i].isupper():
        temp += " "
        temp += str1[i]
    else:
        if str1[i].upper() == "S":
            temp += "$"
        else:
            temp += str1[i]
str1 = temp
print(str1)

temp = ""
for i in range (0, len(str1)):
    if str1[i].isalpha():
        temp += str1[i]
    elif str1[i] == "$":
        temp += "s"
    else:
        temp += str1[i]
str1 = temp
print(str1)