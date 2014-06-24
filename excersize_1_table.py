#!/usr/bin/env python
from __future__ import division
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import scipy as sp
import pdb
import mpmath as mp
import sys
import astropy
import math
import astropy.io.ascii as ascii

f_data = '/Users/jeremybradford/Dropbox/Repositories/SciCoder2014/Data/table.txt'

try:
	txtman = open(f_data)
except IOError:
	print "could not find file '{0}'" .format(f_data)
	sys.exit(1)

targs = dict()
txt_names = list()
txt_ra = list()
txt_dec = list()

for i,line in enumerate(txtman):

	if i == 0:
		continue

	values = line.split(',')
	txt_names.append(values[2])
	txt_ra.append(values[0])
	txt_dec.append(values[1])

targs['name'] = txt_names
targs['ra'] = txt_ra
targs['dec'] = txt_dec
pdb.set_trace()
