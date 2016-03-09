# -*- coding: UTF-8 -*-
from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes


def process(self):
    self.edit("LATIN")

    self.edit("CAPITAL LETTER H WITH STROKE", "Hbar")
    self.edit("SMALL LETTER H WITH STROKE", "hbar")
    self.edit("CAPITAL LETTER T WITH STROKE", "Tbar")
    self.edit("SMALL LETTER T WITH STROKE", "tbar")
    self.edit("CAPITAL LETTER L WITH STROKE", "Lslash")
    self.edit("SMALL LETTER L WITH STROKE", "lslash")
    self.edit("CAPITAL LETTER D WITH STROKE", "Dcroat")
    self.edit("SMALL LETTER D WITH STROKE", "dcroat")

    self.edit("WITH DOUBLE ACUTE", "hungarumlaut")

    self.replace("CAPITAL LIGATURE IJ", "IJ")
    self.replace("SMALL LIGATURE IJ", "ij")

    self.replace("SMALL LIGATURE OE", "oe")
    self.replace("CAPITAL LIGATURE OE", "OE")

    self.processDiacritics()
    self.editSuffix("dot", 'dotaccent')
    self.handleCase()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Latin Extended-A")
