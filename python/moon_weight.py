#!/usr/bin/env python
# encoding: utf-8
"""
moon_weight.py
"""

import sys
import os
	
def moon_weight(weight):		
	return round(weight * 0.165, 2)

def calculate_weight():
	earth_weight = float(input("Please enter your current Earth weight?: "))
	gain = float(input("Please enter the amount your weight might increase each year?: "))
	years = int(input("Please enter the number of years?: "))
	
	for year in range(1, years):
		earth_weight = earth_weight + gain        
		print('Year %s is %skg' % (year, moon_weight(earth_weight)))
		
calculate_weight()
	




