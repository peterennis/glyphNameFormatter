

def process(self):
    # edits go here
    self.edit("BOPOMOFO")
    self.edit("LETTER")
    self.lower()
    self.compress()
    self.scriptPrefix()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Bopomofo")
