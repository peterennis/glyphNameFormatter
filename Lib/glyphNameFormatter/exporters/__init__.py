# -*- coding: UTF-8 -*-
from __future__ import print_function
from glyphNameFormatter.unicodeRangeNames import getRangeByName
from glyphNameFormatter import GlyphName

from glyphNameFormatter.data import unicode2name_AGD


def _rangeNameToRange(rangeName):
    if isinstance(rangeName, tuple):
        return rangeName
    start, end = getRangeByName(rangeName)
    return start, end+1


def printRange(rangeName, toFile=None):
    out = []
    for u in range(*_rangeNameToRange(rangeName)):
        g = GlyphName(uniNumber=u)
        name = g.getName()
        if name is None:
            continue
        AGDName = unicode2name_AGD.get(g.uniNumber)
        if AGDName is None:
            AGDName = "-"
        elif AGDName == name:
            AGDName = u"👍"
        txt = name.ljust(50)
        txt += AGDName.ljust(30)
        txt += "%04X   " % g.uniNumber
        txt += g.uniLetter.ljust(5)
        txt += g.uniName
        out.append(txt)
    out = "\n".join(out)
    out = out.encode("utf-8")
    if toFile:
        toFile.write(out)
    else:
        print(out)
    testDoubles(rangeName, toFile)
    testGLIFFileName(rangeName, toFile)


if __name__ == "__main__":
    from glyphNameFormatter.unicodeRangeNames import getAllRangeNames

    # time test
    import time
    t = time.time()
    for rangeName in getAllRangeNames():
        r = _rangeNameToRange(rangeName)
        for u in range(*r):
            g = GlyphName(uniNumber=u)
            name = g.getName()
    print(time.time() - t)
