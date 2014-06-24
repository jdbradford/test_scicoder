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

f_speech = '/Users/jeremybradford/Dropbox/Repositories/SciCoder2014/Data/gettysburg_address.txt'

try:
	txtspeech = open(f_speech)
except IOError:
	print "could not find file '{0}'" .format(f_speech)
	sys.exit(1)

txt_words = list()
txt_vo_a = txt_vo_e = txt_vo_i = txt_vo_o = txt_vo_u = txt_vo_y = 0

for i,line in enumerate(txtspeech):
	line = line.rstrip("\n")
	values = line.split()
	
	for this_word in values:
		this_word = this_word.replace('.','')
		this_word = this_word.replace(',','')
		this_word = this_word.upper()
		txt_words.append(this_word)
		txt_vo_a = this_word.count('A') + txt_vo_a
		txt_vo_e = this_word.count('E') + txt_vo_e
		txt_vo_i = this_word.count('I') + txt_vo_i
		txt_vo_o = this_word.count('O') + txt_vo_o
		txt_vo_u = this_word.count('U') + txt_vo_u
		txt_vo_y = this_word.count('Y') + txt_vo_y

x = list(set(txt_words))
txt_words = list(x)
txt_words.sort()

with open('/Users/jeremybradford/Dropbox/Repositories/SciCoder2014/Data/gettysburg_address_words.txt', "w") as f:
	f.write(" ".join(txt_words))

print "There are {0} lines" .format(i+1)
print "There are {0} a's " .format(txt_vo_a)
print "There are {0} e's " .format(txt_vo_e)
print "There are {0} i's " .format(txt_vo_i)
print "There are {0} o's " .format(txt_vo_o)
print "There are {0} u's " .format(txt_vo_u)
print "There are {0} y's " .format(txt_vo_y)

pdb.set_trace()


	