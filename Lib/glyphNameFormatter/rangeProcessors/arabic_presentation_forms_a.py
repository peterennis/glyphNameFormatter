from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):
    self.scriptTag = scriptPrefixes['arabic']

    self.processAs("Arabic")
    # more specific edits needed


if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Arabic Presentation Forms-A")
