from glyphNameFormatter.unicodeRangeNames import getRangeByName
from glyphNameFormatter import GlyphName

from glyphNameFormatter.data import unicode2name_AGD


def _rangeNameToRange(rangeName):
    if isinstance(rangeName, tuple):
        return rangeName
    return getRangeByName(rangeName)


def printRange(rangeName):
    for u in range(*_rangeNameToRange(rangeName)):
        g = GlyphName(uniNumber=u)
        name = g.getName()
        if name is None:
            continue
        AGDName = unicode2name_AGD.get(g.uniNumber, "")
        if AGDName is None or AGDName == name:
            AGDName = ""

        print name.ljust(50), AGDName.ljust(30), "%04X" % g.uniNumber, "\t", g.uniLetter.encode("utf-8"), "\t", g.uniName

    testDoubles(rangeName)


def testDoubles(rangeName):
    """
    test if there are doubles
    """
    names = set()
    doubles = set()
    for u in range(*_rangeNameToRange(rangeName)):
        g = GlyphName(uniNumber=u)
        name = g.getName()
        if name in names:
            doubles.add(name)
        else:
            names.add(name)
    if doubles:
        print "doulbes: %s" % ", ".join(sorted(doubles))


def testGLIFFileName(rangeName):
    """
    test on glif file name
    """


