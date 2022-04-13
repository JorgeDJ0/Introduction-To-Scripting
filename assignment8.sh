#!/bin/bash
<<com
Author: Jorge Juarez
Date: 4/12/22
com

<<com
Question 1
This will print the numbers 1 to 15 using a while, until, and for loop
com

#While loop

num=0
while [[ $num -lt 15 ]]
do
	echo $(($num+1))
	let "num++"
done

#Until loop

num=1
until [ $num -eq 16 ]
do
	echo $num
	let "num++"
done

#For loop

num=0
for num in $(seq 15)
do
	echo $num
done

<<com
Question 2
This will find the summation of 20 to 40 using while, until, and for loops
com

#While loop

sum=0
num=20
while  [[ $num -le 40 ]]
do
	let "sum+=num"
	let "num++"
done
echo $sum

#Until loop

sum=0
num=20
until [ $num -eq 41 ]
do
	let "sum+=num"
	let "num++"
done
echo $sum

#For loop

sum=0
for temp in $(seq 20 40)
do
	let "sum+=temp"
done
echo $sum

<<com
Question 3
This will print prime numbers less than 50 using while, until, and for loops
com

#While loop

prime=2
run=0
num3=1
while [ $prime -lt 50 ]
do
	echo $prime
	if [ $((run%2)) -eq 0 ]
	then
		let "prime=6*num3-1"
	else
		let "prime=6*num3+1"
		let "num3++"
	fi
	let "run++"
done

#Until loop

prime=2
run=0
num3=1
until [ $prime -ge 50 ]
do
	echo $prime
	if [ $((run%2)) -eq 0 ]
	then
		let "prime=6*num3-1"
	else
		let "prime=6*num3+1"
		let "num3++"
	fi
	let "run++"
done

#For loop

prime=2
run=0
num3=1
for pTemp in $(seq 17)
do
	echo $prime
	if [ $((run%2)) -eq 0 ]
	then
		let "prime=6*num3-1"
	else
		let "prime=6*num3+1"
		let "num3++"
	fi
	let "run++"
done

<<com
Question 4
This will take input from the user, a city, then outputs the corresponding Texas A&M University
com

echo "Enter a city: "
read city

if [[ $city == 'corpus' || $city == 'Corpus' ]]
then
	echo "Texas A&M University-Corpus Christi"
elif [[ $city == 'kingsville' || $city == 'Kingsville' ]]
then
	echo "Texas A&M University-Kingsville"
elif [[ $city == 'commerce' || $city == 'Commerce' ]]
then
	echo "Texas A&M University-Commerce"
else
	echo "Texas A&M University"
fi

<<com
Bonus Question
This will fix broken code from our lecture
com

var_test=20
#ranges 1 to 10, 11 to 20, more

if [[ $var_test -ge 1 && $var_test -le 10 ]]
then
	echo "Between 1 to 10"
elif [[ $var_test -ge 11 && $var_test -le 20 ]]
then
	echo "Between 11 to 20"
elif [ $var_test -gt 20 ]
then
	echo "Greater than 20"
else
	echo "Less than 1"
fi
