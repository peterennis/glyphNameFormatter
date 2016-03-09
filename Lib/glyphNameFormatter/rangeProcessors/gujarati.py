
def process(self):

	#GUJARATI VOWEL SIGN CANDRA E
	#GUJARATI VOWEL CANDRA E

    self.edit("GUJARATI")
    self.edit("LETTER")
    self.edit("DIGIT")
    self.edit("VOWEL SIGN", "sign")
    self.edit("VOWEL")
    self.edit("SIGN")
    self.processAs("Helper Indic")
    self.processAs("Helper Numbers")
    self.lower()
    

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Gujarati")
