"""Power units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for power.
"""


# English Horsepower (HP)

def HP_to_watt(value):
	result = value * 745.7
	return result

def HP_to_kilowatt(value):
	result = value * 0.7457
	return result

def HP_to_megawatt(value):
	result = value * 0.0007457
	return result

def HP_to_gigawatt(value):
	result = value * 0.0000007457
	return result

# Watt

def watt_to_HP(value):
	result = value / 745.7
	return result

def watt_to_kilowatt(value):
	result = value / 1000
	return result

def watt_to_megawatt(value):
	result = value / 1000000
	return result

def watt_to_gigawatt(value):
	result = value / 1000000000
	return result

# Kilowatts

def kilowatt_to_HP(value):
	result = value / 0.7457
	return result

def kilowatt_to_megawatt(value):
	result = value / 1000
	return result

def kilowatt_to_gigawatt(value):
	result = value / 1000000
	return result

def kilowatt_to_watt(value):
	result = value * 1000
	return result

# Megawatts

def megawatt_to_HP(value):
	result = value / 0.0007457
	return result

def megawatt_to_gigawatt(value):
	result = value / 1000
	return result

def megawatt_to_watt(value):
	result = value * 1000000
	return result

def megawatt_to_kilowatt(value):
	result = value * 1000
	return result

# Gigawatts

def gigawatt_to_HP(value):
	result = value / 0.0000007457
	return result

def gigawatt_to_watt(value):
	result = value * 1000000000
	return result

def gigawatt_to_kilowatt(value):
	result = value * 1000000
	return result

def gigawatt_to_megawatt(value):
	result = value * 1000
	return result
