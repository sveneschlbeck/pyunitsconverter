"""Volume units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for volume.
"""


# Liter

def liter_to_milliliter(value):
	result = value * 1000
	return result

def liter_to_hectoliter(value):
	result = value / 100
	return result

def liter_to_m3(value):
	result = value / 1000
	return result

# Milliliter

def milliliter_to_liter(value):
	result = value / 1000
	return result

def milliliter_to_hectoliter(value):
	result = value / 100000
	return result

def milliliter_to_m3(value):
	result = value / 1000000
	return result

# Hectoliter

def hectoliter_to_liter(value):
	result = value * 100
	return result

def hectoliter_to_milliliter(value):
	result = value * 100000
	return result

def hectoliter_to_m3(value):
	result = value / 10
	return result

# Cubic meter (m3)

def m3_to_liter(value):
	result = value * 1000
	return result

def m3_to_milliliter(value):
	result = value * 1000000
	return result

def m3_to_hectoliter(value):
	result = value * 10
	return result
	