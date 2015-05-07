#!/usr/bin/env python
# encoding: utf-8
"""
favourites.py
"""

import sys
import os

games = ['surfing', 'swimming', 'rock climbing',
               'watching movies', 'eating', 'hanging out']

food = ['butter chicken', 'pizza', 'ice cream',
				'cereal', 'oats']

favourites = games + food

print ("Favourites")
print ("----------")
print (favourites)

print ("Favourites")
print ("----------")
for x in range(0, len(favourites)):
	print (x, favourites[x])

favourites.sort()
print ("Favourites")
print ("----------")
for x in range(0, len(favourites)):
	print (x, favourites[x])

