
def process(self):
    self.replace("BALLOT BOX", "checkbox")
    self.replace("WITH CHECK", "chekced")
    self.replace("WITH X", "x")
    self.replace("SUIT")
    self.replace("CHESS")
    self.replace("SIGN")
    self.replace("RECYCLING", "recycle")
    self.replace("SYMBOL")
    self.replace("FOR GENERIC MATERIALS", "generic")
    self.replace("PARTIALLY-RECYCLED", "recyclepartially")
    self.replace("FOR TYPE-")
    self.replace("FACE-")
    self.replace("WITH")
    self.replace("FOR")
    self.replace("AND")

    self.replace("1", "one")
    self.replace("2", "two")
    self.replace("3", "three")
    self.replace("4", "four")
    self.replace("5", "five")
    self.replace("6", "six")
    self.replace("7", "seven")

    self.replace("WHITE DOT RIGHT", "whitedotright")
    self.replace("DOT RIGHT", "dotright")

    self.replace("WAY LEFT WAY", "wayleftway")
    self.edit("DOUBLE", "dbl")

    parts = [
        "ASCENDING", "DESCENDING",
        "LEFT", "RIGHT", "UP", "DOWN",
        "REVERSED", "ROTATED", "OUTLINED", "HEAVY",
        "UNIVERSAL",
        "BLACK", "WHITE",
        ]
    for part in parts:
        self.edit(part, part.lower())

    self.replace("-")
    self.lower()
    self.compress()


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Miscellaneous Symbols")
