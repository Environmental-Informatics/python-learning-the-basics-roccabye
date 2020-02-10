#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 09:40:34 2020
Revised on Mon Feb 10 14:53:17 2020

ABE 651 - Environmental Informatics; Think Python - Chapter 3: Exercises 3.3(Think Python2)

This Program is for Exercise 3.5 from first edition of Think Python.
Program Description: This program creates 2x2 and 4x4 grids using "+" and"-" symbol. using some functions.

@author: tiwari13 (Alka Tiwari)
"""

#Exercise3.5 - 1. Write a function that draws a grid like following

def do_twice(f):
    """
    create the function do_twice to call the object "f" twice.
    """
    f()
    f()

def do_four(f):
    """
    Create the function do_four to call the function object "f" four times by 
    calling the do_twice function twice
    """
    do_twice(f)
    do_twice(f)

def print_column():
    """
    Create the function print_column to create the row as +----+----+
    """
    print('+----+----+')
    
def print_row():
    """
    Create the function print_row to create the row as |    |    |    |
    """
    print('|    |    |')

def print_rows():
    """
    Create the function print_rows to create four row as |    |     |    |
    """
    do_four(print_row)

def do_block():
    """
    Create the function do_block to create a grid made of one row as +----+----+ and four rows as |    |    |    |   
    """
    print_column()
    print_rows()

def print_block():
    """
    Create the function print_block to make two grids made by function do_block and a row made by print_column
    """
    do_twice(do_block)
    print_column()

#Calling the function print_block to get 2x2 grid.   
print_block()


#2.Write  function that draws simialar grid with 4 rows and 4 column

def do_twice(f):
    """
    Create the function do_twice to call the function "f" twice.
    """
    f()
    f()

def do_four(f):
    """
    Create the function do_four to call the function "f" four times by calling the do_twice function twice.
    """
    do_twice(f)
    do_twice(f)

def print_column():
    """
    Create the function print_column to create the row as +----+----+----+----+
    """
    print('+----+----+----+----+')

def print_row():
    """
    Create the function print_row to create the row as |    |    |    |    |
    """
    print('|    |    |    |    |')

def print_rows():
    """
    Create the function print_rows to create four rows as |    |    |    |    |
    """
    do_four(print_row)

def do_block():
    """
    Create the function do_block to create a grid made of one row as +----+----+----+----+
    and four rows as |    |    |    |    |
    """
    print_column()
    print_rows()

def print_block():
    """
    Create the function print_block to make four grids made by function do_block
    and a row made by print_column.
    """
    do_twice(do_block)
    do_twice(do_block)
    print_column()

#Calling the function print_block to get 4x4 grid   
print_block()