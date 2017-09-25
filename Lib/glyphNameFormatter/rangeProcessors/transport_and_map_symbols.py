
def process(self):
    self.setExperimental()
    self.replace("-", " ")
    self.camelCase()
    #self.edit("LETTER")
    pass
    

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Transport and Map Symbols")
