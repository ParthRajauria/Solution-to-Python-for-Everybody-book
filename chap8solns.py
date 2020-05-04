#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 12:40:48 2020

@author: parthrajauria
"""

""" # Ans1
def chop(list):
    list.remove(list[0])
    list.remove(list[len(list)-1])
    return None

t = [1,2,4]
print(chop(t))

def middle(list):
    list.remove(list[0])
    list.remove(list[len(list)-1])
    print(list)

middle(t)
    
"""

 # Ans2 , Ans 3 are not programming questions
 
""" # Ans 4
list = []
fhand = open('romeo.txt')
#inp = fhand.read() # We should not use this.
for line in fhand:
    
    words = line.split() # Here words will be a list.
    for word in words:
        if word not in list:
            list.append(word)
        #else:
         #   continue
list.sort()   
print(list) 
"""

""" # Ans 5 
 
fopen = input('ENter a file name: ')
fhand = open(fopen)
count = 0
for line in fhand:
    if not line.startswith('From'):
        continue
    elif line.startswith('From:'):
        continue
    else:
        words = line.split()
        count = count + 1
        print(words[1])
print(f'There were {count} lines in the file with From as the first word')
        
"""

""" # Ans 6

list = [] 
while True:
    num = input('Enter a number: ')
    if num != 'done':
        num2 = int(num)
        list.append(num2)
        
    else:
        break
print('Maximum', max(list))
print('Minimum', min(list))    

"""





























 