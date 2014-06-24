#!/usr/bin/env python
from __future__ import division
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import scipy as sp
import pdb
import mpmath as mp
import sys
import astropy as ap
import math
import oo_test


print "hello world!"
mass = None
gal = oo_test.galaxy()

if mass == None:
	print 'Mass is not set!'

mass = {'Planet 1':1.3e9, 'Planet 2':2.5e10, 'Planet 3': 4.3e9}

for p_name in mass.keys():
	print "the mass of {0} is {1:.2f}:" .format(p_name, mass[p_name])

filename = 'blah.txt'
try:
	my_file = open(filename)
except IOError:
	print "error: file '{0}' could not be opened. Did you lose it?" .format(filename)
	sys.exit(1)


