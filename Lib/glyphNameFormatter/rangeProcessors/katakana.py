
def process(self):
    self.edit("KATAKANA-HIRAGANA", "kana")
    self.edit("SOUND MARK")
    self.edit("MARK")
    self.edit("LETTER")
    self.edit("SMALL", "small")
    self.editToFinal("KATAKANA", "katakana")
    self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Katakana")
