
def process(self):

	# Specifically: do not add suffixes for arabic marks
    if 0xfe70 <= self.uniNumber <= 0xfe80:
    	#self.compress()
    	self.camelCase()
    # shadda ligatures do not need suffixes
    # elif 0xfc61 <= self.uniNumber <= 0xfc5e:
    # 	#self.compress()
    # 	self.camelCase()

    # positions
    self.edit('INITIAL FORM', ".init")
    self.edit('MEDIAL FORM', ".medi")
    self.edit('FINAL FORM', ".fina")
    self.edit('ISOLATED FORM', ".isol")

if __name__ == "__main__":
    from glyphNameFormatter.exporters import printRange
    printRange("Helper Arabic Positions")
