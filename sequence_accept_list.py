#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:57:58 2018

@author: karan
"""
# Program to accept items from console and print them as a list
list = []
iter = 5
for i in range(iter):
    item = input("Enter list item: ")
    list.append(item)
print(list)