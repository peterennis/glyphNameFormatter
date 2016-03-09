from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):
    self.edit("SQUARE", "fullwidth")
    self.edit("IDEOGRAPHIC TELEGRAPH SYMBOL FOR", "telegraph")
    self.edit("-")
    self.processAs("Helper Digit Names")
    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("CJK Compatibility")
