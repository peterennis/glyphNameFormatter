
def process(self):
    self.edit("HANGZHOU NUMERAL", "hangzhou")

    self.edit("JAPANESE INDUSTRIAL STANDARD SYMBOL", "jis")
    self.edit("REVERSED DOUBLE PRIME QUOTATION MARK", "quotedblprimereversed")
    self.edit("DOUBLE PRIME QUOTATION MARK", "quotedblprime")
    self.edit("REVERSED", "reversed")
    self.edit("DOUBLE ANGLE", "dblangle")
    self.edit("DOUBLE", "dbl")
    self.edit("LEFT", "left")
    self.edit("RIGHT", "right")
    self.processAs("Helper Digit Names")
    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("CJK Symbols and Punctuation")
