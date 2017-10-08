# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 17:33:56 2017

@author: Yogesh
"""

# simple function

def hello():
    print('hello')

hello()



#Passing argument

def hello(name):
    print('hello,'+name)

hello("yogesh")



# default argument
def hello(name = "Everyone"):
    print('hello ,'+name)

hello("yogesh")
hello()


#keyowrd argument
def hello(name = "Everyone"):
    print('hello ,'+name)
hello(name = "yogesh")


#Lamba expression
def addition(n):
    return lambda x : x+n
 
fun = addition(2)
print(fun(3))


