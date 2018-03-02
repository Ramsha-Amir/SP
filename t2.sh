#!/bin/bash
file1=$1
user_Name1=$2
file2=$3
user_Name2=$4

set `ls -li $1`
user1=$4
group1=$5
perm1=$2

set `ls -li $3`
user2=$4
group2=$5
perm2=$2

if [ $user1 = $user_Name1 ]
then  	
	if [ $user2 = $user_Name2 ]
    then  	
	echo "     OWNER: $user1          			OWNER: $user2"
	echo "     GROUP: $group1         			GROUP: $group2"
	echo "     PERMISSIONS: $perm1    		 	PERMISSIONS: $perm2"
	echo "     FILENAME: $file1       			FILENAME: $file2"
	echo "     cheating : 0       				cheating : 0"			
    else
        echo "     cheating : 0      				cheating : 1"
    fi
else 
	echo "     cheating : 1       			c	heating : 1"
fi

echo "The difference between two files are: "
     diff -c $file1 $file2










