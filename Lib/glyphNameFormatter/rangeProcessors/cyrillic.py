from glyphNameFormatter.scriptPrefixes import scriptPrefixes

def process(self):
    self.scriptTag = scriptPrefixes['cyrillic']
    
    # edits go here
    self.edit("CYRILLIC")

    self.edit("CAPITAL LIGATURE EN GHE", "En_Ghe")
    self.edit("SMALL LIGATURE EN GHE", "en_ghe")
    self.edit("CAPITAL LIGATURE A IE", "A_Ie")
    self.edit("SMALL LIGATURE A IE", "a_ie")
    self.edit("CAPITAL LIGATURE TE TSE", "Te_Tse")
    self.edit("SMALL LIGATURE TE TSE", "te_tse")
    self.edit("CAPITAL LETTER HARD SIGN", "Hard")
    self.edit("CAPITAL LETTER SOFT SIGN", "Soft")

    self.edit("BIG", "big")			# Yus
    self.edit("LITTLE", "little")	# yus
    self.edit("BARRED", "bar")
    self.edit("STRAIGHT", "straight")
    self.edit("SHORT", "short")
    self.edit("IOTIFIED", "iotified")
    self.edit("WITH TITLO", 'titlo')
    self.edit("WITH UPTURN", "up")
    self.edit("WITH DESCENDER", "descender")
    self.edit("WITH VERTICAL STROKE", "verticalstroke")
    self.edit("WITH TAIL", "tail")
    self.edit("WITH TICK", "tick")

    self.edit("HARD SIGN", "hard")
    self.edit("SOFT SIGN", "soft")

    self.edit("ROUND", "round")
    self.edit("PALOCHKA", "Palochka")
    self.edit("KOMI", 'komi')
    self.edit("BYELORUSSIAN-UKRAINIAN", "ukran")
    self.edit("UKRAINIAN", "ukran")
    self.edit("ABKHASIAN", "abkhaz")
    self.edit("BASHKIR", "bashkir")
    self.edit("KHAKASSIAN", "khakas")
    self.edit("ALEUT", "aleut")

    self.processDiacritics()
    self.handleCase()

    # cleanup
    self.edit("CAPITAL")
    self.edit("LETTER")

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Cyrillic")
