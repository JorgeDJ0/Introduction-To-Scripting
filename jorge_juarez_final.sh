#!/bin/bash

<<com
Author: Jorge Juarez
Date: 5/10/22
com


#Question 3
RANDOM=$$
for i in $(seq 30)
do
	let arr[i]=RANDOM%100
done

#Question 7
for i in $(seq 100 1000)
do
	if [ $(())]

#Question 8
evenSum=0
oddSum=0
for i in $(seq 50 101)
do
	if [ $((i%2)) == 0 ]
	then
		let evenSum+=i
	else
		let oddSum+=i
	fi
done

echo $((evenSum))
echo $((oddSum))

#Question 9
for i in $(seq 20)
do
	let arr2[i]=RANDOM%100
done
<<com
for i in $(seq 20)
do
	for j in $(20-i-1)
	do
		if [ arr2[j] > arr2[j+1] ]
		then
com	

#Question 10

