#!/bin/bash
<<com
Author: Jorge Juarez
Date: 4/5/22
com

<<com
Problem 1
This will print "This is assignment 7"
com

echo This is assignment 7

<<com
Problem 2
This will have variables that hold ny name and courses
com

name="Jorge Juarez"
class1="Calculus I"
class2="Composition I"
class3="Introduction to Scripting"
class4="Introduction to Problem Solving"
class5="First-Year Seminar II"

echo "My name is $name"
echo "The classes I take are $class1, $class2, $class3, $class4, $class5"

<<com
Problem 3
This will have the same output as problem 2, but it will use special variables instead
com

echo $#

<<com
Problem 4
This will use special variables to find the current process number of that shell
com

echo $$

<<com
Problem 5
This will use a randomly generated number from 0 to 100 and display the grade for that number
com

RANDOM=$$
grade=$(($RANDOM%100))

if [ $grade -ge 90 ]
then
echo "A"
elif [ $grade -ge 80 ]
then
echo "B"
elif [ $grade -ge 70 ]
then
echo "C"
elif [ $grade -ge 60 ]
then
echo "D"
else
echo "Fail"
fi

<<com
Problem 6
This will perform mathematical functions and then display the increment or decrement
com

x=3
y=4

echo $((x+y))
echo $((x-y))
echo $((x*y))
echo $((x/y))
echo $((x++))
echo $((x--))