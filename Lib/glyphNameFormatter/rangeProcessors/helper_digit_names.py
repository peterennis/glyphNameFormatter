from glyphNameFormatter.scriptPrefixes import scriptPrefixes

def process(self):
    
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

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Helper Digit Names")
