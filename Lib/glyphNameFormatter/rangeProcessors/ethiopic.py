
def process(self):
    pass
    self.edit("ETHIOPIC")
    self.edit("SYLLABLE")
    self.edit("GLOTTAL", "glottal")
    self.processAs("Helper Digit Names")
    self.edit("NUMBER")
    self.edit("DIGIT")
    # edits go here
    # self.edit("ARMENIAN")
    # self.handleCase()
    # self.compress()
    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Ethiopic")
