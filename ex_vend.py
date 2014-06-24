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

from abc import ABCMeta
from abc import abstractproperty

class venItem(object):
	__metaclass__ = ABCMeta

	def __init__(self):
		self.qty = 0.0
		self.price = 0.0
		self.name = ''

class Water(venItem):
	def __init__(self):
		super(Water, self).__init__()
		self.name = 'water'

class IcedTea(venItem):
	def __init__(self):
		super(IcedTea, self).__init__()
		self.name = 'iced tea'

class Soda(venItem):
	def __init__(self):
		super(Soda, self).__init__()
		self.name = 'soda'

class VendingMachine():
	def __init__(self):
		self.water = Water()
		self.icedtea = IcedTea()
		self.soda = Soda()
		self.stocklist = [self.water, self.icedtea, self.soda]
		self.namelist = [type.name for type in self.stocklist]

	def restock(self, stuff, quantity=0.0, price=0.0):
		
		if stuff in self.namelist:
			ind = self.namelist.index(stuff)
			item = self.stocklist[ind]

		item.qty = item.qty + quantity
		item.price = price

	def vend(self, stuff, amt_rec):

		if stuff in self.namelist:
			ind = self.namelist.index(stuff)
			item = self.stocklist[ind]

		if item.price <= amt_rec:
			if item.qty > 0:
				item.qty = item.qty - 1
				change = amt_rec - item.price
				if change > 0:
					print 'Your change is {0}' .format(change)
			else:
				print 'Out of stock! Your change is: {0}' .format(amt_rec)
		else:
			print 'Not enough money! Your change is: {0}' .format(amt_rec)

	def stock(self, stuff):

		if stuff in self.namelist:
			ind = self.namelist.index(stuff)
			item = self.stocklist[ind]


