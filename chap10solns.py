#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:01:50 2020

@author: parthrajauria
"""

""" # Ans1 
list = []
counts = dict()
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    if line.startswith('From'):
        if not line.startswith('From:'):
            words = line.split()
            word = words[1]
            
            counts[word] = counts.get(word,0) + 1
            
for k,v in counts.items():
    newtup = (v,k)
    list.append(newtup)
list = sorted(list, reverse = True)
for val, key in list[:1]:
    print(key,val)
  
"""

""" # Ans2

list = []
counts = dict()
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    if line.startswith('From'):
        if not line.startswith('From:'):
            words = line.split()
            word = words[5]
            ram = word.split(':')
            hour = ram[0]
            counts[hour] = counts.get(hour,0) + 1
            
for k,v in counts.items():
    newtup = (k,v)
    list.append(newtup)
list = sorted(list, reverse = False)
for key,val in list:
    print(key,val)
  
"""

# Ans3 (Incomplete)

list = []
counts = dict()
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    




















             