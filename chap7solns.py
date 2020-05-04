#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 11:16:40 2020

@author: parthrajauria
"""
""" # Ans 1 (not completed)
fname = input('Enter a file name: ')
fhand = open(fname)
for line in fhand:
    for word in line:
        word.upper()
        print(word)
        
"""        

""" # Ans 2
count = 0
total = 0
fname = input('Enter a File name: ')
fhand = open(fname)
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        num_str = line[19:]
        num = float(num_str)
        count = count + 1
        total = total + num
        
print('Average Spam confidence', total/count)        
        
"""


""" # Ans3 (incomplete)
count = 0
fname = input('Enter a File name: ')
if fname is "na na boo boo":
    print('NA NA BOO BOO TO YOU - You have been punk\'d')
else:
        
    fhand = open(fname)
    for line in fhand:
        if line.startswith('X-DSPAM-Confidence:'):
            count = count + 1
    print(count)    
"""


