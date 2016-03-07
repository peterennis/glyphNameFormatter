from glyphNameFormatter.scriptPrefixes import scriptPrefixes

def process(self):
    if self.verbose:
        print "processArabic"
    self.scriptTag = scriptPrefixes['arabic']

    # AGD compatible
    self.edit("ARABIC SMALL HIGH LIGATURE QAF WITH LAM WITH ALEF MAKSURA", "qam_lamalefabove")
    self.edit("ARABIC SMALL HIGH LIGATURE SAD WITH LAM WITH ALEF MAKSURA", "sad_lamalefabove")
    self.edit("ARABIC SIGN SAFHA", "Safha")
    self.edit("ARABIC DATE SEPARATOR", "Date")
    self.edit("ARABIC POETIC VERSE SIGN", "Poetic")
    self.edit("ARABIC SIGN MISRA", "Misra")
    self.edit("ARABIC LETTER DAL WITH INVERTED V", "dalinvertedv")
    self.edit("ARABIC LETTER REH WITH INVERTED V", "rehinvertedv")
    self.edit("ARABIC SMALL WAW", "wawsmall")
    self.edit("ARABIC SMALL YEH", "yehsmall")
    self.edit("WITH DOT BELOW AND DOT ABOVE", "dotbelowdotabove")
    self.edit("WITH DOT MOVED BELOW", 'dotbelowright')
    self.edit("WITH DOT ABOVE", "dotabove")
    self.edit("WITH TWO DOTS ABOVE", 'twoabove')
    self.edit("WITH TWO DOTS BELOW", 'twobelow')
    self.edit("WITH THREE DOTS BELOW AND THREE DOTS ABOVE", 'threebelowthreeabove')
    self.edit("WITH THREE DOTS BELOW", 'threebelow')
    self.edit("WITH THREE DOTS ABOVE", 'threeabove')
    self.edit("HIGH THREE DOTS", "threeabove")
    self.edit("HIGH HAMZA", "highhamza")
    self.edit("ARABIC SMALL HIGH LAM ALEF", "lamalefabove")
    self.edit("ARABIC SMALL HIGH MEEM INITIAL FORM", "meemabove.init")
    self.edit("WITH HAMZA ABOVE", "hamza")
    self.edit("WITH YEH ABOVE", 'yehabove')
    self.edit("ARABIC MADDAH ABOVE", "maddah")
    self.edit("ARABIC SUBSCRIPT ALEF", "alefbelow")
    self.edit("ARABIC VOWEL SIGN DOT BELOW", "dotbelow")
    self.edit("ARABIC REVERSED DAMMA", "dammareversed")
    self.edit("ARABIC FATHA WITH TWO DOTS", "fathadotted")
    self.edit("ARABIC LETTER ALEF WITH MADDA ABOVE", "alefmadda")
    self.edit("ARABIC LETTER ALEF WITH HAMZA ABOVE", "alefhamza")
    self.edit("ARABIC LETTER WAW WITH HAMZA ABOVE", "wawhamza")
    self.edit("ARABIC LETTER ALEF WITH HAMZA BELOW", "alefhamzabelow")
    self.edit("ARABIC-INDIC DIGIT")
    self.edit("ARABIC PERCENT SIGN", "percent")
    self.edit("ARABIC DECIMAL SEPARATOR", "Decimal")
    self.edit("ARABIC THOUSANDS SEPARATOR", "Thousands")
    self.edit("ARABIC LETTER DOTLESS BEH", 'behdotless')
    self.edit("ARABIC LETTER DOTLESS QAF", 'qafdotless')
    self.edit("ARABIC SIGN SINDHI AMPERSAND", "ampersand","sindhi")
    self.edit("ARABIC SIGN SINDHI POSTPOSITION MEN", "Men", "post" ,"sindhi" )
    self.edit("WITH RING", "ring")
    self.edit("WITH TAIL", "tail")
    self.edit("ARABIC LETTER TEH WITH THREE DOTS ABOVE DOWNWARDS", 'tehthreedownabove')
    self.edit("ARABIC LETTER HAH WITH TWO DOTS VERTICAL ABOVE", "hahtwodotsverticalabove")
    self.edit("ARABIC SMALL HIGH UPRIGHT RECTANGULAR ZERO", 'zerosquareabove')
    self.edit("WITH DOT BELOW", "dotbelow")
    self.edit("WITH FOUR DOTS ABOVE", 'fourdotsabove')
    self.edit("END OF AYAH", "ayahend")
    self.edit("ARABIC START OF RUB EL HIZB", "rubElHizbstart")
    self.edit("LOW SEEN", "seenlow")
    self.edit("PLACE OF SAJDAH", 'Sajdah')
    self.edit("EMPTY CENTRE LOW STOP", "stopabove")
    self.edit("EMPTY CENTRE HIGH STOP", "stopbelow")
    self.edit("ROUNDED HIGH STOP WITH FILLED CENTRE", 'stopblackabove')
    self.edit("ARABIC SMALL HIGH DOTLESS HEAD OF KHAH", "khahdotlessabove")
    self.edit("ARABIC SMALL LOW MEEM", "meembelow")
    self.edit("MARK NOON GHUNNA", "noonghunnamark")
    self.edit("WITH INVERTED V", "vinverted")
    self.edit("INVERTED", 'inverted')
    self.edit("SUPERSCRIPT", "above")

    self.edit("EXTENDED", "Far")
    self.replace("ARABIC")

    lowercaseOk = True
    self.replace("ZERO WIDTH NO-BREAK SPACE", "zerowidthnbspace")
    self.edit("AFGHANI SIGN", "afghani")
    self.edit("UIGHUR", "uighur")
    self.edit("KAZAKH", "kazakh")
    self.edit("KIRGHIZ", "kirghiz")
    self.edit("FARSI", "farsi")

    self.edit("SMALL HIGH", "small", "above")
    if self.has("LETTER"):
        self.replace("LETTER")
    if self.has('LIGATURE'):
        self.replace("LIGATURE")
    self.edit('INITIAL FORM', ".init")
    self.edit('MEDIAL FORM', ".medi")
    self.edit('FINAL FORM', ".fina")
    self.edit('ISOLATED FORM', ".isol")
    self.replace("QUESTION MARK", "question")
    self.edit("SIGN SANAH", "Sanah")
    self.edit("FOOTNOTE MARKER", "Footnote")
    if self.has("LIGATURE"):
        self.replace("WITH", "_")
    else:
        self.replace("WITH", "")
    if self.has("-"):
        self.replace('-')
    self.replace("SALLALLAHOU ALAYHE WASALLAM", "sallallahou_alayhe_wasallam")
    if self.replace("BISMILLAH AR-RAHMAN AR-RAHEEM", "bismillah_arRahman_arRaheem"):
        lowercaseOk = False
    if lowercaseOk:
        self.lower()
    self.compress()

if __name__ == "__main__":
    from glyphNameFormatter import GlyphName
    from glyphNameFormatter.unicodeRangeNames import getRangeByName

    for u in range(*getRangeByName("Arabic")):
        g = GlyphName(uniNumber=u)
        if g.uniName is not None:
            print g.getName().ljust(30), "%04X" % g.uniNumber, "\t", g.uniName
