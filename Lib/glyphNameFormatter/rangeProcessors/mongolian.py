from glyphNameFormatter.scriptPrefixes import scriptPrefixes


def process(self):
    self.scriptTag = scriptPrefixes['mongolian']

    # edits go here
    self.edit("MONGOLIAN")

    self.handleCase()
    self.replace("LETTER")
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Mongolian")
