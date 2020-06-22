#!/usr/bin/env python3

# Copyright: Khan Kibria
# License: GNU GPL 3.0

import math

r_type = {}
r_type[20] = 572
r_type[30] = 620
r_type[40] = 626
r_type[60] = 668
r_type[70] = 709
r_type[80] = 656

def calc_wire_length (watts, voltage, wire_type, awg):
    ohm = voltage*voltage/watts
    ohm_per_cmf = r_type[wire_type]
    dia_inch = math.exp(-1.12436 - 0.11594*awg)
    dia_mil = dia_inch*1000
    cs_circular_mil = dia_mil*dia_mil
    cs_sq_mil = cs_circular_mil*math.pi/4
    ohm_per_ft = ohm_per_cmf/cs_circular_mil
    length_in_ft = ohm/ohm_per_ft

    return length_in_ft
