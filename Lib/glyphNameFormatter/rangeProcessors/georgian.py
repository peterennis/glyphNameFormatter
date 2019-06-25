
def process(self):
    # edits go here
    self.edit("GEORGIAN PARAGRAPH SEPARATOR", "paragraphseparator")
    self.edit("GEORGIAN")
    self.handleCase()
    if self.has("GEORGIAN LETTER"):
        self.edit("LETTER")
        self.suffix("Mkhedruli")
        self.lower()
    else:
        self.suffix("Asomtavruli")
    self.compress()
    self.scriptPrefix()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Georgian")
