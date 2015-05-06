#!/usr/bin/env python
# encoding: utf-8
"""
even_numbers.py
"""

your_age = int(input("What is your age?: "))
start = 1
if your_age % 2 == 0:
	print ("Your age is even")
	start = 0
else:
	print ("Your age is odd")
	start = 1

for i in range(start,your_age,2):
	print(i)





