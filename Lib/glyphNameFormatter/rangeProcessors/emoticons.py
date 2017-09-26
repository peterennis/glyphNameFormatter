

def process(self):
    # just to test unicode 8 stuff
    # not complete
    #self.setExperimental()
    self.replace("-", " ")
    self.camelCase()
    #self.replace(" ", "_")
    #self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Emoticons")
