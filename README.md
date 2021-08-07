# **pyunitsconverter**
A package for easy unit conversions

*****
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/sveneschlbeck/pyunitsconverter)
![PyPI](https://img.shields.io/pypi/v/pyunitsconverter)
![PyPI - Status](https://img.shields.io/pypi/status/pyunitsconverter)
*****

## Project description

A python package for STEM students and scientific developers, aiming for easy and intuitive conversions of commonly used metric and non-metric units.

## Installation

Use ``pip`` to install ``pyunitsconverter`` by typing or copying the following command.
```python
pip install pyunitsconverter
```

## License

This package is licensed under ``MIT``.

## Supported physical quantities and units

The package currently includes the modules ``amperage``, ``area``, ``energy``, ``frequency``, ``length``, ``mass``, ``power``, ``pressure``, ``speed``, ``temperature``, ``time``, ``voltage``, ``volume``.  

- ``amperage`` supports **ampere, milliampere, microampere and megaampere**
- ``area`` supports **hectare, are, squaremeter, squarefeet, squarekilometer and squaremile**
- ``energy`` supports **joule, kilojoule, kWh, calorie and BTU**
- ``frequency`` supports **hertz, millihertz, kilohertz, megahertz, gigahertz and terahertz**
- ``length`` supports **nanometer, micrometer, millimeter, centimeter, decimeter, meter, kilometer, inch, feet, yard and mile**
- ``mass`` supports **nanogram, microgram, milligram, centigram, decigram, gram, kilogram, ton, karat, ounce and pound**
- ``power`` supports **HP, watt, kilowatt, megawatt and gigawatt**
- ``pressure`` supports **pascal, bar, torr, at and atm**
- ``speed`` supports **Kph, Mph, mps and knots**
- ``temperature`` supports **celcius, fahrenheit, kelvin, rankine and reaumur**
- ``time`` supports **nanosecond, millisecond, second, minute, hour, week, month, year, decade and century**
- ``voltage`` supports **volt, millivolt, microvolt and megavolt**
- ``volume`` supports **liter, milliliter, hectoliter and m3**

All of these units of one class can be converted into each other with the following syntax:
```python
<first_unit>_to_<second_unit>(<number>)
```
## Example usage

To convert units, you first need to import the relevant module and/or function. In the following example, we want to convert a length in kilometers into a length in miles.
```python
from length import *
```
Now, we can convert the number.
```python
kilometers_to_miles(100)
```

## Source code & further information

The source code is maintained at https://github.com/sveneschlbeck/pyunitsconverter  
There are also further information concerning the MIT license model, contributing guidelines and more...
