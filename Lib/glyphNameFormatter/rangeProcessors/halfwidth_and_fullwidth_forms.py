
def process(self):

    if 0xFF01 <= self.uniNumber <= 0xFF5E:
        self.editToFinal("FULLWIDTH", 'fullwidth')
        self.processAs('Basic Latin')
        self.edit("COMMERCIAL AT", "at")
    elif 0xFF65 <= self.uniNumber <= 0xFF9F:
        self.editToFinal("HALFWIDTH", 'halfwidth')
        self.processAs('Katakana')
    elif 0xFFA0 <= self.uniNumber <= 0xFFEE:
        self.editToFinal("HALFWIDTH", 'halfwidth')
        self.editToFinal("FULLWIDTH", 'fullwidth')
        self.replace("-", "_")
        self.edit("HANGUL LETTER")
        self.processAs('Hangul')
        self.lower()

    # XXXXX add support for HANGUL
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Halfwidth and Fullwidth Forms")
