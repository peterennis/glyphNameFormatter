
def process(self):
    self.edit("MTAVRULI", "Mtavruli")
    self.processAs("Georgian")


if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Georgian Extended")
