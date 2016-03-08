from glyphNameFormatter.data.scriptPrefixes import scriptPrefixes

def process(self):
    # self.scriptTag = scriptPrefixes['arabic']
    lowercaseOk = True

    # note: these categories are practical
    # but it is always possible to have one
    # edit outside its category just to make it work    self.edit("ARABIC LETTER HAMZA", 'hamza')
    self.edit("ARABIC LETTER ALEF", "alef")

    # digits
    self.edit("EXTENDED ARABIC-INDIC DIGIT", "far")
    self.edit("ARABIC-INDIC CUBE", 'cube')
    self.edit("ARABIC-INDIC FOURTH", 'fourth')
    self.edit("ROOT", 'root')
    self.edit("ARABIC-INDIC DIGIT")

    self.edit("AFGHANI", "afghani")
    self.edit("UIGHUR", "uighur")
    self.edit("KAZAKH", "kazakh")
    self.edit("KIRGHIZ", "kirghiz")
    self.edit("FARSI", "farsi")

    # ligatures
    self.edit("ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA", "sad_lam_alefmaksuraabove")
    self.edit("ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA", "qaf_lam_alefmaksuraabove")
    self.edit("ARABIC SMALL HIGH LIGATURE ALEF WITH LAM WITH YEH", "alef_lam_yehabove")

    # letters
    self.edit("ARABIC LETTER HAMZA", 'hamza')
    self.edit("ARABIC LETTER ALEF", "alef")
    self.edit("MAKSURA", "maksura")
    self.edit("ARABIC LETTER WAW", 'waw')
    self.edit("WASLA", 'wasla')
    self.edit("ARABIC PLACE OF SAJDAH", "Sajdah")
    self.edit('ARABIC END OF AYAH', "Ayahend")
    self.edit("ARABIC VOWEL SIGN", "vowel")

    # letter with letter above
    self.edit("WITH MADDA ABOVE", "madda")
    self.edit("MADDAH ABOVE", "madda")
    self.edit("WITH HAMZA BELOW", 'hamzabelow')
    self.edit("GOAL", "goal")   # needs to preceed hamza above
    self.edit("WITH HAMZA ABOVE", "hamza")
    self.edit("WITH YEH ABOVE", "yeh")
    self.edit("WITH TAIL", "tail")
    self.edit("WITH INVERTED V", "invertedV")
    self.edit("INVERTED V", "invertedV")
    self.edit("INVERTED SMALL V ABOVE", "invertedVabove")
    self.edit("WITH SMALL V BELOW", "Vbelow")
    self.edit("WITH SMALL V", "Vabove")
    self.edit("SMALL V ABOVE", "Vabove")
    self.edit("ARABIC SMALL LOW MEEM", "meembelow")
    self.edit("WITH WAVY HAMZA ABOVE", "wavyhamza")
    self.edit("WITH WAVY HAMZA BELOW", "wavyhamzabelow")
    self.edit("ARABIC SMALL LOW SEEN", "seenlow")

    # signs, markers
    self.edit("ARABIC POETIC VERSE SIGN", "poeticverse")
    self.edit("ARABIC EMPTY CENTRE LOW STOP", 'stopbelow')
    self.edit("ARABIC EMPTY CENTRE HIGH STOP", "stopabove")
    self.edit("ARABIC ROUNDED HIGH STOP WITH FILLED CENTRE", "filledstopabove")
    self.edit("ARABIC SIGN SAFHA", "Safha")
    self.edit("ARABIC SIGN SANAH", "Sanah")
    self.edit("ARABIC FOOTNOTE MARKER", "footnote")
    self.edit("ARABIC SIGN MISRA", "misra")
    self.edit("ARABIC SIGN TAKHALLUS", "takhallus")
    self.edit("ARABIC START OF RUB EL HIZB", "RubElHizbstart")
    self.edit("ARABIC SIGN SALLALLAHOU ALAYHE WASSALLAM", "HonSAW")
    self.edit("ARABIC SIGN ALAYHE ASSALLAM", "HonAA")
    self.edit("ARABIC SIGN RAHMATULLAH ALAYHE", "HonRA")
    self.edit("RABIC SIGN RADI ALLAHOU ANHU", "HonRAA")
    self.edit("ARABIC SMALL HIGH DOTLESS HEAD OF KHAH", "khahdotlessabove")
    self.edit("TATWEEL", "kashida")
    self.edit("RAY", 'ray')
    self.edit("ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO", 'zerosquareabove')

    # punctuation
    self.edit("ARABIC PERCENT SIGN", "percent")
    self.edit("ARABIC NUMBER SIGN", "numbersign")
    self.edit("ARABIC COMMA", "comma")
    self.edit("ARABIC FULL STOP", "period")
    self.edit("ARABIC QUESTION MARK", "question")
    self.edit("ARABIC DECIMAL SEPARATOR", "decimal")
    self.edit("ARABIC THOUSANDS SEPARATOR", "thousands")
    self.edit("ARABIC-INDIC PER MILLE SIGN", "permille")
    self.edit("ARABIC-INDIC PER TEN THOUSAND SIGN", 'perthousand')
    self.edit("ARABIC DATE SEPARATOR", "date")
    self.edit("ARABIC SEMICOLON", "semicolon")
    self.edit("ARABIC TRIPLE DOT PUNCTUATION MARK", 'tripledot')
    self.edit("POSTPOSITION MEN", "menpost")
    self.edit("ARABIC SIGN SINDHI", "Sindhi")

    # marks
    self.edit("WITH RING", "ring")
    self.edit("WITH TAIL", "tail")
    self.edit("SWASH", "swash")
    self.edit("DOTLESS", "dotless")

    # dots
    self.edit("WITH DOT BELOW AND DOT ABOVE", "dotbelowdotabove")
    self.edit("WITH DOT MOVED BELOW", 'dotbelowright')
    self.edit("WITH DOT ABOVE", "dotabove")
    self.edit("WITH DOT BELOW", "dotbelow")
    self.edit("DOT BELOW", "dotbelow")
    self.edit("WITH TWO DOTS ABOVE", 'twoabove')
    self.edit("WITH TWO DOTS VERTICAL ABOVE", "twodotsvertical")
    self.edit("WITH TWO DOTS BELOW", 'twobelow')
    self.edit("WITH TWO DOTS", "dotted")
    self.edit("WITH THREE DOTS BELOW", 'threebelow')
    self.edit("DOWNWARDS", "down")
    self.edit("AND THREE DOTS ABOVE", 'threeabove')
    self.edit("WITH THREE DOTS ABOVE", 'threeabove')
    self.edit("THREE DOTS", "threeabove")
    self.edit("WITH FOUR DOTS ABOVE", 'fourdotsabove')
    self.edit("HIGH HAMZA", "highhamza")
    self.edit("ARABIC LETTER SUPERSCRIPT ALEF", "alefabove")
    self.edit("AND SMALL TAH", "tahsmall")  # needs to follow dotbelow
    self.edit("ARABIC SMALL HIGH", 'above') # needs to be after all the dots
    self.edit("SMALL", 'small')
    self.edit("REVERSED", "reversed")

    self.processAs("Helper Arabic Positions")

    if self.uniName is not None:
        if "ARABIC LETTER" in self.uniName:
            lowercaseOk = True
        elif "ARABIC-INDIC DIGIT" in self.uniName:
            lowercaseOk = True

    # cleanup
    self.replace("ARABIC")
    self.replace("SIGN")
    self.replace("LETTER")
    if self.has("-"):
        self.replace('-')
    if lowercaseOk:
       self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter.test import printRange
    printRange("Arabic")
