#!/bin/bash
echo "Array of UNIX is:"
    UNIX=('Debian' 'Red hat' 'Ubuntu' 'Suse' 'Fedora')


echo "Print the whole array without using loop:"
	echo ${UNIX[*]}


echo "Display the length of the array:"
	echo ${#UNIX[*]}

echo "print the length of element on index 2:"
	echo ${#UNIX[2]}

echo "Extract 2 elements starting from the position 3 from an array called UNIX:"
	echo ${UNIX[@] :3 :2}

echo "Search UBUNTU from array elements and replace with SCO Unix:"	
	echo ${UNIX[@]/"Ubuntu"/"SCO Unix"}

echo "Add two elements AIX and HP-UX in the existing array:"
	temp=(${UNIX[@]} "AIX" "HP-UX")
	echo ${temp[*]}

echo "Remove the 3rd element from UNIX array:"
	unset UNIX[2]
	echo ${UNIX[*]}

echo "Make new array LINUX and copy the content of UNIX TO LINUX:"
LINUX=(${UNIX[@]})
	echo ${LINUX[*]} 

echo "Make new array BASH and concatenate both LINUX and UNIX arrays:"
bash=(${UNIX[@]}  ${UNIX[@]})
	echo ${bash[*]}

echo " Remove both the arrays LINUX AND UNIX"
	unset UNIX[*]

	unset LINUX[*]


echo "UNIX array after unset:"
	echo ${UNIX[*]}

echo "LINUX array after unset:"
	echo ${LINUX[*]}










































