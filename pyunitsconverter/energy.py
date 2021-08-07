"""Energy units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for energy.
"""


# Joule

def joule_to_kilojoule(value):
	result = value / 1000
	return result

def joule_to_kWh(value):
	result = value / 3600000
	return result

def joule_to_calorie(value):
	result = value / 4.184
	return result

def joule_to_BTU(value):
	result = value / 1055
	return result

# Kilojoule

def kilojoule_to_joule(value):
	result = value * 1000
	return result

def kilojoule_to_kWh(value):
	result = value / 3600
	return result

def kilojoule_to_calorie(value):
	result = value / 0.004184
	return result

def kilojoule_to_BTU(value):
	result = value / 1.055
	return result

# Kilowatt hour

def kWh_to_joule(value):
	result = value * 3600000
	return result

def kWh_to_kilojoule(value):
	result = value * 3600
	return result

def kWh_to_calorie(value):
	result = value * 860420.65
	return result

def kWh_to_BTU(value):
	result = value * 3410
	return result

# Calorie

def calorie_to_joule(value):
	result = value * 4.184
	return result

def calorie_to_kilojoule(value):
	result = value * 0.004184
	return result

def calorie_to_kWh(value):
	result = value / 860420.65
	return result

def calorie_to_BTU(value):
	result = value * 252
	return result

# BTU

def BTU_to_joule(value):
	result = value * 1055
	return result

def BTU_to_kilojoule(value):
	result = value * 1.055
	return result

def BTU_to_kWh(value):
	result = value / 3410
	return result

def BTU_to_calorie(value):
	result = value / 252
	return result
