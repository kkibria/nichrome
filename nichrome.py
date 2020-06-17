#!/usr/bin/env python3

# Copyright: Khan Kibria
# License: GNU GPL 3.0

import math
import argparse

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

def spec(string):
    try:
        values = string.split(':')
        parts = []
        for value in values:
            parts.append(int(value))
        assert len(parts) <= 2
        if len(parts) == 2:
            assert parts[0] < parts[1]
        return parts
    except:
        msg = "%r not a valid range format, use <int> or <int:int>" % string
        raise argparse.ArgumentTypeError(msg)

def to_range(spec, inc):
    if len(spec) == 1:
        return range(spec[0], spec[0]+inc, inc)
    return range(spec[0], spec[1]+inc, inc)

def spec_range(range_obj, spec, arg_name):
    new_range_obj = to_range(spec, range_obj.step)
    if new_range_obj.start < range_obj.start or new_range_obj.stop > range_obj.stop:
        raise Exception('invalid argument "{} {}:{}", must be within {}:{}'.format(arg_name, new_range_obj.start, new_range_obj.stop-1, range_obj.start, range_obj.stop-1))
    return new_range_obj 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--watts", action="store", type=spec, help="Power range in watts")
    parser.add_argument("-v", "--voltage", action="store", type=spec, help="Supply voltage in volts")
    parser.add_argument("-t", "--wire-type", action="store", type=spec, help="Nichrome wire type")
    parser.add_argument("-g", "--awg", action="store", type=spec, help="Nichrome wire gauge")
    parser.add_argument("-l", "--length", action="store", type=spec, help="Wire length in foot")
    args = parser.parse_args()

    tolerance = 1

    watts_range = range(1, 5000, 1)
    voltage_range = range(1, 5000, 1)
    wire_type_range = range(20, 90, 10)
    awg_range = range(1, 50, 1)
    length_range = range(1, 200, tolerance)

    constraint = 0
    try:
        if args.watts:
            watts_range = spec_range(watts_range, args.watts, "--watts")
            constraint += 1
        if args.voltage:
            voltage_range = spec_range(voltage_range, args.voltage, "--voltage")
            constraint += 1
        if args.wire_type:
            wire_type_range = spec_range(wire_type_range, args.wire_type, "--wire-type")
            constraint += 1
        if args.awg:
            awg_range = spec_range(awg_range, args.awg, "--awg")
            constraint += 1
        if args.length:
            if constraint < 4:
                length_range = spec_range(length_range, args.length, "--length")
                constraint += 1
            else:
                raise Exception("You can only specify maximum 4 constraints, length is ignored")
        if constraint < 1:
            raise Exception ("You have to specify at least 1 constraints")

    except Exception as e:
        print(e)
        exit(1)

    len = calc_wire_length(30, 110, 60, 40)

    for watts in watts_range:
        for voltage in voltage_range:
            for wire_type in wire_type_range:
                for awg in awg_range:
                    for length in length_range:
                        min_length = length
                        max_length = length + length_range.step
                        try:
                            l = calc_wire_length(watts, voltage, wire_type, awg)
                            if (l >= min_length and l < max_length):
                                print ('power: {} watts, voltage: {} volts, wire-type: Nichrome-{}, gauge: {} awg, length: {:3.2f} feet'.format(watts, voltage, wire_type, awg, l))
                        except:
                            pass
