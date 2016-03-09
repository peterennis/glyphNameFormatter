from glyphNameFormatter.data.scriptPrefixes import addScriptPrefix


def process(self):
    self.edit("CYRILLIC")
    if self.uniNumber == 0x042D:
        self.uniNameProcessed = "Ereversed"
        return
    if self.uniNumber == 0x044D:
        self.uniNameProcessed = "ereversed"
        return

    self.edit("CAPITAL LIGATURE EN GHE", "En_Ghe")
    self.edit("SMALL LIGATURE EN GHE", "en_ghe")
    self.edit("CAPITAL LIGATURE A IE", "A_Ie")
    self.edit("SMALL LIGATURE A IE", "a_ie")
    self.edit("CAPITAL LIGATURE TE TSE", "Te_Tse")
    self.edit("SMALL LIGATURE TE TSE", "te_tse")
    self.edit("CAPITAL LETTER HARD SIGN", "Hard")
    self.edit("CAPITAL LETTER SOFT SIGN", "Soft")

    # corrections from Ilya
    self.edit("CAPITAL LETTER YERU", "Ylong")
    self.edit("SMALL LETTER YERU", "ylong")
    self.edit("CAPITAL LETTER GHE", "Ge")
    self.edit("SMALL LETTER GHE", "ge")

    self.edit("SMALL LETTER PALOCHKA", "palochka")
    self.edit("LETTER PALOCHKA", "Palochka")

    self.edit("BIG", "big")         # Yus
    self.edit("LITTLE", "little")   # yus
    self.edit("BARRED", "bar")
    self.edit("STRAIGHT", "straight")
    self.edit("SHORT", "short")
    self.edit("IOTIFIED", "iotified")
    self.edit("WITH TITLO", 'titlo')
    self.edit("TITLO", 'titlo')
    self.edit("WITH UPTURN", "up")
    self.edit("WITH DESCENDER", "descender")
    self.edit("WITH VERTICAL STROKE", "verticalstroke")
    self.edit("WITH TAIL", "tail")
    self.edit("WITH TICK", "tick")

    self.edit("HARD SIGN", "hard")
    self.edit("SOFT SIGN", "soft")

    self.edit("ROUND", "round")
    self.edit("KOMI", 'komi')
    self.edit("BYELORUSSIAN-UKRAINIAN", "ukr")
    self.edit("UKRAINIAN", "ukr")
    self.edit("ABKHASIAN", "abkhaz")
    self.edit("BASHKIR", "bashkir")
    self.edit("KHAKASSIAN", "khakas")
    self.edit("ALEUT", "aleut")

    self.edit("HUNDRED THOUSANDS SIGN", "hundredthousands")
    self.edit("MILLIONS SIGN", "millions")
    self.edit("THOUSANDS SIGN", "thousands")
    self.edit("POKRYTIE", "pokrytie")
    self.edit("PALATALIZATION", "palatalization")
    self.edit("DASIA PNEUMATA", "dasia", "pneumata")
    self.edit("PSILI PNEUMATA", "psili", "pneumata")

    self.edit("COMBINING", "cmb")


    self.replace("CAPITAL LETTER KSI", addScriptPrefix("Ksi", script="Cyrillic"))
    self.replace("SMALL LETTER KSI", addScriptPrefix("ksi", script="Cyrillic"))
    self.replace("CAPITAL LETTER PSI", addScriptPrefix("Psi", script="Cyrillic"))
    self.replace("SMALL LETTER PSI", addScriptPrefix("psi", script="Cyrillic"))

    self.processDiacritics()
    self.handleCase()


    # cleanup
    self.edit("CAPITAL")
    self.edit("LETTER")

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Cyrillic")
