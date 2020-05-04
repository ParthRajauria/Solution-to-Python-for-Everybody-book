#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:53:34 2020

@author: parthrajauria
"""

""" # Ans 1
counts = dict()
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
        
print(counts)        

'or' in counts    

"""

"""# Ans 2

counts = dict()
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    if line.startswith('From'):
        if not line.startswith('From:'):
            words = line.split()
            word = words[2]
            
            counts[word] = counts.get(word,0) + 1
#            if word not in counts:
#                counts[word] = 1
#            else:
#                counts[word] += 1
    
    
print(counts)    
"""

""" # Ans3

counts = dict()
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    if line.startswith('From'):
        if not line.startswith('From:'):
            words = line.split()
            word = words[1]
            
            counts[word] = counts.get(word,0) + 1

print(counts)
"""

 # Ans4 (Incomplete)
"""
largest = 0
counts = dict()
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    if line.startswith('From'):
        if not line.startswith('From:'):
            words = line.split()
            word = words[1]
            
            counts[word] = counts.get(word,0) + 1
            
for i in counts:
    if int(counts[i]) > largest:
        largest = counts[i]
for i in counts:
    if counts[i] == largest:
        i = ram
        
print(ram, largest)                    
"""         
  
           
 # Ans 5

""" counts = dict()
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    if line.startswith('From'):
        if not line.startswith('From:'):
            words = line.split()
            word = words[1]
            ram = word.split('@')
            laks = ram[1]
            
            counts[laks] = counts.get(laks,0) + 1
print(counts)

"""




#largest = None
#print('Before:', largest)
#for itervar in [3,41,12,5]:
#    if largest is None or itervar > largest:
#        largest = i
#    print('Loop: ', i, largest)































