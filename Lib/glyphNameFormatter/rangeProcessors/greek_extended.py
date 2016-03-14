
def process(self):
    self.processAs("Greek and Coptic")
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Greek Extended")
