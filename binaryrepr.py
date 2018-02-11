#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: binaryrepr.py
Author: David LAMOULLER
Email: yourname@email.com
Github: https://github.com/yourname
Description: 
"""

from __future__ import unicode_literals
import sys
from math import log
import  click

#option fo click
click.disable_unicode_literals_warning = True
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

drepr = {   1 : bin,
            3 : oct,
            4 : hex
        }

delim = lambda x, y: " " * x + y + " "

class BaseDepiction(object):
    """BaseDepiction"""

    def __init__(self, x, delimiter="|", delimiterhead="~", short_repr=False, verbosity=False):
        super(BaseDepiction, self).__init__()
        self.x = x
        self.delimiter = delimiter
        self.delimiterhead = delimiterhead
        self.short_repr = short_repr
        self.verbosity = verbosity
        if self.verbosity:
            self.reprpos = "number bits: "
            self.reprbin = "value: "
        else:
            self.reprpos = ""
            self.reprbin = ""
        self.depth = 7
        for d in filter(lambda e: round(log(x, 2) + 0.5) <= e, [8, 16, 32, 64, 128]):
            self.depth = d
            break
        self.position = list(map(str, range(self.depth, -1, -1)))


    def __repr__(self):
        header = ""
        data   = ""
        if self.verbosity:
            print("endianness: {0}".format(sys.byteorder))
        adjustspace = len(self.reprpos) - len(self.reprbin)
        for s in self.position:
            header += s + delim(0, self.delimiter)
        header = self.reprpos + delim(0, self.delimiter) + header[:-1] + "\n"
        delimheader = (len(header) - 1 )* self.delimiterhead + "\n"

        for p, x in zip(self.position, self.x):
            if int(p) > 9: 
                nbspace = 1
            else:
                nbspace = 0
            data += x + delim(nbspace, self.delimiter)
        data = self.reprbin + delim(adjustspace, self.delimiter) + data[:-1] + "\n"
        return header + delimheader + data

class Bin(BaseDepiction):
    """docstring for Bin"""

    def __init__(self, x, delimiter = "|", delimiterhead="~", short_repr=False, verbosity=False):
        super(BaseDepiction, self).__init__()
        BaseDepiction.__init__(self, x, delimiter, delimiterhead, short_repr, verbosity)
        self.x = format(x, 'b')
        if short_repr:
            if sys.byteorder == "little":
                self.position = list(map(str, range(len(self.x) - 1, -1, -1)))
            else:
                self.position = list(map(str, range(len(self.x) - 1)))
        else:
            self.x = (self.depth - len(self.x) + 1) * "0" + self.x


class Hex(BaseDepiction):
    """docstring for Hex"""
    
    def __init__(self, x, delimiter = "|", delimiterhead="~", short_repr=False, verbosity=True):
        super(BaseDepiction, self).__init__()
        BaseDepiction.__init__(self, x, delimiter, delimiterhead, verbosity=verbosity)
        self.x = format(x, 'x')
        if not short_repr:
            self.x = int((self.depth/4 - len(self.x) + 1)) * "0" + self.x
        if sys.byteorder == "little":
            nbbits = [i * 4 for i in range(len(self.x) - 1, -1, -1)]
        else:
            nbbits = [i * 4 for i in range(len(self.x) - 1)]
        self.position = list(map(str, nbbits))

    
class Oct(BaseDepiction):
    """docstring for Oct"""

    def __init__(self, x, delimiter = "|", delimiterhead="~", short_repr=False, verbosity=True):
        super(BaseDepiction, self).__init__()
        BaseDepiction.__init__(self, x, delimiter, delimiterhead, verbosity=verbosity)
        self.x = format(x, 'o')
        if not short_repr:
            self.x = int((self.depth/2 - len(self.x) + 1)) * "0" + self.x
        if sys.byteorder == "little":
            nbbits = [i * 3 for i in range(len(self.x) -1, -1, -1)]
        else:
            nbbits = [i * 3 for i in range(len(self.x) -1)]
        self.position = list(map(str, nbbits))

@click.command(context_settings=CONTEXT_SETTINGS, help="representation of a number according to your system byteorder")
@click.option("-t", "--type_repr", default="bin", type=click.Choice(['bin', 'b', 'hex', 'h', 'oct', 'o']), help="type of representation of number")
@click.option("-s", "--short", is_flag=True, help="short representation")
@click.option("-v", "--verbose", is_flag=True, help="verbose mode")
@click.argument("value", type=int)
def display(value, type_repr, short, verbose):
    if type_repr=="hex" or type_repr=="h":
        print(Hex(value, short_repr=short, verbosity=verbose))
    elif type_repr=="oct" or type_repr=="o":
        print(Oct(value, short_repr=short, verbosity=verbose))
    else:
        print("representation of {0}:\n{1}".format(value, Bin(value, short_repr=short, verbosity=verbose)))


if __name__ == "__main__":
    display()
    # value = 2
    # print("representation de {0}:\n{1}".format(value, Bin(value, verbosity=True)))
    # print(Hex(value, verbosity=False))
    # print(Oct(value, verbosity=False))

