
def process(self):
    self.replace("EURO-CURRENCY", "euroarchaic")
    self.replace("EURO", "Euro")
    self.replace("SIGN")
    self.compress()
    if not self.has("EURO"):
        self.lower()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Currency Symbols")
