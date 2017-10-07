# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:36:03 2017

@author: Yogesh
"""


# break statement break inner most loop (loop2)
for n in range(2, 10):  #loop1 
   for x in range(2, n):   # loop2
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            print(n, 'is a prime number')


#Pass

for num in range(2, 10):
   if num % 2 == 0:
       print("Found an even number", num)
       continue
   print("Found a number", num)