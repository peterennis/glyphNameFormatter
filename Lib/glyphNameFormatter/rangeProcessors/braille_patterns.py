
def process(self):
    #self.setExperimental()
    #self.edit("TAMIL")
    self.replace("BRAILLE PATTERN BLANK", "blank")
    self.replace("BRAILLE PATTERN DOTS", "dots")
    self.replace("-", "")
    pass
    

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Braille Patterns")
