from glyphNameFormatter.data.scriptPrefixes import addScriptPrefix


def process(self):
    self.edit("LATIN")

    self.replace("CAPITAL LETTER D WITH SMALL LETTER Z", "Dz")
    self.replace("CAPITAL LETTER DZ", "DZ")

    self.edit("AFRICAN", "african")

    self.edit("WITH LONG RIGHT LEG", "long", "right", "leg")
    self.edit('LETTER YR', "yr")
    self.edit("CAPITAL LETTER O WITH MIDDLE TILDE", "Obar")
    self.edit("CAPITAL LETTER SMALL Q WITH HOOK TAIL", "Qsmallhooktail")
    self.edit("LETTER REVERSED ESH LOOP", "eshreversedloop")
    self.edit("CAPITAL LETTER L WITH SMALL LETTER J", "Lj")
    self.edit("CAPITAL LETTER N WITH SMALL LETTER J", "Nj")
    self.edit("LETTER INVERTED GLOTTAL STOP WITH STROKE", "glottalinvertedstroke")
    self.edit("LETTER TWO WITH STROKE", "twostroke")

    self.edit("CAPITAL LETTER LJ", "LJ")
    self.edit("CAPITAL LETTER NJ", "NJ")
    self.edit("CAPITAL LETTER AE WITH", "AE")

    self.edit("CAPITAL LETTER WYNN", "Wynn")

    self.edit("WITH PALATAL", "palatal")
    self.edit("DENTAL", "dental")
    self.edit("LATERAL", "lateral")
    self.edit("ALVEOLAR", "alveolar")
    self.edit("RETROFLEX", "retroflex")

    self.replace("LETTER CLICK", "click")

    self.replace("CAPITAL LETTER GAMMA", addScriptPrefix("Gamma", script="latin"))
    self.replace("CAPITAL LETTER IOTA", addScriptPrefix("Iota", script="latin"))
    self.replace("CAPITAL LETTER UPSILON", addScriptPrefix("Upsilon", script="latin"))

    self.processAs("Helper Diacritics")
    self.processAs("Helper Shapes")
    self.handleCase()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Latin Extended-B")
