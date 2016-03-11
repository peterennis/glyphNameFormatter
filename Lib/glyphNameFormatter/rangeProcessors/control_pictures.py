

def process(self):
    self.edit("SYMBOL")
    self.replace("FORM", "form")
    self.edit("FOR")
    self.edit("TABULATION", "tab")
    self.lower()
    self.compress()
    self.scriptPrefix()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Control Pictures")
