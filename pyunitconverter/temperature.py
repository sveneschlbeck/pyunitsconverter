"""Temperature units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for temperature.
"""


# Celcius

def celcius_to_fahrenheit(value):
	result = value * (9/5) + 32
	return result

def celcius_to_kelvin(value):
	result = value + 273.15
	return result

def celcius_to_rankine(value):
	result = value * (9/5) + 491.67
	return result

def celcius_to_reaumur(value):
	result = value * (4/5)
	return result

# Fahrenheit

def fahrenheit_to_celcius(value):
	result = (value - 32) * (5/9)
	return result

def fahrenheit_to_kelvin(value):
	result = (value - 32) * (5/9) + 273.15
	return result

def fahrenheit_to_rankine(value):
	result = value + 459.67
	return result

def fahrenheit_to_reaumur(value):
	result = (value - 32) * 0.44444
	return result

# Kelvin

def kelvin_to_celcius(value):
	result = value - 273.15
	return result

def kelvin_to_fahrenheit(value):
	result = (value - 273.15) * (9/5) + 32
	return result

def kelvin_to_rankine(value):
	result = (value - 273.15) * 1.8 + 491.67
	return result

def kelvin_to_reaumur(value):
	result = 0.8 * (value - 273.15)
	return result

# Rankine

def rankine_to_celcius(value):
	result = (value - 491.67) * (5/9)
	return result

def rankine_to_fahrenheit(value):
	result = value - 491.67
	return result

def rankine_to_kelvin(value):
	result = value * (5/9)
	return result

def rankine_to_reaumur(value):
	result = (value - 491.67) * 0.44444
	return result

# Réaumur

def reaumur_to_celcius(value):
	result = value / 0.8
	return result

def reaumur_to_fahrenheit(value):
	result = (value * 2.25) + 32
	return result

def reaumur_to_kelvin(value):
	result = (value / 0.8) + 273.15
	return result

def reaumur_to_rankine(value):
	result = (value * 2.25) + 491.67
	return result
	