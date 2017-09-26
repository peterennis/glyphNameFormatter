
def process(self):
    #self.setExperimental()
    #self.edit("circled", )
    self.edit("-", " ")
    self.edit("SYMBOL", "")
    self.camelCase()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Miscellaneous Symbols and Pictographs")
