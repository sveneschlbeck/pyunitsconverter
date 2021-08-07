"""Area units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for area.
"""


# Hectare

def hectare_to_are(value):
	result = value * 100
	return result

def hectare_to_squaremeter(value):
	result = value * 10000
	return result

def hectare_to_squarefeet(value):
	result = value * 107639
	return result

def hectare_to_squarekilometer(value):
	result = value * 0.01
	return result

def hectare_to_squaremile(value):
	result = value * 0.00386102
	return result

# Are

def are_to_hectare(value):
	result = value / 100
	return result

def are_to_squaremeter(value):
	result = value * 100
	return result

def are_to_squarefeet(value):
	result = value * 1076.391042
	return result

def are_to_squarekilometer(value):
	result = value * 0.0001
	return result

def are_to_squaremile(value):
	result = value * 0.00003861021
	return result

# Squaremeter

def squaremeter_to_hectare(value):
	result = value / 10000
	return result

def squaremeter_to_are(value):
	result = value / 100
	return result

def squaremeter_to_squarefeet(value):
	result = value * 10.7639
	return result

def squaremeter_to_squarekilometer(value):
	result = value / 1000000
	return result

def squaremeter_to_squaremile(value):
	result = value / 2589988.110336
	return result

# Squarefeet

def squarefeet_to_hectare(value):
	result = value * 0.0000092903
	return result

def squarefeet_to_are(value):
	result = value * 0.00092903
	return result

def squarefeet_to_squarekilometer(value):
	result = value * 0.00000009290304
	return result

def squarefeet_to_squaremeter(value):
	result = value * 0.092903
	return result

def squarefeet_to_squaremile(value):
	result = value * 0.00000004
	return result

# Squarekilometer

def squarekilometer_to_hectare(value):
	result = value * 10
	return result

def squarekilometer_to_are(value):
	result = value * 10000
	return result

def squarekilometer_to_squarefeet(value):
	result = value * 10763910.41671
	return result

def squarekilometer_to_squaremeter(value):
	result = value * 1000000
	return result

def squarekilometer_to_squaremile(value):
	result = value  * 0.386102
	return result

# Squaremile

def squaremile_to_hectare(value):
	result = value / 0.00386102
	return result

def squaremile_to_are(value):
	result = value / 0.00003861021
	return result

def squaremile_to_squarefeet(value):
	result = value / 0.00000004
	return result

def squaremile_to_squaremeter(value):
	result = value * 2589988.110336
	return result

def squaremile_to_squarekilometer(value):
	result = value  / 0.386102
	return result
