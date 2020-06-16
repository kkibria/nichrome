# Nichrome wire calculator
A python command like tool for calculating nichrome wire specifics for heating applications.

```
usage: nichrome.py [-h] [-w WATTS] [-v VOLTAGE] [-t WIRE_TYPE] [-g AWG]
                   [-l LENGTH]

  -h, --help            show this help message and exit
  -w WATTS, --watts WATTS
                        Power range in watts
  -v VOLTAGE, --voltage VOLTAGE
                        Supply voltage in volts
  -t WIRE_TYPE, --wire-type WIRE_TYPE
                        Nichrome wire type
  -g AWG, --awg AWG     Nichrome wire gauge
  -l LENGTH, --length LENGTH
                        Wire length in feet
```

## Arguments
All arguments can take two forms,
* Single integer value. Example, '``-w 100``'.
* A range specified by two integer values separated by a '``:``' (colon).
Example, '``-l 10:15``'.  

## Wire types
The command supports following nichrome wire types, which indicates the percentage of Nickel in the alloy:
* 20 
* 30
* 40
* 60
* 70
* 80

For example, The nichrome wire commonly called *Nichrome 60*, which actually has 60% Nickel, is to be entered as '``-t 60``'. The range format is also 
supported for wire types so you can specify type like '``-t 30:70``' as well.

## Current Capacity
Make sure not to exceed the current capacity of the nichrome wire. Check the
Wikipedia article, <https://en.wikipedia.org/wiki/Nichrome> for more information. The heat produced by the wire must be carried away
the surrounding material. Depending on the surrounding material's thermal conductivity the temperature of the wire can vary for a given current.
You have to make sure that the temperature does no exceed the manufacturer's
recommendation.
