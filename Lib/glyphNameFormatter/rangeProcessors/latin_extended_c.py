from glyphNameFormatter.data.scriptPrefixes import addScriptPrefix


def process(self):
    # edits go here
    self.edit("LATIN")

    self.replace("CAPITAL LETTER ALPHA", addScriptPrefix("Alpha", script="latin"))
    self.replace("CAPITAL LETTER TURNED ALPHA", addScriptPrefix("Alphaturned", script="latin"))

    self.replace("LETTER SMALL CAPITAL TURNED E", "Esmallturned")

    self.edit("DOUBLE", "dbl")
    self.edit("BAR", "bar")
    self.edit("SUBSCRIPT", ".inferior")
    self.edit("HALF", "half")
    self.edit("TAILLESS", "tailless")

    self.edit("DIAGONAL")
    self.edit("WITH")

    self.processAs("Helper Diacritics")
    self.processAs("Helper Shapes")
    self.handleCase()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Latin Extended-C")
