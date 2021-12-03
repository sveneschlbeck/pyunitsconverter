*****
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/sveneschlbeck/pyunitsconverter)
![GitHub top language](https://img.shields.io/github/languages/top/sveneschlbeck/pyunitsconverter)
![GitHub](https://img.shields.io/github/license/sveneschlbeck/pyunitsconverter)
![PyPI](https://img.shields.io/pypi/v/pyunitsconverter)
![Wheel](https://img.shields.io/pypi/wheel/pyunitsconverter)
*****

<p align="center">
  <img src="https://github.com/sveneschlbeck/pyunitsconverter/blob/main/logo.png" href="https://pypi.org/project/pyunitsconverter/">
</p>

## Project description

A python package for STEM students and scientific developers, aiming for easy and intuitive conversions of commonly used metric and non-metric units.

## Installation

Use ``pip`` to install ``pyunitsconverter`` by typing or copying the following command.
```python
pip install pyunitsconverter
```

## License

This package is licensed under ``BSD Clause 3``.

## Example usage

Users of the package can import the individual modules from this package, for example:
```python
import pyunitsconverter.amperage
import pyunitsconverter.area
...
```

This loads the submodules ``pyunitsconverter.amperage`` and ``pyunitsconverter.area``.
They must be referenced with their full name.
```python
pyunitsconverter.amperage.ampere_to_microampere(<value>)
pyunitsconverter.area.hectare_to_squarefeet(<value>)
```

An alternative way of importing the submodules is:
```python
from pyunitsconverter import amperage
from pyunitsconverter import area
```

This also loads the submodules ``pyunitsconverter.amperage`` and ``pyunitsconverter.area``,
and makes them available without their prefix, so they can be used as follows:
```python
amperage.ampere_to_microampere(<value>)
area.hectare_to_squarefeet(<value>)
```

Yet another variation is to import the desired functions directly:
```python
from pyunitsconverter.amperage import ampere_to_microampere
from pyunitsconverter.area import hectare_to_squarefeet
```

Again, this loads the submodules, but makes them directly available:
```python
ampere_to_microampere(<value>)
hectare_to_squarefeet(<value>)
```

Imagine you want to convert a length in kilometers (100 km) into a length in miles (??? mi).
You could then let the specific function handle the calculation.
```python
from pyunitsconverter.length import kilometer_to_mile
kilometer_to_mile(100)
```

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

After importing the required module, all of these units of one class can be converted into each other with the following syntax:
```python
<first_unit>_to_<second_unit>(<number>)
```

## Source code & further information

The source code is maintained at https://github.com/sveneschlbeck/quick_eda  
There are also further information concerning the BSD license model, contributing guidelines and more...
