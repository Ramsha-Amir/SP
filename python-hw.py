#Problem 01: ​ Given a list of strings, return the count the number of strings where the string length is 2
#or more and the first and last chars of the string are the same.
#Note: python does not have a ++ operator, but += works.

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221','abcda']))

#####################################
#Problem 02: ​ Given a string str, return a string made of the first 2 and the last 2 chars of the original
#string, so 'spring' yields 'spng'. However, if the string length is less than 2, return instead the empty
#string.

def both_ends(s):
  if len(s) < 2:
    return ''

  return s[0:2] + s[-2:]
print(both_ends("abcdr"))

#######################################
#Problem 3a: ​ Given a string str, return a string where all occurrences of its first char have been changed
#to '*', except the first char itself.
#For example:
#'babble' yields 'ba**le'
#Assume that the string is length 1 or more.


def fix_me(str1):
  char = str1[0]
  length = len(str1)
  str1 = str1.replace(char, '*')
  str1 = char + str1[1:]

  return str1

print(fix_me('babble'))


#Problem 3b: ​ Find ch in given string str, and replace all occurrences of given ch to "*", except the first
#occurrence of the ch itself.

def fix_me(str1, ch):
  char = 't'
  length = len(str1)
  str1 = str1.replace(char, '*')
  str1 = str1[0:]

  return str1

	
ch='t'
print(fix_me('babble',ch))


#####################################
#Problem 04: ​ Given a list of numbers, return a list where all adjacent duplicates have been reduced to a
#single element
#For example:
#[1, 2, 2, 3] returns [1, 2, 3]
#You may create a new list or modify the list passed as argument.

def remove_adjacent(nums):
  a = []
  for item in nums:
    if len(a):
      if a[-1] != item:
        a.append(item)
    else: a.append(item)        
  return a


print(remove_adjacent("1221"))


def remove_adjacent(nums):
  i = 1
  while i < len(nums):    
    if nums[i] == nums[i-1]:
      nums.pop(i)
      i -= 1  
    i += 1
  return nums

###############################
#Problem 05: ​ Write a script that make your sum function work for a list of strings as well.
#Example:
#>>> sum(["hello", "world"])
#helloworld


items=[x for x in raw_input().split(' ')]
print ''.join(items)



#//////////
#lines = []
#while True:
#    s = raw_input()
#    if s:
#        lines.append(s.upper())
#    else:
#        break;

#for sentence in lines:
#print sentence


##############################

#Problem 06: ​ Arrange a list on the basis of their data-types.
#Example:
#mylist = [1,2,3,[4,5], "I am", "25", 3.4, 5.7,65]
#int -> [1,2,3,65]
#str -> [​ "I am", "25"​ ]
#list -> [[4,5]]
#float -> [3.4,5.7]

input_list= [1,2,3,[4,5], "I am", "25", 3.4, 5.7,65]
dict1={}
for data in input_list:
	d_list=dict1.get(type(data),[])
	d_list.append(data)
	dict1[type(data)]=d_list

print dict1 


#############################
​ #Parse the given web pages of baby_names, and list down all the names having length > 3
#using Beautiful Soup.

import requests
from PIL import Image
from bs4 import BeautifulSoup
from StringIO import StringIO

def get_names(URL):
	if(URL):
		fd=open(URL,'r')
		n=fd.read()
		soup=BeautifulSoup(n,'lxml')
		names=soup.find_all("table",summary="Popularity for top 1000")
		print names
		rows=names.find_all("tr",align="right")[0]
		for data in rows.find_all('td'):
				print data

def main():
	URL="/home/ramsha/Desktop/babynames/baby2000.html"
	get_names(URL)

if __name__ =="__main__":
	main()


