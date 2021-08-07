"""Voltage units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for voltage.
"""


# Volt

def volt_to_millivolt(value):
	result = value * 1000
	return result

def volt_to_microvolt(value):
	result = value * 1000000
	return result

def volt_to_megavolt(value):
	result = value / 1000000
	return result

# Millivolt

def millivolt_to_volt(value):
	result = value / 1000
	return result

def millivolt_to_microvolt(value):
	result = value * 1000
	return result

def millivolt_to_megavolt(value):
	result = value / 1000000000
	return result

# Microvolt

def microvolt_to_millivolt(value):
	result = value * 1000
	return result

def microvolt_to_volt(value):
	result = value / 1000000
	return result

def microvolt_to_megavolt(value):
	result = value / 1000000000000
	return result

# Megavolt

def megavolt_to_volt(value):
	result = value * 1000000
	return result

def megavolt_to_millivolt(value):
	result = value * 1000000000
	return result

def megavolt_to_microvolt(value):
	result = value * 1000000000000
	return result
