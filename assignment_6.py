"""
Author: Jorge Juarez
Date: 3/8/22
"""

"""
Question 1
This program will take a file of students and extract the infromation from it.
It will then get append the contents of another list to this one. It will then
sort the students.
"""

class student():
    def __init__(self, fName, lName, email, allCourse):
        self.fName = fName
        self.lName = lName
        self.email = email
        self.allCourse = allCourse

def main():
    students = []
    temp = []
    studentsNew = []
    try:
        infile = open('students.txt', 'r')
        for i in range (0,12):
            students.append(infile.readline())
        infile.close()
    except :
        print("File not found")
    
    for i in range(1,12):
        print(students[i])

    try:
        appendObject = open('students.txt', 'a')
        infile = open('more_students.txt', 'r')
        contents = '\n'
        contents += infile.read()
        appendObject.write(contents)
        infile.close()
        appendObject.close()
    except :
        print("File not found")

    try:
        infile = open('students.txt', 'r')
        for i in range (0, 37):
            temp.append(infile.readline())
        for i in range (1, 37):
            studentsNew.append(temp[i])
        infile.close()
    except:
        print("File not found")

    outfile = open('studentsSorted.txt', 'w')
    studentsNew.sort()
    for i in range (0, len(studentsNew)):
        outfile.write(studentsNew[i])
    outfile.close()

main()

"""
Question 2
This program will write the contents for 3 files into one and catch any errors that
may occur during the process.
"""

def writeFile(fileContents):
    try:
        infile = open('final_file.txt', 'a')
        infile.write(fileContents)
        infile.close()
    except :
        print("File not found")

def main():
    try:
        infile = open('f1.txt', 'r')
        fContents1 = infile.read()
        infile.close()
    except :
        print("file not found")

    writeFile(fContents1)

    try:
        infile = open('f2.txt', 'r')
        fContents2 = infile.read()
        infile.close()
    except :
        print("file not found")

    writeFile(fContents2)

    try:
        infile = open('f3.txt', 'r')
        fContents3 = infile.read()
        infile.close()
    except :
        print("file not found")

    writeFile(fContents3)

main()