from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):
    self.scriptTag = scriptPrefixes['hiragana']

    self.edit("LETTER")
    self.edit("SMALL", "small")
    self.edit("KATAKANA-HIRAGANA VOICED SOUND MARK", "voicedmarkkana")
    self.edit("KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK", "semivoicedmarkkana")
    self.edit("HIRAGANA ITERATION MARK", "iterationhiragana")
    self.edit("HIRAGANA VOICED ITERATION MARK", "voicediterationhiragana")
    self.editToFinal("HIRAGANA", "hiragana")
    self.editToFinal("COMBINING", "cmb")
    self.lower()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Hiragana")
