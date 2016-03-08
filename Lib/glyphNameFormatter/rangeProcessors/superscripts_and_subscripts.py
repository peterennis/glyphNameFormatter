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
    self.replace('ZERO', 'zero')
    self.replace('ONE', 'one')
    self.replace('TWO', 'two')
    self.replace('THREE', 'three')
    self.replace('FOUR', 'four')
    self.replace('FIVE', 'five')
    self.replace('SIX', 'six')
    self.replace('SEVEN', 'seven')
    self.replace('EIGHT', 'eight')
    self.replace('NINE', 'nine')
    self.edit("LATIN")
    self.handleCase()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Superscripts and Subscripts")
