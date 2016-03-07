from glyphNameFormatter.scriptPrefixes import scriptPrefixes

def process(self):
    if self.verbose:
        print "processArabic"
    self.scriptTag = scriptPrefixes['hebrew']

    self.replace("HEBREW LIGATURE YIDDISH DOUBLE VAV", "vav_vav")   # yiddish ?
    self.replace("HEBREW LIGATURE YIDDISH VAV YOD", "vav_yod")  # yiddish ?
    self.replace("HEBREW LIGATURE YIDDISH DOUBLE YOD", "yod_yod")
    self.replace("HEBREW MARK UPPER DOT", "dotupper")
    self.replace("HEBREW MARK LOWER DOT", "dotlower")
    self.edit("ACCENT", "accent")
    self.edit("FINAL", ".fina")    # .fina
    self.edit("POINT", "pt")   # point?
    if self.has("YIDDISH"):
        if self.replace("YIDDISH"):
            self.suffix("yiddish")
    if self.has("PUNCTUATION"):
        self.replace("PUNCTUATION")

    self.edit("HEBREW LETTER")
    self.edit('HEBREW')
    self.edit("LETTER")

    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter import GlyphName
    from glyphNameFormatter.unicodeRangeNames import getRangeByName

    for u in range(*getRangeByName("Hebrew")):
        g = GlyphName(uniNumber=u)
        if g.uniName is not None:
            print g.getName().ljust(30), "%04X" % g.uniNumber, "\t", g.uniName
