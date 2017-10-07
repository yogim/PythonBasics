# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:37:04 2017

@author: Yogesh
"""

# "" and '' are used for writing string
str  = "abcd"
str1 = 'abcd'
print(str,str1)



# Esacpe char(\) : Next character to \ is ignoreed 
#for string which has '  for eg : doesn't use \.
str = 'doesn\'t'
print(str)


#new line \n : This will print string next to \n  on new line
str = "print \n on new line"
print(str)


#  raw string (r): Use r before string to print string with special char as it is.
str =r"This will print string next to \n  on new line"
print(str)


# """ .....""" - is used  for print mutiple line
str = """ 
Student: Name
         Class
         Age 
         """
print(str)



#####Concatenate String
# Use * for repeating string
#use + for concatinating string
str =  "abcd"
print(3 * str)
print(str + str)



#Index : Str = |a|b|c|d|
#               0 1 2 3
#              -4-3-2-1

str =  "abcd"
print(str[0])
print(str[-4])



#####Slicing charater (:): Used for range for example print a to c in str
#                         we print by str[0:2]
#str[:2] = str[0:2]  by default number before : is first index
#str[:-2] = str[0:-2]  by default number before : is first index

print(str[:2])
print(str[:-2])

#str[2:] = str[2:3]  by default number after : is last index
#str[-2:] = str[-2:-4]  by default number after : is last index

print(str[2:])
print(str[-2:])


  

