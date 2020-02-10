#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 06:42:17 2020
Revised on Mon Feb 10 14:51:07 2020

ABE 651 - Environmental Informatics; Think Python Chapter 3: Exercises 3.2 (ThinkPython2)

Programm Description:
The following script has been written for Exercise 3.4 of Think Python Edition one. 
This program is about defining "function" with function object and value and then calling the function.
It also uses an in-built function "len". This program has 5 parts with Exercise 3.4 has five parts.

@author: tiwari13 (Alka Tiwari)
"""

#program contains two function definitions, print_lyrics and repeat_lyrics
# create print_lyrics() function
def print_lyrics():
    print("I am Lumberjack, and I am okay.")
    print("I asleep all night and I work all day.")
 
# create function repea_lyrics()
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
#call the function   
repeat_lyrics()
    
#Exercise3.1-Function call appear before the definitions
#call the function   
repeat_lyrics()

def print_lyrics():
    print("I am Lumberjack, and I am okay.")
    print("I asleep all night and I work all day.")
 
# create function repea_lyrics()
def repeat_lyrics():
    print_lyrics()
    print_lyrics()

#calling function before creating it is giving similar result
    
#Exercise3.2-move definition of print_lyrics() after definition of repeat_lyrics()

# create function repea_lyrics()
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
    
def print_lyrics():
    print("I am Lumberjack, and I am okay.")
    print("I asleep all night and I work all day.")
 
#call the function   
repeat_lyrics()

#this also gives similar result
#Exercise3.3-Function named right_justify that takes a string named as a parameter 
#and print the string with enough leading spaces so that the last letter of the string 
#is in column 70 of the dissplay
len('allen')
def right_justify(a):
    print(' '*(70-len(a))+a)
    
right_justify('allen')

#Exercise3.4 - 
#1. type and test the script of do_twice
def do_twice(f):
    f()
    f()

def print_spam():
    print ('spam')
    
do_twice(print_spam)

#2.Modify do_twice so that it takes two arguments, a function object and a value
#and calls the function twice, passing the value as an argument.
def do_twice(f,val):
    f(val)
    f(val)

#3. Write more general version of print_spam, call print_twice that takes string as a parameter 
#and prits it twice
def print_twice(spam):
    print ('spam')
    print ('spam')
    
#4. Use the modified verison of do_twice to call print_twice, passing spam as an argument
do_twice(print_twice,'spam')

#5.Define anew function called do_four that takes a function object and a value and 
#calls the fuction four times, passing the value as parameter
def do_four(f,val):
    print(do_twice(f,val))
    print(do_twice(f,val))
    
do_four(print_twice, 'spam')





    


