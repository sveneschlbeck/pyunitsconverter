"""Length units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for length, both metrical and non-metrical units.
"""


##############################################
############# METRIC-TO-METRIC ###############
##############################################

# Scale-Up

# Nanometer

def nanometer_to_micrometer(value):
	result = value / 1000
	return result

def nanometer_to_millimeter(value):
	result = value / 1000000
	return result

def nanometer_to_centimeter(value):
	result = value / 10000000
	return result

def nanometer_to_decimeter(value):
	result = value / 100000000
	return result

def nanometer_to_meter(value):
	result = value / 1000000000
	return result

def nanometer_to_kilometer(value):
	result = value / 1000000000000
	return result

# Micrometer

def micrometer_to_millimeter(value):
	result = value / 1000
	return result

def micrometer_to_centimeter(value):
	result = value / 10000
	return result

def micrometer_to_decimeter(value):
	result = value / 100000
	return result

def micrometer_to_meter(value):
	result = value / 1000000
	return result

def micrometer_to_kilometer(value):
	result = value / 1000000000
	return result

# Millimeter

def millimeter_to_centimeter(value):
	result = value / 10
	return result

def millimeter_to_decimeter(value):
	result = value / 100
	return result

def millimeter_to_meter(value):
	result = value / 1000
	return result

def millimeter_to_kilometer(value):
	result = value / 1000000
	return result

# Centimeter

def centimeter_to_decimeter(value):
	result = value / 10
	return result

def centimeter_to_meter(value):
	result = value / 100
	return result

def centimeter_to_kilometer(value):
	result = value / 100000
	return result

# Decimeter

def decimeter_to_meter(value):
	result = value / 10
	return result

def decimeter_to_kilometer(value):
	result = value / 10000
	return result

# Meter

def meter_to_kilometer(value):
	result = value / 1000
	return result


# Scale-Down

# Kilometer

def kilometer_to_meter(value):
	result = value * 1000
	return result

def kilometer_to_decimeter(value):
	result = value * 10000
	return result

def kilometer_to_centimeter(value):
	result = value * 100000
	return result

def kilometer_to_millimeter(value):
	result = value * 1000000
	return result

def kilometer_to_micrometer(value):
	result = value * 1000000000
	return result

def kilometer_to_nanometer(value):
	result = value * 1000000000000
	return result

# Meter

def meter_to_decimeter(value):
	result = value * 10
	return result

def meter_to_centimeter(value):
	result = value * 100
	return result

def meter_to_millimeter(value):
	result = value * 1000
	return result

def meter_to_micrometer(value):
	result = value * 1000000
	return result

def meter_to_nanometer(value):
	result = value * 1000000000
	return result

# Decimeter

def decimeter_to_centimeter(value):
	result = value * 10
	return result

def decimeter_to_millimeter(value):
	result = value * 100
	return result

def decimeter_to_micrometer(value):
	result = value * 100000
	return result

def decimeter_to_nanometer(value):
	result = value * 100000000
	return result

# Centimeter

def centimeter_to_millimeter(value):
	result = value * 10
	return result 

def centimeter_to_micrometer(value):
	result = value * 10000
	return result

def centimeter_to_nanometer(value):
	result = value * 10000000
	return result

# Millimeter

def millimeter_to_micrometer(value):
	result = value * 1000
	return result

def millimeter_to_nanometer(value):
	result = value * 1000000
	return result

# Micrometer

def micrometer_to_nanometer(value):
	result = value * 1000
	return result



#######################################################
############## NON-METRIC-TO-NON-METRIC ###############
#######################################################

# Scale-Up

# Inch

def inch_to_feet(value):
	result = value * 0.0833333
	return result

def inch_to_yard(value):
	result = value * 0.0277778
	return result

def inch_to_mile(value):
	result = value / 63360
	return result

# Feet

def feet_to_yard(value):
	result = value / 3
	return result

def feet_to_mile(value):
	result = value / 5280
	return result

# Yard

def yard_to_mile(value):
	result = value / 1760
	return result


# Scale-Down

# Mile

def mile_to_yard(value):
	result = value * 1760
	return result

def mile_to_feet(value):
	result = value * 5280
	return result

def mile_to_inch(value):
	result = value * 63360
	return result

# Yard

def yard_to_feet(value):
	result = value * 3
	return result

def yard_to_inch(value):
	result = value / 0.0277778
	return result

# Feet

def feet_to_inch(value):
	result = value / 0.0833333
	return result



###################################################
############## METRIC-TO-NON-METRIC ###############
###################################################

# One-Way

# Nanometer

def nanometer_to_inch(value):
	result = value * (3.93701 * 10**-8)
	return result

def nanometer_to_feet(value):
	result = value * (3.28084 * 10**-9)
	return result

def nanometer_to_yard(value):
	result = value * (1.09361 * 10**-9)
	return result

def nanometer_to_mile(value):
	result = value * (6.2137 * 10**-13)
	return result

# Micrometer

def micrometer_to_inch(value):
	result = value * (3.93701 * 10**-5)
	return result

def micrometer_to_feet(value):
	result = value * (3.28084 * 10**-6)
	return result

def micrometer_to_yard(value):
	result = value * (1.09361 * 10**-6)
	return result

def micrometer_to_mile(value):
	result = value * (6.21371 * 10**-10)
	return result

# Millimeter

def millimeter_to_inch(value):
	result = value * 0.0393701
	return result

def millimeter_to_feet(value):
	result = value * 0.00328084
	return result

def millimeter_to_yard(value):
	result = value * 0.00109361
	return result

def millimeter_to_mile(value):
	result = value * (6.2137 * 10**-7)
	return result

# Centimeter

def centimeter_to_inch(value):
	result = value * 0.393701
	return result

def centimeter_to_feet(value):
	result = value * 0.0328084
	return result

def centimeter_to_yard(value):
	result = value * 0.0109361
	return result

def centimeter_to_mile(value):
	result = value * (6.2137 * 10**-6)
	return result

# Decimeter

def decimeter_to_inch(value):
	result = value * 3.93701
	return result

def decimeter_to_feet(value):
	result = value * 0.328084
	return result

def decimeter_to_yard(value):
	result = value * 0.109361
	return result

def decimeter_to_mile(value):
	result = value * (6.21371 * 10**-5)
	return result

# Meter

def meter_to_inch(value):
	result = value * 0.0254
	return result

def meter_to_feet(value):
	result = value * 3.28084
	return result

def meter_to_yard(value):
	result = value * 1.09361
	return result

def meter_to_mile(value):
	result = value * 0.000621371
	return result

# Kilometer

def kilometer_to_inch(value):
	result = value * 39370.1
	return result

def kilometer_to_feet(value):
	result = value * 3280.84
	return result

def kilometer_to_yard(value):
	result = value * 1093.61
	return result

def kilometer_to_mile(value):
	result = value * 0.621371
	return result


# Other-Way

# Mile

def mile_to_kilometer(value):
	result = value * 1.60934
	return result

def mile_to_meter(value):
	result = value * 1.60934 * 1000
	return result

def mile_to_decimeter(value):
	result = value * 1.60934 * 1000 * 10
	return result

def mile_to_centimeter(value):
	result = value * 1.60934 * 1000 * 100
	return result

def mile_to_millimeter(value):
	result = value * 1.60934 * 1000 * 1000
	return result

def mile_to_micrometer(value):
	result = value * 1.60934 * 1000 * 1000000
	return result

def mile_to_nanometer(value):
	result = value * 1.60934 * 1000 * 1000000000
	return result

# Yard

def yard_to_kilometer(value):
	result = value * 0.0009144
	return result

def yard_to_meter(value):
	result = value * 0.9144
	return result

def yard_to_decimeter(value):
	result = value * 9.144
	return result

def yard_to_centimeter(value):
	result = value * 91.44
	return result

def yard_to_millimeter(value):
	result = value * 914.4
	return result

def yard_to_micrometer(value):
	result = value * 914.4 * 1000
	return result

def yard_to_nanometer(value):
	result = value * 914.4 * 1000000
	return result

# Feet

def feet_to_kilometer(value):
	result = value * 0.0003048
	return result

def feet_to_meter(value):
	result = value * 0.3048
	return result

def feet_to_decimeter(value):
	result = value * 3.048
	return result

def feet_to_centimeter(value):
	result = value * 30.48
	return result

def feet_to_millimeter(value):
	result = value * 304.8
	return result

def feet_to_micrometer(value):
	result = value * 304.8 * 1000
	return result

def feet_to_nanometer(value):
	result = value * 304.8 * 1000000
	return result

# Inch

def inch_to_kilometer(value):
	result = value * (2.54 * 10**-5)
	return result

def inch_to_meter(value):
	result = value * 0.0254
	return result

def inch_to_decimeter(value):
	result = value * 0.254
	return result

def inch_to_centimeter(value):
	result = value * 2.54
	return result

def inch_to_millimeter(value):
	result = value * 25.4
	return result

def inch_to_micrometer(value):
	result = value * 25.4 * 1000
	return result

def inch_to_nanometer(value):
	result = value * 25.4 * 1000000
	return result
