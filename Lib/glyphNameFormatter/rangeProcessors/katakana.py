from glyphNameFormatter.scriptPrefixes import scriptPrefixes

def process(self):
    self.scriptTag = scriptPrefixes['japan']
    self.editToFinal("KATAKANA-HIRAGANA", "kana")
    self.editToFinal("KATAKANA", "katakana")
    self.edit("SOUND MARK")
    self.edit("MARK")
    self.edit("LETTER")
    self.edit("SMALL", "small")
    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Katakana")
