

def process(self):
    self.edit("OCR")
    self.edit("DOUBLE", "dbl")
    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Optical Character Recognition")
