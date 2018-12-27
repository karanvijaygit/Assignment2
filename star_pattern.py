#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 12:19:58 2018

@author: karan
"""

# Program to print star pattern in a particular style
n = 5 # user input for max stars
k = 2*n - 1 # max. bound for ist dimension
for i in range(0,k):
    if i<n:
        for j in range(0,i+1):
            print("*", end = " ")
        print("\r")
    else:
        rev = k - i
        for j in range(0,rev):
            print("*", end = " ")
        print("\r")