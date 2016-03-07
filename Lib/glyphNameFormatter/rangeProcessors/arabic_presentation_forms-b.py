from arabic import process

if __name__ == "__main__":
    from glyphNameFormatter import GlyphName
    from glyphNameFormatter.unicodeRangeNames import getRangeByName

    for u in range(*getRangeByName("Arabic Presentation Forms-B")):
        g = GlyphName(uniNumber=u)
        if g.uniName is not None:
            print g.getName().ljust(30), "%04X" % g.uniNumber, "\t", g.uniName
