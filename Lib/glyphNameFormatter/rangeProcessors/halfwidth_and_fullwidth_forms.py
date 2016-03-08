from glyphNameFormatter.scriptPrefixes import scriptPrefixes


def process(self):
    #self.scriptTag = scriptPrefixes['<-scriptname->']
    
    # edits go here
    #self.edit("ARMENIAN")
    #self.handleCase()
    if 0xFF01 <= self.uniNumber <= 0xFF5E:
        self.editToFinal("FULLWIDTH", 'fullwidth')
        self.processAs('Basic Latin')
        self.edit("COMMERCIAL AT", "at")
    elif 0xFF65 <= self.uniNumber <= 0xFF9F:
        self.editToFinal("HALFWIDTH", 'halfwidth')
        self.processAs('Katakana')

    # XXXXX add support for HANGUL
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Halfwidth and Fullwidth Forms")
