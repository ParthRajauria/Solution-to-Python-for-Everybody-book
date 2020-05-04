#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 23:12:55 2020

@author: parthrajauria
"""

# Ans1
#import random
#
#for i in range(10):
#    x = random.random()
#    print(x)

""" Ans 2 """


#def print_lyrics():
#    print("I'm a lumberjack, and I'm okay. ")
#
#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()
#repeat_lyrics()    

""" Ans3 """

#def repeat_lyrics():
#    print_lyrics()
#    print_lyrics()
##def print_lyrics():
##    print("I'm a lumberjack, and I'm okay. ")
#        
#repeat_lyrics() 
##def print_lyrics():
##    print("I'm a lumberjack, and I'm okay. ")

""" Ans4 """

def computepay(a,b):
  
   
    if a or b < 0:
        print ('Please enter integer values greater than or equal to 0')
    elif a < 40:
        return (a*b)
    elif a > 40:
        return ((a-40)*1.5*b + 40*b)


computepay(45,6)











