# -*- coding: UTF-8 -*-


def process(self):
    self.edit("LATIN")

    self.edit("CAPITAL LETTER L WITH STROKE", "Lslash")
    self.edit("SMALL LETTER L WITH STROKE", "lslash")
    self.edit("CAPITAL LETTER D WITH STROKE", "Dcroat")
    self.edit("SMALL LETTER D WITH STROKE", "dcroat")

    self.replace("CAPITAL LIGATURE IJ", "IJ")
    self.replace("SMALL LIGATURE IJ", "ij")

    self.replace("SMALL LIGATURE OE", "oe")
    self.replace("CAPITAL LIGATURE OE", "OE")

    self.processDiacritics()
    self.handleCase()
    self.compress()
    return True


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Latin Extended-A")
