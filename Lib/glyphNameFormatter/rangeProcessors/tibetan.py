from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes


def process(self):
    self.edit("TIBETAN")
    if self.has("DIGIT"):
        self.edit("DIGIT", "")
        self.lower()

    # self.edit("SIGN", 'sign')
    # self.edit("MARK", 'mark')
    # self.replace("VOWEL", "vowel")
    # self.edit("SYMBOL", "symbol")
    # self.edit("SUBJOINED", "subjoined")
    # self.replace("LOGOTYPE", "logotype")
    # self.edit("FIXED-FORM", "fixed")

    # self.replace("INITIAL", 'initial')
    # self.replace("CLOSING", 'closing')
    # self.replace("CANTILLATION", "cantillation")
    # self.edit("VOCALIC", "vocalic")

    self.edit("RIGHT-FACING SVASTI SIGN WITH DOTS", "svastirightdot")
    self.edit("LEFT-FACING SVASTI SIGN WITH DOTS", "svastileftdot")
    self.edit("RIGHT-FACING SVASTI SIGN", "svastiright")
    self.edit("LEFT-FACING SVASTI SIGN", "svastileft")

    self.edit("-A", "AA")  # Old name TIBETAN LETTER AA
    self.edit("LETTER")
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Tibetan")
