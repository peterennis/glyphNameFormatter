
def process(self):
    self.edit("GURMUKHI")
    self.edit("LETTER")
    self.edit("DIGIT")
    self.processAs("Helper Indic")
    self.processAs("Helper Numbers")
    self.edit("SIGN", "sign")
    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Gurmukhi")
