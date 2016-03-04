


import unicodedata

from unicodeRangeNames import *

class GlyphName(object):

    ambiguousNames =[
        "A",
        "Abreve",
        "Adieresis",
        "E",
        "Edieresis",
        "Gamma",
        "I",
        "Idieresis",
        "Igrave",
        "Imacron",
        "Iota",
        "Koppa",
        "O",
        "Odieresis",
        "Omega",
        "Psi",
        "Schwa",
        "U",
        "Udblacute",
        "Udieresis",
        "Umacron",
        "Upsilon",
        "a",
        "abreve",
        "adieresis",
        "delta",
        "e",
        "edieresis",
        "i",
        "idieresis",
        "igrave",
        "imacron",
        "koppa",
        "o",
        "odieresis",
        "omega",
        "pe",
        "psi",
        "question",
        "u",
        "udblacute",
        "udieresis",
        "umacron",
    ]

    def __init__(self, niceName=None, uniNumber=None):
        self.niceName = niceName
        self.uniNumber = uniNumber
        self.uniLetter = None
        self.uniName = ""
        self.uniNameProcessed = self.uniName
        self.uniRangeName = "No Range"
        self.letterCase = None
        self.isLigature = False
        self.scriptPrefix = ""
        self.languageSuffix = []
        self.suffixParts = []
        self.finalParts = []
        self.mustAddScript = False  # set to True if we need to add script to disambiguate
        self.latinCentric = True    # admit latincentric naming, if we can leave out latin tags, go for it
        self.lookup()
        self.process()

    def hasName(self):
        if not self.uniName:
            return False
        return True
        # print "xx", self.uniNameProcessed
        # if self.uniNameProcessed is not self.uniName and self.uniName is not None:
        #     return True
        # return False

    def hashWords(self):
        parts = {}
        if not self.uniName:
            return parts
        for p in self.uniName.split(" "):
            for q in p.split("-"):
                try:
                    int("0x"+q, 16)
                except ValueError:
                    if not q in parts:
                        parts[q] = 0
                    parts[q] += 1
        return parts

    def lookup(self):
        if self.uniNumber is None:
            return
        self.uniLetter = unichr(self.uniNumber)
        try:
            self.uniName = unicodedata.name(self.uniLetter)
            self.uniNameProcessed = self.uniName
        except ValueError:
            pass
        self.uniRangeName = getRangeName(self.uniNumber)

    def has(self, namePart):
        if namePart in self.uniName:
            return True
        return False

    def handleGreekCase(self):
        if self.has("GREEK LETTER") or self.has("GREEK SMALL LETTER"):
            parts = self.uniNameProcessed.split(" ")
            for i in range(len(parts)-1):
                p = parts[i].strip()
                src = new = parts[i+1].strip()
                if p == "small" or p == "SMALL":
                    new = new.lower()
                elif p == "capital" or p == "CAPITAL":
                    if len(new)==1:
                        new = new[0].upper()
                    else:
                        new = new[0].upper()+new[1:].lower()
                else:
                    continue
                self.replace(p)
                self.replace(src, new)
                break

    def handleCase(self):
        if self.has("CAPITAL LETTER") or self.has("SMALL LETTER"):
            parts = self.uniNameProcessed.split(" ")
            for i in range(len(parts)-1):
                p = parts[i].strip()
                src = new = parts[i+1].strip()
                if p == "small" or p == "SMALL":
                    new = new.lower()
                elif p == "capital" or p == "CAPITAL":
                    if len(new)==1:
                        new = new[0].upper()
                    else:
                        new = new[0].upper()+new[1:].lower()
                else:
                    continue
                self.replace(p)
                self.replace(src, new)
                break

    def processStructure(self):
        if self.has("LIGATURE"):
            self.isLigature = True

    def processCase(self):
        if self.has("CAPITAL LETTER"):
            self.letterCase = "uppercase"
        if self.has("SMALL LETTER"):
            self.letterCase = "lowercase"

    def processShape(self):
        self.edit("LITTLE", "little")
        self.edit("BIG", "big")
        self.edit("ROUND", "round")

        self.edit("SHORT", "short")
        if self.has("STRAIGHT"):
            self.replace("STRAIGHT")
            self.suffix("straight")
        self.edit("BARRED", "barred")
        if self.has('CLOSED'):
            self.replace("CLOSED")
            self.suffix("closed")
        if self.has('REVERSED'):
            if self.replace("REVERSED"):
                self.suffix("reversed")
        if self.has("MONOCULAR"):
            self.replace("MONOCULAR")
            self.suffix("monocular")

        if self.has("WITH TITLO"):
            self.replace("WITH TITLO")
            self.suffix("titlo")
        if self.has("TITLO"):
            self.replace("TITLO")
            self.suffix("titlo")
        if self.has("WITH TAIL"):
            self.replace("WITH TAIL")
            self.suffix("tail")
        if self.has("WITH TICK"):
            self.replace("WITH TICK")
            self.suffix("tick")
        if self.has("WITH DESCENDER"):
            if self.replace("WITH DESCENDER"):
                self.suffix("descender")
        if self.has("WITH UPTURN"):
            if self.replace("WITH UPTURN"):
                self.suffix("up")
        if self.has("WITH STROKE"):
            if self.replace("WITH STROKE"):
                self.suffix("stroke")
        if self.has("WITH VERTICAL STROKE"):
            self.replace("WITH VERTICAL STROKE")
            self.suffix("verticalstroke")
        if self.has("WITH DIAGONAL STROKE"):
            self.replace("WITH DIAGONAL STROKE")
            self.suffix("diagonalstroke")
        if self.has("WITH HIGH STROKE"):
            if self.replace("WITH HIGH STROKE"):
                self.suffix("highstroke")
        if self.has("WITH SWASH TAIL"):
            self.replace("WITH SWASH TAIL")
            self.suffix("swash")
            self.suffix("tail")
        if self.has("WITH COMMA BELOW"):
            self.replace("WITH COMMA BELOW")
            self.suffix("commaaccent")
        if self.has("WITH PALATAL HOOK"):
            if self.replace("WITH PALATAL HOOK"):
                self.suffix("palatalhook")


    def processDiacritics(self):

        if self.has("WITH CIRCUMFLEX AND HOOK ABOVE"):
            if self.replace("WITH CIRCUMFLEX AND HOOK ABOVE"):
                self.suffix("circumflex")
                self.suffix("hookabove")
        if self.has("WITH CIRCUMFLEX AND DOT BELOW"):
            if self.replace("WITH CIRCUMFLEX AND DOT BELOW"):
                self.suffix("circumflex")
                self.suffix("dotbelow")
        if self.has("WITH DOT BELOW AND DOT ABOVE"):
            if self.replace("WITH DOT BELOW AND DOT ABOVE"):
                self.suffix("dotbelow")
                self.suffix("dotabove")
        if self.has("WITH CIRCUMFLEX AND TILDE"):
            if self.replace("WITH CIRCUMFLEX AND TILDE"):
                self.suffix("circumflex")
                self.suffix("tilde")
        if self.has("WITH CARON AND DOT ABOVE"):
            if self.replace("WITH CARON AND DOT ABOVE"):
                self.suffix("caron")
                self.suffix("dotaccent")
        if self.has("WITH ACUTE AND DOT ABOVE"):
            if self.replace("WITH ACUTE AND DOT ABOVE"):
                self.suffix("acute")
                self.suffix("dotaccent")

        if self.has("WITH HORN AND GRAVE"):
            if self.replace("WITH HORN AND GRAVE"):
                self.suffix("horn")
                self.suffix('grave')
        if self.has("WITH HORN AND ACUTE"):
            if self.replace("WITH HORN AND ACUTE"):
                self.suffix("horn")
                self.suffix('acute')
        if self.has("WITH HORN AND TILDE"):
            if self.replace("WITH HORN AND TILDE"):
                self.suffix("horn")
                self.suffix('tilde')
        if self.has("WITH HORN AND HOOK ABOVE"):
            if self.replace("WITH HORN AND HOOK ABOVE"):
                self.suffix("horn")
                self.suffix("hookabove")
        if self.has("WITH HORN AND DOT BELOW"):
            if self.replace("WITH HORN AND DOT BELOW"):
                self.suffix("horn")
                self.suffix("dot")
                self.suffix("below")
        if self.has("WITH BREVE AND TILDE"):
            if self.replace("WITH BREVE AND TILDE"):
                self.suffix("breve")
                self.suffix("tilde")
        if self.has("WITH BREVE AND ACUTE"):
            if self.replace("WITH BREVE AND ACUTE"):
                self.suffix("breve")
                self.suffix("acute")
        if self.has("WITH BREVE AND HOOK ABOVE"):
            if self.replace("WITH BREVE AND HOOK ABOVE"):
                self.suffix("breve")
                self.suffix("hookabove")
        if self.has("WITH BREVE AND DOT BELOW"):
            if self.replace("WITH BREVE AND DOT BELOW"):
                self.suffix("breve")
                self.suffix("dotbelow")
        if self.has("WITH BREVE BELOW"):
            if self.replace("WITH BREVE BELOW"):
                self.suffix("breve")
                self.suffix("below")
        if self.has("WITH TILDE AND DIAERESIS"):
            if self.replace("WITH TILDE AND DIAERESIS"):
                self.suffix("tilde")
                self.suffix("dieresis")
        if self.has("WITH BREVE AND GRAVE"):
            if self.replace("WITH BREVE AND GRAVE"):
                self.suffix("breve")
                self.suffix("grave")

        if self.has("WITH DOT BELOW AND MACRON"):
            self.replace("WITH DOT BELOW AND MACRON")
            self.suffix("macron")
            self.suffix("dot")
        if self.has("WITH DIAERESIS AND ACUTE"):
            self.replace("WITH DIAERESIS AND ACUTE")
            self.suffix("dieresis")
            self.suffix("acute")
        if self.has("WITH DIAERESIS AND TILDE"):
            self.replace("WITH DIAERESIS AND TILDE")
            self.suffix("dieresis")
            self.suffix("tilde")
        if self.has("WITH TILDE BELOW"):
            self.replace("WITH TILDE BELOW")
            self.suffix("tilde")
            self.suffix("below")
        if self.has('WITH CIRCUMFLEX AND ACUTE'):
            self.replace("WITH CIRCUMFLEX AND ACUTE")
            self.suffix('circumflex')
            self.suffix('acute')
        if self.has('WITH CIRCUMFLEX AND GRAVE'):
            self.replace("WITH CIRCUMFLEX AND GRAVE")
            self.suffix('circumflex')
            self.suffix('grave')
        if self.has("WITH CIRCUMFLEX BELOW"):
            self.replace("WITH CIRCUMFLEX BELOW")
            self.suffix("circumflex")
            self.suffix("below")
        if self.has("WITH CEDILLA AND ACUTE"):
            self.replace("WITH CEDILLA AND ACUTE")
            self.suffix("cedilla")
            self.suffix("acute")

        if self.has("WITH CEDILLA AND BREVE"):
            self.replace("WITH CEDILLA AND BREVE")
            self.suffix("cedilla")
            self.suffix('breve')
        if self.has("WITH MACRON AND DIAERESIS"):
            if self.replace("WITH MACRON AND DIAERESIS"):
                self.suffix("macron")
                self.suffix("dieresis")
        if self.has("WITH MACRON AND ACUTE"):
            self.replace("WITH MACRON AND ACUTE")
            self.suffix("macron")
            self.suffix("acute")
        if self.has("WITH MACRON AND GRAVE"):
            self.replace("WITH MACRON AND GRAVE")
            self.suffix("macron")
            self.suffix("grave")
        if self.has("WITH INVERTED BREVE"):
            self.replace("WITH INVERTED BREVE")
            self.suffix("inverted")
            self.suffix("breve")
        if self.has("WITH TILDE AND ACUTE"):
            self.replace("WITH TILDE AND ACUTE")
            self.suffix("tilde")
            self.suffix("acute")
        if self.has("WITH TILDE AND MACRON"):
            self.replace("WITH TILDE AND MACRON")
            self.suffix("tilde")
            self.suffix("macron")
        if self.has("WITH DIAERESIS AND MACRON"):
            self.replace("WITH DIAERESIS AND MACRON")
            self.suffix("dieresis")
            self.suffix("macron")
        if self.has("WITH DOT ABOVE AND MACRON"):
            self.replace("WITH DOT ABOVE AND MACRON")
            self.suffix("dotaccent")
            self.suffix("macron")
        if self.has("WITH TOPBAR"):
            self.replace("WITH TOPBAR")
            self.suffix("topbar")

        if self.has("PRECEDED BY APOSTROPHE"):
            self.replace("PRECEDED BY APOSTROPHE")
            self.suffix("apostrophe")

        if self.has("WITH MIDDLE DOT"):
            self.replace("WITH MIDDLE DOT")
            self.suffix("dot")

        if self.has("WITH DOUBLE ACUTE"):
            self.replace("WITH DOUBLE ACUTE")
            self.suffix("dblacute")
            return

        if self.has("WITH DOUBLE GRAVE ACCENT"):
            self.replace("WITH DOUBLE GRAVE ACCENT")
            self.suffix("dblgrave")
            return
        if self.has("WITH DOUBLE GRAVE"):
            self.replace("WITH DOUBLE GRAVE")
            self.suffix("dblgrave")
            return

        if self.has("WITH DOT ABOVE"):
            self.replace("WITH DOT ABOVE")
            self.suffix("dotaccent")
        if self.has("WITH DOT BELOW"):
            if self.replace("WITH DOT BELOW"):
                self.suffix("dotbelow")

        if self.has("WITH GRAVE"):
            self.replace("WITH GRAVE")
            self.suffix("grave")
        if self.has("GRAVE"):
            if self.replace("GRAVE"):
                self.suffix("grave")

        if self.has("WITH HORN"):
            self.replace("WITH HORN")
            self.suffix("horn")

        if self.has("WITH BREVE"):
            self.replace("WITH BREVE")
            self.suffix("breve")
        if self.has("BREVE"):
            if self.replace("BREVE"):
                self.suffix("breve")

        if self.has("WITH DIAERESIS BELOW"):
            if self.replace("WITH DIAERESIS BELOW"):
                self.suffix("dieresis")
                self.suffix("below")
        if self.has("WITH DIAERESIS"):
            self.replace("WITH DIAERESIS")
            self.suffix("dieresis")
        if self.has("DIAERESIS"):
            self.replace("DIAERESIS")
            self.suffix("dieresis")

        if self.has("WITH MACRON"):
            self.replace("WITH MACRON")
            self.suffix("macron")
        if self.has("MACRON"):
            if self.replace("MACRON"):
                self.suffix("macron")


        if self.has("WITH ACUTE"):
            self.replace("WITH ACUTE")
            self.suffix("acute")
        if self.has("ACUTE"):
            if self.replace("ACUTE"):
                self.suffix("acute")

        if self.has("WITH CARON"):
            self.replace("WITH CARON")
            self.suffix("caron")
        if self.has("CARON"):
            if self.replace("CARON"):
                self.suffix("caron")

        if self.has("WITH CIRCUMFLEX"):
            if self.replace("WITH CIRCUMFLEX"):
                self.suffix("circumflex")
        if self.has("CIRCUMFLEX"):
            if self.replace("CIRCUMFLEX"):
                self.suffix("circumflex")

        if self.has("WITH TILDE"):
            self.replace("WITH TILDE")
            self.suffix("tilde")
        if self.has("TILDE"):
            self.replace("TILDE")
            self.suffix("tilde")


        if self.has("WITH CEDILLA"):
            self.replace("WITH CEDILLA")
            self.suffix("cedilla")
        if self.has("CEDILLA"):
            self.replace("CEDILLA")
            self.suffix("cedilla")

        if self.has("WITH OGONEK"):
            if self.replace("WITH OGONEK"):
                self.suffix("ogonek")
        if self.has("OGONEK"):
            if self.replace("OGONEK"):
                self.suffix("ogonek")

        if self.has("WITH RING ABOVE AND ACUTE"):
            if self.replace('WITH RING ABOVE AND ACUTE'):
                self.suffix("ring")
                self.suffix("acute")

        if self.has("WITH RING ABOVE"):
            if self.replace("WITH RING ABOVE"):
                self.suffix("ring")

        if self.has("WITH RING BELOW"):
            self.replace("WITH RING BELOW")
            self.suffix("ringbelow")

        if self.has("WITH RIGHT HALF RING"):
            self.replace("WITH RIGHT HALF RING")
            self.suffix("right")
            self.suffix("halfring")

        if self.has("WITH RETROFLEX HOOK"):
            if self.replace("WITH RETROFLEX HOOK"):
                self.suffix("retroflexhook")

        if self.has("WITH LINE BELOW"):
            self.replace("WITH LINE BELOW")
            self.suffix("linebelow")

        if self.has("WITH BAR"):
            self.replace("WITH BAR")
            self.suffix("bar")

        if self.has("WITH MACRON"):
            if self.replace("WITH MACRON"):
                self.suffix("macron")

        if self.has("WITH MIDDLE TILDE"):
            if self.replace("WITH MIDDLE TILDE"):
                self.suffix('middletilde')
        if self.has("WITH HOOK TAIL"):
            if self.replace("WITH HOOK TAIL"):
                self.suffix("hook")
                self.suffix("tail")

        if self.has("WITH MIDDLE HOOK"):
            if self.replace("WITH MIDDLE HOOK"):
                self.suffix("middlehook")
        if self.has("WITH LOOP"):
            if self.replace("WITH LOOP"):
                self.suffix("loop")


        if self.has("WITH LEFT HOOK"):
            self.replace("WITH LEFT HOOK")
            self.suffix("left")
            self.suffix("hook")
        if self.has("WITH HOOK ABOVE"):
            if self.replace("WITH HOOK ABOVE"):
                self.suffix("hook")
                self.suffix("above")
        if self.has("WITH HOOK"):
            if self.replace("WITH HOOK"):
                self.suffix("hook")
        if self.has("AND HOOK"):
            if self.replace("AND HOOK"):
                self.suffix("hook")
        if self.has("HOOK"):
            if self.replace("HOOK"):
                self.suffix("hook")

        if self.has("BAR") and not self.has("AKBAR") and not self.has("TOPBAR") and not self.has("BARRED"):
            if self.replace("BAR"):
                self.suffix("bar")

        if self.has("WITH CURL"):
            self.replace("WITH CURL")
            self.suffix("curl")


    def processArabic(self):
        self.replace("ARABIC")
        self.scriptPrefix = "ar"

        lowercaseOk = True
        self.edit("UIGHUR", "uighur")
        self.edit("KAZAKH", "kazakh")
        self.edit("KIRGHIZ", "kirghiz")
        self.edit("FARSI", "farsi")
        if self.has("LETTER"):
            self.replace("LETTER")
        if self.has('LIGATURE'):
            self.replace("LIGATURE")
        self.edit('INITIAL FORM', ".init")
        self.edit('MEDIAL FORM', ".medi")
        self.edit('FINAL FORM', ".fina")
        self.edit('ISOLATED FORM', ".isol")

        self.replace("WITH", "_")

        self.replace("SALLALLAHOU ALAYHE WASALLAM", "sallallahou_alayhe_wasallam")
        if self.replace("BISMILLAH AR-RAHMAN AR-RAHEEM", "bismillah_arRahman_arRaheem"):
            lowercaseOk = False

        if lowercaseOk:
            self.lower()
        self.compress()

    def processBoxDrawing(self):
        self.scriptPrefix = "bxd"
        self.replace("BOX DRAWINGS")
        self.replace("AND")
        self.replace("TO")
        self.replace("VERTICAL", "vert")
        self.replace("HORIZONTAL", "horz")
        self.replace("DIAGONAL", "diag")
        self.replace("DOUBLE", "dbl")
        self.replace("TRIPLE", "trpl")
        self.replace("QUAD", "quad")
        self.replace("UPPER", "up")
        self.replace("SINGLE", "sng")
        self.replace("DOWN", "dn")
        self.replace("LOWER", "dn")
        self.lower()
        self.compress()


    def processCyrillic(self):

        if self.has("CYRILLIC"):
            self.replace("CYRILLIC")
            self.scriptPrefix = "cy"

        self.replace("CAPITAL LIGATURE EN GHE", "En_Ghe")
        self.replace("SMALL LIGATURE EN GHE", "en_ghe")
        self.replace("CAPITAL LIGATURE A IE", "A_IE")
        self.replace("SMALL LIGATURE A IE", "a_ie")

        self.processShape()
        self.processDiacritics()

        self.edit("IOTIFIED", "iotified")
        if self.has("HARD SIGN"):
            self.replace("HARD SIGN", "hard")
        if self.has("SOFT SIGN"):
            self.replace("SOFT SIGN", "soft")

        self.edit("COMBINING", "comb")
        if self.has("CAPITAL LETTER"):
            self.replace("CAPITAL LETTER", "capital")
        elif self.has("SMALL LETTER"):
            self.replace("SMALL LETTER", "small")
        elif self.has("SMALL LIGATURE"):
            self.replace("SMALL LIGATURE", "ligsmall")
        elif self.has("LETTER"):
            self.replace("LETTER")
        elif self.has("CAPITAL LIGATURE"):
            self.replace("CAPITAL LIGATURE", "liga")
        if self.has("PALOCHKA"):
            self.replace("PALOCHKA", "Palochka")
        self.edit("KOMI", 'komi')
        self.edit("BYELORUSSIAN-UKRAINIAN", "belarus", "ukrain")
        self.edit("UKRAINIAN", "ukrain")
        self.edit("ABKHASIAN", "abkhas")
        self.edit("BASHKIR", "bashkir")
        self.edit("KHAKASSIAN", "khakas")
        self.edit("ALEUT", "aleut")


        # hard exceptions, or, further coding
        if self.has("HUNDRED THOUSANDS SIGN"):
            self.replace("HUNDRED THOUSANDS SIGN", "hundredthousands")
        if self.has("MILLIONS SIGN"):
            self.replace("MILLIONS SIGN", "millions")
        if self.has("THOUSANDS SIGN"):
            self.replace("THOUSANDS SIGN", "thousands")
        if self.has("POKRYTIE"):
            self.replace("POKRYTIE", "pokrytie")
        if self.has("PALATALIZATION"):
            self.replace("PALATALIZATION", "palatalization")
        if self.has("DASIA PNEUMATA"):
            self.replace("DASIA PNEUMATA", "dasiapneumata")
        if self.has("PSILI PNEUMATA"):
            self.replace("PSILI PNEUMATA", "psilipneumata")

        if self.has("WITH"):
            self.replace("WITH")

        self.handleCase()
        self.compress()

    def processMisc(self):
        # appear in the arabic list
        self.replace("ORNATE LEFT PARENTHESIS", "parenthesisornateleft")
        self.replace("ORNATE RIGHT PARENTHESIS", "parenthesisornateright")
        if self.has("RIAL SIGN"):
            if self.replace("RIAL SIGN"):
                self.suffix("rial")

    def processHangul(self):
        if self.has("HANGUL SYLLABLE"):
            self.replace("HANGUL SYLLABLE", "-hangul")

    def processLatin(self):
        # sort these before anything else
        self.replace("BROKEN BAR", "brokenbar")
        self.replace("LATIN LETTER WYNN", "wynn")
        self.replace("LATIN LETTER DENTAL CLICK", "clickdental")
        self.replace("LATIN LETTER LATERAL CLICK", "clicklateral")
        self.replace("LATIN LETTER ALVEOLAR CLICK", "clickalveolar")
        self.replace("LATIN LETTER RETROFLEX CLICK", "clickretroflex")
        self.replace("LATIN LETTER INVERTED GLOTTAL STOP WITH STROKE", 'glottalstopinvertedstroke')
        self.replace("LATIN CAPITAL LETTER SMALL Q WITH HOOK TAIL", "Qsmallhooktail")
        self.replace("LATIN SMALL LETTER AE", "ae")   # case gets wrong
        self.replace("LATIN CAPITAL LETTER AE", "AE")   # case gets wrong
        self.replace("LATIN SMALL LETTER DOTLESS I", "dotlessi")
        self.replace("SMALL LIGATURE OE", "oe")
        self.replace("CAPITAL LIGATURE OE", "OE")
        self.replace("CAPITAL LIGATURE IJ", "IJ")
        self.replace("SMALL LIGATURE IJ", "ij")
        self.replace("LATIN SMALL LETTER DOTLESS J", "dotlessj")
        self.replace("LATIN LETTER TWO WITH STROKE", "twostroke")
        self.replace("COPYRIGHT SIGN", "copyright")  # triggers "right"
        self.replace("LEFT-POINTING DOUBLE ANGLE QUOTATION MARK", "guillemetleft")  # or guillemot ?
        self.replace("RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK", "guillemetright")  # or guillemot ?
        self.replace("FEMININE ORDINAL INDICATOR", "ordfeminine")
        self.replace("MASCULINE ORDINAL INDICATOR", "ordmasculine")
        self.replace("SOFT HYPHEN", "hyphensoft")
        self.replace("FULL STOP", "period")
        self.replace("LOW LINE", "underscore")
        self.replace("LATIN CAPITAL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE", "Ocircumflexhookabove")
        self.replace("LATIN SMALL LETTER O WITH CIRCUMFLEX AND HOOK ABOVE", "ocircumflexhookabove")
        self.replace("LATIN CAPITAL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE", "Ecircumflexhookabove")
        self.replace("LATIN SMALL LETTER E WITH CIRCUMFLEX AND HOOK ABOVE", "ecircumflexhookabove")
        self.replace("LATIN CAPITAL LETTER O WITH MIDDLE TILDE", "Omiddletilde")
        self.replace("LATIN CAPITAL LETTER O WITH OGONEK AND MACRON", "Oogonekmacron")
        self.replace("LATIN SMALL LETTER O WITH OGONEK AND MACRON", "oogonekmacron")
        self.replace("LATIN CAPITAL LETTER A WITH RING ABOVE AND ACUTE",  "Aringacute")
        self.replace("LATIN SMALL LETTER A WITH RING ABOVE AND ACUTE",  "aringacute")


        self.replace("LATIN CAPITAL LETTER O WITH STROKE AND ACUTE", "Oslashacute")
        self.replace("LATIN SMALL LETTER O WITH STROKE AND ACUTE", "oslashacute")
        self.replace("LATIN LETTER REVERSED ESH LOOP", "eshreversedloop")

        self.replace("LATIN CAPITAL LETTER MIDDLE-WELSH LL", "LLmiddlewelsh")
        self.replace("LATIN SMALL LETTER MIDDLE-WELSH LL", "llmiddlewelsh")

        if self.has("MIDDLE-WELSH"):
            if self.replace("MIDDLE-WELSH"):
                self.suffix("middlewelsh")

        if self.has("WITH LONG RIGHT LEG"):
            self.replace("WITH LONG RIGHT LEG")
            self.suffix("long")
            self.suffix("leg")
            self.suffix("right")
        if self.has("AFRICAN"):
            self.replace("AFRICAN")
            self.suffix("african")
        if self.has("TURNED"):
            self.replace("TURNED")
            self.suffix("turned")
        if self.has("OPEN"):
            self.replace("OPEN")
            self.suffix("open")
        self.replace("OPEN O", "")
        if self.has("ACUTE ACCENT"):
            self.replace("ACUTE ACCENT")
            self.suffix("acute")
        if self.has("CIRCUMFLEX ACCENT"):
            self.replace("CIRCUMFLEX ACCENT")
            self.suffix("circumflex")
        if self.has("GRAVE ACCENT"):
            self.replace("GRAVE ACCENT")
            self.suffix("grave")

        if self.has("STOP"):
            if self.replace("STOP"):
                self.suffix("stop")
        if self.has("DIGRAPH"):
            if self.replace("DIGRAPH"):
                self.suffix("digraph")

        self.replace('LATIN LETTER YR', "yr")

        if self.has("LATIN CAPITAL LETTER DZ WITH CARON"):
            if self.replace("LATIN CAPITAL LETTER DZ WITH CARON"):
                self.suffix("D")
                self.suffix("Z")
                self.suffix("caron")
        if self.has("LATIN CAPITAL LETTER D WITH SMALL LETTER Z"):
            if self.replace("LATIN CAPITAL LETTER D WITH SMALL LETTER Z"):
                self.suffix("Dz")
        if self.has("LATIN CAPITAL LETTER DZ"):
            if self.replace("LATIN CAPITAL LETTER DZ"):
                self.suffix("DZ")
        if self.has("WITH SMALL LETTER Z WITH CARON"):
            if self.replace("WITH SMALL LETTER Z WITH CARON"):
                self.suffix("z")
                self.suffix("caron")
        if self.has("LATIN CAPITAL LETTER LJ"):
            if self.replace("LATIN CAPITAL LETTER LJ"):
                self.suffix("LJ")
        if self.has("LATIN SMALL LETTER LJ"):
            if self.replace("LATIN SMALL LETTER LJ"):
                self.suffix("lj")
        if self.has("LATIN CAPITAL LETTER L WITH SMALL LETTER J"):
            if self.replace("LATIN CAPITAL LETTER L WITH SMALL LETTER J"):
                self.suffix("Lj")
        if self.has("LATIN CAPITAL LETTER NJ"):
            if self.replace("LATIN CAPITAL LETTER NJ"):
                self.suffix("NJ")
        if self.has("LATIN CAPITAL LETTER N WITH SMALL LETTER J"):
            if self.replace("LATIN CAPITAL LETTER N WITH SMALL LETTER J"):
                self.suffix("Nj")

        # process
        self.processShape()
        if self.has("LATIN"):
            self.replace("LATIN")
            self.scriptPrefix = "lt"
        self.processDiacritics()
        if self.has("CAPITAL LETTER"):
            self.replace("CAPITAL LETTER", "capital")
        elif self.has("SMALL LETTER"):
            self.replace("SMALL LETTER", "small")

        if self.has("SHARP S"):
            self.replace("SHARP S", "germandbls")
        # hard exceptions
        self.replace("COMMERCIAL AT", "at")
        self.replace("TILDE", "asciitilde")
        self.replace("NO-BREAK", "nbspace")
        if self.has("SPACE"):
            self.replace("SPACE")
            self.suffix("space")
            # INVERTED QUESTION MARK
        self.replace("EXCLAMATION MARK", "exclamation")
        self.replace("QUESTION MARK", "question")
        self.replace("QUOTATION MARK", "quotedouble")
        self.replace("NUMBER SIGN", "numbersign")
        self.replace("DOLLAR SIGN", "dollar")
        self.replace("PERCENT SIGN", "percent")
        self.replace("PLUS SIGN", "plus")
        self.replace("SEMICOLON", "semicolon")
        self.replace("MULTIPLICATION SIGN", "multiply")
        self.replace("DIVISION SIGN", "divide")
        self.replace("COLON", "colon")
        self.replace("COMMA", "comma")
        self.replace("EQUALS SIGN", "equal")
        self.replace("LESS-THAN SIGN", "less")
        self.replace("GREATER-THAN SIGN", "greater")
        self.replace("REVERSE SOLIDUS", "backslash")
        self.replace("SOLIDUS", "slash")
        self.replace("VERTICAL LINE", "bar")
        self.replace("HYPHEN-MINUS", "hyphen")
        self.replace("AMPERSAND", "ampersand")
        self.replace("ASTERISK", "asterisk")
        self.replace("APOSTROPHE", "apostrophe")
        self.replace("NOT SIGN", "logicalnot")
        self.replace("REGISTERED SIGN", "registered")
        self.replace("DEGREE SIGN", "degree")
        self.replace("PLUS-MINUS SIGN", "plusminus")
        self.replace("SUPERSCRIPT ONE", "onesuperior")
        self.replace("SUPERSCRIPT TWO", "twosuperior")
        self.replace("SUPERSCRIPT THREE", "threesuperior")
        self.replace("MICRO SIGN", "mu.math")
        self.replace("PILCROW SIGN", "paragraph")
        self.replace("MIDDLE DOT", 'periodcentered')
        self.replace("VULGAR FRACTION ONE QUARTER", "onequarter")
        self.replace("VULGAR FRACTION ONE HALF", "onehalf")
        self.replace("VULGAR FRACTION THREE QUARTERS", "threequarters")

        self.replace("SQUARE BRACKET", "bracket")
        self.replace("CURLY BRACKET", "brace")
        self.replace("PARENTHESIS", "parenthesis")
        if self.has("LEFT"):
            self.replace("LEFT")
            self.suffix("left")
        if self.has("RIGHT") and not self.has("COPYRIGHT"):
            self.replace("RIGHT")
            self.suffix("right")

        # digits
        self.replace("DIGIT ZERO", "zero")  
        self.replace("ZERO", "zero")  
        self.replace("DIGIT ONE", "one")   
        self.replace("ONE", "one")   
        self.replace("DIGIT TWO", "two")
        self.replace("TWO", "two")
        self.replace("DIGIT THREE", "three")
        self.replace("THREE", "three")
        self.replace("DIGIT FOUR", "four")  
        self.replace("FOUR", "four")  
        self.replace("DIGIT FIVE", "five")  
        self.replace("FIVE", "five")  
        self.replace("DIGIT SIX", "six")   
        self.replace("SIX", "six")   
        self.replace("DIGIT SEVEN", "seven")
        self.replace("SEVEN", "seven")
        self.replace("DIGIT EIGHT", "eight")
        self.replace("EIGHT", "eight")
        self.replace("DIGIT NINE", "nine")
        self.replace("NINE", "nine")

        self.replace("CENT SIGN", "cent")
        self.replace("POUND SIGN", "sterling")
        self.replace("CURRENCY SIGN", "currency")
        self.replace("YEN SIGN", "yen")
        self.replace("SECTION SIGN", "section")

        if self.has("INVERTED"):
            if self.replace("INVERTED"):
                self.suffix("down")

        if self.has("AND"):
            self.replace("AND")

        self.handleCase()
        self.compress()

    def processHebrew(self):
        self.scriptPrefix = "hb"

        self.replace("HEBREW LIGATURE YIDDISH DOUBLE VAV", "vav_vav")   # yiddish ?
        self.replace("HEBREW LIGATURE YIDDISH VAV YOD", "vav_yod")  # yiddish ?
        self.replace("HEBREW LIGATURE YIDDISH DOUBLE YOD", "yod_yod")
        self.replace("HEBREW MARK UPPER DOT", "dotupper")
        self.replace("HEBREW MARK LOWER DOT", "dotlower")
        if self.has('HEBREW'):
            self.replace('HEBREW')
        if self.has("ACCENT"):
            if self.replace("ACCENT"):
                self.suffix("accent")
        if self.has("LETTER"):
            self.replace("LETTER")
        if self.has("FINAL"):
            self.replace("FINAL")
            self.suffix(".final")
        if self.has("POINT"):
            if self.replace("POINT"):
                self.suffix("point")
        if self.has("YIDDISH"):
            if self.replace("YIDDISH"):
                self.suffix("yiddish")
        if self.has("PUNCTUATION"):
            self.replace("PUNCTUATION")


        self.lower()
        self.compress()

    def processIPA(self):
        self.scriptPrefix = "ipa"
        self.processCase()

        self.replace('LETTER PHARYNGEAL VOICED FRICATIVE', "pharyngealvoicedfricative")

        if self.has('BILABIAL PERCUSSIVE'):
            if self.replace("BILABIAL PERCUSSIVE"):
                self.suffix("bilabialpercussive")
                self.replace("LETTER")

        if self.has('BIDENTAL PERCUSSIVE'):
            if self.replace("BIDENTAL PERCUSSIVE"):
                self.suffix("bidentalpercussive")
                self.replace("LETTER")

        if self.has('BILABIAL CLICK'):
            if self.replace("BILABIAL CLICK"):
                self.suffix("bilabialclick")
                self.replace("LETTER")
                

        if self.has("GLOTTAL STOP"):
            if self.replace("GLOTTAL STOP"):
                self.suffix("glottal")
                self.suffix("stop")
                self.replace("LETTER")

        if self.has("WITH MIDDLE TILDE"):
            if self.replace("WITH MIDDLE TILDE"):
                self.suffix('middle')
                self.suffix('tilde')


        if self.has("WITH FISHHOOK"):
            if self.replace("WITH FISHHOOK"):
                self.suffix("fishhook")

        if self.has("SQUAT REVERSED"):
            if self.replace("SQUAT REVERSED"):
                self.suffix("squat")
                self.suffix("reversed")

        if self.has("AND TAIL"):
            if self.replace("AND TAIL"):
                self.suffix("tail")

        if self.has("TURNED"):
            if self.replace("TURNED"):
                self.suffix("turned")


        self.processShape()
        self.processDiacritics()


        self.replace("LATIN")

        self.edit("CAPITAL LETTER", "capital")
        self.edit("SMALL LETTER", "small")

        if self.has("SMALL CAPITAL"):
            if self.replace("SMALL CAPITAL"):
                self.suffix("small")
            self.replace("LETTER")

        self.edit("WITH CROSSED-TAIL", "crossedtail")
        self.edit("STRETCHED", "stretched")
        self.edit("OPEN", "open")
        self.edit("DOTLESS", "dotless")
        self.edit("HORN", "horn") # roundabout case change

        self.edit("WITH LONG LEG", "longleg")
        self.edit("WITH BELT", "belt")
        self.edit("INVERTED", "inverted")
        self.handleCase()
        self.replace("DIGRAPH")
        self.replace("LETTER")
        self.compress()

    def processGreek(self):
        self.scriptPrefix = "gr"
        self.replace("GREEK")

        self.replace("UPSILON WITH HOOK SYMBOL", "upsilonhooksymbol")
        self.replace("UPSILON WITH ACUTE AND HOOK SYMBOL", "upsilonacutehooksymbol")
        self.replace("UPSILON WITH DIAERESIS AND HOOK SYMBOL", "upsilondieresishooksymbol")
        self.replace("CAPITAL LUNATE SIGMA SYMBOL", "Sigmalunatesymbol")
        self.replace("CAPITAL REVERSED LUNATE SIGMA SYMBOL", "Sigmalunatereversedsymbol")
        self.replace("SMALL REVERSED LUNATE SIGMA SYMBOL", "sigmalunatereversedsymbol")
        self.replace("CAPITAL DOTTED LUNATE SIGMA SYMBOL", "Sigmalunatedottedsymbol")
        self.replace("SMALL DOTTED LUNATE SIGMA SYMBOL", "sigmalunatedottedsymbol")
        self.replace("CAPITAL REVERSED DOTTED LUNATE SIGMA SYMBOL", "Sigmalunatedottedreversedsymbol")
        self.replace("SMALL REVERSED DOTTED LUNATE SIGMA SYMBOL", "sigmalunatedottedreversedsymbol")
        self.replace("LUNATE SIGMA SYMBOL", "sigmalunatesymbol")
        self.replace("LUNATE EPSILON SYMBOL", "epsilonlunatesymbol")
        self.replace("RHO WITH STROKE SYMBOL", "rhostrokesymbol")

        self.replace("CAPITAL THETA SYMBOL", "Thetasymbol")
        self.replace("ANO TELEIA", "anoteleia")

        self.replace("DIGAMMA", "Digamma")
        self.replace("KOPPA", "Koppa")
        self.replace("LETTER STIGMA", "Stigma")
        self.replace("LETTER SAMPI", "Sampi")
        self.replace("YOT", "yot")

        self.edit("COPTIC", "coptic")
        self.edit("LUNATE", "lunate")
        self.edit("ARCHAIC", "archaic")

        self.processShape()
        self.processDiacritics()


        self.replace("QUESTION MARK", "question")

        self.edit("NUMERAL SIGN", "numeral", "sign")
        self.edit("LOWER", "lower")
        self.edit("FINAL", "final")
        self.edit("WITH HOOK", "hook")


        self.edit("UPSILON SYMBOL", "upsilonsymbol")
        self.edit("PHI SYMBOL", "phisymbol")
        self.edit("CAPITAL KAI SYMBOL", "Kaisymbol")
        self.edit("KAI SYMBOL", "kaisymbol")
        self.edit("PI SYMBOL", "pisymbol")
        self.edit("THETA SYMBOL", "thetasymbol")
        self.edit("BETA SYMBOL", "betasymbol")
        self.edit("UPSILON SYMBOL", "upsilonsymbol")
        self.edit("KAPPA SYMBOL", "kappasymbol")
        self.edit("RHO SYMBOL", "rhosymbol")
        if self.has("SIGMA SYMBOL"):
            if self.replace("SYMBOL"):
                self.suffix("symbol")


        # with / and 
        parts = ['PROSGEGRAMMENI',
            'YPOGEGRAMMENI',
            'PERISPOMENI',
            'VARIA',
            'PSILI',
            'DIALYTIKA',
            'VRACHY',
            'OXIA',
            'DASIA',
            "TONOS"
        ]
        for p in parts:
            if self.has("WITH "+p):
                if self.replace("WITH "+p):
                    self.suffix(p.lower())
        for p in parts:
            if self.has("AND "+p):
                if self.replace("AND "+p):
                    self.suffix(p.lower())
        for p in parts:
            self.replace(p, p.lower())


        self.replace("KORONIS", "koronis")
        self.replace("LETTER")
        self.handleCase()
        self.handleGreekCase()
        self.compress()

    def processPrivateUse(self):
        self.uniNameProcessed = "privateUseArea_%04x"%self.uniNumber

    def process(self):
        self.processStructure()
        self.processCase()
        self.processMisc()

        if self.uniRangeName == "Box Drawing":
            self.processBoxDrawing()
        if self.uniRangeName in ['Cyrillic', 'Cyrillic Supplementary']:
            #if self.has("CYRILLIC"):
            self.processCyrillic()

        if self.has("ARABIC"):
            self.processArabic()

        if self.has("HEBREW"):
            self.processHebrew()

        if self.uniRangeName in ["Basic Latin",
            'Latin-1 Supplement',
            'Latin Extended-A',
            'Latin Extended-B',
            'Latin Extended Additional',
            ]:
            self.processLatin()

        if self.uniRangeName == "IPA Extensions":
            self.processIPA()


        if self.uniRangeName in ["Private Use Area"]:
            self.processPrivateUse()

        if self.uniRangeName in [ "Greek Extended", "Greek and Coptic",]:
            self.processGreek()

        #if self.has("HANGUL"):
        #    self.processHangul()

        self.processDiacritics()
        self.uniNameProcessed = self.uniNameProcessed + "".join(self.suffixParts) + "-".join(self.finalParts)
        if self.uniNameProcessed in self.ambiguousNames:
            # the final name has a duplicate in another script
            # take disambiguation action
            self.mustAddScript = True
        # compress
        #self.compress()

    def edit(self, pattern, *suffix):
        """
        a method that does the same as this:
        if self.has("PATTERN"):
            if self.replace("PATTERN"):
                self.suffix("suffix")
                self.suffix("suffix")
        """
        if self.has(pattern):
            if self.replace(pattern):
                [self.suffix(s) for s in suffix]

    def getName(self, extension=True):
        if not extension:
            if self.mustAddScript:
                # we don't want a script extension,
                # but we've been warned that it might be necessary
                # for disambiguation
                if self.scriptPrefix != "lt" or self.latinCentric:
                    return "%s-%s"%(self.scriptPrefix, self.uniNameProcessed)
                else:
                    return self.uniNameProcessed
            else:
                # hope for the best then
                return self.uniNameProcessed
        else:
            if self.scriptPrefix:
                return "%s-%s"%(self.scriptPrefix, self.uniNameProcessed)
            else:
                return self.uniNameProcessed

    def compress(self):
        self.uniNameProcessed = self.uniNameProcessed.replace(" ", "")

    def lower(self):
        self.uniNameProcessed = self.uniNameProcessed.lower()

    def suffix(self, namePart):
        if namePart not in self.suffixParts:
            self.suffixParts.append(namePart)

    def replace(self, lookFor, replaceWith=""):
        after = self.uniNameProcessed.replace(lookFor, replaceWith)
        if self.uniNameProcessed == after:
            return False
        self.uniNameProcessed = self.uniNameProcessed.replace(lookFor, replaceWith)
        self.uniNameProcessed = self.uniNameProcessed.replace("  ", " ")
        self.uniNameProcessed.strip()
        return True

    def __repr__(self):
        return "%s\t\t%05x\t\t%s"%(self.getName(extension=False), self.uniNumber, self.uniName)
        #return "<%s: %s, %05x>"%(self.uniNameProcessed, self.uniRangeName, self.uniNumber)
        

show = [
    #'Hangul Syllables',
    #'Private Use Area',
    
    'Basic Latin',
    'Latin-1 Supplement',
    'Latin Extended-A',
    'Latin Extended-B',
    'Latin Extended Additional',
    'Cyrillic',
    'Cyrillic Supplementary',
    'Arabic Presentation Forms-A',
    'Hebrew',
    "IPA Extensions"
    "Box Drawing",

    "Greek and Coptic",
    "Greek Extended",

]

from pprint import pprint
skipped = {}

lines = []
uniqueNamesExtension = {}
uniqueNamesNoExtension = {}
for uniNumber in range(1, 0xffff):
    glyphName = GlyphName(uniNumber=uniNumber)
    if glyphName.uniRangeName not in show:
        skipped[glyphName.uniRangeName]=True
        continue
    if glyphName.hasName():
        print glyphName.getName(extension=True), glyphName.getName(extension=False)
        thisName = glyphName.getName()
        if not thisName in uniqueNamesExtension:
            uniqueNamesExtension[thisName] = []
        uniqueNamesExtension[thisName].append(glyphName)

        thisName = glyphName.getName(extension=False)
        if not thisName in uniqueNamesNoExtension:
            uniqueNamesNoExtension[thisName] = []
        uniqueNamesNoExtension[thisName].append(glyphName)

        lines.append(str(glyphName))

path = "generatedGlyphNames.txt"
f = open(path, 'w')
f.write("\n".join(lines))
f.close()

# check for duplicate names
for k, v in uniqueNamesNoExtension.items():
    if len(v) > 1:
        print "Failed unique test without extension:", v

for k, v in uniqueNamesExtension.items():
    if len(v) > 1:
        print "Failed unique test:", v

# print all the keys 
# s = skipped.keys()
# s.sort()
# print "to do"
# for cat in s:
#     if cat in show:
#         continue
#     print "\t", cat