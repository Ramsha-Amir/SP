#!/bin/bash
echo "Enetr first number: "   
read n1
echo "Enetr first number: "
read n2


expr $n1 + 0 && expr $n2 + 0 && echo "Both are numbers"  || echo " not number"
if [ $? -eq 0 ]
then 
	echo "Addition of two  numbers: `expr $n1 + $n2`"
	echo "Subtraction of two  numbers: `expr $n1 - $n2`"
	echo "Multiplication of two numbers: `expr $n1 \* $n2`"
	echo "Modulus of two numbers: `expr $n1 % $n2`"

	if [ $n2 -ne 0 ]
	 then 
		echo "Division of two numbers `expr $n1 / $n2`"
         else 
	 	echo "Denominator is zero" 
	fi

fi


