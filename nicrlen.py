#!/usr/bin/env python3

# Copyright: Khan Kibria
# License: GNU GPL 3.0

import math
import argparse
import nicrlib

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--watts", action="store", type=float, default=1, help="Power range in watts")
    parser.add_argument("-v", "--voltage", action="store", type=float, default=1, help="Supply voltage in volts")
    parser.add_argument("-t", "--wire-type", action="store", type=int, default=60, help="Nichrome wire type")
    parser.add_argument("-g", "--awg", action="store", type=int, default=42, help="Nichrome wire gauge")
    parser.add_argument("-n", "--number", action="store", type=int, default=1, help="Number of parallel sections")
    args = parser.parse_args()

    len =  nicrlib.calc_wire_length(args.watts / args.number , args.voltage, args.wire_type, args.awg)

    feet = int(len)
    inches = len*12 % 12

    lenstr = "{:3.2f} inches".format(inches)
    if feet:
        lenstr = "{} feet {:3.2f} inches".format(feet, inches)

    print ('sections: {}, power: {} watts, voltage: {} volts, wire-type: Nichrome-{}, gauge: {} awg, length: {}.'.format(
        args.number, args.watts, args.voltage, args.wire_type, args.awg, lenstr))
