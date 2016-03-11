from __future__ import print_function
import glyphNameFormatter
from glyphNameFormatter.unicodeRangeNames import getRangeByName, getAllRangeNames
import os

skipped = {}

columnFormat = "{0:50} {1:10} {2:10} {3:10}"

def getStats(rangeName):
    # generate all the names in the range
    explicitPrefixes = 0
    autoPrefixes = 0
    total = 0
    r = getRangeByName(rangeName)
    if r is None:
        print("unknown range name", rangeName)
        return
    start, end = r
    for uniNumber in range(start, end+1):
        total += 1
        glyphName = glyphNameFormatter.GlyphName(uniNumber)
        if glyphName.mustAddScript and not glyphName.statsPrefixRequested:
            autoPrefixes += 1
            #print("auto prefix", glyphName.getName(extension=False), glyphName.getName(extension=True))
        if glyphName.mustAddScript and glyphName.statsPrefixRequested:
            explicitPrefixes += 1
        result = glyphName.getName(extension=True)
    print(columnFormat.format(rangeName, explicitPrefixes, autoPrefixes, total) )
    return explicitPrefixes, autoPrefixes, total

if __name__ == "__main__":
    explicitPrefixes = 0
    autoPrefixes = 0
    total = 0
    print(columnFormat.format("Range name", "Expl.", "Auto", "Total") )
    print("-"*150)
    for rangeName in getAllRangeNames():
        a, b, c = getStats(rangeName)
        explicitPrefixes += a
        autoPrefixes += b
        total += c
    print("-"*150)
    print(columnFormat.format("All names", explicitPrefixes, autoPrefixes, total) )

