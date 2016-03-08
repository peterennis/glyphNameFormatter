from glyphNameFormatter.scriptPrefixes import scriptPrefixes

def process(self):
    self.scriptTag = scriptPrefixes['<-scriptname->']
    
    # edits go here
    #self.edit("ARMENIAN")
    #self.handleCase()
    #self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("<-rangename->")
