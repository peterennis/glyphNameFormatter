# -*- coding: UTF-8 -*-
from __future__ import print_function
from glyphNameFormatter.unicodeRangeNames import getRangeByName
from glyphNameFormatter import GlyphName

from glyphNameFormatter.data import unicode2name_AGD



def testDoubles(rangeName, toFile=None):
    """
    test if there are doubles
    """
    names = set()
    doubles = set()
    r = _rangeNameToRange(rangeName)
    for u in range(*r):
        g = GlyphName(uniNumber=u)
        name = g.getName()
        if name is None:
            # ignore
            continue
        if name in names:
            doubles.add(name)
        else:
            names.add(name)
    if doubles:
        rangeText = "%04X - %04X" % (r[0], r[1])
        txt = "\n\ndouble names for range %s:\n\t%s" % (rangeText, "\n\t".join(sorted(doubles)))
        if toFile:
            toFile.write(txt)
        else:
            print(txt)


def testGLIFFileName(rangeName, toFile=None):
    """
    test on glif file name
    """
    # support both UFO2 as UFO3
    try:
        # UFO3 ufoLib
        from ufoLib.filenames import userNameToFileName

        def nameToFileName(name):
            return userNameToFileName(unicode(name))
    except:
        # UFO2 robofab
        from robofab.tools.glyphNameSchemes import glyphNameToShortFileName

        def nameToFileName(name):
            return glyphNameToShortFileName(name, None)
    existing = set()
    doubles = set()
    r = _rangeNameToRange(rangeName)
    for u in range(*r):
        g = GlyphName(uniNumber=u)
        name = g.getName()
        if name is None:
            # ignore
            continue
        glifFileName = nameToFileName(name)
        if glifFileName in existing:
            doubles.add(glifFileName)
        else:
            existing.add(glifFileName)
    if doubles:
        rangeText = "%04X - %04X" % (r[0], r[1])
        txt = "\n\ndouble glif file names for range %s:\n\t%s" % (rangeText, "\n\t".join(sorted(doubles)))

        if toFile:
            toFile.write(txt)
        else:
            print(txt)

