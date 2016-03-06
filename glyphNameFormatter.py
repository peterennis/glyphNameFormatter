import unicodedata
from unicodeRangeNames import *

#
#   this is an experimental approach
#   to generating a list of glyph names
#   from the standard unicode names
#
#
class GlyphName(object):
    prefSpelling_dieresis = "dieresis"
    languageTags = {
        'latin': "lt",
        'arabic': 'ar',
        'ipa': 'ipa',
        'greek': 'gr',
        'hebrew': 'hb',
        'boxdrawings': 'bxd',
        'cyrillic': 'cy'
    }
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
        "a", "ae",
        "abreve",
        "adieresis",
        "comma",
        "delta",
        "e",
        "edieresis",
        "i",
        "idieresis",
        "igrave",
        "imacron",
        "koppa",
        "o", "oe",
        "odieresis",
        "omega",
        "pe",
        "psi",
        "question",
        "u",
        "udblacute",
        "udieresis",
        "umacron",
        "yu",
        "ve",

        "numbersign",
        "semicolon",
    ]

    def __init__(self, niceName=None, uniNumber=None, verbose=False):
        self.niceName = niceName
        self.uniNumber = uniNumber
        self.uniLetter = None
        self.uniName = ""
        self.uniNameProcessed = self.uniName
        self.uniRangeName = "No Range"
        self.letterCase = None
        self.isLigature = False
        self.scriptTag = ""
        self.languageSuffix = []
        self.suffixParts = []
        self.finalParts = []
        self.mustAddScript = False  # set to True if we need to add script to disambiguate
        self.latinCentric = True    # admit latincentric naming, if we can leave out latin tags, go for it
        self._log = []
        self.verbose = verbose
        self.lookup()
        self.process()

    def hasName(self):
        if not self.uniName:
            return False
        return True

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
        # look up all the external references we need.
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

    def handleCase(self):
        upperCaseIndicators = [
            # from complex to simple
            ("LETTER SMALL CAPITAL", "small"),
            ("SMALL CAPITAL LETTER", "smallcapital"),
            ("CAPITAL LETTER", ""),
            ("MODIFIER LETTER CAPITAL", "modifier"),
            ("MODIFIER LETTER SMALL CAPITAL", "modifiersmall"),
            ("CAPITAL", ""),
        ]
        lowercaseIndicators = [
            # from complex to simple
            ("LATIN SMALL LETTER", ""),
            ("SMALL LETTER", ""),
            ("MODIFIER LETTER SMALL", "modifier"),
            ("SMALL", ""),
        ]
        for upperNames, suffix in upperCaseIndicators:
            if self.has(upperNames):
                start = self.uniNameProcessed.find(upperNames)
                if start == -1:
                    continue
                before = after = self.uniNameProcessed[start + len(upperNames):].strip()
                if not before:
                    continue
                elif len(before) == 1:
                    after = before.upper()
                else:
                    after = before[0].upper()+before[1:].lower()
                self.edit(upperNames, suffix)
                self.replace(before, after)
        for lowerNames, suffix in lowercaseIndicators:
            if self.has(lowerNames):
                start = self.uniNameProcessed.find(lowerNames)
                if start == -1:
                    continue
                before = after = self.uniNameProcessed[start + len(lowerNames):].strip()
                after = after.lower()
                self.edit(lowerNames, suffix)
                self.replace(before, after)


    def processStructure(self):
        if self.verbose:
            print "processStructure"
        if self.has("LIGATURE"):
            self.isLigature = True

    def processCase(self):
        if self.verbose:
            print "processCase"
        if self.has("CAPITAL LETTER"):
            self.letterCase = "uppercase"
        if self.has("SMALL LETTER"):
            self.letterCase = "lowercase"

    def processShape(self):
        if self.verbose:
            print "processShape"
        self.edit("LITTLE", "little")
        self.edit("BIG", "big")
        self.edit("ROUND", "round")

        self.edit("SHORT", "short")
        self.edit("STRAIGHT", "straight")
        self.edit("BARRED", "barred")
        self.edit('CLOSED', "closed")
        self.edit('REVERSED', "reversed")
        self.edit("MONOCULAR", "monocular")
        self.edit("SIDEWAYS", 'sideways')
        self.edit("BOTTOM HALF", 'bottomhalf')
        self.edit("TOP HALF", 'tophalf')

        self.edit("WITH TITLO", "titlo")
        self.edit("TITLO", "titlo")
        self.edit("WITH TAIL", "tail")
        self.edit("WITH TICK", "tick")
        self.edit("WITH DESCENDER", "descender")
        self.edit("WITH UPTURN", "up")
        self.edit("WITH STROKE", "stroke")
        self.edit("WITH VERTICAL STROKE", "verticalstroke")
        self.edit("WITH DIAGONAL STROKE", "diagonalstroke")
        self.edit("WITH HIGH STROKE", "highstroke")
        self.edit("WITH SWASH TAIL", "swash", "tail")
        self.edit("WITH COMMA BELOW", "commaaccent")
        self.edit("WITH PALATAL HOOK", "palatalhook")

    def processDiacritics(self):
        if self.verbose:
            print "processDiacritics"
        # WITH ___ AND ___
        self.edit("WITH CIRCUMFLEX AND HOOK ABOVE", "circumflex", "hookabove")
        self.edit("WITH CIRCUMFLEX AND DOT BELOW", "circumflex", "dotbelow")
        self.edit("WITH DOT BELOW AND DOT ABOVE", "dotbelow", "dotabove")
        self.edit("WITH CIRCUMFLEX AND TILDE", "circumflex", "tilde")
        self.edit("WITH CARON AND DOT ABOVE", "caron", "dotaccent")
        self.edit("WITH ACUTE AND DOT ABOVE", "acute", "dotaccent")
        self.edit("WITH HORN AND GRAVE", "horn", 'grave')
        self.edit("WITH HORN AND ACUTE", "horn", 'acute')
        self.edit("WITH HORN AND TILDE", "horn", 'tilde')
        self.edit("WITH HORN AND HOOK ABOVE", "horn", "hookabove")
        self.edit("WITH HORN AND DOT BELOW", "horn", "dotbelow")
        self.edit("WITH BREVE AND TILDE", "breve", "tilde")
        self.edit("WITH BREVE AND ACUTE", "breve", "acute")
        self.edit("WITH BREVE AND HOOK ABOVE", "breve", "hookabove")
        self.edit("WITH BREVE AND DOT BELOW", "breve", "dotbelow")
        self.edit("WITH BREVE BELOW", "breve", "below")
        self.edit("WITH TILDE AND DIAERESIS", "tilde", self.prefSpelling_dieresis)
        self.edit("WITH BREVE AND GRAVE", "breve", "grave")
        self.edit("WITH DOT BELOW AND MACRON", "macron", "dot")
        self.edit("WITH DIAERESIS AND ACUTE", self.prefSpelling_dieresis, "acute")
        self.edit("WITH DIAERESIS AND TILDE", self.prefSpelling_dieresis, "tilde")
        self.edit("WITH TILDE BELOW", "tilde", "below")
        self.edit('WITH CIRCUMFLEX AND ACUTE', 'circumflex', 'acute')
        self.edit('WITH CIRCUMFLEX AND GRAVE', 'circumflex', 'grave')
        self.edit("WITH CIRCUMFLEX BELOW", "circumflex", "below")
        self.edit("WITH CEDILLA AND ACUTE", "cedilla", "acute")
        self.edit("WITH CEDILLA AND BREVE", "cedilla", 'breve')
        self.edit("WITH MACRON AND DIAERESIS", "macron", self.prefSpelling_dieresis)
        self.edit("WITH MACRON AND ACUTE", "macron", "acute")
        self.edit("WITH MACRON AND GRAVE", "macron", "grave")
        self.edit("WITH TILDE AND ACUTE", "tilde", "acute")
        self.edit("WITH TILDE AND MACRON", "tilde", "macron")
        self.edit("WITH DIAERESIS AND MACRON", self.prefSpelling_dieresis, "macron")
        self.edit("WITH DOT ABOVE AND MACRON", "dotaccent", "macron")
        # PRECEDED BY ___
        self.edit("PRECEDED BY APOSTROPHE", "apostrophe")
        # WITH ___ 
        self.edit("WITH INVERTED BREVE", "inverted", "breve")
        self.edit("WITH TOPBAR", "topbar")
        self.edit("WITH MIDDLE DOT", "dot")
        self.edit("WITH DOUBLE ACUTE", "dblacute")
        self.edit("WITH DOUBLE GRAVE ACCENT", "dblgrave")
        self.edit("WITH DOUBLE GRAVE", "dblgrave")
        self.edit("WITH DOT ABOVE", "dotaccent")
        self.edit("WITH DOT BELOW", "dotbelow")
        self.edit("WITH GRAVE", "grave")
        self.edit("GRAVE", "grave")
        self.edit("WITH HORN", "horn")
        self.edit("WITH BREVE", "breve")
        self.edit("BREVE", "breve")
        self.edit("WITH DIAERESIS BELOW", self.prefSpelling_dieresis, "below")
        self.edit("WITH DIAERESIS", self.prefSpelling_dieresis)
        self.edit("DIAERESIS", self.prefSpelling_dieresis)
        self.edit("WITH MACRON", "macron")
        self.edit("MACRON", "macron")
        self.edit("WITH ACUTE", "acute")
        self.edit("ACUTE", "acute")
        self.edit("WITH CARON", "caron")
        self.edit("CARON", "caron")
        self.edit("WITH CIRCUMFLEX", "circumflex")
        self.edit("CIRCUMFLEX", "circumflex")
        self.edit("WITH TILDE", "tilde")
        self.edit("TILDE", "tilde")
        self.edit("WITH CEDILLA", "cedilla")
        self.edit("CEDILLA", "cedilla")
        self.edit("WITH OGONEK", "ogonek")
        self.edit("OGONEK", "ogonek")
        self.edit("WITH RING ABOVE AND ACUTE","ring","acute")
        self.edit("WITH RING ABOVE", "ring")
        self.edit("WITH RING BELOW", "ringbelow")
        self.edit("WITH RIGHT HALF RING", "right", "halfring")
        self.edit("WITH RETROFLEX HOOK", "retroflexhook")
        self.edit("WITH LINE BELOW", "linebelow")
        self.edit("WITH BAR", "bar")
        self.edit("WITH MACRON", "macron")
        self.edit("WITH MIDDLE TILDE", 'middletilde')
        self.edit("WITH HOOK TAIL", "hook", "tail")
        self.edit("WITH MIDDLE HOOK", "middlehook")
        self.edit("WITH LOOP", "loop")
        self.edit("WITH LEFT HOOK", "left", "hook")
        self.edit("WITH HOOK ABOVE", "hook", "above")
        self.edit("WITH HOOK", "hook")
        self.edit("AND HOOK", "hook")
        self.edit("HOOK", "hook")
        self.edit("WITH CURL", "curl")
        if self.has("BAR") and not self.has("AKBAR") and not self.has("TOPBAR") and not self.has("BARRED"):
            if self.replace("BAR"):
                self.suffix("bar")

    def processArabic(self):
        if self.verbose:
            print "processArabic"
        self.edit("ARABIC-INDIC", "indic")
        self.replace("ARABIC")
        self.scriptTag = self.languageTags['arabic']

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
        self.replace("WITH", "_")
        self.replace("SALLALLAHOU ALAYHE WASALLAM", "sallallahou_alayhe_wasallam")
        if self.replace("BISMILLAH AR-RAHMAN AR-RAHEEM", "bismillah_arRahman_arRaheem"):
            lowercaseOk = False
        if lowercaseOk:
            self.lower()
        self.compress()

    def processBoxDrawing(self):
        if self.verbose:
            print "processBoxDrawing"
        self.scriptTag = self.languageTags['boxdrawings']
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
        if self.verbose:
            print "processCyrillic"
        self.scriptTag = self.languageTags['cyrillic']
        if self.has("CYRILLIC"):
            self.replace("CYRILLIC")
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
        if self.has("SMALL LIGATURE"):
            self.replace("SMALL LIGATURE", "ligsmall")
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
        if self.verbose:
            print "processMisc"
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
        if self.verbose:
            print "processLatin"
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
        self.edit("MIDDLE-WELSH", "middlewelsh")
        self.edit("WITH LONG RIGHT LEG", "long", "leg", "right")
        self.edit("AFRICAN", "african")
        self.edit("TURNED", "turned")
        self.edit("OPEN", "open")
        self.replace("OPEN O", "")
        self.edit("ACUTE ACCENT", "acute")
        self.edit("CIRCUMFLEX ACCENT", "circumflex")
        self.edit("GRAVE ACCENT", "grave")
        self.edit("STOP", "stop")
        self.edit("DIGRAPH", "digraph")
        self.replace('LATIN LETTER YR', "yr")
        self.edit("LATIN CAPITAL LETTER DZ WITH CARON", "D", "Z", "caron")
        self.edit("LATIN CAPITAL LETTER D WITH SMALL LETTER Z", "Dz")
        self.edit("LATIN CAPITAL LETTER DZ", "DZ")
        self.edit("WITH SMALL LETTER Z WITH CARON", "z", "caron")
        self.edit("LATIN CAPITAL LETTER LJ", "LJ")
        self.edit("LATIN SMALL LETTER LJ", "lj")
        self.edit("LATIN CAPITAL LETTER L WITH SMALL LETTER J", "Lj")
        self.edit("LATIN CAPITAL LETTER NJ", "NJ")
        self.edit("LATIN CAPITAL LETTER N WITH SMALL LETTER J", "Nj")

        # process
        self.processShape()
        self.edit("LATIN")
        self.scriptTag = self.languageTags['latin']
        self.processDiacritics()

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
        self.scriptTag = self.languageTags['hebrew']

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
        self.scriptTag = self.languageTags['ipa']
        self.processCase()

        self.edit("LATIN")
        self.edit("GREEK")
        self.edit("INVERTED", "inverted")
        self.edit("MODIFIER LETTER", "modifier")
        self.replace('LETTER PHARYNGEAL VOICED FRICATIVE', "pharyngealvoicedfricative")
        self.edit("LETTER VOICED LARYNGEAL SPIRANT", "laryngealvoicedspirant")
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
        self.edit("LETTER AIN", "Ain")
        self.edit("WITH CROSSED-TAIL", "crossedtail")
        self.edit("STRETCHED", "stretched")
        self.edit("OPEN", "open")
        self.edit("DOTLESS", "dotless")
        self.edit("GREEK SUBSCRIPT", "greek", "subscript")
        self.edit("SUBSCRIPT", "subscript")
        self.edit("CYRILLIC", 'cyrillic')
        self.edit("HORN", "horn") # roundabout case change
        self.edit("WITH LONG LEG", "longleg")
        self.edit("WITH BELT", "belt")
        self.edit("DIAERESIZED", self.prefSpelling_dieresis)        
        self.handleCase()
        self.replace("DIGRAPH")
        self.compress()

    def processGreek(self):
        self.scriptTag = self.languageTags['greek']
        self.replace("GREEK")
        self.replace("UPSILON WITH HOOK SYMBOL", "upsilonhooksymbol")
        self.replace("UPSILON WITH ACUTE AND HOOK SYMBOL", "upsilonacutehooksymbol")
        self.replace("UPSILON WITH DIAERESIS AND HOOK SYMBOL", "upsilondieresishooksymbol")
        self.replace("SMALL REVERSED LUNATE SIGMA SYMBOL", "sigmalunatereversedsymbol")
        self.replace("SMALL DOTTED LUNATE SIGMA SYMBOL", "sigmalunatedottedsymbol")
        self.replace("SMALL REVERSED DOTTED LUNATE SIGMA SYMBOL", "sigmalunatedottedreversedsymbol")
        self.replace("LUNATE SIGMA SYMBOL", "sigmalunatesymbol")
        self.replace("LUNATE EPSILON SYMBOL", "epsilonlunatesymbol")
        self.replace("RHO WITH STROKE SYMBOL", "rhostrokesymbol")
        self.replace("ANO TELEIA", "anoteleia")

        self.replace("DIGAMMA", "Digamma")
        self.replace("KOPPA", "Koppa")
        self.replace("LETTER STIGMA", "Stigma")
        self.replace("LETTER SAMPI", "Sampi")
        self.replace("YOT", "yot")

        self.edit("COPTIC", "coptic")
        self.edit("LUNATE", "lunate")
        self.edit("LETTER ARCHAIC", "archaic")

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
            self.processCyrillic()
        if self.uniRangeName in ["Arabic", 'Arabic Presentation Forms-A', 'Arabic Presentation Forms-B']:
            self.processArabic()
        if self.uniRangeName == "Hebrew":
            self.processHebrew()
        if self.uniRangeName in ["Basic Latin", 'Latin-1 Supplement', 'Latin Extended-A', 'Latin Extended-B', 'Latin Extended Additional', ]:
            self.processLatin()
        if self.uniRangeName in ["IPA Extensions", "Phonetic Extensions"]:
            self.processIPA()
        if self.uniRangeName in ["Private Use Area"]:
            self.processPrivateUse()
        if self.uniRangeName in [ "Greek Extended", "Greek and Coptic",]:
            self.processGreek()
        if self.verbose:
            print self.uniNameProcessed, self.suffixParts, self.finalParts
        self.uniNameProcessed = self.uniNameProcessed + "".join(self.suffixParts) + "-".join(self.finalParts)
        if self.uniNameProcessed in self.ambiguousNames:
            # the final name has a duplicate in another script
            # take disambiguation action
            self.mustAddScript = True

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

    def getExport(self, name=True, useExtension=False, uniNumber=True, uniName=True):
        # return a string fit for exporting
        t = []
        if name:
            t.append(self.getName(extension=useExtension))
        if uniNumber:
            t.append("%04x"%self.uniNumber)
        if uniName:
            t.append(self.uniName)
        return "\t".join(t)

    def getName(self, extension=True):
        # return the name, add extensions or not.
        if not extension:
            if self.mustAddScript:
                # we don't want a script extension,
                # but we've been warned that it might be necessary
                # for disambiguation
                if self.scriptTag != self.languageTags['latin'] and self.scriptTag != "":
                    return "%s-%s"%(self.scriptTag, self.uniNameProcessed)
                else:
                    return self.uniNameProcessed
            else:
                # hope for the best then
                return self.uniNameProcessed
        else:
            if self.scriptTag:
                return "%s-%s"%(self.scriptTag, self.uniNameProcessed)
            else:
                return self.uniNameProcessed

    def compress(self):
        # remove the spaces from the name
        self.uniNameProcessed = self.uniNameProcessed.replace(" ", "")

    def lower(self):
        # whole name to lowercase
        self.uniNameProcessed = self.uniNameProcessed.lower()

    def suffix(self, namePart):
        # add a suffix part
        if namePart not in self.suffixParts:
            self.suffixParts.append(namePart)

    def log(self, lookFor, replaceWith, before, after):
        self._log.append((lookFor, replaceWith, before, after))

    def replace(self, lookFor, replaceWith=""):
        after = self.uniNameProcessed.replace(lookFor, replaceWith)
        if self.uniNameProcessed == after:
            return False
        before = self.uniNameProcessed
        self.uniNameProcessed = self.uniNameProcessed.replace(lookFor, replaceWith)
        self.uniNameProcessed = self.uniNameProcessed.replace("  ", " ")
        self.uniNameProcessed = self.uniNameProcessed.strip()
        self.log(lookFor, replaceWith, before, self.uniNameProcessed)
        return True

    def __repr__(self):
        return "%s\t\t%05x\t\t%s"%(self.getName(extension=False), self.uniNumber, self.uniName)
        

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
    "Arabic",
    'Arabic Presentation Forms-A',
    'Arabic Presentation Forms-B'
    'Hebrew',
    "IPA Extensions",
    "Phonetic Extensions",
    "Box Drawing",

    "Greek and Coptic",
    "Greek Extended",

]

from pprint import pprint

def generateAll(path):
    # generate all the names in the first plane
    skipped = {}
    lines = []
    uniqueNamesExtension = {}
    uniqueNamesNoExtension = {}
    for uniNumber in range(1, 0xffff):
        glyphName = GlyphName(uniNumber=uniNumber, verbose=False)
        if glyphName.uniRangeName not in show:
            skipped[glyphName.uniRangeName]=True
            continue
        if glyphName.hasName():
            lines.append(glyphName.getExport())
    f = open(path, 'w')
    f.write("\n".join(lines))
    f.close()

def testUniqueNames():
    # test if results are unique
    uniqueNamesExtension = {}
    uniqueNamesNoExtension = {}
    for uniNumber in range(1, 0xffff):
        glyphName = GlyphName(uniNumber=uniNumber)
        if glyphName.hasName():
            print glyphName.getName(extension=True), glyphName.getName(extension=False)
            thisName = glyphName.getName()
            if not thisName in uniqueNamesExtension:
                uniqueNamesExtension[thisName] = []
            uniqueNamesExtension[thisName].append(glyphName)

            thisName = glyphName.getName(extension=True)
            if not thisName in uniqueNamesNoExtension:
                uniqueNamesNoExtension[thisName] = []
            uniqueNamesNoExtension[thisName].append(glyphName)
    for k, v in uniqueNamesNoExtension.items():
        if len(v) > 1:
            print "Failed unique test without extension:", v

    for k, v in uniqueNamesExtension.items():
        if len(v) > 1:
            print "Failed unique test:", v


def debug(uniNumber):
    # trace the processing of a specific number
    glyphName = GlyphName(uniNumber=uniNumber, verbose=True)
    glyphName.process()
    print "debug %04x"%uniNumber
    print glyphName.getExport()
    for step in glyphName._log:
        print "\t", step

def findCapitals():
    # find all unicode names that refer to CAPITAL or SMALL
    parts = ["CAPITAL", 
        #"SMALL",
        ]
    caseNumbers = []
    for uniNumber in range(1, 0xffff):
        glyphName = GlyphName(uniNumber=uniNumber, verbose=False)
        if glyphName.uniRangeName not in show:
            continue
        for p in parts:
            if glyphName.has(p):
                caseNumbers.append(uniNumber)
    caseNumbers.sort()
    return caseNumbers

#for n in findCapitals():
#    print GlyphName(uniNumber=n)
    #print
    #debug(n)

generateAll("generatedGlyphNames.txt")

#testUniqueNames()

# check for duplicate names
# print all the keys 
# s = skipped.keys()
# s.sort()
# print "to do"
# for cat in s:
#     if cat in show:
#         continue
#     print "\t", cat