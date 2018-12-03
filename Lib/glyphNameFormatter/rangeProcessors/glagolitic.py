
def process(self):
    self.setExperimental()
    self.edit("GLAGOLITIC")
    self.handleCase()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Glagolitic")
