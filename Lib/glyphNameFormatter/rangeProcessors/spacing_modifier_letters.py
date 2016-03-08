
def process(self):

    self.edit("TONE", "tone")
    self.edit("HALF", "half")
    self.edit("LEFT", "left")
    self.edit("RIGHT", "right")
    self.edit("UP", "up")
    self.edit("DOWN", "down")
    self.edit("EXTRA-LOW", "extralow")
    self.edit("LOW", "low")
    self.edit("EXTRA-HIGH", "extrahigh")
    self.edit("HIGH", "high")
    self.edit("BEGIN", "begin")
    self.edit("MIDDLE", "middle")
    self.edit("END", "end")

    self.edit("RAISED", "raised")
    self.edit("SHELF", "shelf")

    self.processShape()

    self.edit("MODIFIER", "mod")

    self.replace("DOUBLE", "dbl")
    self.replace("ACCENT")
    self.replace("LETTER")

    self.lower()
    self.handleCase()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Spacing Modifier Letters")
