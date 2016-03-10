
def process(self):
    pass
    self.edit("ETHIOPIC")
    self.edit("SYLLABLE")
    self.edit("GLOTTAL", "glottal")
    self.processAs("Helper Digit Names")
    self.edit("NUMBER")
    self.edit("DIGIT")
    self.edit("COMBINING", "cmb")
    # edits go here
    # self.edit("ARMENIAN")
    # self.handleCase()
    # self.compress()
    self.lower()
    self.compress()
    self.final("-et")

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Ethiopic")
