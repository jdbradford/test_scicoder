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

class galaxy(object):
	def __init__(self):
		self.height = 0
		self.width = 0
		self.color = 'aquamarine'
		self.inclination = 78.0
		self.inc_uom = 'deg'

	def sini(self):
		if self.inc_uom == 'deg':
			return np.sin(self.inclination*np.pi/180.)
		if self.inc_uom == 'rad':
			return np.sin(self.inclination) 

class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def distance_to(self, test):
		return np.sqrt((self.x-test.x)**2 + (self.y-test.y)**2)




