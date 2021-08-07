"""Time units

# @see https://www.nist.gov/pml/weights-and-measures/metric-si/si-units
# @see https://www.bipm.org/en/home

This module contains functions converting common units for time.
"""


# Nanosecond

def nanosecond_to_millisecond(value):
	result = value / 1000
	return result

def nanosecond_to_second(value):
	result = value / 1000000
	return result

def nanosecond_to_minute(value):
	result = value / (1000000 * 60)
	return result

def nanosecond_to_hour(value):
	result = value / (1000000 * 60 * 60)
	return result

def nanosecond_to_day(value):
	result = value / 86400000000
	return result

def nanosecond_to_week(value):
	result = value / (86400000000 * 7)
	return result

def nanosecond_to_month(value):
	result = value / (86400000000 * 28)
	return result

def nanosecond_to_year(value):
	result = value / (86400000000 * 365)
	return result

def nanosecond_to_decade(value):
	result = value / (86400000000 * 3650)
	return result

def nanosecond_to_century(value):
	result = value / (86400000000 * 36500)
	return result

# Millisecond

def millisecond_to_nanosecond(value):
	result = value * 1000
	return result

def millisecond_to_second(value):
	result = value / 1000
	return result

def millisecond_to_minute(value):
	result = value / (1000 * 60)
	return result

def millisecond_to_hour(value):
	result = value / (1000 * 3600)
	return result

def millisecond_to_day(value):
	result = value / 86400000
	return result

def millisecond_to_week(value):
	result = value / (86400000 * 7)
	return result

def millisecond_to_month(value):
	result = value / (86400000 * 28)
	return result

def millisecond_to_year(value):
	result = value / (86400000 * 365)
	return result

def millisecond_to_decade(value):
	result = value / (86400000 * 3650)
	return result

def millisecond_to_century(value):
	result = value / (86400000 * 36500)
	return result

# Second

def second_to_nanosecond(value):
	result = value * 1000000
	return result

def second_to_millisecond(value):
	result = value * 1000
	return result

def second_to_minute(value):
	result = value / 60
	return result

def second_to_hour(value):
	result = value / 3600
	return result

def second_to_day(value):
	result = value / 86400
	return result

def second_to_week(value):
	result = value / (86400 * 7)
	return result

def second_to_month(value):
	result = value / (86400 * 28)
	return result

def second_to_year(value):
	result = value / (86400 * 365)
	return result

def second_to_decade(value):
	result = value / (86400 * 3650)
	return result

def second_to_century(value):
	result = value / (86400 * 36500)
	return result

# Minute

def minute_to_nanosecond(value):
	result = value * 1000000 * 60
	return result

def minute_to_millisecond(value):
	result = value * 1000 * 60
	return result

def minute_to_second(value):
	result = value * 60
	return result

def minute_to_hour(value):
	result = value / 60
	return result

def minute_to_day(value):
	result = value / 1440

def minute_to_week(value):
	result = value / (1440 * 7)
	return result

def minute_to_month(value):
	result = value / (1440 * 28)
	return result

def minute_to_year(value):
	result = value / (1440 * 365)
	return result

def minute_to_decade(value):
	result = value / (1440 * 3650)
	return result

def minute_to_century(value):
	result = value / (1440 * 36500)
	return result

# Hour

def hour_to_nanosecond(value):
	result = value * 1000000 * 3600
	return result

def hour_to_millisecond(value):
	result = value * 1000 * 3600
	return result

def hour_to_second(value):
	result = value * 3600
	return result

def hour_to_minute(value):
	result = value * 60
	return result

def hour_to_day(value):
	result = value / 24
	return result

def hour_to_week(value):
	result = value / (24 * 7)
	return result

def hour_to_month(value):
	result = value / (24 * 28)
	return result

def hour_to_year(value):
	result = value / (24 * 365)
	return result

def hour_to_decade(value):
	result = value / (24 * 3650)
	return result

def hour_to_century(value):
	result = value / (24 * 36500)
	return result

# Week

def week_to_nanosecond(value):
	result = value * 604800000000000
	return result

def week_to_millisecond(value):
	result = value * 604800000000
	return result

def week_to_second(value):
	result = value * 604800000
	return result

def week_to_minute(value):
	result = value * 10080000
	return result

def week_to_hour(value):
	result = value * 168000
	return result

def week_to_day(value):
	result = value / 7
	return result

def week_to_month(value):
	result = value / 4
	return result

def week_to_year(value):
	result = value / 52
	return result

def week_to_decade(value):
	result = value / 520
	return result

def week_to_century(value):
	result = value / 5200
	return result

# Month

def month_to_nanosecond(value):
	result = value * 2592000000000000
	return result

def month_to_millisecond(value):
	result = value * 2592000000000
	return result

def month_to_second(value):
	result = value * 2592000000
	return result

def month_to_minute(value):
	result = value * 43200000
	return result

def month_to_hour(value):
	result = value * 720000
	return result

def month_to_day(value):
	result = value * 30.4167
	return result

def month_to_week(value):
	result = value * 4
	return result

def month_to_year(value):
	result = value / 12
	return result

def month_to_decade(value):
	result = value / 120
	return result

def month_to_century(value):
	result = value / 1200
	return result

# Year

def year_to_nanosecond(value):
	result = value * 31556952000000000
	return result

def year_to_millisecond(value):
	result = value * 31556952000000
	return result

def year_to_second(value):
	result = value * 31556952000
	return result

def year_to_minute(value):
	result = value * 525949200

def year_to_hour(value):
	result = value * 8765820
	return result

def year_to_day(value):
	result = value * 365
	return result

def year_to_week(value):
	result = value * 52
	return result

def year_to_month(value):
	result = value * 12
	return result

def year_to_decade(value):
	result = value / 10
	return result

def year_to_century(value):
	result = value / 100
	return result

# Decade

def decade_to_nanosecond(value):
	result = value * 315569520000000000
	return result

def decade_to_millisecond(value):
	result = value * 315569520000000
	return result

def decade_to_second(value):
	result = value * 315569520000
	return result

def decade_to_minute(value):
	result = value * 5259492000
	return result

def decade_to_hour(value):
	result = value * 87658200
	return result

def decade_to_day(value):
	result = value * 3650
	return result

def decade_to_week(value):
	result = value * 520
	return result

def decade_to_month(value):
	result = value * 120
	return result

def decade_to_year(value):
	result = value * 10
	return result

def decade_to_century(value):
	result = value / 10
	return result

# Century

def century_to_nanosecond(value):
	result = value * 3155695200000000000
	return result

def century_to_millisecond(value):
	result = value * 3155695200000000
	return result

def century_to_second(value):
	result = value * 3155695200000
	return result

def century_to_minute(value):
	result = value * 52594920000
	return result

def century_to_hour(value):
	result = value * 876582000
	return result

def century_to_day(value):
	result = value * 36500
	return result

def century_to_week(value):
	result = value * 5200
	return result

def century_to_month(value):
	result = value * 1200
	return result

def century_to_year(value):
	result = value * 100
	return result

def century_to_decade(value):
	result = value * 10
	return result
