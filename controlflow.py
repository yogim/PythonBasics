# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:02:37 2017

@author: Yogesh
"""


# if statement

a=2
b=3

if(a>b):
    print("a is greater than b")
else: 
    print("b is greater than a")    


a= 3

if a>b:
    print("a is greater than b")
elif a<b : 
    print("b is greater than a") 
else:
    print("a and b are equal")
    
    
# for statement
words = ['A', 'B', 'C']
for w in words:
    print(w, len(w))
  # range  
for i in range(5):
    print(i)
  # range(start, end)
 for i in range(5,10):
    print(i)
   #range(start,end, increment)
for i in range(10,100,10):
    print(i)