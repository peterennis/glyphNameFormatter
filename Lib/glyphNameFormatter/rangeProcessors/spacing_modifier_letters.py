
def process(self):

    self.edit("COLON", "colon")
    self.edit("TRIANGULAR", "triangular")
    self.edit("TONE MARK", "tone")
    self.edit("TONE", "tone")
    self.edit("BAR", "bar")
    self.edit("HALF", "half")
    self.edit("LEFT", "left")
    self.edit("RIGHT", "right")
    self.edit("UP", "up")
    self.edit("DOWN", "down")
    self.edit("EXTRA-LOW", "extralow")
    self.edit("LOW", "low")
    self.edit("MIDDLE", "middle")
    self.edit("MID", "mid")
    self.edit("EXTRA-HIGH", "extrahigh")
    self.edit("HIGH", "high")
    self.edit("BEGIN", "begin")

    self.edit("END", "end")

    self.edit("RAISED", "raised")
    self.edit("SHELF", "shelf")

    self.edit("DOUBLE", "dbl")

    self.processShape()

    self.edit("MODIFIER", "mod")

    self.replace("ACCENT")
    self.replace("LETTER")

    self.lower()
    self.handleCase()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Spacing Modifier Letters")
