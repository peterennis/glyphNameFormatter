
def process(self):
    self.edit("LATIN")
    self.processShape()

    self.edit("LATIN CAPITAL LETTER O WITH MIDDLE TILDE", "Obar")

    # self.edit("AFRICAN", "african")
    # self.edit("TURNED", "turned")
    # self.edit("OPEN", "open")

    self.processDiacritics()
    self.handleCase()
    self.compress()
    return True


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Latin Extended-B")
