from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):
    self.uniNameProcessed = "private_use_%04X"%self.uniNumber

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Private Use Area")
