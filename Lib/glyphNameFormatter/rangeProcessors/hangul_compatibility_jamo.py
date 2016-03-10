

def process(self):
    self.edit("HANGUL")
    self.edit("LETTER")
    self.edit("-")
    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Hangul Compatibility Jamo")
