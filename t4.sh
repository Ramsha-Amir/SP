#!/bin/bash

#read data from file
array=(`cat file3`)


#display  the content of file using array
echo ${array[*]}

#dispaly the total size
echo ${#array[*]}

#dispaly the data of 3rd index
echo ${#array[3]}
