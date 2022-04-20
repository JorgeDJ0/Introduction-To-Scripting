#!/bin/bash
<<com
Author: Jorge Juarez
Date: 4/19/22
com

RANDOM=$$

<<com
Problem 1
This will create an array of size 20. Will use random to generate the elements, and sort them lowest to
highest
com

for i in $(seq 20)
do
	let array1[i]=RANDOM%100
done
smallest=${array1[1]}
index=1
for i in $(seq 20)
do
	temp=${#array1}
	for j in $(seq $temp)
	do
		if [ ${array1[j]} -lt $smallest ]
		then
			let smallest=array1[j]
			let index=j
		fi
		let newArray1[i]=smallest
		unset array1[index]
	done
	echo ${newArray1[i]}
done

<<com
Problem 2
This will create an array of size 20, use random to generate the elements, and sort them highest to lowest
com

for i in $(seq 20)
do
	let array2[i]=RANDOM%100
done
largest=${array2[1]}
index=1
for i in $(seq 20)
do
	for j in $(seq ${#array2})
	do
		if [ ${array2[j]} -gt $largest ]
		then
			let largest=array2[j]
			let index=j
		fi
		let newArray2[i]=largest
		unset array1[index]
	done
	echo ${newArray2[i]}
done

<<com
Problem 3
This will create an array for numbers 1 to 50
com

for i in $(seq 50)
do
	let fifty[i]=i
	echo ${fifty[i]}
done

<<com
Problem 4
This will use a function and find the prime numbers from 1 to 50. Then it will find the sum of the prime
numbers
com

primeNumbers() {
prime=0
count=1
i=1
sum=0
until [ $prime -ge 50 ]
do
	if [ $((count%2)) -eq 1 ]
	then
		let prime=6*i-1
	else
		let prime=6*i+1
		let i++
	fi
	let sum=sum+prime
	let count++
done
echo "The sum of the prime numbers 1 through 50 is $sum"
}
primeNumbers

<<com
Problem 5
This program will have two arrays, one with the odd numbers from 1 to 50 and it's sum, and one with the even
numbers from 1 to 50 and it's sum
com

oddSum=0
evenSum=0
oddCount=0
evenCount=0
for i in $(seq 50)
do
	if [ $((i%2)) -eq 1 ]
	then
		let oddFifty[oddCount]=i
		let oddCount++
		let oddSum=oddSum+i
	else
		let evenFifty[evenCount]=i
		let evenCount++
		let evenSum=evenSum+i
	fi
done
echo "Sum of even numbers is $evenSum"
echo "Sum of odd numbers is $oddSum"
