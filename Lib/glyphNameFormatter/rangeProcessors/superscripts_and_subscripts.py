from glyphNameFormatter.scriptPrefixes import scriptPrefixes

def process(self):
    #self.scriptTag = scriptPrefixes['<-scriptname->']
    
    # edits go here
    self.edit("PARENTHESIS", "paren")
    self.edit("EQUALS SIGN", "equal")
    self.edit("PLUS SIGN", "plus")
    self.edit("MINUS", "minus")

    self.edit("LEFT", "left")
    self.edit("RIGHT", "right")

    self.edit("SUPERSCRIPT", ".superior")
    self.edit("SUBSCRIPT", ".inferior")
    self.processAs("Helper Digit Names")
    self.edit("LATIN")
    self.handleCase()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Superscripts and Subscripts")
