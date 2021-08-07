"""Amperage units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for amperage.
"""


# Ampere

def ampere_to_milliampere(value):
	result = value * 1000
	return result

def ampere_to_microampere(value):
	result = value * 1000000
	return result

def ampere_to_megaampere(value):
	result = value / 1000000
	return result

# Milliampere

def milliampere_to_ampere(value):
	result = value / 1000
	return result

def milliampere_to_microampere(value):
	result = value * 1000
	return result

def milliampere_to_megaampere(value):
	result = value / 1000000000
	return result

# Microampere

def microampere_to_milliampere(value):
	result = value * 1000
	return result

def microampere_to_ampere(value):
	result = value / 1000000
	return result

def microampere_to_megaampere(value):
	result = value / 1000000000000
	return result

# Megaampere

def megaampere_to_ampere(value):
	result = value * 1000000
	return result

def megaampere_to_milliampere(value):
	result = value * 1000000000
	return result

def megaampere_to_microampere(value):
	result = value * 1000000000000
	return result
	