#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:53:45 2020

@author: parthrajauria
"""

""" # Ans 1 
total = 0
count = 0


while True:
    a = input('Enter a number: ')
    if a == 'done':
        break
    try:
        num = int(a)
    except:
        print("Invalid Input, type a number")
        continue
    
        
    count = count + 1
    total = total + int(a)
print('total is ', total)
print('count is', count)
print('average is', total/count)
      
"""

""" # Ans 2 """

smallest = None
largest = None

while True:
    a = input('Enter a number: ')
    if a == 'done':
        break
    try:
        num = int(a)
    except:
        print("Invalid Input, type a number")
        continue
    
    for value in [num]:
#        if value is None:
#            Largest = value 
        if value > largest: # Some error here.
            largest = value
    
    for value in [num]: # We created list to use in function.
        if smallest is None:
            smallest = value
        elif value < smallest:
            smallest = value
    
        
print('Smallest value is ', smallest)
print('Largest value is ', largest)



















