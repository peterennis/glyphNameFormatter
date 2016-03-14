
def process(self):
    self.edit("CHEROKEE")
    self.edit("LETTER")
    self.lower()
    self.scriptPrefix()
    

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    from glyphNameFormatter.tools import debug
    printRange("Cherokee Supplement")
    debug(0xAB70)