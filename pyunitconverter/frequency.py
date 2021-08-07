"""Frequency units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for frequency.
"""


# Hertz

def hertz_to_millihertz(value):
	result = value * 1000
	return result

def hertz_to_kilohertz(value):
	result = value / 1000
	return result

def hertz_to_megahertz(value):
	result = value / 1000000
	return result

def hertz_to_gigahertz(value):
	result = value / 1000000000
	return result

def hertz_to_terahertz(value):
	result = value / 1000000000000
	return result

# Millihertz

def millihertz_to_hertz(value):
	result = value / 1000
	return result

def millihertz_to_kilohertz(value):
	result = value / 1000000
	return result

def millihertz_to_megahertz(value):
	result = value / 1000000000
	return result

def millihertz_to_gigahertz(value):
	result = value / 1000000000000
	return result

def millihertz_to_terahertz(value):
	result = value / 1000000000000000
	return result

# Kilohertz

def kilohertz_to_hertz(value):
	result = value * 1000
	return result

def kilohertz_to_millihertz(value):
	result = value * 1000000
	return result

def kilohertz_to_megahertz(value):
	result = value / 1000
	return result

def kilohertz_to_gigahertz(value):
	result = value / 1000000
	return result

def kilohertz_to_terahertz(value):
	result = value / 1000000000
	return result

# Megahertz

def megahertz_to_hertz(value):
	result = value * 1000000
	return result

def megahertz_to_millihertz(value):
	result = value * 1000000000
	return result

def megahertz_to_kilohertz(value):
	result = value * 1000
	return result

def megahertz_to_gigahertz(value):
	result = value / 1000
	return result

def megahertz_to_terahertz(value):
	result = value / 1000000
	return result

# Gigahertz

def gigahertz_to_hertz(value):
	result = value * 1000000000
	return result

def gigahertz_to_millihertz(value):
	result = value * 1000000000000
	return result

def gigahertz_to_kilohertz(value):
	result = value * 1000000
	return result

def gigahertz_to_megahertz(value):
	result = value * 1000
	return result

def gigahertz_to_terahertz(value):
	result = value / 1000
	return result

# Terahertz

def terahertz_to_hertz(value):
	result = value * 1000000000000
	return result

def terahertz_to_millihertz(value):
	result = value * 1000000000000000
	return result

def terahertz_to_kilohertz(value):
	result = value * 1000000000
	return result

def terahertz_to_megahertz(value):
	result = value * 1000000
	return result

def terahertz_to_gigahertz(value):
	result = value * 1000
	return result
