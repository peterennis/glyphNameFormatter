
def process(self):
    self.edit("SINHALA")
    self.edit("LETTER")
    self.edit("DIGIT")
    self.edit("VOWEL")
    self.edit("SIGN")
    self.processAs("Helper Indic")
    self.processAs("Helper Numbers")
    self.replace("-")
    self.lower()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Sinhala")
