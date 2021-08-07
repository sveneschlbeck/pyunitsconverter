"""Pressure units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for pressure.
"""


# Pascal

def pascal_to_bar(value):
	result = value / 100000
	return result

def pascal_to_torr(value):
	result = value * 0.00750062
	return result

def pascal_to_at(value):
	result = value * 0.0000101971621298
	return result

def pascal_to_atm(value):
	result = value / 101325
	return result

# Bar

def bar_to_pascal(value):
	result = value * 100000
	return result

def bar_to_torr(value):
	result = value * 750.062
	return result

def bar_to_at(value):
	result = value * 1.0197162129779
	return result

def bar_to_atm(value):
	result = value * 0.986923
	return result

def bar_to_millibar(value):
	result = value * 1000
	return result

def millibar_to_bar(value):
	result = value / 1000
	return result

# Torr

def torr_to_bar(value):
	result = value * 0.00133322
	return result

def torr_to_pascal(value):
	result = value * 133.322
	return result

def torr_to_at(value):
	result = value * 0.0013595098063156
	return result

def torr_to_atm(value):
	result = value * 0.00131579
	return result

# Technical Atmosphere (at)

def at_to_bar(value):
	result = value / 1.0197162129779
	return result

def at_to_pascal(value):
	result = value / 0.0000101971621298
	return result

def at_to_torr(value):
	result = value * 735.561
	return result

def at_to_atm(value):
	result = value * 0.9678411053541
	return result

# Physical Atmosphere (atm)

def atm_to_at(value):
	result = value / 0.9678411053541
	return result

def atm_to_bar(value):
	result = value * 1.01325
	return result

def atm_to_pascal(value):
	result = value * 101325
	return result

def atm_to_torr(value):
	result = value / 0.00131579
	return result
