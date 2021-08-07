"""Mass units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for mass, both metrical and non-metrical units.
"""


##############################################
############# METRIC-TO-METRIC ###############
##############################################

# Scale-Up

# Nanogram

def nanogram_to_microgram(value):
	result = value / 1000
	return result

def nanogram_to_milligram(value):
	result = value / 1000000
	return result

def nanogram_to_centigram(value):
	result = value / 10000000
	return result

def nanogram_to_decigram(value):
	result = value / 100000000
	return result

def nanogram_to_gram(value):
	result = value / 1000000000
	return result

def nanogram_to_kilogram(value):
	result = value / 1000000000000
	return result

def nanogram_to_ton(value):
	result = value / 1000000000000000
	return result

# Microgram

def microgram_to_milligram(value):
	result = value / 1000
	return result

def microgram_to_centigram(value):
	result = value / 10000
	return result

def microgram_to_decigram(value):
	result = value / 100000
	return result

def microgram_to_gram(value):
	result = value / 1000000
	return result

def microgram_to_kilogram(value):
	result = value / 1000000000
	return result

def microgram_to_ton(value):
	result = value / 1000000000000
	return result

# Milligram

def milligram_to_centigram(value):
	result = value / 10
	return result

def milligram_to_decigram(value):
	result = value / 100
	return result

def milligram_to_gram(value):
	result = value / 1000
	return result

def milligram_to_kilogram(value):
	result = value / 1000000
	return result

def milligram_to_ton(value):
	result = value / 1000000000
	return result

# Centigram

def centigram_to_decigram(value):
	result = value / 10
	return result

def centigram_to_gram(value):
	result = value / 100
	return result

def centigram_to_kilogram(value):
	result = value / 100000
	return result

def centigram_to_ton(value):
	result = value / 100000000
	return result

# Decigram

def decigram_to_gram(value):
	result = value / 10
	return result

def decigram_to_kilogram(value):
	result = value / 10000
	return result

def decigram_to_ton(value):
	result = value / 10000000
	return result

# Gram

def gram_to_kilogram(value):
	result = value / 1000
	return result

def gram_to_ton(value):
	result = value / 1000000
	return result


# Scale-Down

# Ton

def ton_to_gram(value):
	result = value * 1000000
	return result

def ton_to_decigram(value):
	result = value * 10000000
	return result

def ton_to_centigram(value):
	result = value * 100000000
	return result

def ton_to_milligram(value):
	result = value * 1000000000
	return result

def ton_to_microgram(value):
	result = value * 1000000000000
	return result

def ton_to_nanogram(value):
	result = value * 1000000000000000
	return result

# Kilogram

def kilogram_to_gram(value):
	result = value * 1000
	return result

def kilogram_to_decigram(value):
	result = value * 10000
	return result

def kilogram_to_centigram(value):
	result = value * 100000
	return result

def kilogram_to_milligram(value):
	result = value * 1000000
	return result

def kilogram_to_microgram(value):
	result = value * 1000000000
	return result

def kilogram_to_nanogram(value):
	result = value * 1000000000000
	return result

# Gram

def gram_to_decigram(value):
	result = value * 10
	return result

def gram_to_centigram(value):
	result = value * 100
	return result

def gram_to_milligram(value):
	result = value * 1000
	return result

def gram_to_microgram(value):
	result = value * 1000000
	return result

def gram_to_nanogram(value):
	result = value * 1000000000
	return result

# Decigram

def decigram_to_centigram(value):
	result = value * 10
	return result

def decigram_to_milligram(value):
	result = value * 100
	return result

def decigram_to_microgram(value):
	result = value * 100000
	return result

def decigram_to_nanogram(value):
	result = value * 100000000
	return result

# Centigram

def centigram_to_milligram(value):
	result = value * 10
	return result 

def centigram_to_microgram(value):
	result = value * 10000
	return result

def centigram_to_nanogram(value):
	result = value * 10000000
	return result

# Milligram

def milligram_to_microgram(value):
	result = value * 1000
	return result

def milligram_to_nanogram(value):
	result = value * 1000000
	return result

# Microgram

def microgram_to_nanogram(value):
	result = value * 1000
	return result



#######################################################
############## NON-METRIC-TO-NON-METRIC ###############
#######################################################

# Karat

def karat_to_ounce(value):
	result = value / 141.748
	return result

def karat_to_pound(value):
	result = value * 0.000440925
	return result

# Ounce

def ounce_to_karat(value):
	result = value * 141.748
	return result

def ounce_to_pound(value):
	result = value * 0.0625
	return result

# Pound

def pound_to_karat(value):
	result = value / 0.000440925
	return result

def pound_to_ounce(value):
	result = value / 0.0625
	return result



###################################################
############## METRIC-TO-NON-METRIC ###############
###################################################

# One-Way

# Nanogram

def nanogram_to_karat(value):
	result = value * (5 * 10**-9)
	return result

def nanogram_to_ounce(value):
	result = value * (3.5274 * 10**-11)
	return result

def nanogram_to_pound(value):
	result = value * (2.20462 * 10**-12)
	return result

# Microgram

def microgram_to_karat(value):
	result = value * (5 * 10**-6)
	return result

def microgram_to_ounce(value):
	result = value * (3.5274 * 10**-8)
	return result

def microgram_to_pound(value):
	result = value * (2.20462 * 10**-9)
	return result

# Milligram

def milligram_to_karat(value):
	result = value * (5 * 10**-3)
	return result

def milligram_to_ounce(value):
	result = value * (3.5274 * 10**-5)
	return result

def milligram_to_pound(value):
	result = value * (2.20462 * 10**-6)
	return result

# Centigram

def centigram_to_karat(value):
	result = value * (5 * 10**-2)
	return result

def centigram_to_ounce(value):
	result = value * (3.5274 * 10**-4)
	return result

def centigram_to_pound(value):
	result = value * (2.20462 * 10**-5)
	return result

# Decigram

def decigram_to_karat(value):
	result = value * (5 * 10**-1)
	return result

def decigram_to_ounce(value):
	result = value * (3.5274 * 10**-3)
	return result

def decigram_to_pound(value):
	result = value * (2.20462 * 10**-4)
	return result

# Gram

def gram_to_karat(value):
	result = value * 5
	return result

def gram_to_ounce(value):
	result = value * (3.5274 * 10**-2)
	return result

def gram_to_pound(value):
	result = value * (2.20462 * 10**-3)
	return result

# Kilogram

def kilogram_to_karat(value):
	result = value * 5 * 1000
	return result

def kilogram_to_ounce(value):
	result = value * (3.5274 * 10**-2 * 1000)
	return result

def kilogram_to_pound(value):
	result = value * (2.20462 * 10**-3 * 1000)
	return result

# Ton

def ton_to_karat(value):
	result = value * 5 * 1000 * 1000
	return result

def ton_to_ounce(value):
	result = value * (3.5274 * 10**-2 * 1000 * 1000)
	return result

def ton_to_pound(value):
	result = value * (2.20462 * 10**-3 * 1000 * 1000)
	return result


# Other-Way

# Karat

def karat_to_nanogram(value):
	result = value / (5 * 10**-9)
	return result

def karat_to_microgram(value):
	result = value / (5 * 10**-6)
	return result

def karat_to_milligram(value):
	result = value / (5 * 10**-3)
	return result

def karat_to_centigram(value):
	result = value / (5 * 10**-2)
	return result

def karat_to_decigram(value):
	result = value / (5 * 10**-1)
	return result

def karat_to_gram(value):
	result = value / 5
	return result

def karat_to_kilogram(value):
	result = value / 5000
	return result

def karat_to_ton(value):
	result = value / 5000000
	return result

# Ounce

def ounce_to_nanogram(value):
	result = value / (3.5274 * 10**-11)
	return result

def ounce_to_microgram(value):
	result = value / (3.5274 * 10**-8)
	return result

def ounce_to_milligram(value):
	result = value / (3.5274 * 10**-5)
	return result

def ounce_to_centigram(value):
	result = value / (3.5274 * 10**-4)
	return result

def ounce_to_decigram(value):
	result = value / (3.5274 * 10**-3)
	return result

def ounce_to_gram(value):
	result = value / (3.5274 * 10**-2)
	return result

def ounce_to_kilogram(value):
	result = value / (3.5274 * 10**-2 * 1000)
	return result

def ounce_to_ton(value):
	result = value / (3.5274 * 10**-2 * 1000 * 1000)
	return result

# Pound

def pound_to_nanogram(value):
	result = value / (2.20462 * 10**-12)
	return result

def pound_to_microgram(value):
	result = value / (2.20462 * 10**-9)
	return result

def pound_to_milligram(value):
	result = value / (2.20462 * 10**-6)
	return result

def pound_to_centigram(value):
	result = value / (2.20462 * 10**-5)
	return result

def pound_to_decigram(value):
	result = value / (2.20462 * 10**-4)
	return result

def pound_to_gram(value):
	result = value / (2.20462 * 10**-3)
	return result

def pound_to_kilogram(value):
	result = value / (2.20462 * 10**-3 * 1000)
	return result

def pound_to_ton(value):
	result = value / (2.20462 * 10**-3 * 1000 * 1000)
	return result
