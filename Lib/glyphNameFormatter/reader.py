# -*- coding: UTF-8 -*-
from __future__ import print_function, absolute_import

import glyphNameFormatter
from glyphNameFormatter.unicodeRangeNames import getRangeByName, getAllRangeNames, getSupportedRangeNames
from glyphNameFormatter.data import upperToLower, lowerToUpper

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

def readJoiningTypes(path):
    # read the joiningTypes.txt
    joiningTypes = {}
    f = open(path, 'r')
    d = f.read()
    f.close()
    lines = d.split("\n")
    for l in lines:
        if not l: continue
        if l[0] == "#": continue
        parts = l.split("\t")
        uni = int('0x'+parts[0], 0)
        jT = parts[1]
        joiningTypes[uni] = jT
    return joiningTypes


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
			print('parts', parts)
			assert(len(parts)==3)
			name = parts[0]
			value = int(parts[1], 16)
			cat = parts[2]
			name2uni[name] = value
			uni2name[value] = name
			uni2cat[value] = cat

root = os.path.dirname(glyphNameFormatter.__file__)
path = os.path.join(root, 'names', sanctionedNameList)
if os.path.exists(path):
	_parse(path)
else:
	print("GNUFL error: can't find name lists at %s"%(path))


rangeNames = getSupportedRangeNames()
for rangeName in rangeNames:
	start, end = getRangeByName(rangeName)
	ranges[(start, end)] = rangeName

def n2jT(name):
	"""name to joiningType"""
	pass

def u2r(value):
	"""Unicode value to range name"""
	for k, v in ranges.items():
		if k[0]<=value<=k[1]:
			return v
	return None

def n2N(name):
	# name to uppercase
	uni = n2u(name)
	if uni:
		uprUni = lowerToUpper.get(uni)
		if uprUni:
			return u2n(uprUni)
	return name

def N2n(name):
	# name to lowercase
	uni = n2u(name)
	if uni:
		lwrUni = upperToLower.get(uni)
		if lwrUni:
			return u2n(lwrUni)
	return name

def u2U(uni):
	# unicode to uppercase unicode
	uprUni = lowerToUpper.get(uni)
	if uprUni is not None:
		return uprUni
	return uni

def U2u(uni):
	# unicode to lowercase unicode
	lwrUni = upperToLower.get(uni)
	if lwrUni is not None:
		return lwrUni
	return lwr

if __name__ == "__main__":
	print("upperToLower map:", len(upperToLower))
	print("lowerToUpper map:", len(lowerToUpper))
	allNames = list(name2uni.keys())
	allNames.sort()
	print("\ntest lower -> upper -> lower")
	for n in allNames:
		upr = n2N(n)
		if upr != n and upr is not None:
			lwr = N2n(upr)
			if n != lwr:
				print("\t\tn2N failed", n, "->", upr, "->", lwr)
			#else:
			#	print("\ta ok", n, "->", upr, "->", lwr)

		lwr = N2n(n)
		if lwr != n and lwr is not None:
			upr = n2N(lwr)
			if n != upr:
				print("\t\tN2n failed", n, "->", lwr, "->", upr)
			#else:
			#	print("\tb ok", n, "->", lwr, "->", upr)
	assert N2n("non-existing-glyphname") == "non-existing-glyphname"
	assert n2N("non-existing-glyphname") == "non-existing-glyphname"
	assert n2N("germandbls") == "germandbls"
	assert N2n("A") == 'a'
	assert n2N("a") == 'A'
	assert U2u(65) == 97	# A -> a
	assert u2U(97) == 65	# a -> A

	if False:
		allNames = list(name2uni.keys())
		allNames.sort()
		for n in allNames:
			print(n)
			assert(n == u2n(n2u(n)))


		for n in allNames:
			u = n2u(n)
			print(n, u2r(u))