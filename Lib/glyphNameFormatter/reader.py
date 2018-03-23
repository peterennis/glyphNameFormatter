# -*- coding: UTF-8 -*-
from __future__ import print_function, absolute_import

from glyphNameFormatter.unicodeRangeNames import getRangeByName, getAllRangeNames, getSupportedRangeNames

import os

"""

Find the sanctioned export file
Provide conversions for

name to unicode
unicode to name

maybe later: some version info
header:

# Glyph Name Formatted Unicode List - GNFUL
# GlyphNameFormatter version 0.28 - git commit: 400
# Unicode version: Unicode 10.0.0
# Source code: https://github.com/LettError/glyphNameFormatter/tree/fcca7b3
# Generated on 2018 03 23 20:36:46
# <glyphName> <hex unicode> <unicodeCategory>
#


Parse the file when the module loads, then save the data in 3 dicts.

"""

sanctionedNameList = 'glyphNamesToUnicodeAndCategories.txt'

name2uni = {}
uni2name = {}
uni2cat = {}
ranges = {}

def u2n(value):
	"""Unicode value to glyphname"""
	global uni2name
	return uni2name.get(value)

def n2u(name):
	"""Glyphname to Unicode value"""
	global name2uni
	return name2uni.get(name)

def u2c(value):
	"""Unicode value to Unicode category"""
	global uni2cat
	return uni2cat.get(value)

def n2c(name):
	"""Glyphname to Unicode category"""
	global name2uni, uni2cat
	return uni2cat.get(name2uni.get(name))

def _parse(path):
	lines = None
	global name2uni, uni2name, uni2cat
	with open(path, 'r') as f:
		lines = f.read().split("\n")
	if lines:
		for l in lines:
			if not l: continue
			if l[0]=="#": continue
			parts = l.split(" ")
			assert(len(parts)==3)
			name = parts[0]
			value = int(parts[1], 16)
			cat = parts[2]
			name2uni[name] = value
			uni2name[value] = name
			uni2cat[value] = cat

path = os.path.join(os.getcwd(), 'names', sanctionedNameList)
if os.path.exists(path):
	_parse(path)
else:
	print("GNUFL error: can't find name lists at %s"%(path))

rangeNames = getSupportedRangeNames()
for rangeName in rangeNames:
	start, end = getRangeByName(rangeName)
	ranges[(start, end)] = rangeName

def u2r(value):
	"""Unicode value to range name"""
	for k, v in ranges.items():
		if k[0]<=value<=k[1]:
			return v
	return None


if __name__ == "__main__":
	allNames = name2uni.keys()
	#print(allNames)
	allNames.sort()
	for n in allNames:
		print(n)
		assert(n == u2n(n2u(n)))


	for n in allNames:
		u = n2u(n)
		print(n, u2r(u))