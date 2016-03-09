
def process(self):
    self.edit("DEVANAGARI")

    # parts
    self.edit("LETTER")
    self.edit("DIGIT")

    self.edit("LONG E", "elong")
    self.edit("SHORT", "short")
    self.edit("DOUBLE", "dbl")

    self.edit("SIGN CANDRABINDU", "candrabindu")
    self.edit("SIGN INVERTED CANDRABINDU", "candrabinduinverted")
    self.edit("CANDRA", "candra")
    self.edit("DANDA", "danda")
    self.edit("GRAVE ACCENT", "grave")
    self.edit("ACUTE ACCENT", "acute")

    self.edit("VOWEL SIGN VOCALIC", "vocalsign")
    self.edit("VOWEL SIGN", "sign")
    self.edit("VOCALIC", "vocal")
    self.edit("STRESS SIGN")
    self.edit("PRISHTHAMATRA", "prishthamatra")
    self.edit("SIGN NUKTA", "nukta")
    self.edit("SIGN VIRAMA", "virama")
    self.edit("SIGN AVAGRAHA", "avagraha")
    self.edit("SIGN VISARGA", "visarga")
    self.edit("SIGN ANUSVARA", "anusvara")
    self.edit("ABBREVIATION SIGN", "abbreviation")
    self.edit("SIGN HIGH SPACING DOT", "dothigh")
    self.edit("HEAVY", "heavy")
    self.edit("GLOTTAL STOP", "glottalstop")

    self.processAs("Helper Digit Names")

    # AGD uses camelcase, but there do not seem to be casing differences between the letters
    self.lower()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Devanagari")
