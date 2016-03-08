

def process(self):
    self.replace("EURO-CURRENCY", "euroarchaic")
    self.replace("SIGN")
    self.compress()
    self.lower()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Currency Symbols")
