
def printRange(rangeName):
    from glyphNameFormatter import GlyphName
    from glyphNameFormatter.unicodeRangeNames import getRangeByName

    from glyphNameFormatter.data import unicode2name_AGD

    for u in range(*getRangeByName(rangeName)):
        g = GlyphName(uniNumber=u)
        name = g.getName()
        if name is None:
            name = "! ! ! ! ! ! ! ! !"
        AGDName = unicode2name_AGD.get(g.uniNumber, "")
        if AGDName is None or AGDName == name:
            AGDName = ""

        print name.ljust(50), AGDName.ljust(20), "%04X" % g.uniNumber, "\t", g.uniName
