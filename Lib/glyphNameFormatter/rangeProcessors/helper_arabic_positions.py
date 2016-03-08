from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):

    # positions
    self.edit('INITIAL FORM', ".init")
    self.edit('MEDIAL FORM', ".medi")
    self.edit('FINAL FORM', ".fina")
    self.edit('ISOLATED FORM', ".isol")

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Helper Arabic Positions")
