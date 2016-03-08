from glyphNameFormatter.scriptPrefixes import scriptPrefixes

def process(self):
    
    self.replace("FOURTEEN", "fourteen")
    self.replace("SIXTEEN", "sixteen")
    self.replace("SEVENTEEN", "seventeen")
    self.replace("EIGHTEEN", "eighteen")
    self.replace("NINETEEN", "nineteen")

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
    self.replace("TEN", "ten")
    self.replace("ELEVEN", "eleven")
    self.replace("TWELVE", "twelve")
    self.replace("THIRTEEN", "thirteen")
    self.replace("FIFTEEN", "fifteen")
    self.replace("TWENTY", "twenty")

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Helper Digit Names")
