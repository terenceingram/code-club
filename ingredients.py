#!/usr/bin/env python
# encoding: utf-8
"""
ingredinets.py
"""
import sys

ingredients = ['snails', 'leeches', 'gorilla belly-button lint',
               'caterpillar eyebrows', 'centipede toes']

ingredients.sort()

print ("Ingredients")
print ("-----------")
for x in range(0, len(ingredients)):
	print (x, ingredients[x])