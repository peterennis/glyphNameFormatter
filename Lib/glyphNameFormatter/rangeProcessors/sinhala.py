
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
    self.scriptPrefix()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Sinhala")
