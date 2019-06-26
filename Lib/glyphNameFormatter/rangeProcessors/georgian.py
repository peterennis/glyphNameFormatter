
def process(self):
    # edits go here
    self.edit("GEORGIAN PARAGRAPH SEPARATOR", "paragraphseparator")
    self.edit("MODIFIER LETTER GEORGIAN NAR", "narmod")
    self.edit("GEORGIAN")
    self.handleCase()
    if self.has("GEORGIAN LETTER"):
        self.edit("LETTER")
        self.suffix("Mkhedruli")
        self.lower()
    elif self.has("GEORGIAN CAPITAL LETTER"):
        self.suffix("Asomtavruli")
    self.compress()
    if self.has("GEORGIAN PARAGRAPH SEPARATOR"):
        self.scriptPrefix()


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Georgian")
