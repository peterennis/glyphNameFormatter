
def process(self):
    self.edit("LATIN")
    self.processShape()

    self.edit("LATIN CAPITAL LETTER O WITH MIDDLE TILDE", "Obar")

    # self.edit("AFRICAN", "african")
    # self.edit("TURNED", "turned")
    # self.edit("OPEN", "open")

    self.processDiacritics()
    self.handleCase()
    self.compress()
    return True


if __name__ == "__main__":
    from glyphNameFormatter import GlyphName
    from glyphNameFormatter.unicodeRangeNames import getRangeByName

    from glyphNameFormatter.data import unicode2name_AGD

    for u in range(*getRangeByName("Latin Extended-B")):
        g = GlyphName(uniNumber=u)
        name = g.getName()

        AGDName = unicode2name_AGD.get(g.uniNumber, "")
        if AGDName == name:
            AGDName = ""

        print name.ljust(50), AGDName.ljust(20), "%04X" % g.uniNumber, "\t", g.uniName
