from glyphNameFormatter.data import unicode2name_AGD


def process(self):
    if self.uniNumber in unicode2name_AGD:
        self.replace(self.uniName, unicode2name_AGD[self.uniNumber])
        return

    # self.edit("TONE", "tone")
    # self.edit("LOW", "low")
    # self.edit("HIGH", "high")
    # self.edit("BEGIN", "begin")
    # self.edit("MIDDLE", "middle")
    # self.edit("END", "end")
    # self.edit("")
    # self.edit("RAISED", "raised")
    # self.edit("SHELF", "shelf")

    # self.processShape()

    # self.edit("MODIFIER", "mod")

    # self.replace("DOUBLE", "dbl")
    # self.replace("ACCENT")
    # self.replace("LETTER")

    self.lower()
    self.handleCase()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Spacing Modifier Letters")
