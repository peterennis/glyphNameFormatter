from glyphNameFormatter.scriptPrefixes import scriptPrefixes

def process(self):
    self.scriptTag = scriptPrefixes['greek']

    self.processAs("Greek and Coptic")

    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Greek Extended")
