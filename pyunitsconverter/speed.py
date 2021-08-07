"""Speed units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for speed.
"""


# Kph

def Kph_to_Mph(value):
	result = value * 0.621371
	return result

def Kph_to_mps(value):
	result = value * 0.277778
	return result

def Kph_to_knots(value):
	result = value / 1.852

# Mph

def Mph_to_Kph(value):
	result = value / 0.621371
	return result

def Mph_to_mps(value):
	result = value * 0.44704
	return result

def Mph_to_knots(value):
	result = value * 0.868976
	return result

# mps

def mps_to_Kph(value):
	result = value / 0.277778
	return result

def mps_to_Mph(value):
	result = value / 0.44704
	return result

def mps_to_knots(value):
	result = value * 1.94384
	return result

# Knots

def knots_to_Kph(value):
	result = value * 1.852
	return result

def knots_to_Mph(value):
	result = value / 0.868976
	return result

def knots_to_mps(value):
	result = value / 1.94384
	return result
	