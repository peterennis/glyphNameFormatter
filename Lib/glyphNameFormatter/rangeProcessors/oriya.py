
def process(self):
    # edits go here
    # self.edit("ARMENIAN")
    # self.handleCase()
    # self.compress()
    pass
    self.edit("ORIYA")
    self.edit("LETTER")
    self.edit("DIGIT")
    self.edit("VOWEL SIGN", "sign")
    self.edit("VOWEL SIGN VOCALIC", "vocalsign")
    self.edit("VOCALIC", "vocal")
    self.edit("SIGN NUKTA", "nukta")
    self.edit("SIGN VIRAMA", "virama")
    self.edit("SIGN AVAGRAHA", "avagraha")
    self.edit("SIGN VISARGA", "visarga")
    self.edit("SIGN ANUSVARA", "anusvara")
    self.edit("SIGN CANDRABINDU", "candrabindu")
    self.processAs("Helper Numbers")
    self.lower()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Oriya")
