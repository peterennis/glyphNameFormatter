

def process(self):
    self.edit("ANNOTATION")
    self.edit("CHARACTER", "char")
    self.edit("OBJECT", "obj")
    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Specials")
