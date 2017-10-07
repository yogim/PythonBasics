# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 15:14:06 2017

@author: Yogesh
"""

######List basics


# Intialization
list1 = [1,2,3,4]
print(list1)



#List can be concatenated
list2 = [5,6,7,9]
print (list1 + list2)



# List are mutable 
list2[3] = 8
print(list2)



# Append element at the last of the list
list2.append(9)
print(list2)



#slicing char works same as string
list3 = list1 + list2
print(list3[:3])
print(list3[3:])
print(list3[-2:])
print(list3[:-2])
print(list3[2:5])



# for length use  len(list name)
len(list3)



# List nesting :  we can use list in list
list4 = [list1,list2]
# list4  = |1|5|
#          |2|6|
#          |3|7|
#          |4|8| 
# for printing second element of 1 row
#                               list[row][colummn]
print(list4[1][2])




